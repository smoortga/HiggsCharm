import os
import sys
import numpy as np
from pprint import pprint
import random
import itertools



#******************************************************
#
# This configuration file specifies the model / EFT operators
# / reweighting schemes etc to be used for the generation of
# dedicated MC samples using Madgraph5_aMC@NLO
#
# author: Seth Moortgat
# date: 11/12-2019
#
#******************************************************


#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		TAG
#
# please enter here a tag name that will be propagated 
# throughout the sample production.
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

tag = "Higgs_Effective_Couplings_Test"


#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		UFO MODEL
#
# this should match the name of a directory in "addons/models/"
# that contains the model UFO.
#
# Models used so far:    SMEFTsim_A_general_MwScheme_UFO_v2,
#                        Higgs_Effective_Couplings_UFO
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

model_name = "Higgs_Effective_Couplings_UFO" # aanpassen 

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		PROCESSES
#
# please write here as a string the process
# that MadGraph should be running.
# This is formatted as an array in case you want to
# add multiple processes.
#
# default header of the proc_card.dat will look like:
# 
# import model <model_name>
# define l+ = e+ mu+ ta+
# define l- = e- mu- ta-
# define vl = ve vm vt
# define vl~ = ve~ vm~ vt~
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# p p > h c toevoegen
processes = [
	#"generate p p > h j"
        "generate p p > h c HIG=1, (h > z mu+ mu-, z > mu+ mu-)",
	"add process p p > h c~ HIG=1, (h > z mu+ mu-, z > mu+ mu-)"
	#,"generate p p > t t~ / a z h w+ DIM6=1 , (t > w+ b DIM6=0, w+ > l+ vl DIM6=0), (t~ > w- b~ DIM6=0, w- > l- vl~ DIM6=0)"
	#,"add process p p > t t~ j / a z h w+ DIM6=1 , (t > w+ b DIM6=0, w+ > l+ vl DIM6=0), (t~ > w- b~ DIM6=0, w- > l- vl~ DIM6=0)"
]

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		FLAVOUR SCHEME
#
# please specify here whether you would
# like to use the four-flavour (4F) or the
# five-flavour scheme (5F)
#
# In case of 5F scheme, default header of proc_card.dat will look like
# 
# import model <model_name>
# define p = p b b~
# define j = p
# define l+ = e+ mu+ ta+
# define l- = e- mu- ta-
# define vl = ve vm vt
# define vl~ = ve~ vm~ vt~
# 
# Additionally, the "maxjetflavor" variable in the run_card.dat will be changed accordingly
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

flavour_scheme = "4F" # or "5F"


#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		OPERATORS
#
# please write here the list of operators to be considered.
# Have a look at the "parameters.py" file in the UFO directory.
# Any parameter not in this list has its Wilson Coefficient defaulted to 0
#
# Please also define the baseline scenario for the Wilson Coefficients
# This will be the baseline to which the reweighting factors are calculated.
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# operators = ["ctG","ctGI","ctW","ctWI"]
operators = []

# baseline_values = ["1.0","1.0","1.0","1.0"]
baseline_values = []
assert len(baseline_values) == len(operators), \
	"ERROR: length of baseline_values should be the same as that of operators"

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		RESTRICTIONS
#
# Default: SMlimit
# 
# Also possible: SMlimit_massless, SMlimit_top, TopEFT, massless, CPconserving
#
# No restriction: empty string ""
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

restriction = ""

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
#               PT AND ETA
# (to be changed through customizecard)
# Don't change anything: empty string ""
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

minimum_jet_pt = "20.0" # Minimum pt of j, b, a, l. (GeV)
maximum_jet_eta = "3.0" # Maximum absolute eta of j, b, a, l.
delta_R = "0.5" # DeltaR op 0.4 zetten (allemaal op hetzelfde zetten)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#
# 		REWEIGHTING
#
# please choose one or multiple of the following options
# 	no_reweights: no reweighting is applied
#	individual: each operator is varied individually
#	minimal: a minimal set of scan points over all operators, to derive the quadratic dependence (based on tetrahedron construction)
# 	rnd_scan: a random scan over all operators is performed
#	grid: a rectangular grid of Wilson coefficients is scanned
#	custom: a custom reweighting scheme is provided by the user
#
#	--> specify your desired strategies in an array of strings
#
# Then navigate to the corresponding "if statement(s)" and fill everything
#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*	
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#          |	
#          |
#          \/	
	
reweighting_strategy = ["custom"]

#     /\  		  /\	
#     |   	 	   | 
#     | 	   	   |  
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
assert all(x in ["no_reweights","individual","rnd_scan","grid","custom","minimal"] for x in reweighting_strategy), \
	"ERROR: the reweighting_strategy needs to be no_reweights, individual, rnd_scan, grid, minimal or custom"
#assert reweighting_strategy in ["no_reweights","individual","rnd_scan","grid","custom"]
		
		


# small helper function to create weight names
def translate_weight_name(operators,values):
	"""
	operators and values are arrays of relevant (non-zero) operators and values
	"""
	out_str_ = "rwgt_"
	for idx,op in enumerate(operators):
		out_str_ += op + "_" + str(values[idx]).replace("-","min").replace(".","p") + "_"
	return out_str_[:-1]
	
		
# * - * - * - * - 
#
#			INDIVIDUAL
#
# Please specify for each operator in "operators" a range of values to scan
#
# ----------------------------
# op1:	*	*	*	*	*
# ----------------------------
# op2:	 	 *	 *	 *	 *
# ----------------------------
# op3:  * * * * *
# ----------------------------
# op4:	*		*		*
# ----------------------------
#
# * - * - * - * - 

points_individual = [
		[-2.,-1.,1.,2.],
		[-2.,-1.,1.,2.],
		[-2.,-1.,1.,2.],
		[-2.,-1.,1.,2.],
	]

if reweighting_strategy == "individual":
	assert len(points_individual) == len(operators), \
				"ERROR: length of points_individual should be the same as that of operators"







# * - * - * - * - 
#
#		RND_SCAN
#
# A random rnd_scan will be produced
# one needs at least 1 + 2d + [d(d-1)]/2
# rnd_scan points for d operators
#
# /\
# |	*        *           *
# |	     *         *
# |	  *	              *
# |  *          *
# |
# |     *            *
# ---------------------------->
#
# * - * - * - * - 

n_points = 30
if reweighting_strategy == "rnd_scan":
	assert n_points >= (1. + 2.*len(operators) + (len(operators)*(len(operators)-1.))/2.), \
			"ERROR: you need at least %i points for %i operators to fully determine the coefficients of the quadratic form"%((1. + 2.*len(operators) + (len(operators)*(len(operators)-1.))/2.),len(operators))

# * - * - * - * - 
# Please specify lower and upper limits for rnd_scanning each operator
# * - * - * - * - 

boundaries = [
	[-2.,2.],
	[-2.,2.],
	[-2.,2.],
	[-2.,2.]
]

if reweighting_strategy == "rnd_scan":
	assert len(boundaries) == len(operators), \
				"ERROR: length of boundaries should be the same as that of operators"





# * - * - * - * - 
#
#		MINIMAL
#
# A minimal set of scan points is selected to construct 
# the d-dimensional quadratic function.
# when d Wilson coefficients are considered,
# one needs at least 1 + 2d + [d(d-1)]/2
# scan points for d operators.
# Construction based on the sum of the wilson coeff being smaller than
# the order of the polinomial (2 in most cases, but can be higher for 
# multiple insertions of EFT operators) + equally spaced
# Example with 2 operators: C1+C2<2 --> 6 combinations with sum < 2: (2,0), (1,1), (0,2), (0,1), (1,0), (0,0)
# (can be scaled to other boundaries)
#
# /\
# |		*
# |	
# |		*	 	*
# |  
# |		*		*		*
# |    
# ---------------------------->
#
# * - * - * - * - 

# * - * - * - * - 
# Please specify lower and upper limits for rnd_scanning each operator
# * - * - * - * - 

boundaries_minimal_scan = [
	[-2.,2.],
	[-2.,5.2],
	[-2.,2.],
	[-7.3,1.22]
]

if reweighting_strategy == "minimal":
	assert len(boundaries_minimal_scan) == len(operators), \
				"ERROR: length of boundaries_minimal_scan should be the same as that of operators"


# * - * - * - * - 
# Please specify the order of the polinomial (usually 2)
# * - * - * - * - 

order = 2






# * - * - * - * - 
#
#		GRID
#
# A grid will be made for all combination of points
# within the range specified and with the
# number of points specified
#
#	NOTE: NUMBER OF POINTS SCALES AS n_point^n_operators
#	example: 5 points per 4 operators = 5^4 = 625 weights!
# /\
# |	*	*	*	*	*
# |	*	*	*	*	*
# |	*	*	*	*	*
# |	*	*	*	*	*
# ---------------------------->
#
# * - * - * - * - 

boundaries_and_npoints = [
	[-2.,2.,5],
	[-2.,2.,5],
	[-2.,2.,5],
	[-2.,2.,5],
]

if reweighting_strategy == "grid":
	assert len(boundaries_and_npoints) == len(operators), \
			"ERROR: length of boundaries_and_npoints should be the same as that of operators"







#* - * - * - * - 
#
#		CUSTOM
#
# Please fill the reweight_dict_tmp_ yourself as indicated in the example
# Each operator needs to be assigned a value
# the name of the weight can be freely chosen
#
# /\
# |	*	
# |		*	
# |			*	
# |				*
# ---------------------------->
#
# * - * - * - * - 

reweight_dict_tmp_ = {}

# reweight_dict_tmp_["rwgt_ctG_5p0_ctGI_2p0"] = 	{'ctG': 5.0,
# 											'ctGI': 2.0,
# 											'ctW': 0.0,
# 											'ctWI': 0.0}
# reweight_dict_tmp_["rwgt_ctG_min3p0_ctW_2p0"] = 	{'ctG': -3.0,
# 											'ctGI': 0.0,
# 											'ctW': 2.0,
# 											'ctWI': 0.0}


reweight_dict_tmp_["rwgt_kc0p5"] = {'YUKAWA 4': 0.64}
reweight_dict_tmp_["rwgt_kc2"] = {'YUKAWA 4': 2.56}

# include the SM by default
reweight_dict_tmp_["rwgt_SM"] = {'YUKAWA 4': 1.28}

for op in operators:
	reweight_dict_tmp_["rwgt_SM"][op] = 0.0



















