
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
	match_index_to_weight.update({1:"weight_kcm10"})
	match_index_to_weight.update({2:"weight_kc5"})
	match_index_to_weight.update({3:"weight_kc10"})
	match_index_to_weight.update({4:"weight_SM"})
	match_index_to_weight.update({5:"weight_kcm0p5"})
	match_index_to_weight.update({6:"weight_kc0p5"})
        match_index_to_weight.update({7:"weight_kc0"})
        match_index_to_weight.update({8:"weight_kcm2"})
        match_index_to_weight.update({9:"weight_kcm1"})
        match_index_to_weight.update({10:"weight_kcm5"})
        for idx,weight_name in match_index_to_weight.iteritems():
		dict_variableName_Leaves.update({weight_name: [array('d', [0]),"D"]})
	
	
	# JETS
	dict_variableName_Leaves.update({"nSelectedJets": [array('d', [0]),"D"]}) # number of jets passing the event selections criteria
	dict_variableName_Leaves.update({"LeadingJet_Pt": [array('d', [0]),"D"]}) # Transverse momentum of the hardest jet
	
	#LEPTONS
	dict_variableName_Leaves.update({"nSelectedMuons": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon1_pt": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon2_pt": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon3_pt": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon4_pt": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon1_eta": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon2_eta": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon3_eta": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon4_eta": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon_deltaR_12": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon_deltaR_13": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon_deltaR_14": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon_deltaR_23": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon_deltaR_24": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"Muon_deltaR_34": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"MuonPair_deltaR": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"MuonPair_InvMass": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"MuonsInvariantMass": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"CvsL": [array('d', [0]), "D"]})
        dict_variableName_Leaves.update({"CvsB": [array('d', [0]), "D"]})
        
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
                leading_jetpt_idx = selected_jet_idx[selected_jet_pt.index(max(selected_jet_pt))]

		######################
                #
                # muon selections
                #
                ######################
		selected_muon_idx = []
                selected_muon_pt = []
                selected_muon_eta = []
                # Loop over de muonen:
                for m_idx in range(intree_.nMuon):
                        # selecteer enkel muonen met pT>25 |eta|<2.4 :
                        if intree_.Muon_pt[m_idx] > 10 and abs(intree_.Muon_eta[m_idx]) < 2.4:
                                selected_muon_idx.append(m_idx)
                                selected_muon_pt.append(intree_.Muon_pt[m_idx])
        
                #  vraag minstens 4 muonen die hieraan voldoen:
                if len(selected_muon_idx) < 4: continue
                dict_variableName_Leaves["nSelectedMuons"][0][0] = len(selected_muon_idx)
                
                # Sorts from highest pt to lowest
                muon_info_combined = zip(selected_muon_pt, selected_muon_idx)
                muon_info_combined = sorted(muon_info_combined, reverse=True)
                # Sort idx array according to pt (from highest to lowest)
                selected_muon_idx = [y for x,y in muon_info_combined]
                
                if intree_.Muon_pt[selected_muon_idx[0]] < 20:
                        continue
                if intree_.Muon_pt[selected_muon_idx[1]] < 10:
                        continue
                
                dict_variableName_Leaves["Muon1_pt"][0][0] = intree_.Muon_pt[selected_muon_idx[0]]
                dict_variableName_Leaves["Muon2_pt"][0][0] = intree_.Muon_pt[selected_muon_idx[1]]
                dict_variableName_Leaves["Muon3_pt"][0][0] = intree_.Muon_pt[selected_muon_idx[2]]
                dict_variableName_Leaves["Muon4_pt"][0][0] = intree_.Muon_pt[selected_muon_idx[3]] 

                dict_variableName_Leaves["Muon1_eta"][0][0] = intree_.Muon_eta[selected_muon_idx[0]]
                dict_variableName_Leaves["Muon2_eta"][0][0] = intree_.Muon_eta[selected_muon_idx[1]]
                dict_variableName_Leaves["Muon3_eta"][0][0] = intree_.Muon_eta[selected_muon_idx[2]]
                dict_variableName_Leaves["Muon4_eta"][0][0] = intree_.Muon_eta[selected_muon_idx[3]]
                
                FourVector_Muon1 = ROOT.TLorentzVector()
                FourVector_Muon2 = ROOT.TLorentzVector()
                FourVector_Muon3 = ROOT.TLorentzVector()
                FourVector_Muon4 = ROOT.TLorentzVector()

                FourVector_Muon1.SetPtEtaPhiM(intree_.Muon_pt[selected_muon_idx[0]], intree_.Muon_eta[selected_muon_idx[0]], intree_.Muon_phi[selected_muon_idx[0]], intree_.Muon_mass[selected_muon_idx[0]])
                FourVector_Muon2.SetPtEtaPhiM(intree_.Muon_pt[selected_muon_idx[1]], intree_.Muon_eta[selected_muon_idx[1]], intree_.Muon_phi[selected_muon_idx[1]], intree_.Muon_mass[selected_muon_idx[1]])
                FourVector_Muon3.SetPtEtaPhiM(intree_.Muon_pt[selected_muon_idx[2]], intree_.Muon_eta[selected_muon_idx[2]], intree_.Muon_phi[selected_muon_idx[2]], intree_.Muon_mass[selected_muon_idx[2]])
                FourVector_Muon4.SetPtEtaPhiM(intree_.Muon_pt[selected_muon_idx[3]], intree_.Muon_eta[selected_muon_idx[3]], intree_.Muon_phi[selected_muon_idx[3]], intree_.Muon_mass[selected_muon_idx[3]])
                
                FourVector_Sum = FourVector_Muon1 + FourVector_Muon2 + FourVector_Muon3 + FourVector_Muon4

                InvariantMass = FourVector_Sum.M()

                if (InvariantMass < 100) or (InvariantMass > 150): continue
                
                dict_variableName_Leaves["MuonsInvariantMass"][0][0] = InvariantMass

                dict_variableName_Leaves["Muon_deltaR_12"][0][0] = FourVector_Muon1.DeltaR(FourVector_Muon2)
                dict_variableName_Leaves["Muon_deltaR_13"][0][0] = FourVector_Muon1.DeltaR(FourVector_Muon3)
                dict_variableName_Leaves["Muon_deltaR_14"][0][0] = FourVector_Muon1.DeltaR(FourVector_Muon4)
                dict_variableName_Leaves["Muon_deltaR_23"][0][0] = FourVector_Muon2.DeltaR(FourVector_Muon3)
                dict_variableName_Leaves["Muon_deltaR_24"][0][0] = FourVector_Muon2.DeltaR(FourVector_Muon4)
                dict_variableName_Leaves["Muon_deltaR_34"][0][0] = FourVector_Muon3.DeltaR(FourVector_Muon4)

                # Select muon pair with invariant mass closest to the Z-boson mass. Thus the pair for which | M - MZ | is smallest.
                # Also check whether the pair has opposite charge.
                FourVector_Muons = [FourVector_Muon1, FourVector_Muon2, FourVector_Muon3, FourVector_Muon4]
                Combinations = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
                InvMass = []
                InvMass_Diffs = []
                for i, j in Combinations:
                        V_Sum = FourVector_Muons[i-1] + FourVector_Muons[j-1]
                        InvMass_Dif = abs(V_Sum.M() - 91.18)
                        InvMass_Diffs.append(InvMass_Dif)
                        InvMass.append(V_Sum.M())
                # Pair closest to Z boson mass: sort Combinations according to InvMass_Diff
                TempSortingArray = zip(InvMass_Diffs, Combinations)
                TempSortingArray = sorted(TempSortingArray)
                CombSorted = [comb for m, comb in TempSortingArray]
                SelectedPair = CombSorted[0]
                # Check whether the selected pair has opposite charge:
                pair_idx = 1
                pair_found = True
                while intree_.Muon_charge[selected_muon_idx[SelectedPair[0]-1]] != -intree_.Muon_charge[selected_muon_idx[SelectedPair[1]-1]]:
                        if pair_idx > 5:
                                pair_found = False
                                break
                        SelectedPair = CombSorted[pair_idx]
                        pair_idx += 1

                if not pair_found: continue

                # Invariant Mass Cut:
                MuonPair_InvMass = InvMass[Combinations.index(SelectedPair)]
                if (MuonPair_InvMass < 70) or (MuonPair_InvMass > 110): continue
                
                # Find other Z candidate:
                OtherPair = ()
                for pair in Combinations:
                        if (pair[0] not in SelectedPair) and (pair[1] not in SelectedPair):
                                OtherPair = pair
                
                OtherPair_InvMass = InvMass[Combinations.index(OtherPair)]
                if (OtherPair_InvMass < 50) and (OtherPair_InvMass > 130): continue
                
                # Check if other Z candidate has opposite sign muons:
                if intree_.Muon_charge[selected_muon_idx[OtherPair[0]-1]] != -intree_.Muon_charge[selected_muon_idx[OtherPair[1]-1]]: continue
                
                dict_variableName_Leaves["MuonPair_deltaR"][0][0] = FourVector_Muons[SelectedPair[0]-1].DeltaR(FourVector_Muons[SelectedPair[1]-1])
                dict_variableName_Leaves["MuonPair_InvMass"][0][0] = MuonPair_InvMass

                CvsL = float(intree_.Jet_btagDeepFlavC[leading_jetpt_idx])/(1. -float(intree_.Jet_btagDeepFlavB[leading_jetpt_idx]))
                CvsB = float(intree_.Jet_btagDeepFlavC[leading_jetpt_idx])/(float(intree_.Jet_btagDeepFlavC[leading_jetpt_idx]) + float(intree_.Jet_btagDeepFlavB[leading_jetpt_idx]))
                dict_variableName_Leaves["CvsL"][0][0] = CvsL
                dict_variableName_Leaves["CvsB"][0][0] = CvsB
                
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


