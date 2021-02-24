from argparse import ArgumentParser
import sys
import os
import time
import pickle

"""

python submit_analyze_nanoAOD.py \
--outdir=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/Selection/ \
--CMSSWdir=/user/smoortga/HiggsCharm/analyze/CMSSW_10_6_19/src/ \
--sampledict=/storage_mnt/storage/user/smoortga/HiggsCharm/analyze/sample_dict.pkl \
--tag=testing \
--nmaxevtsperjob=50000 \
--jobflavour=longlunch



"""


def main():

	
	parser = ArgumentParser()
	parser.add_argument('--outdir', default="FILLMEPLEASE",help='path and name of output file')
	parser.add_argument('--CMSSWdir', default="FILLMEPLEASE",help='path to a valid CMSSW scram-based directory')
	parser.add_argument('--sampledict', default="FILLMEPLEASE",help='path to the sample dictionary created by "samples.py"')
	parser.add_argument('--tag', default=time.strftime("%a%d%b%Y_%Hh%Mm%Ss"),help='name of output directory')
	parser.add_argument('--jobflavour', default="microcentury",help='jobFlavour as described in https://batchdocs.web.cern.ch/local/submit.html')
	parser.add_argument('--nmaxevtsperjob', type=int, default=200000,help='maximum number of events per job (otherwise split)')
	parser.add_argument('--nevents', type=int, default=-1,help='maximum number of events for each dataset to process')
	parser.add_argument('--ncpu', type=int, default=-1,help='number of CPU to use in parallel')
	args = parser.parse_args()
	
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

	
	
	######################
	#
	# GRID PROXY
	#
	######################
	
	workingdir = os.getcwd()
	
	print("Creating new grid proxy...")
	os.system("voms-proxy-init --voms cms --valid 192:0")
	os.system("cp $X509_USER_PROXY /user/$USER/")
	
	if not os.path.isdir(args.outdir): os.system("mkdir %s"%(args.outdir))
	
	# Create batch temp
	tmpdirname="BATCH_TMP_"+args.tag
	if not os.path.isdir(workingdir+"/"+tmpdirname): os.mkdir(workingdir+"/"+tmpdirname)
	
	
	######################
	#
	# LOAD THE SAMPLE DICTIONARY
	#
	######################
	
	assert os.path.isfile(args.sampledict), \
		"ERROR: could not find sample dict (%s), did you run samples.py beforehand?"%args.sampledict
	
	sample_dict = pickle.load(open(args.sampledict,"rb"))
	
	
	######################
	#
	# Create a text file with all
	# bash files to run via condor
	#
	######################
	
	jobs_file = open(tmpdirname+"/jobs.txt","w")
	
	######################
	#
	# Run over each sample
	#
	######################
	print ""
	for sample_tag,sample_properties in sample_dict.iteritems():
		
		
		#
		# CREATE DIRECTORY FOR JOB SUMISSION OF THIS SAMPLE
		#
		sampledir = workingdir+"/"+tmpdirname+"/"+sample_tag
                if not os.path.isdir(sampledir): os.mkdir(sampledir)
		
		#
		# TOTAL NUMBER OF EVENTS TO PROCESS
		#
		total_nevents_to_process = args.nevents
		if total_nevents_to_process < 0 or total_nevents_to_process > sample_properties["nevents"]:
			total_nevents_to_process = sample_properties["nevents"]
		
		#
		# do some arithmetic on the per-job event ranges
		#
		ranges_tmp = range(0,total_nevents_to_process,args.nmaxevtsperjob)
		if ranges_tmp[-1] != sample_properties["nevents"]: ranges_tmp.append(sample_properties["nevents"])
		#print ranges_tmp
		event_ranges = [[ranges_tmp[idx],ranges_tmp[idx+1]-1] for idx,i in enumerate(ranges_tmp) if idx < len(ranges_tmp)-1]
		#print event_ranges
		
		print "Submitting %i jobs for %s"%(len(event_ranges),sample_tag)
		
		for job_id,first_last_array in enumerate(event_ranges):
			firstEvt = first_last_array[0]
			lastEvt = first_last_array[1]
			outfilename = "selected_%s_events_%i_%i.root"%(sample_tag,firstEvt,lastEvt)
			
			#
			# Create subdirectory for this job
			#
			
			jobdir = sampledir + "/job_%i"%(job_id+1)
			if not os.path.isdir(jobdir): os.mkdir(jobdir)
			
			flaunch_ = open(jobdir+"/launch.sh","w")
			flaunch_.write("#!/bin/bash \n") 
			flaunch_.write("source $VO_CMS_SW_DIR/cmsset_default.sh \n")                                                                                                                                                           
			flaunch_.write("cd %s \n"%(args.CMSSWdir))                                                                                                                                                          
			flaunch_.write("eval `scram runtime -sh` \n")                                                                                                                                           
			flaunch_.write("cd %s \n"%(workingdir))  
			flaunch_.write("export X509_USER_PROXY=/user/$USER/x509up_u$(id -u $USER) \n")
			flaunch_.write("python Analyze_nanoAOD.py --sampletag=%s --outfile=%s --sampledict=%s --firstEvt=%i --lastEvt=%i --splitted=1 --private=%i \n"%(sample_tag,"$TMPDIR/"+outfilename,args.sampledict,firstEvt,lastEvt,int(sample_properties["private"])))
			flaunch_.write("cp $TMPDIR/%s %s/%s \n"%(outfilename,args.outdir,outfilename))
			flaunch_.write("rm $TMPDIR/%s \n"%(outfilename))
			flaunch_.close()
                        os.system("chmod +rwx %s"%(jobdir+"/launch.sh"))
			
			jobs_file.write("%s \n"%(jobdir))
			
			
	jobs_file.close()
	
	#
	# CREATE CONDOR SUBMISSION SCRIPT
	#
	
	condor_submit_file = open(workingdir+"/"+tmpdirname+"/condor.submit","w")
	condor_submit_file.write("Universe = vanilla \n")
	condor_submit_file.write("Executable = $(jobdir)/launch.sh \n")
	condor_submit_file.write(" \n")
	condor_submit_file.write("Error = $(jobdir)/output.err \n")
	condor_submit_file.write("Output = $(jobdir)/output.out \n")
	condor_submit_file.write("Log = $(jobdir)/output.log \n")
	condor_submit_file.write(" \n")
	condor_submit_file.write('+JobFlavour = "%s" \n' %args.jobflavour)
	condor_submit_file.write("queue jobdir from %s/jobs.txt \n"%(workingdir+"/"+tmpdirname))
	condor_submit_file.close()
	
	print ""
	print "Done!"
	print("The jobs can now be submitted via condor with 'condor_submit %s/condor.submit'"%(workingdir+"/"+tmpdirname))
	print("The status can then be checked using 'condor_q'")

if __name__ == "__main__":
	main()
