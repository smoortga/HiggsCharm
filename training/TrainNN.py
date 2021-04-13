import ROOT
import sys
import os
import time
import pickle
from argparse import ArgumentParser
from array import array
from math import *
import numpy as np
import root_numpy as rootnp
from array import array
import re

import keras as K

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score

# from keras.models import Sequential, load_model
# from keras.layers import Dense, Activation, Dropout
# from keras.callbacks import ModelCheckpoint
# from keras.optimizers import SGD


"""

python TrainNN.py \
--indir=/pnfs/iihe/cms/store/user/nbreugel/HiggsCharm/Selection/ \
--nepoch=20 \
--tag=test2

python TrainNN.py \
--indir=/pnfs/iihe/cms/store/user/nbreugel/HiggsCharm/Selection/ \
--nepoch=10 \
--tag=test \
--TrainingFile=/storage_mnt/storage/user/smoortga/HiggsCharm/training/test/model_checkpoint_save.hdf5

"""        

def makeROC(signal_tag, bkg_tag, category_dict, model, X_test, y_test, output, model_tag):

	target_label_signal  = list(category_dict.keys())[list([i["tag"] for i in category_dict.values()]).index(signal_tag)]
	target_label_bkg	 = list(category_dict.keys())[list([i["tag"] for i in category_dict.values()]).index(bkg_tag)]
	
	pred_signalTruth = model.predict(X_test[y_test == target_label_signal])
	pred_ProbSig_signalTruth = pred_signalTruth[:,target_label_signal]
	pred_Probbkg_signalTruth = pred_signalTruth[:,target_label_bkg]
	discr_signalTruth = [(i)/(i+j) for i,j in zip(pred_ProbSig_signalTruth,pred_Probbkg_signalTruth)]
	
	pred_bkgTruth = model.predict(X_test[y_test == target_label_bkg])
	pred_ProbSig_bkgTruth = pred_bkgTruth[:,target_label_signal]
	pred_Probbkg_bkgTruth = pred_bkgTruth[:,target_label_bkg]
	discr_bkgTruth = [(i)/(i+j) for i,j in zip(pred_ProbSig_bkgTruth,pred_Probbkg_bkgTruth)]
	
	fpr, tpr, thres = roc_curve( np.concatenate(( np.ones(len(discr_signalTruth)),np.zeros(len(discr_bkgTruth)) )),np.concatenate((discr_signalTruth,discr_bkgTruth)) )
	AUC = 1-roc_auc_score( np.concatenate(( np.ones(len(discr_signalTruth)),np.zeros(len(discr_bkgTruth)) )),np.concatenate((discr_signalTruth,discr_bkgTruth)) )
	
        pickle.dump([fpr, tpr, AUC],open(os.getcwd() + "/"+ model_tag +"/fpr_and_tpr_%s_VERSUS_%s.pkl"%(signal_tag, bkg_tag),'wb'))
        
	print "AUC for %s vs. %s is: %.3f"%(signal_tag, bkg_tag, AUC)

	
	#
	# CREATE ROC
	#
	
	c = ROOT.TCanvas("c","c",700,600)
	ROOT.gPad.SetMargin(0.15,0.07,0.15,0.07)
	ROOT.gPad.SetLogy(0)
	ROOT.gPad.SetGrid(1,1)
	ROOT.gStyle.SetGridColor(15)

        
	
	roc = ROOT.TGraph(len(fpr),tpr,fpr)

	roc.SetLineColor(2)
	roc.SetLineWidth(2)
	roc.SetTitle(";Signal efficiency (%s); Background efficiency (%s)"%(signal_tag, bkg_tag))
	roc.GetXaxis().SetTitleOffset(1.4)
	roc.GetXaxis().SetTitleSize(0.045)
	roc.GetYaxis().SetTitleOffset(1.4)
	roc.GetYaxis().SetTitleSize(0.045)
	roc.GetXaxis().SetRangeUser(0,1)
	roc.GetYaxis().SetRangeUser(0.000,1)
	roc.Draw("AL")
	
	diag = ROOT.TGraph(2,array('d',[0,1]),array('d',[0,1]))
	diag.SetLineStyle(2)
	diag.SetLineWidth(2)
	diag.SetLineColor(13)
	diag.Draw("same L")

	latex = ROOT.TLatex()
	latex.SetTextFont(43)
	latex.SetTextSize(25)
	latex.DrawLatexNDC(0.2,0.88,'AUC = %.3f'%AUC)
	latex.SetTextSize(20)
	latex.DrawLatexNDC(0.2,0.79,'#splitline{discriminator =}{#frac{P(%s)}{P(%s)+P(%s)}}'%(signal_tag, signal_tag, bkg_tag))
	
	latex.SetTextFont(43)
	latex.SetTextSize(35)
	latex.SetTextAlign(31)
	latex.DrawLatexNDC(0.93,0.95,"13 TeV")

	latex_cms = ROOT.TLatex()
	latex_cms.SetTextFont(43)
	latex_cms.SetTextSize(35)
	latex_cms.SetTextAlign(11)
	latex_cms.DrawLatexNDC(0.15,0.95,"#bf{CMS} #it{Preliminary}")
	#latex_cms.DrawLatexNDC(0.19,0.83,"#bf{CMS} #it{Simulation}")
	#latex_cms.DrawLatexNDC(0.19,0.83,"#bf{CMS}")

	c.SaveAs(output+".pdf")
	c.SaveAs(output+".png")
	
	#
	# CREATE ALSO DISCRIMINATOR DISTRIBUTIONS
	#
	
	c2 = ROOT.TCanvas("c2","c2",800,600)
	ROOT.gPad.SetMargin(0.15,0.07,0.20,0.07)
	#ROOT.gPad.SetLogy(0)
	
	hist_signalTruth = ROOT.TH1D("hist_signalTruth",";#frac{P(%s)}{P(%s)+P(%s)};Events (a.u.)"%(signal_tag, signal_tag, bkg_tag),20,0,1)
	hist_signalTruth.SetLineColor(2)
	hist_signalTruth.SetLineWidth(2)
	hist_bkgTruth = ROOT.TH1D("hist_bkgTruth",";#frac{P(%s)}{P(%s)+P(%s)};Events (a.u.)"%(signal_tag, signal_tag, bkg_tag),20,0,1)
	hist_bkgTruth.SetLineColor(4)
	hist_bkgTruth.SetLineWidth(2)
	
	hist_signalTruth.FillN(len(discr_signalTruth), array("d",discr_signalTruth), array("d",[1]*len(discr_signalTruth)))
	hist_signalTruth.Scale(1./hist_signalTruth.Integral())
	hist_bkgTruth.FillN(len(discr_bkgTruth), array("d",discr_bkgTruth), array("d",[1]*len(discr_bkgTruth)))
	hist_bkgTruth.Scale(1./hist_bkgTruth.Integral())
	
	hist_bkgTruth.Draw("hist")
	hist_bkgTruth.GetXaxis().SetLabelFont(43)
	hist_bkgTruth.GetXaxis().SetLabelSize(25)
	hist_bkgTruth.GetXaxis().SetTitleFont(43)
	hist_bkgTruth.GetXaxis().SetTitleSize(30)
	hist_bkgTruth.GetXaxis().SetTitleOffset(1.35)
	hist_bkgTruth.GetYaxis().SetLabelFont(43)
	hist_bkgTruth.GetYaxis().SetLabelSize(25)
	hist_bkgTruth.GetYaxis().SetTitleFont(43)
	hist_bkgTruth.GetYaxis().SetTitleSize(30)
	hist_bkgTruth.GetYaxis().SetTitleOffset(1.25)
	height = 1.5*max(hist_bkgTruth.GetBinContent(hist_bkgTruth.GetMaximumBin()),hist_signalTruth.GetBinContent(hist_signalTruth.GetMaximumBin()))
	hist_bkgTruth.GetYaxis().SetRangeUser(0,height)
	hist_signalTruth.Draw("hist same")
	
	latex.DrawLatexNDC(0.93,0.95,"13 TeV")
	latex_cms.DrawLatexNDC(0.15,0.95,"#bf{CMS} #it{Preliminary}")
	
	l = ROOT.TLegend(0.59,0.75,0.92,0.91)
	l.SetBorderSize(0)
	l.SetFillStyle(0)
	l.SetTextFont(43)
	l.SetTextSize(30)
	l.AddEntry(hist_bkgTruth,bkg_tag,"l")
	l.AddEntry(hist_signalTruth,signal_tag,"l")
	l.Draw("same")

	
	c2.SaveAs(output.replace("ROC","Discriminator")+".pdf")
	c2.SaveAs(output.replace("ROC","Discriminator")+".png")
	
	

def drawTrainingCurve(input,output):
	hist = pickle.load(open(input,"rb"))
	tr_acc = hist["acc"]
	tr_loss = hist["loss"]
	val_acc = hist["val_acc"]
	val_loss = hist["val_loss"]
	epochs = [i+1 for i in range(len(tr_acc))]

	c = ROOT.TCanvas("c","c",800,500)
	ROOT.gStyle.SetOptStat(0)
	uppad = ROOT.TPad("u","u",0.,0.55,1.,1.)
	downpad = ROOT.TPad("d","d",0.,0.,1.,0.55)
	uppad.Draw()
	downpad.Draw()
	uppad.cd()
	ROOT.gPad.SetMargin(0.15,0.05,0.02,0.15)
	ROOT.gPad.SetGrid(1,1)
	ROOT.gStyle.SetGridColor(13)

	gr_acc_train = ROOT.TGraph(len(epochs),array('d',epochs),array('d',tr_acc))
	gr_acc_train.SetLineColor(2)
	gr_acc_train.SetLineWidth(2)
	gr_acc_test = ROOT.TGraph(len(epochs),array('d',epochs),array('d',val_acc))
	gr_acc_test.SetLineColor(4)
	gr_acc_test.SetLineWidth(2)

	mgup = ROOT.TMultiGraph("mgup",";number of epochs;accuracy")
	mgup.Add(gr_acc_train,"l")
	mgup.Add(gr_acc_test,"l")
	mgup.Draw("AL")
	mgup.GetXaxis().SetRangeUser(min(epochs),max(epochs))
	mgup.GetXaxis().SetLabelSize(0)
	mgup.GetYaxis().CenterTitle()
	mgup.GetYaxis().SetTitleSize(0.12)
	mgup.GetYaxis().SetTitleOffset(0.5)
	mgup.GetYaxis().SetLabelSize(0.105)
	mgup.GetYaxis().SetNdivisions(8)

	l = ROOT.TLegend(0.6,0.15,0.88,0.6)
	l.SetTextSize(0.14)
	l.AddEntry(gr_acc_train,"training","l")
	l.AddEntry(gr_acc_test,"validation","l")
	l.Draw("same")

	downpad.cd()
	ROOT.gPad.SetMargin(0.15,0.05,0.25,0.02)
	ROOT.gPad.SetGrid(1,1)
	ROOT.gStyle.SetGridColor(13)

	gr_loss_train = ROOT.TGraph(len(epochs),array('d',epochs),array('d',tr_loss))
	gr_loss_train.SetLineColor(2)
	gr_loss_train.SetLineWidth(2)
	gr_loss_test = ROOT.TGraph(len(epochs),array('d',epochs),array('d',val_loss))
	gr_loss_test.SetLineColor(4)
	gr_loss_test.SetLineWidth(2)

	mgdown = ROOT.TMultiGraph("mgdown",";number of epochs;loss")
	mgdown.Add(gr_loss_train,"l")
	mgdown.Add(gr_loss_test,"l")
	mgdown.Draw("AL")
	mgdown.GetXaxis().SetRangeUser(min(epochs),max(epochs))
	mgdown.GetXaxis().SetLabelSize(0.085)
	mgdown.GetXaxis().SetTitleSize(0.11)
	mgdown.GetXaxis().SetTitleOffset(0.9)
	mgdown.GetXaxis().CenterTitle()
	mgdown.GetYaxis().CenterTitle()
	mgdown.GetYaxis().SetTitleSize(0.11)
	mgdown.GetYaxis().SetTitleOffset(0.55)
	mgdown.GetYaxis().SetLabelSize(0.085)
	mgdown.GetYaxis().SetNdivisions(8)

	c.SaveAs(output+".pdf")
	c.SaveAs(output+".png")


def main():
	
	parser = ArgumentParser()
	parser.add_argument('--nepoch', type=int, default=50,help='number of epochs to run the training for')
	parser.add_argument('--TrainingFile', default = "", help='path to training') # this can be useful when you want to continue training from an existing model or for validation...
	parser.add_argument('--indir', default = "/pnfs/iihe/cms/store/user/nbreugel/HiggsCharm/Selection/", help='path to the training files')
	parser.add_argument('--tag', default=time.strftime("%a%d%b%Y_%Hh%Mm%Ss"),help='name of output directory')
	parser.add_argument('--skipEvery', type=int, default=1,help='ignore one entry every X')
	parser.add_argument('--verbose', type=int, default=1,help='verbosity of training')
	args = parser.parse_args()
	
	ROOT.gROOT.SetBatch(1)
	ROOT.gStyle.SetOptStat(0)
	
	#***********************
	#
	# DEFINE OUTPUT DIRECTORY
	#
	#***********************
	
	if not os.path.isdir(os.getcwd() + "/"+args.tag): os.mkdir(os.getcwd() + "/"+args.tag)
	
	#***********************
	#
	# DEFINE INPUT VARIABLES
	#
	#***********************
	
        Leading_CvL_vars = [
        "LeadingCvLJet_Pt",
        "CvsL_LeadingCvLJet",
        "LeadingCvLJet_Eta"
        ]

        Leading_Pt_vars = [
        "LeadingPtJet_Pt",
        "CvsL_LeadingPtJet",
        "LeadingPtJet_Eta"
        ]

        Leading_CvB_vars = [
        "LeadingCvBJet_Pt",
        "LeadingCvBJet_Eta",
        "CvsL_LeadingCvBJet",
        "CvsB_LeadingCvBJet",
        "CvsB_LeadingCvLJet",
        "CvsB_LeadingPtJet"
        ]

        Subleading_CvL_vars = [
        "SubleadingCvLJet_Pt",
        "CvsL_SubleadingCvLJet",
        "SubleadingCvLJet_Eta"
        ]

        Subleading_Pt_vars = [
        "SubleadingPtJet_Pt",
        "CvsL_SubleadingPtJet",
        "SubleadingPtJet_Eta"
        ]

        Subleading_CvB_vars = [
        "SubleadingCvBJet_Pt",
        "SubleadingCvBJet_Eta",
        "CvsL_SubleadingCvBJet",
        "CvsB_SubleadingCvBJet",
        "CvsB_SubleadingCvLJet",
        "CvsB_SubleadingPtJet"
        ]

        Subsubleading_CvL_vars = [
        "SubsubleadingCvLJet_Pt",
        "CvsL_SubsubleadingCvLJet",
        "SubsubleadingCvLJet_Eta"
        ]

        Subsubleading_Pt_vars = [
        "SubsubleadingPtJet_Pt",
        "CvsL_SubsubleadingPtJet",
        "SubsubleadingPtJet_Eta"
        ]

        Subsubleading_CvB_vars = [
        "SubsubleadingCvBJet_Pt",
        "SubsubleadingCvBJet_Eta",
        "CvsL_SubsubleadingCvBJet",
        "CvsB_SubsubleadingCvBJet",
        "CvsB_SubsubleadingCvLJet",
        "CvsB_SubsubleadingPtJet"
        ]

        Muon_Jet_deltaR_vars = [
        "LeadingPtJet_Muon1_deltaR",
        "LeadingPtJet_Muon2_deltaR",
        "LeadingPtJet_Muon3_deltaR",
        "LeadingPtJet_Muon4_deltaR",
        "LeadingCvLJet_Muon1_deltaR",
        "LeadingCvLJet_Muon2_deltaR",
        "LeadingCvLJet_Muon3_deltaR",
        "LeadingCvLJet_Muon4_deltaR"
        ]

        Muon_Kinematics_vars = [
        "Muon1_pt",
        "Muon2_pt",
        "Muon3_pt",
        "Muon4_pt",
        "Muon1_eta",
        "Muon2_eta",
        "Muon3_eta",
        "Muon4_eta"
        ]

        MuonPair_Kinematics_vars = [
        "MuonPair1_InvMass",
        "MuonPair2_InvMass",
        "MuonPair1_deltaR",
        "MuonPair2_deltaR"
        ]
        
	base_variables = [
        "MuonsInvariantMass"
	]

        Leading_All_vars = Leading_CvL_vars + Leading_Pt_vars + Leading_CvB_vars
        Subleading_All_vars = Subleading_CvL_vars + Subleading_Pt_vars + Subleading_CvB_vars
        Subsubleading_All_vars = Subsubleading_CvL_vars + Subsubleading_Pt_vars + Subsubleading_CvB_vars

        variables = []

        m = re.search(r'\d+$', args.tag)
        Model_Number = int(m.group())
        
        if not args.TrainingFile:
                                        
                if Model_Number == 1:
                        variables = base_variables + Leading_All_vars + Subleading_All_vars
                elif Model_Number == 2:
                        variables = base_variables + Leading_All_vars + Subleading_All_vars + Subsubleading_All_vars
                elif Model_Number == 3:
                        variables = base_variables + Leading_All_vars
                elif Model_Number == 4:
                        variables = base_variables + Leading_All_vars + Muon_Jet_deltaR_vars + Muon_Kinematics_vars + MuonPair_Kinematics_vars
                elif Model_Number == 5:
                        variables = base_variables + Leading_All_vars + Muon_Jet_deltaR_vars + Muon_Kinematics_vars + MuonPair_Kinematics_vars + Subleading_All_vars
                elif Model_Number == 10:
                        variables = base_variables
                elif Model_Number == 11:
                        variables = ["LeadingPtJet_Pt", "SubleadingPtJet_Pt", "SubsubleadingPtJet_Pt"]
                elif Model_Number == 12:
                        variables = ["LeadingPtJet_Pt", "LeadingCvLJet_Pt", "LeadingCvBJet_Pt"]
                else:
                        variables = base_variables + Leading_All_vars + Muon_Jet_deltaR_vars + Muon_Kinematics_vars + MuonPair_Kinematics_vars + Subleading_All_vars
	
                pickle.dump(variables,open(os.getcwd() + "/"+args.tag+"/variables.pkl",'wb'))

        else:
                variables = pickle.load(open(os.getcwd() + "/"+args.tag+"/variables.pkl",'rb'))
                print("Variables loaded!")
                print(variables)
	
	#***********************
	#
	# DEFINE SAMPLES/CATEGORIES
	# (one entry per output category)
	#
	#***********************
	
	category_dict = {
	0:    {"info":"qg #rightarrow Hc, diagrams sensitive to yc)",
			"tag":"qgToHc_yc",
			"samples":["selected_HcTo4mu"],
			"selection":"(weight_kc2 >= 2)",
			},
	1:    {"info":"qg #rightarrow Hc, diagrams not sensitive to yc)",
			"tag":"qgToHc_noyc",
			"samples":["selected_HcTo4mu"],
			"selection":"(weight_kc2 < 2)",
			},
	2:    {"info":"gg #rightarrow Hj (SM)",
			"tag":"ggToHj",
			"samples":["selected_GluGluToHiggs0MToZZTo4L","selected_VBF_HToZZTo4L", "selected_WplusH_HToZZTo4L", "selected_WminH_HToZZTo4L", "selected_ZH_HToZZTo4L", "selected_ttH_HToZZTo4L"],
			"selection":"1", # "1" is no selection
			},
	3:    {"info":"ZZ #rightarrow 4L (no Higgs) (SM)",
			"tag":"ZZ_noH",
			"samples":["selected_GluGluToContinToZZTo4mu", "selected_QQToZZTo4L"],
			"selection":"1", # "1" is no selection
			},
	# ADD MORE SAMPLES / OUTPUT CATEGORIES HERE	
	}
	
	nb_classes = len(category_dict.keys())
	
	#***********************
	#
	# READ SAMPLE CONTENT
	#
	#***********************
	
	print ""
	print "******** READING SAMPLES ************"
	print ""
	
	total_nevents = 0
	for target_id, samples_dict in category_dict.iteritems():
		for f_idx,f_ in enumerate(samples_dict["samples"]):
			assert os.path.isfile(args.indir+f_+".root"), "ERROR, did not find file %s"%(args.indir+f_+".root")
			
			f_ = ROOT.TFile(args.indir+f_+".root")
			tree = f_.Get("tree")
			
			X_tmp = rootnp.tree2array(tree,variables,"1*"+samples_dict["selection"],step=args.skipEvery)
			X_tmp = rootnp.rec2array(X_tmp)
			y_tmp = np.full(len(X_tmp),target_id)
			Y_tmp = K.utils.np_utils.to_categorical(y_tmp.astype(int), nb_classes)
			w_tmp = np.full(len(X_tmp),1./len(X_tmp))
			total_nevents += len(X_tmp)
			
			print samples_dict["info"]
			print "number of entries: ", len(X_tmp)
			print "target: ",Y_tmp[0]
			print ""
			
			if target_id == 0 and f_idx == 0:
				X = X_tmp
				y = y_tmp
				Y = Y_tmp
				w = w_tmp
			else:
				X = np.concatenate((X,X_tmp))
				y = np.concatenate((y,y_tmp))
				Y = np.concatenate((Y,Y_tmp))
				w = np.concatenate((w,w_tmp)) 
			
			
			
			f_.Close()
	
	# weight for each sample = total/n_sample
	w = w*float(total_nevents)
	list_of_all_samples = []
	for target_id, samples_dict in category_dict.iteritems():
		for sample_ in samples_dict["samples"]:
			list_of_all_samples.append(sample_)
		
	for idx, weight in enumerate(set(w)):
		print "weight for the sample:"
		print list_of_all_samples[idx]
		print "--> ", weight
	
	#***********************
	#
	# SCALING INPUT FEATURES
	# (mean around 0 and std.dev. around 1)
	#
	#***********************
	
	print ""
	print "******** SCALING INPUTS ************"
	print ""

	scaler = StandardScaler()
	scaler.fit(X)
	print "storing output 'scaler.pkl' in %s"%(os.getcwd() + "/"+args.tag)
	pickle.dump(scaler,open(os.getcwd() + "/"+args.tag+"/scaler.pkl",'wb'))
	X = scaler.transform(X)
	
	
	#***********************
	#
	# SPLITTING TRAINING AND TESTING SETS
	#
	#***********************
	
	print ""
	print "******** SPLITTING TRAIN/TEST ************"
	print ""
	
	fraction_for_testing = 0.25
	X_train, X_test , y_train, y_test, Y_train, Y_test, w_train, w_test = train_test_split(X, y, Y, w, test_size=fraction_for_testing)
	

	#***********************
	#
	# BUILDING MODEL
	#
	#***********************
	
	# --------> Enter parameters here < ---------------
	init_learning_rate_sgd = 0.0005
	nb_epoch = args.nepoch
	momentum_sgd = 0.8
	batch_size = 256
	dropout = 0.1
	# -------------------------------------------------
	
	# if a training file has been provided as input, you don't have to train, only validate.
	if args.TrainingFile == "": 
		print ""
		print "******** BUILDING MODEL ************"
		print ""
	
		input_dim = X_train.shape[1:]
	
		decay_sgd = init_learning_rate_sgd/float(nb_epoch) if nb_epoch !=0 else 0.0001
		sgd = K.optimizers.SGD(lr=init_learning_rate_sgd, decay=decay_sgd, momentum=momentum_sgd, nesterov=True)
	
		model = K.models.Sequential()
                
                nNeuronsFirstLayer = 20
                nNeuronsSecondLayer = 0
                SecondLayer = False
                if Model_Number == 6:
                        nNeuronsFirstLayer = 40
                        nNeuronsSecondLayer = 30
                        SecondLayer = True
                elif Model_Number == 7:
                        nNeuronsFirstLayer = 30
                        nNeuronsSecondLayer = 20
                        SecondLayer = True
                elif Model_Number == 8:
                        nNeuronsFirstLayer = 20
                        nNeuronsSecondLayer = 10
                        SecondLayer = True
                elif Model_Number == 13:
                        nNeuronsFirstLayer = 60
                        nNeuronsSecondLayer = 40
                        SecondLayer = True
                elif Model_Number == 14:
                        nNeuronsFirstLayer = 50
                        nNeuronsSecondLayer = 40
                        SecondLayer = True
                elif Model_Number == 15:
                        nNeuronsFirstLayer = 40
                        nNeuronsSecondLayer = 40
                        SecondLayer = True
                elif Model_Number == 16:
                        nNeuronsFirstLayer = 25
                elif Model_Number == 17:
                        nNeuronsFirstLayer = 30
                elif Model_Number == 18:
                        nNeuronsFirstLayer = 40
                        
                
		model.add(K.layers.Dense(nNeuronsFirstLayer ,input_shape= input_dim))
		model.add(K.layers.Activation('relu'))
		model.add(K.layers.Dropout(dropout))
                if SecondLayer:
                        model.add(K.layers.Dense(nNeuronsSecondLayer)) 
                        model.add(K.layers.Activation('relu'))
                        model.add(K.layers.Dropout(dropout))
                
		model.add(K.layers.Dense(nb_classes))
		model.add(K.layers.Activation('softmax'))

		model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
	
		print model.summary()
	
	
	#***********************
	#
	# TRAINING MODEL
	#
	#***********************
	
	
	
	if args.TrainingFile == "":
		print ""
		print "******** TRAINING MODEL ************"
		print ""
		train_history = model.fit(X_train, Y_train, sample_weight = w_train, batch_size=batch_size, epochs=args.nepoch, validation_data=(X_test, Y_test, w_test), callbacks = [K.callbacks.ModelCheckpoint(os.getcwd() + "/"+args.tag+"/model_checkpoint_save.hdf5")], shuffle=True ,verbose=args.verbose)
		pickle.dump(train_history.history,open(os.getcwd() + "/"+args.tag+"/loss_and_acc.pkl",'wb'))
		drawTrainingCurve(os.getcwd() + "/"+args.tag+"/loss_and_acc.pkl",os.getcwd() + "/"+args.tag+"/training_curve")
	
	else:
		print ""
		print "NOT TRAINING (ONLY VALIDATION IS RAN)! USING TRAINED MODEL (args.TrainingFile)"
		print ""
		model = K.models.load_model(args.TrainingFile)
		print model.summary()
	
	#***********************
	#
	# VALIDATION (output+ROC)
	#
	#***********************
	
	print ""
	print "******** VALIDATING MODEL ************"
	print ""
	
	makeROC("qgToHc_yc", "ggToHj", category_dict, model, X_test, y_test, os.getcwd() + "/"+args.tag+"/ROC_qgToHc_yc_VERSUS_ggToHj", args.tag)
	makeROC("qgToHc_yc", "ZZ_noH", category_dict, model, X_test, y_test, os.getcwd() + "/"+args.tag+"/ROC_qgToHc_yc_VERSUS_ZZ_noH", args.tag)
        makeROC("qgToHc_yc", "qgToHc_noyc", category_dict, model, X_test, y_test, os.getcwd() + "/"+args.tag+"/ROC_qgToHc_yc_VERSUS_qgToHc_noyc", args.tag)
	makeROC("qgToHc_noyc", "ggToHj", category_dict, model, X_test, y_test, os.getcwd() + "/"+args.tag+"/ROC_qgToHc_noyc_VERSUS_ggToHj", args.tag)
        makeROC("qgToHc_noyc", "ZZ_noH", category_dict, model, X_test, y_test, os.getcwd() + "/"+args.tag+"/ROC_qgToHc_noyc_VERSUS_ZZ_noH", args.tag)
        makeROC("ZZ_noH", "ggToHj", category_dict, model, X_test, y_test, os.getcwd() + "/"+args.tag+"/ROC_ZZ_noH_VERSUS_ggToHj", args.tag)

if __name__ == "__main__":
	main()
