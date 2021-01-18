import ROOT
import os
import sys
from argparse import ArgumentParser
#from xsec import xsec_table, color_table, legend_array
import pickle

ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptStat(0)

"""
EXAMPLE:

python PlotKappaCharmVariations.py \
--indir=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/Selection/ \
--outdir=./testing \
--sampledict=/storage_mnt/storage/user/smoortga/HiggsCharm/analyze/sample_dict.pkl

"""

parser = ArgumentParser()
parser.add_argument('--indir', default="FILL",help='input directory that contains all the samples')
parser.add_argument('--outdir', default=os.getcwd(),help='name of output directory')
parser.add_argument('--sampledict', default="/storage_mnt/storage/user/smoortga/HiggsCharm/analyze/sample_dict.pkl",help='path to the sample dictionary created by "samples.py"')
args = parser.parse_args()

samples_dict = pickle.load(open(args.sampledict,"rb"))

display_dict = {
	1:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 0)",
			"samples":["selected_HcTo4mu"],
			"tag":["HcTo4mu"],#used for xsec
			"color":ROOT.kCyan,
			"style":1,
			"weights":"weight_kc0",
			"reference":0
			},
	2:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 0.5)",
			"samples":["selected_HcTo4mu"],
			"tag":["HcTo4mu"],#used for xsec
			"color":ROOT.kGreen+2,
			"style":1,
			"weights":"weight_kc0p5",
			"reference":0
			},
	3:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 1, SM)",
			"samples":["selected_HcTo4mu"],
			"tag":["HcTo4mu"],#used for xsec
			"color":ROOT.kBlack,
			"style":1,
			"weights":"weight_kc1",
			"reference":1
			},
	4:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 2)",
			"samples":["selected_HcTo4mu"],
			"tag":["HcTo4mu"],#used for xsec
			"color":ROOT.kRed,
			"style":1,
			"weights":"weight_kc2",
			"reference":0
			},
	5:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 5)",
			"samples":["selected_HcTo4mu"],
			"tag":["HcTo4mu"],#used for xsec
			"color":ROOT.kOrange,
			"style":1,
			"weights":"weight_kc5",
			"reference":0
			},
	6:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 10)",
			"samples":["selected_HcTo4mu"],
			"tag":["HcTo4mu"],#used for xsec
			"color":ROOT.kBlue,
			"style":1,
			"weights":"weight_kc10",
			"reference":0
			},
	
	7:    {"legend":"gg #rightarrow Hj (SM)",
			"samples":["selected_GluGluToHiggs0MToZZTo4mu"],
			"tag":["GluGluToHiggs0MToZZTo4mu"],
			"color":ROOT.kGray,
			"style":1,
			"weights":"weight_kc1",
			"reference":0
			},

}

# display_dict = {
# 	1:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 0)",
# 			"samples":["selected_HcTo4mu","selected_GluGluToHiggs0MToZZTo4mu"],
# 			"tag":["HcTo4mu","GluGluToHiggs0MToZZTo4mu"],#used for xsec
# 			"color":ROOT.kCyan,
# 			"style":1,
# 			"weights":"weight_kc0",
# 			"reference":0
# 			},
# 	2:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 0.5)",
# 			"samples":["selected_HcTo4mu","selected_GluGluToHiggs0MToZZTo4mu"],
# 			"tag":["HcTo4mu","GluGluToHiggs0MToZZTo4mu"],#used for xsec
# 			"color":ROOT.kGreen+2,
# 			"style":1,
# 			"weights":"weight_kc0p5",
# 			"reference":0
# 			},
# 	3:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 1, SM)",
# 			"samples":["selected_HcTo4mu","selected_GluGluToHiggs0MToZZTo4mu"],
# 			"tag":["HcTo4mu","GluGluToHiggs0MToZZTo4mu"],#used for xsec
# 			"color":ROOT.kBlack,
# 			"style":1,
# 			"weights":"weight_kc0p5",
# 			"reference":1
# 			},
# 	4:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 2)",
# 			"samples":["selected_HcTo4mu","selected_GluGluToHiggs0MToZZTo4mu"],
# 			"tag":["HcTo4mu","GluGluToHiggs0MToZZTo4mu"],#used for xsec
# 			"color":ROOT.kRed,
# 			"style":1,
# 			"weights":"weight_kc2",
# 			"reference":0
# 			},
# 	5:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 5)",
# 			"samples":["selected_HcTo4mu","selected_GluGluToHiggs0MToZZTo4mu"],
# 			"tag":["HcTo4mu","GluGluToHiggs0MToZZTo4mu"],#used for xsec
# 			"color":ROOT.kOrange,
# 			"style":1,
# 			"weights":"weight_kc5",
# 			"reference":0
# 			},
# 	6:    {"legend":"qg #rightarrow Hc (#kappa_{c} = 10)",
# 			"samples":["selected_HcTo4mu","selected_GluGluToHiggs0MToZZTo4mu"],
# 			"tag":["HcTo4mu","GluGluToHiggs0MToZZTo4mu"],#used for xsec
# 			"color":ROOT.kBlue,
# 			"style":1,
# 			"weights":"weight_kc10",
# 			"reference":0
# 			},
# 	
# 	7:    {"legend":"gg #rightarrow Hj (SM)",
# 			"samples":["selected_GluGluToHiggs0MToZZTo4mu"],
# 			"tag":["GluGluToHiggs0MToZZTo4mu"],
# 			"color":ROOT.kGray,
# 			"style":1,
# 			"weights":"weight_kc1",
#			"reference":0
# 			},
# 
# }

def Plot1D(var,x_name,y_name,nbins,xmin,xmax,logy=1,normalized=1,overflow=1, underflow = 1,weights_to_apply=""):

	###############################
	#
	#	PREAPRE HISTOGRAMS
	#
	################################
	binwidth = float(xmax-xmin)/nbins
	if "[" in x_name: units_x = x_name.split("[")[1].split("]")[0]
	else: units_x = ""
	#datahist = ROOT.TH1D("data",";%s;%s / %.1f %s"%(x_name,y_name,binwidth,units_x),nbins,xmin,xmax)
	MC_hists = {}
	for order in range(max(display_dict.keys())):
		MC_hists[order+1] = ROOT.TH1D("MC_%i"%(order+1),";%s;%s / %.1f %s"%(x_name,y_name,binwidth,units_x),nbins,xmin,xmax)
		MC_hists[order+1].Sumw2()
	
	Ratio_hists = {}
	#ratio_hist = ROOT.TH1D("ratio",";%s;Data/MC"%(x_name),nbins,xmin,xmax)

	###############################
	#
	#	READ FILES
	#
	################################

	# MC
	
	
	
	for idx,entry_dict in display_dict.iteritems():
		for sample_idx,f in enumerate(entry_dict["samples"]):
			print f
			full_path = args.indir + "/" + f + ".root"
			f_ = ROOT.TFile(full_path)
			n_original_h = f_.Get("hweight")
			#n_original = original_nevents_dict[f+".root"]
			n_original = n_original_h.GetBinContent(1)
			f_.Close()
			print n_original
	
			hist_tmp = ROOT.TH1D("h_"+f,";%s;%s / %.2f %s"%(x_name,y_name,binwidth,units_x),nbins,xmin,xmax)
			t_ = ROOT.TChain("tree")
			t_.Add(full_path)
			t_.Draw(var+">>h_"+f,weights_to_apply+"*%s"%entry_dict["weights"])
			if underflow: hist_tmp.SetBinContent(1,hist_tmp.GetBinContent(0)+hist_tmp.GetBinContent(1))
			# t_.GetEntry(1)
# 			if t_.is_data == 1:
# 				continue

			xsec = samples_dict[entry_dict["tag"][sample_idx]]["xsec"]*1000 #[fb]
 			int_lumi=300 #[fb^-1	]
			scale = xsec*int_lumi/n_original
			#hist_tmp.SetBinContent(MC_hists[order_table[name]].GetNbinsX(),MC_hists[order_table[name]].GetBinContent(MC_hists[order_table[name]].GetNbinsX()+1))
			#scale=1.
			MC_hists[idx].Add(hist_tmp,scale)
			MC_hists[idx].SetLineColor(entry_dict["color"])
			MC_hists[idx].SetLineStyle(entry_dict["style"])
			#print entry_dict["legend"]," --> ", hist_tmp.Integral(), " (unweighed) --> ", hist_tmp.Integral()*scale , " (weighted)"
			if (not MC_hists[idx].Integral() == 0) and normalized: MC_hists[idx].Scale(1./MC_hists[idx].Integral(1,MC_hists[idx].GetNbinsX()+1))
				# if overflow: MC_hists[idx].Scale(1./MC_hists[idx].Integral(1,hist.GetNbinsX()+1))
#                 else: MC_hists[idx].Scale(1./MC_hists[idx].Integral())
			print entry_dict["legend"], MC_hists[idx].GetMean()
			
			if entry_dict["reference"]: reference_hist = MC_hists[idx]
			del hist_tmp
		
	#
	# Now calculate ratio histograms w.r.t. reference
	#	
	
	


	###############################
	#
	#	STYLE
	#
	################################

	#if overflow: datahist.GetXaxis().SetRange(1,datahist.GetNbinsX()+1)
	for idx,hist in MC_hists.iteritems():
		hist.SetLineWidth(3)
		if overflow: 
			hist.GetXaxis().SetRange(1,hist.GetNbinsX()+1)
	

	###############################
	#
	#	PLOTTING
	#
	################################
	c = ROOT.TCanvas("c","c",800,1100)
	c.cd()
	uppad = ROOT.TPad("u","u",0.,0.30,1.,1.)
	downpad = ROOT.TPad("d","d",0.,0.0,1.,0.30)
	uppad.Draw()
	downpad.Draw()

	uppad.cd()
	ROOT.gPad.SetLogy(logy)
	ROOT.gPad.SetMargin(0.15,0.05,0.01,0.08)
	mg = ROOT.THStack("mg",";%s;%s / %.2f %s"%(x_name,y_name,binwidth,units_x))
	max_bin_content = 0
	min_bin_content = 99999
	for idx,hist in MC_hists.iteritems():
		mg.Add(hist,"hist")
		if hist.GetBinContent(hist.GetMaximumBin()) > max_bin_content: max_bin_content = hist.GetBinContent(hist.GetMaximumBin())
		if hist.GetBinContent(hist.GetMinimumBin()) < min_bin_content: min_bin_content = hist.GetBinContent(hist.GetMinimumBin())
	mg.Draw("hist nostack")
	if overflow: mg.GetXaxis().SetRange(1,mg.GetHistogram().GetNbinsX()+1)
	ROOT.TGaxis.SetMaxDigits(3)
	if (logy): 
		if normalized: mg.SetMinimum(min_bin_content)
		else: mg.SetMinimum(min_bin_content)
		mg.SetMaximum(1.5*max_bin_content*10**2.8)
	else:
		mg.SetMinimum(0)
		mg.SetMaximum(1.8*max_bin_content)
	mg.GetYaxis().SetLabelFont(43)
	mg.GetYaxis().SetTitleFont(43)
	mg.GetYaxis().SetLabelSize(30)
	mg.GetYaxis().SetLabelOffset(0.01)
	mg.GetYaxis().SetTitleSize(35)
	mg.GetYaxis().SetTitleOffset(2.1)
	mg.GetXaxis().SetTitleSize(0)
	mg.GetXaxis().SetTitleOffset(500)
	mg.GetXaxis().SetLabelSize(0)


	#redraw borders
	ROOT.gPad.RedrawAxis()
	line = ROOT.TLine()
	if overflow: line.DrawLine(xmax+binwidth, ROOT.gPad.GetUymin(), xmax+binwidth, ROOT.gPad.GetUymax())
	else:line.DrawLine(xmax, ROOT.gPad.GetUymin(), xmax, ROOT.gPad.GetUymax())

	#########
	# TEXT
	#########
	lumi = "%.1f"%int_lumi
	year = "2017"
	latex = ROOT.TLatex()
	latex.SetTextFont(43)
	latex.SetTextSize(35)
	latex.SetTextAlign(32)
	latex.DrawLatexNDC(0.95,0.96,"13 TeV")

	latex_cms = ROOT.TLatex()
	latex_cms.SetTextFont(43)
	latex_cms.SetTextSize(35)
	latex_cms.SetTextAlign(11)
	latex_cms.DrawLatexNDC(0.20,0.87,"#bf{CMS} #it{Simulation Preliminary}")
	#latex_cms.DrawLatexNDC(0.19,0.83,"#bf{CMS} #it{Simulation}")
	#latex_cms.DrawLatexNDC(0.19,0.83,"#bf{CMS}")




	#############
	# LEGEND
	#############
	if len(display_dict.keys()) <= 9: 
		l = ROOT.TLegend(0.19,0.64,0.94,0.84)
		l.SetNColumns(2)
	elif len(display_dict.keys()) > 9: 
		l = ROOT.TLegend(0.19,0.64,0.94,0.8)
		l.SetNColumns(3)
	entries_dict={}
	for idx,e in display_dict.iteritems():
		if idx == -1: continue
		entries_dict[e["legend"]]=l.AddEntry(None,e["legend"],"l")
		entries_dict[e["legend"]].SetFillStyle(1000)
		entries_dict[e["legend"]].SetLineColor(e["color"])
		entries_dict[e["legend"]].SetLineStyle(e["style"])
		entries_dict[e["legend"]].SetLineWidth(6)
	#l.AddEntry(datahist,"Data","ep")
	l.SetBorderSize(0)
	l.SetTextFont(43)
	l.SetTextSize(25)
	l.SetFillStyle(0)
	l.Draw("same")




	#############
	# DOWN PAD
	#############
	
	for idx,hist in MC_hists.iteritems():
		Ratio_hists[idx] = MC_hists[idx].Clone()
		Ratio_hists[idx].Divide(reference_hist)

		
	
	downpad.cd()
	ROOT.gPad.SetMargin(0.15,0.05,0.3,0.01)
	
	mg_ratio = ROOT.THStack("mg_ratio",";%s;Ratio to SM"%(x_name))
	#max_bin_content = 0
	#min_bin_content = 99999
	for idx,ratio_hist in Ratio_hists.iteritems():
		mg_ratio.Add(ratio_hist,"ratio_hist")
		#if ratio_hist.GetBinContent(ratio_hist.GetMaximumBin()) > max_bin_content: max_bin_content = ratio_hist.GetBinContent(ratio_hist.GetMaximumBin())
		#if ratio_hist.GetBinContent(ratio_hist.GetMinimumBin()) < min_bin_content: min_bin_content = ratio_hist.GetBinContent(ratio_hist.GetMinimumBin())
	mg_ratio.Draw("hist nostack")
	#if overflow: mg_ratio.GetXaxis().SetRange(1,mg_ratio.GetHistogram().GetNbinsX()+1)
	ROOT.TGaxis.SetMaxDigits(3)
	
	mg_ratio.SetMinimum(0.1)
	mg_ratio.SetMaximum(1.9)
	mg_ratio.GetYaxis().SetLabelFont(43)
	mg_ratio.GetYaxis().SetTitleFont(43)
	mg_ratio.GetYaxis().SetNdivisions(505)
	mg_ratio.GetYaxis().CenterTitle()
	mg_ratio.GetYaxis().SetLabelSize(30)
	mg_ratio.GetYaxis().SetLabelOffset(0.01)
	mg_ratio.GetYaxis().SetTitleSize(35)
	mg_ratio.GetYaxis().SetTitleOffset(2.1)
	mg_ratio.GetXaxis().SetLabelFont(43)
	mg_ratio.GetXaxis().SetTitleFont(43)
	mg_ratio.GetXaxis().SetTitleSize(35)
	mg_ratio.GetXaxis().SetTitleOffset(4.1)
	mg_ratio.GetXaxis().SetLabelSize(30)
	
	
	
	ROOT.gPad.RedrawAxis()
	# line = ROOT.TLine()
# 	if overflow: line.DrawLine(xmax+binwidth, ROOT.gPad.GetUymin(), xmax+binwidth, ROOT.gPad.GetUymax())
# 	else:line.DrawLine(xmax, ROOT.gPad.GetUymin(), xmax, ROOT.gPad.GetUymax())


# 	line3 = ROOT.TLine()
# 	line3.SetLineColor(1)
# 	line3.SetLineStyle(2)
# 	line3.SetLineWidth(2)
# 	if overflow: 
# 		#if use_custom_bins: line3.DrawLine(xmin, 1, xmax+(custom_bins[-1]-custom_bins[-2]), 1)
# 		#else: line3.DrawLine(xmin, 1, xmax+binwidth, 1)
# 		line3.DrawLine(xmin, 1, xmax+binwidth, 1)
# 	else: line3.DrawLine(xmin, 1, xmax, 1)
# 	line3.SetLineWidth(1)


	if not os.path.isdir(args.outdir): os.mkdir(args.outdir)


	if (logy): 
		if (normalized):
			c.SaveAs(args.outdir+"/"+var+"_normalized_Log.pdf")
			c.SaveAs(args.outdir+"/"+var+"_normalized_Log.png")
			c.SaveAs(args.outdir+"/"+var+"_normalized_Log.C")
		else:
			c.SaveAs(args.outdir+"/"+var+"_Log.pdf")
			c.SaveAs(args.outdir+"/"+var+"_Log.png")
			c.SaveAs(args.outdir+"/"+var+"_Log.C")
	else: 
		if (normalized):
			c.SaveAs(args.outdir+"/"+var+"_normalized_Linear.pdf")
			c.SaveAs(args.outdir+"/"+var+"_normalized_Linear.png")
			c.SaveAs(args.outdir+"/"+var+"_normalized_Linear.C")
		else:
			c.SaveAs(args.outdir+"/"+var+"_Linear.pdf")
			c.SaveAs(args.outdir+"/"+var+"_Linear.png")
			c.SaveAs(args.outdir+"/"+var+"_Linear.C")





def main():

	no_weights = "1"
	lepton_channel="inclusive"

	Plot1D("LeadingJet_Pt","Leading jet p_{T} [GeV]","Events",30,20,400,logy=1,normalized=1,overflow=1, underflow = 1,weights_to_apply=no_weights)
	#Plot1D("LeadingJet_Pt","Leading jet p_{T} [GeV]","Events",30,20,400,logy=0,normalized=1,overflow=1, underflow = 1,weights_to_apply=no_weights)
	#Plot1D("LeadingJet_Pt","Leading jet p_{T} [GeV]","Events",30,20,400,logy=1,normalized=0,overflow=1, underflow = 1,weights_to_apply=no_weights)
	#Plot1D("LeadingJet_Pt","Leading jet p_{T} [GeV]","Events",30,20,400,logy=0,normalized=0,overflow=1, underflow = 1,weights_to_apply=no_weights)

	sys.exit(1)


if __name__ == "__main__":
	main()
