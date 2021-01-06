import os
import time
import sys
from argparse import ArgumentParser

"""

python submit_RECO-AOD-MINIAOD.py \
--config=./test_MINIAOD_cfg.py \
--indir=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/GENSIMDIGI_testing/ \
--outdir=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/RECOAODMINIAOD \
--jobflavour=tomorrow \
--tag=testing_MINIAOD

"""

parser = ArgumentParser()
parser.add_argument('--config', default="FILLME",help='path to the configuration file')
parser.add_argument('--indir', default="FILLME",help='path to input files (lhe)')
parser.add_argument('--outdir', default="FILLME",help='path to output directory (pnfs?)')
parser.add_argument('--jobflavour', default="microcentury",help='jobFlavour as described in https://batchdocs.web.cern.ch/local/submit.html')
parser.add_argument('--tag', default=time.strftime("%a%d%b%Y_%Hh%Mm%Ss"),help='name of output directory')
args = parser.parse_args()


####################
#
# Doing some checks on the given arguments
#
####################

# check if jobflavour is valid
"""
https://batchdocs.web.cern.ch/local/submit.html
espresso     = 20 minutes
microcentury = 1 hour
longlunch    = 2 hours
workday      = 8 hours
tomorrow     = 1 day
testmatch    = 3 days
nextweek     = 1 week
"""
if not(args.jobflavour in ["espresso","microcentury","longlunch","workday","tomorrow","testmatch","nextweek"]):
	print("ERROR: unknown jobflavour! should be one of the following: 'espresso','microcentury','longlunch','workday','tomorrow','testmatch','nextweek'")
	print("Exiting...")
	sys.exit(1)

indir = os.path.abspath(args.indir)+"/"
if not os.path.isdir(indir):
	print "Error: could not find input directory '%s'"%indir
	sys.exit(1)
	
outdir = os.path.abspath(args.outdir)+"_"+args.tag+"/"
if not os.path.isdir(outdir):
	need_answer = True
	while need_answer:
		answer = raw_input("The output directory (%s) is not found, should I try to create it now (y/n)?"%outdir)
		if answer == "n": 
			print("Exiting...")
			sys.exit(1)
		elif answer == "y": 
			#os.system("gfal-mkdir srm://maite.iihe.ac.be:8443%s"%(outdir))
			os.system("mkdir %s"%(outdir))
			if not os.path.isdir(outdir):
				print("creating directory failed (do you have proper acces rights?)")
				print("Exiting...")
				sys.exit(1)
			need_answer = False
		else:
			print("please type either 'y' or 'n'")
else:
	print("The output directory (%s) already exists! Please remove it, or pick another destiantion."%outdir)
	print("Exiting...")
	sys.exit(1)

config = os.path.abspath(args.config)
assert os.path.isfile(config), "Could not find config file %s"%config

print("Creating new grid proxy...")
os.system("voms-proxy-init --voms cms --valid 192:0")
os.system("export X509_USER_PROXY=$(voms-proxy-info -path)")    
os.system("cp $X509_USER_PROXY /user/$USER/")


####################
#
# Creating a local repo for job submission
#
####################

localdir = os.getcwd()+"/"+args.tag+"_submission"
if not os.path.isdir(localdir): os.mkdir(localdir)
#if not os.path.isdir(localdir+"/condor_log/"): os.mkdir(localdir+"/condor_log/")

# text file with all the files in it
files_txt = open(localdir+"/input_files.txt","w")
files_ = [i for i in os.listdir(indir) if i.endswith(".root")]
for f_ in files_:
	number_ = int(f_.split(".")[0].split("_")[-1])
	files_txt.write(str(number_)+" "+f_+"\n")
files_txt.close()


# create for each job a new subdirectory with launch.sh file
for f_ in files_:
	number_ = int(f_.split(".")[0].split("_")[-1])
	localdir_job = localdir+"/job_%i"%number_
	if not os.path.isdir(localdir_job): os.mkdir(localdir_job)
	ff_ = open(localdir_job+"/launch.sh", 'w')
	ff_.write("#!/bin/bash \n")
	ff_.write("pwd=$PWD \n")  
	ff_.write("source $VO_CMS_SW_DIR/cmsset_default.sh \n")                                                                                                                                                           
	ff_.write("cd %s \n"%(os.getcwd()))                                                                                                                                                          
	ff_.write("eval `scram runtime -sh` \n")                                                                                                                                           
	ff_.write("cd $pwd \n")  
	ff_.write("export X509_USER_PROXY=/user/$USER/x509up_u$(id -u $USER) \n")
	ff_.write("echo $HOME \n")
	ff_.write("export HOME=/user/$USER \n")
	ff_.write("cmsRun %s infile=file:%s%s outfile=file:$TMPDIR/%s_RECO-AOD-MINIAOD_%i.root nevents=-1 \n"%(config,indir,f_,args.tag,number_))  
	ff_.write("cp $TMPDIR/%s_RECO-AOD-MINIAOD_%i.root %s%s_RECO-AOD-MINIAOD_%i.root \n"%(args.tag,number_,outdir,args.tag,number_))
	ff_.write("rm $TMPDIR/%s_RECO-AOD-MINIAOD_%i.root \n"%(args.tag,number_))
	ff_.close()

# write condor submission script
f_tmp_condor_ = open(localdir+"/condor_"+args.tag+".submit","w")
f_tmp_condor_.write("Universe = vanilla \n")
f_tmp_condor_.write("Executable = %s/job_$(number)/launch.sh \n"%(localdir))
#f_tmp_condor_.write("Arguments = %s $(nevents) $(rnd) $(number) \n"%((args.gridpack).split("/")[-1]))
f_tmp_condor_.write(" \n")
f_tmp_condor_.write("Error = %s/job_$(number)/job.err \n"%(localdir))
f_tmp_condor_.write("Output = %s/job_$(number)/job.out \n"%(localdir))
f_tmp_condor_.write("Log = %s/job_$(number)/job.log \n"%(localdir))
f_tmp_condor_.write(" \n")
#f_tmp_condor_.write("should_transfer_files = YES \n")
#f_tmp_condor_.write("transfer_input_files = %s \n"%(config))
f_tmp_condor_.write('+JobFlavour = "%s" \n' %args.jobflavour)
f_tmp_condor_.write("queue number,file from %s/input_files.txt \n"%localdir)
f_tmp_condor_.close()

print("")
print("DONE!")
print("The jobs can now be submitted via condor with 'condor_submit %s/condor_%s.submit'"%(localdir,args.tag))
print("The status can then be checked using 'condor_q'")
	