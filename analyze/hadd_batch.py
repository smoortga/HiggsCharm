import os
from argparse import ArgumentParser
import sys
import time

"""
EXAMPLE:

python hadd_batch.py \
--indir=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/Selection/ \
--CMSSWdir=/user/smoortga/HiggsCharm/analyze/CMSSW_10_6_19/src/ \
--jobflavour=longlunch \
--tag=testing

"""

parser = ArgumentParser()
parser.add_argument('--indir', default="FILLME",help='name of SelectedSamples directory')
parser.add_argument('--CMSSWdir', default="FILLMEPLEASE",help='path to a valid CMSSW scram-based directory')
parser.add_argument('--jobflavour', default="microcentury",help='jobFlavour as described in https://batchdocs.web.cern.ch/local/submit.html')
parser.add_argument('--tag', default=time.strftime("%a%d%b%Y_%Hh%Mm%Ss"),help='name of output directory')
args = parser.parse_args()

print("Creating new grid proxy...")
os.system("voms-proxy-init --voms cms --valid 192:0")
os.system("cp $X509_USER_PROXY /user/$USER/")

if args.indir.endswith("/"): 
	indir = os.path.abspath(args.indir[:-1])
else:
	indir= os.path.abspath(args.indir)



localdir = os.getcwd()+"/HADD_TMP_"+args.tag
print localdir
if not os.path.isdir(localdir): 
	os.mkdir(localdir)
else:
	print "HADD DIR ALREADY EXISTS!!! PLEASE FIRST DELETE IT!!!"
	sys.exit(1)


allfiles = [i for i in os.listdir(indir) if ".root" in i]
unique_files = {}
for f in allfiles:
	if not "_events_" in f: continue
	f_tmp = f.split(".root")[0]
	if "_events_" in f_tmp: f_tmp = f_tmp.split("_events_")[0]
	if f_tmp in unique_files: unique_files[f_tmp].append(f)
	else: unique_files[f_tmp] = [f]

jobs_file = open(localdir+"/jobs.txt","w")

for sample,files in unique_files.iteritems():
	print sample
	if not os.path.isdir(localdir+"/"+sample): os.mkdir(localdir+"/"+sample)

        ff_ = open(localdir+"/"+sample+"/launch.sh", 'w')
	ff_.write("#!/bin/bash \n")
	ff_.write("pwd=$PWD \n")  
	ff_.write("source $VO_CMS_SW_DIR/cmsset_default.sh \n")                                                                                                                                                           
	ff_.write("cd %s \n"%(args.CMSSWdir))                                                                                                                                                          
	ff_.write("eval `scram runtime -sh` \n")                                                                                                                                             
	ff_.write("cd $pwd \n")  
	ff_.write("export X509_USER_PROXY=/user/$USER/x509up_u$(id -u $USER) \n")


	if sample+".root" in allfiles:
	   print "WARNING: File %s exists already in %s. Skipping this file"%(sample+".root",indir)
	   continue
	cmd = "hadd %s.root"%("$TMPDIR/"+sample)
	for ff in files:
	   cmd += " %s"%(indir+"/"+ff)
	ff_.write("%s \n"%cmd)
	ff_.write("cp $TMPDIR/"+sample+".root "+indir+"/"+sample+".root \n")
	ff_.write("rm $TMPDIR/"+sample+".root \n")
	for fff in files:
		ff_.write("rm %s/%s \n"%(indir,fff))
	ff_.close()
        os.system("chmod 777 %s"%(localdir+"/"+sample+"/launch.sh"))
	jobs_file.write("%s/%s \n"%(localdir,sample))

jobs_file.close()

#
# CREATE CONDOR SUBMISSION SCRIPT
#

condor_submit_file = open(localdir+"/condor.submit","w")
condor_submit_file.write("Universe = vanilla \n")
condor_submit_file.write("Executable = $(jobdir)/launch.sh \n")
condor_submit_file.write(" \n")
condor_submit_file.write("Error = $(jobdir)/output.err \n")
condor_submit_file.write("Output = $(jobdir)/output.out \n")
condor_submit_file.write("Log = $(jobdir)/output.log \n")
condor_submit_file.write(" \n")
condor_submit_file.write('+JobFlavour = "%s" \n' %args.jobflavour)
condor_submit_file.write("queue jobdir from %s/jobs.txt \n"%(localdir))
condor_submit_file.close()

print ""
print "Done!"
print("The jobs can now be submitted via condor with 'condor_submit %s/condor.submit'"%(localdir))
print("The status can then be checked using 'condor_q'")
# 
# print "Submit via: '\033[92mbig-submission %s/bigsub.txt\033[0m'"%(localdir)
# print "Use '\033[94mqstat -u $USER\033[0m' to monitor samples"
# print "use '\033[94mfor j in $(qselect -u $USER);do timeout 3 qdel -a $j;done\033[0m' to delete all your jobs"


