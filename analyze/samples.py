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
	"HcTo4mu":{	"path":"/pnfs/iihe/cms/store/user/nbreugel/HiggsCharm/NANOAOD_HcToFourMuons_NanoAOD/",
						"private":True, # If private production, put to True. If central production, put to False
						"files":[], # sub dictionary to save files with start and end event
						"nevents":-1,
						"xsec":0.000005864815,
		},
	# https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D/GluGluToHiggs0MToZZTo4mu_M125_GaSM_13TeV_MCFM701_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM
	"GluGluToHiggs0MToZZTo4L":{	"path":"/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM",
									"private":False, 
									"files":[], 
									"nevents":-1,
									"xsec":0.0127,
		},
	# https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM
	"GluGluToContinToZZTo4mu":{	"path":"/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",
									"private":False, # If private production, put to True. If central production, put to False
									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
									"nevents":-1, #992547
									"xsec":0.00158,
		},
	# url:
        "QQToZZTo4L":{	"path":"/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",
									"private":False, # If private production, put to True. If central production, put to False
									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
									"nevents":-1, #992547
									"xsec":0.01325,
		},

	# url:
        "DY_ZPlusJets":{	"path":"/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",
									"private":False, # If private production, put to True. If central production, put to False
									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
									"nevents":-1, #992547
									"xsec":6435,
		},
        # url:
        "VBF_HToZZTo4L":{	"path":"/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM",
									"private":False, # If private production, put to True. If central production, put to False
									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
									"nevents":-1, #992547
									"xsec":0.000986,
		}, 
        # url:
        "ttH_HToZZTo4L":{	"path":"/ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",
									"private":False, # If private production, put to True. If central production, put to False
									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
									"nevents":-1, #992547
									"xsec":0.000393,
		},
        # url:
        "ZH_HToZZTo4L":{	"path":"/ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",
									"private":False, # If private production, put to True. If central production, put to False
									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
									"nevents":-1, #992547
									"xsec":0.000668,
		},
        # url:
        "WplusH_HToZZTo4L":{	"path":"/WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",
									"private":False, # If private production, put to True. If central production, put to False
									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
									"nevents":-1, #992547
									"xsec":0.0002176,
		},
        # url:
        "WminH_HToZZTo4L":{	"path":"/WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",
									"private":False, # If private production, put to True. If central production, put to False
									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
									"nevents":-1, #992547
									"xsec":0.0001380,
		},
        
# 	# https://cmsweb.cern.ch/das/request?input=dataset%3D%2FTTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8%2FRunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1%2FNANOAODSIM&instance=prod/global
# 	"TTZToLLNuNu":{	"path":"/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
# 									"private":False, # If private production, put to True. If central production, put to False
# 									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
# 									"nevents":-1, #13914900
# 									"xsec":0.2432,
# 		},
# 	# https://cmsweb.cern.ch/das/request?input=dataset%3D%2FZZ_TuneCP5_13TeV-pythia8%2FRunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1%2FNANOAODSIM&instance=prod/global
# 	"ZZ":{	"path":"/ZZ_TuneCP5_13TeV-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
# 									"private":False, # If private production, put to True. If central production, put to False
# 									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
# 									"nevents":-1, # 2000000 
# 									"xsec":12.14,
# 		},
# 	#https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D%2FWW_TuneCP5_13TeV-pythia8%2FRunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1%2FNANOAODSIM	
# 	"WW":{	"path":"/WW_TuneCP5_13TeV-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
# 									"private":False, # If private production, put to True. If central production, put to False
# 									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
# 									"nevents":-1, # 7959200 
# 									"xsec":75.8,
# 		},
# 	# https://cmsweb.cern.ch/das/request?input=dataset%3D%2FWZ_TuneCP5_13TeV-pythia8%2FRunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1%2FNANOAODSIM&instance=prod/global
# 	"WZ":{	"path":"/WZ_TuneCP5_13TeV-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
# 									"private":False, # If private production, put to True. If central production, put to False
# 									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
# 									"nevents":-1, # 4000000 
# 									"xsec":27.6,
# 		},
# 	# https://cmsweb.cern.ch/das/request?input=dataset%3D%2FWZZ_TuneCP5_13TeV-amcatnlo-pythia8%2FRunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1%2FNANOAODSIM&instance=prod/global
# 	"WZZ":{	"path":"/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",
# 									"private":False, # If private production, put to True. If central production, put to False
# 									"files":[], # sub dictionary to save files with start and end event {name:[begin,end]}
# 									"nevents":-1, # 250000
# 									"xsec":0.05565,
# 		},
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
                        f_ = ROOT.TFile(properties["path"]+f)
                        if (not f_): 
                                print "encountered NULL pointer, skipping this file"
                                continue
                        properties["files"].append([properties["path"]+f,counter])
                        t_ = f_.Get("Events")
                        nen_ = int(t_.GetEntries())
                        properties["files"][f_idx].append(counter+nen_-1)
                        counter += nen_
                properties["nevents"] = counter
			
	else:
		files = (os.popen('dasgoclient -query="file dataset=%s"'%properties["path"]).read()).split("\n")[:-1]
                files_xrootd = ["root://cms-xrd-global.cern.ch//"+f_ for f_ in files]
                counter = 0
                files_skipped = 0
                for f_idx,f  in enumerate(files_xrootd):
                        print "--> processing " + f
                        #f_name = f.split(".root")[0]
                        f_ = ROOT.TFile.Open(f)
                        if (not f_): 
                                print "encountered NULL pointer, skipping this file"
                                files_skipped += 1
                                continue
                        properties["files"].append([f,counter])
                        t_ = f_.Get("Events")
                        nen_ = int(t_.GetEntries())
                        properties["files"][f_idx-files_skipped].append(counter+nen_-1)
                        counter += nen_
                properties["nevents"] = counter
	print "Done processing sample with tag: "+sample
	print ""
		

pprint(sample_dict)
pickle.dump(sample_dict,open("sample_dict.pkl","wb"))

print "Dictionary stored in '%s/sample_dict.pkl'"%os.getcwd()
