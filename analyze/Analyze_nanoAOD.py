from argparse import ArgumentParser
import sys
import os
import pickle
import ROOT
from array import array
from math import sqrt, pow, pi

"""
examples:

python Analyze_nanoAOD.py \
--sampletag=GluGluToHiggs0MToZZTo4mu \
--outfile=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/Selection/selected_GluGluToHiggs0MToZZTo4mu_events_673000_673499.root \
--sampledict=/storage_mnt/storage/user/smoortga/HiggsCharm/analyze/sample_dict.pkl \
--firstEvt=673000 \
--lastEvt=673499 \
--splitted=1 \
--private=0

python Analyze_nanoAOD.py \
--sampletag=GluGluToHiggs0MToZZTo4mu \
--outfile=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/Selection/selected_GluGluToHiggs0MToZZTo4mu_events_671900_672399.root \
--sampledict=/storage_mnt/storage/user/smoortga/HiggsCharm/analyze/sample_dict.pkl \
--firstEvt=671900 \
--lastEvt=672399 \
--splitted=1 \
--private=0

python Analyze_nanoAOD.py \
--sampletag=GluGluToHiggs0MToZZTo4mu \
--outfile=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/Selection/selected_GluGluToHiggs0MToZZTo4mu_events_280005_6721035.root \
--sampledict=/storage_mnt/storage/user/smoortga/HiggsCharm/analyze/sample_dict.pkl \
--firstEvt=280005 \
--lastEvt=672135 \
--splitted=1 \
--private=0






python Analyze_nanoAOD.py \
--sampletag=HcTo4mu \
--outfile=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/Selection/selected_HcTo4mu_events_400_599.root \
--sampledict=/storage_mnt/storage/user/smoortga/HiggsCharm/analyze/sample_dict.pkl \
--firstEvt=550 \
--lastEvt=1399 \
--splitted=1 \
--private=1

"""

def Analyze_nanoAOD(sampletag,outfile,sampledict, private, IdxBegin = 0, IdxEnd = -1, Splitted = False):
	
	######################
	#
	# LOAD THE SAMPLE DICTIONARY
	#
	######################
	
	assert os.path.isfile(sampledict), \
		"ERROR: could not find sample dict (%s), did you run samples.py beforehand?"%sampledict
		
	sample_dict = pickle.load(open(sampledict,"rb"))
	
	######################
	#
	# extract from the dictionary the sample tag, 
	# with corresponding file information
	#
	######################
	
	assert sampletag in sample_dict.keys(), \
		"ERROR: could not find sample tag (%s) in the sample dictionary!"%sampletag
		
	indir = sample_dict[sampletag]["path"]
	infiles = sample_dict[sampletag]["files"] # array of subarrays, each containing name, beginEvt and endEvt: [[file1.root,0,199][file2.root,200,399],...]
	
	######################
	#
	# Calculate which files are needed for 
	# this job (and where to start/stop)
	#
	#  There are 4 possibilities for each file
	#  1. {IdxBegin,IdxEnd} lies completely in the current file (only 1 file needed)
	#  2. The current file has IdxBegin in it, but more files are needed to reach IdxEnd
	#  3. All events in the current file are within {IdxBegin,IdxEnd}. Need to add the file and continue adding more files
	#  4. The current file has IdxEnd in it, but IdxBegin was in another file. Need to adding files here
	#
	#  5. Special cases if IdxBegin < 0 or IdxEnd > total events in all files or IdxBegin > IdxEnd (should not happen)
	#
	######################
	
	list_of_files_to_add = []
	relative_start = -1
	relative_stop = -1
	relative_nevents = 0
	
	if IdxEnd < 0: IdxEnd = infiles[-1][2]
	
	for file_name,start,stop in infiles:
	
		#  1. {IdxBegin,IdxEnd} lies completely in the current file (only 1 file needed)
		if IdxBegin >= start and IdxEnd <= stop:
			list_of_files_to_add.append(file_name)
			relative_start = IdxBegin-start
			relative_stop = IdxEnd-start
			relative_nevents = relative_stop-relative_start+1
			break
		
		#  2. The current file has IdxBegin in it, but more files are needed to reach IdxEnd
		elif (IdxBegin >= start and IdxBegin <= stop) and IdxEnd > stop:
			list_of_files_to_add.append(file_name)
			relative_start = IdxBegin-start
			relative_nevents += stop-IdxBegin+1
			continue
		
		#  3. All events in the current file are within {IdxBegin,IdxEnd}. Need to add the file and continue adding more files
		elif IdxBegin < start and IdxEnd > stop:
			list_of_files_to_add.append(file_name)
			relative_nevents += stop-start+1
			continue
		
		#  4. The current file has IdxEnd in it, but IdxBegin was in another file. Need to adding files here
		elif IdxBegin < start and (IdxEnd <= stop and IdxEnd >= start):
			list_of_files_to_add.append(file_name)
			relative_nevents += IdxEnd-start+1
			relative_stop = relative_start+relative_nevents -1
			break
			

	#  5. Special cases if IdxBegin < 0 or IdxEnd > total events in all files or IdxBegin > IdxEnd (should not happen)
	assert (relative_start > -1) and (relative_stop > -1) and (relative_stop-relative_start > 0) and relative_nevents > 0, \
		"ERROR: something went wrong in calculating srating and stopping number of the events! (are IdxBegin and IdxEnd within the sample boundaries?)"
		
	
	print ""	
	print "Loaded the following files:"
	for i in list_of_files_to_add:
		print i
	print ""	
	print "Start (relative): %i | Stop (relative): %i | # Events (boundaries included): %i"%(relative_start,relative_stop,relative_nevents)
	print ""
	
	
	######################
	#
	# Load the input files and 
	# define the output file
	#
	######################	
	
	intree_ = ROOT.TChain("Events")
	for f_ in list_of_files_to_add:
		intree_.Add(f_)
	
	outdir = "/".join(outfile.split("/")[:-1])
	assert os.path.isdir(outdir), \
		"ERROR: output directory (%s) does not exist. Please create it before!"%outdir
	
	ofile_ = ROOT.TFile(outfile,"RECREATE")
	otree_ = ROOT.TTree("tree","tree")
	
	# **************************** add branches to output ****************************
	dict_variableName_Leaves = {}
	
	# MadGraph WEIGHTS
	"""
	Ordering from .lhe files:
	
	<wgt id='rwgt_kc2'> +5.8019767e-06 </wgt>
	<wgt id='rwgt_kc0'> +5.8668415e-06 </wgt>
	<wgt id='rwgt_kc5'> +5.7053556e-06 </wgt>
	<wgt id='rwgt_kc10'> +5.5461233e-06 </wgt>
	<wgt id='rwgt_SM'> +5.8343640e-06 </wgt>
	<wgt id='rwgt_kc0p5'> +5.8505915e-06 </wgt>
	
	Make sure you have the same ordering!
	"""
	match_index_to_weight = {}
	match_index_to_weight.update({0:"weight_kc2"})
	match_index_to_weight.update({1:"weight_kc0"})
	match_index_to_weight.update({2:"weight_kc5"})
	match_index_to_weight.update({3:"weight_kc10"})
	match_index_to_weight.update({4:"weight_kc1"})
	match_index_to_weight.update({5:"weight_kc0p5"})
	for idx,weight_name in match_index_to_weight.iteritems():
		dict_variableName_Leaves.update({weight_name: [array('d', [0]),"D"]})
	
	
	# JETS
	dict_variableName_Leaves.update({"nSelectedJets": [array('d', [0]),"D"]}) # number of jets passing the event selections criteria
	dict_variableName_Leaves.update({"LeadingJet_Pt": [array('d', [0]),"D"]}) # Transverse momentum of the hardest jet
	
	#LEPTONS
	
	# ********************************************************************************
	
	
	for name,arr in dict_variableName_Leaves.iteritems():
		otree_.Branch(name,arr[0],name+"/"+arr[1])
		
	
	# Save a histogram with number of processed events (weighted)
	hweight = ROOT.TH1D("hweight","",1,0,2)
		
		
		
	
	######################
	#
	# Start event loop
	#
	######################
	
	# ***************** Start event loop ********************
	for evt in range(relative_start,relative_stop+1):
		if ((evt-relative_start) % int(relative_nevents/10.) == 0): print"%s: Processing event %i/%i (%.1f %%)"%(sampletag,evt-relative_start+IdxBegin,IdxEnd,100*float(evt-relative_start)/float(relative_nevents))
		intree_.GetEntry(evt)
		
		######################
		#
		# keep track of how many (weighted)
		# events have been processed (not selected!)
		#
		######################
		
		weight = 1.
		hweight.Fill(1,weight)
		
		
		
		
		######################
		#
		# jet selections
		#
		######################
		selected_jet_idx = []
		selected_jet_pt = []
		for jet_Idx in range (intree_.nJet):
			if intree_.Jet_pt[jet_Idx] > 20 and abs(intree_.Jet_eta[jet_Idx]) < 2.4 and intree_.Jet_jetId >= 7:
				selected_jet_idx.append(jet_Idx)
				selected_jet_pt.append(intree_.Jet_pt[jet_Idx])
		
		if len(selected_jet_idx) < 1: continue
		dict_variableName_Leaves["nSelectedJets"][0][0] = len(selected_jet_idx)
		dict_variableName_Leaves["LeadingJet_Pt"][0][0] = max(selected_jet_pt)
			
		
		
		
		######################
		#
		# MadGraph Reweighting weights
		#
		######################
		for rwgt_idx,weight_name in match_index_to_weight.iteritems():
			if private: dict_variableName_Leaves[weight_name][0][0] = intree_.LHEReweightingWeight[rwgt_idx]
			else: dict_variableName_Leaves[weight_name][0][0] = 1.

		otree_.Fill()
	# ***************** end of  event loop ********************
	
	print ""
	print "%s: Selected %i/%i (%.3f%%) of events"%(sampletag,otree_.GetEntries(),relative_nevents,100*float(otree_.GetEntries())/float(relative_nevents))

	
	
	
	
	
	
	ofile_.cd()
	hweight.Write()
	otree_.Write()

	ofile_.Close()
	
	print ""
	print "output stored in %s"%outfile



def main():

	parser = ArgumentParser()
	parser.add_argument('--sampletag', default="FILLMEPLEASE",help='tag for the sample that corresponds to the entry in the sampledict')
	parser.add_argument('--outfile', default="FILLMEPLEASE",help='path and name of output file')
	parser.add_argument('--sampledict', default="FILLMEPLEASE",help='path to the sample dictionary created by "samples.py"')
	parser.add_argument('--firstEvt', type=int, default=0,help='first event')
	parser.add_argument('--lastEvt', type=int, default=-1,help='last event')
	parser.add_argument('--splitted', type=int, default=0,help='bool for splitted or not')
	parser.add_argument('--private', type=int, default=0,help='private production (1) or central production (0)')
	args = parser.parse_args()

	Analyze_nanoAOD(args.sampletag, args.outfile, args.sampledict, args.private, args.firstEvt, args.lastEvt, bool(args.splitted))



if __name__ == "__main__":
	main()


