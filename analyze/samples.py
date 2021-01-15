import os
import sys
import numpy as np
import ROOT
from pprint import pprint
import pickle

"""
EXAMPLE:

python samples.py

"""


sample_dict = {
	"HcTo4mu":{	"path":"/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/NANOAOD_HcToFourMuons/",
						"private":True, # If private production, put to True. If central production, put to False
						"files":[], # sub dictionary to save files with start and end event
						"nevents":-1,
		},
	"GluGluToHiggs0MToZZTo4mu":{	"path":"/GluGluToHiggs0MToZZTo4mu_M125_GaSM_13TeV_MCFM701_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
									"private":False, # If private production, put to True. If central production, put to False
									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
									"nevents":-1,
		},
}


print("Creating new grid proxy...")
os.system("voms-proxy-init --voms cms --valid 192:0")


for sample, properties in sample_dict.iteritems():
	print "Start processing sample with tag: "+sample
	
	if properties["private"] == True:
		files = os.listdir(properties["path"])
		counter = 0
		for f_idx,f in enumerate(files):
			print "--> processing " + properties["path"]+f
			#f_name = f.split(".root")[0]
			properties["files"].append([properties["path"]+f,counter])
			f_ = ROOT.TFile(properties["path"]+f)
			t_ = f_.Get("Events")
			nen_ = int(t_.GetEntries())
			properties["files"][f_idx].append(counter+nen_-1)
			counter += nen_
		properties["nevents"] = counter
			
			
	else:
		files = (os.popen('dasgoclient -query="file dataset=%s"'%properties["path"]).read()).split("\n")[:-1]
		files_xrootd = ["root://cms-xrd-global.cern.ch//"+f_ for f_ in files]
		counter = 0
		for f_idx,f  in enumerate(files_xrootd):
			print "--> processing " + f
			#f_name = f.split(".root")[0]
			properties["files"].append([f,counter])
			f_ = ROOT.TFile.Open(f)
			t_ = f_.Get("Events")
			nen_ = int(t_.GetEntries())
			properties["files"][f_idx].append(counter+nen_-1)
			counter += nen_
		properties["nevents"] = counter
	
	print "Done processing sample with tag: "+sample
	print ""
		

pprint(sample_dict)
pickle.dump(sample_dict,open("sample_dict.pkl","wb"))

print "Dictionary stored in '%s/sample_dict.pkl'"%os.getcwd()
