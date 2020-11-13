# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Mon 5 Feb 2018 13:13:57


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(-2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-(complex(0,1)*G)',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-6*complex(0,1)*lam',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '(cdd1x1x1x2*complex(0,1))/LambdaSMEFT**2 + (cdd1x2x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '(cdd1x1x1x3*complex(0,1))/LambdaSMEFT**2 + (cdd1x3x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '(cdd1x2x1x3*complex(0,1))/LambdaSMEFT**2 + (cdd1x3x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '(cdd1x1x2x1*complex(0,1))/LambdaSMEFT**2 + (cdd2x1x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '(cdd1x2x2x1*complex(0,1))/LambdaSMEFT**2 + (cdd2x1x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '(cdd1x3x2x1*complex(0,1))/LambdaSMEFT**2 + (cdd2x1x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '(cdd1x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cdd2x2x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '(cdd1x2x2x2*complex(0,1))/LambdaSMEFT**2 + (cdd2x2x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '(cdd1x3x2x2*complex(0,1))/LambdaSMEFT**2 + (cdd2x2x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(cdd2x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cdd2x2x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '(cdd1x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cdd2x3x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(cdd1x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cdd2x3x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '(cdd1x3x2x3*complex(0,1))/LambdaSMEFT**2 + (cdd2x3x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '(cdd2x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cdd2x3x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '(cdd2x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cdd2x3x2x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(cdd1x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cdd3x1x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '(cdd1x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cdd3x1x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(cdd1x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cdd3x1x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(cdd2x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cdd3x1x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(cdd2x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cdd3x1x2x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(cdd2x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cdd3x1x2x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(cdd1x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cdd3x2x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(cdd1x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cdd3x2x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(cdd1x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cdd3x2x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(cdd2x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cdd3x2x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cdd2x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cdd3x2x2x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(cdd2x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cdd3x2x2x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(cdd3x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cdd3x2x3x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(cdd1x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cdd3x3x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(cdd1x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cdd3x3x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(cdd1x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cdd3x3x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(cdd2x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cdd3x3x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '(cdd2x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cdd3x3x2x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '(cdd2x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cdd3x3x2x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '(cdd3x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cdd3x3x3x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(cdd3x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cdd3x3x3x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '(cee1x1x1x2*complex(0,1))/LambdaSMEFT**2 + (cee1x2x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '(cee1x1x1x3*complex(0,1))/LambdaSMEFT**2 + (cee1x3x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(cee1x2x1x3*complex(0,1))/LambdaSMEFT**2 + (cee1x3x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(cee1x1x2x1*complex(0,1))/LambdaSMEFT**2 + (cee2x1x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(cee1x2x2x1*complex(0,1))/LambdaSMEFT**2 + (cee2x1x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '(cee1x3x2x1*complex(0,1))/LambdaSMEFT**2 + (cee2x1x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '(cee1x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cee2x2x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(cee1x2x2x2*complex(0,1))/LambdaSMEFT**2 + (cee2x2x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(cee1x3x2x2*complex(0,1))/LambdaSMEFT**2 + (cee2x2x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '(cee2x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cee2x2x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '(cee1x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cee2x3x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(cee1x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cee2x3x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(cee1x3x2x3*complex(0,1))/LambdaSMEFT**2 + (cee2x3x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(cee2x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cee2x3x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '(cee2x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cee2x3x2x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '(cee1x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cee3x1x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '(cee1x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cee3x1x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '(cee1x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cee3x1x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '(cee2x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cee3x1x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(cee2x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cee3x1x2x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '(cee2x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cee3x1x2x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '(cee1x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cee3x2x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '(cee1x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cee3x2x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '(cee1x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cee3x2x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(cee2x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cee3x2x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '(cee2x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cee3x2x2x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(cee2x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cee3x2x2x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '(cee3x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cee3x2x3x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '(cee1x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cee3x3x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '(cee1x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cee3x3x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '(cee1x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cee3x3x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '(cee2x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cee3x3x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '(cee2x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cee3x3x2x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '(cee2x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cee3x3x2x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '(cee3x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cee3x3x3x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '(cee3x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cee3x3x3x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '(cll1x1x1x2*complex(0,1))/LambdaSMEFT**2 + (cll1x2x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '(cll1x1x1x3*complex(0,1))/LambdaSMEFT**2 + (cll1x3x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '(cll1x2x1x3*complex(0,1))/LambdaSMEFT**2 + (cll1x3x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(cll1x1x2x1*complex(0,1))/LambdaSMEFT**2 + (cll2x1x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '(cll1x2x2x1*complex(0,1))/LambdaSMEFT**2 + (cll2x1x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '(cll1x3x2x1*complex(0,1))/LambdaSMEFT**2 + (cll2x1x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '(cll1x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cll2x2x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '(cll1x2x2x2*complex(0,1))/LambdaSMEFT**2 + (cll2x2x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(cll1x3x2x2*complex(0,1))/LambdaSMEFT**2 + (cll2x2x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '(cll2x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cll2x2x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '(cll1x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cll2x3x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '(cll1x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cll2x3x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '(cll1x3x2x3*complex(0,1))/LambdaSMEFT**2 + (cll2x3x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = '(cll2x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cll2x3x2x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '(cll2x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cll2x3x2x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '(cll1x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cll3x1x1x1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = '(cll1x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cll3x1x1x2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '(cll1x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cll3x1x1x3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '(cll2x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cll3x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '(cll2x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cll3x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '(cll2x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cll3x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = '(cll1x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cll3x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '(cll1x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cll3x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = '(cll1x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cll3x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '(cll2x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cll3x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = '(cll2x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cll3x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_108 = Coupling(name = 'GC_108',
                  value = '(cll2x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cll3x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '(cll3x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cll3x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_110 = Coupling(name = 'GC_110',
                  value = '(cll1x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cll3x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '(cll1x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cll3x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = '(cll1x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cll3x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '(cll2x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cll3x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_114 = Coupling(name = 'GC_114',
                  value = '(cll2x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cll3x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '(cll2x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cll3x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = '(cll3x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cll3x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = '(cll3x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cll3x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '(clq11x1x1x1*complex(0,1))/LambdaSMEFT**2 - (clq31x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = '(clq11x1x1x1*complex(0,1))/LambdaSMEFT**2 + (clq31x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '(clq11x1x1x2*complex(0,1))/LambdaSMEFT**2 - (clq31x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = '(clq11x1x1x2*complex(0,1))/LambdaSMEFT**2 + (clq31x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '(clq11x1x1x3*complex(0,1))/LambdaSMEFT**2 - (clq31x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '(clq11x1x1x3*complex(0,1))/LambdaSMEFT**2 + (clq31x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '(clq11x1x2x1*complex(0,1))/LambdaSMEFT**2 - (clq31x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '(clq11x1x2x1*complex(0,1))/LambdaSMEFT**2 + (clq31x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '(clq11x1x2x2*complex(0,1))/LambdaSMEFT**2 - (clq31x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '(clq11x1x2x2*complex(0,1))/LambdaSMEFT**2 + (clq31x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '(clq11x1x2x3*complex(0,1))/LambdaSMEFT**2 - (clq31x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '(clq11x1x2x3*complex(0,1))/LambdaSMEFT**2 + (clq31x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_130 = Coupling(name = 'GC_130',
                  value = '(clq11x1x3x1*complex(0,1))/LambdaSMEFT**2 - (clq31x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '(clq11x1x3x1*complex(0,1))/LambdaSMEFT**2 + (clq31x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '(clq11x1x3x2*complex(0,1))/LambdaSMEFT**2 - (clq31x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = '(clq11x1x3x2*complex(0,1))/LambdaSMEFT**2 + (clq31x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '(clq11x1x3x3*complex(0,1))/LambdaSMEFT**2 - (clq31x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '(clq11x1x3x3*complex(0,1))/LambdaSMEFT**2 + (clq31x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '(clq11x2x1x1*complex(0,1))/LambdaSMEFT**2 - (clq31x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_137 = Coupling(name = 'GC_137',
                  value = '(clq11x2x1x1*complex(0,1))/LambdaSMEFT**2 + (clq31x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '(clq11x2x1x2*complex(0,1))/LambdaSMEFT**2 - (clq31x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '(clq11x2x1x2*complex(0,1))/LambdaSMEFT**2 + (clq31x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '(clq11x2x1x3*complex(0,1))/LambdaSMEFT**2 - (clq31x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_141 = Coupling(name = 'GC_141',
                  value = '(clq11x2x1x3*complex(0,1))/LambdaSMEFT**2 + (clq31x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '(clq11x2x2x1*complex(0,1))/LambdaSMEFT**2 - (clq31x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_143 = Coupling(name = 'GC_143',
                  value = '(clq11x2x2x1*complex(0,1))/LambdaSMEFT**2 + (clq31x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_144 = Coupling(name = 'GC_144',
                  value = '(clq11x2x2x2*complex(0,1))/LambdaSMEFT**2 - (clq31x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_145 = Coupling(name = 'GC_145',
                  value = '(clq11x2x2x2*complex(0,1))/LambdaSMEFT**2 + (clq31x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_146 = Coupling(name = 'GC_146',
                  value = '(clq11x2x2x3*complex(0,1))/LambdaSMEFT**2 - (clq31x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_147 = Coupling(name = 'GC_147',
                  value = '(clq11x2x2x3*complex(0,1))/LambdaSMEFT**2 + (clq31x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_148 = Coupling(name = 'GC_148',
                  value = '(clq11x2x3x1*complex(0,1))/LambdaSMEFT**2 - (clq31x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_149 = Coupling(name = 'GC_149',
                  value = '(clq11x2x3x1*complex(0,1))/LambdaSMEFT**2 + (clq31x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '(clq11x2x3x2*complex(0,1))/LambdaSMEFT**2 - (clq31x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '(clq11x2x3x2*complex(0,1))/LambdaSMEFT**2 + (clq31x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = '(clq11x2x3x3*complex(0,1))/LambdaSMEFT**2 - (clq31x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '(clq11x2x3x3*complex(0,1))/LambdaSMEFT**2 + (clq31x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_154 = Coupling(name = 'GC_154',
                  value = '(clq11x3x1x1*complex(0,1))/LambdaSMEFT**2 - (clq31x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '(clq11x3x1x1*complex(0,1))/LambdaSMEFT**2 + (clq31x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_156 = Coupling(name = 'GC_156',
                  value = '(clq11x3x1x2*complex(0,1))/LambdaSMEFT**2 - (clq31x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_157 = Coupling(name = 'GC_157',
                  value = '(clq11x3x1x2*complex(0,1))/LambdaSMEFT**2 + (clq31x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = '(clq11x3x1x3*complex(0,1))/LambdaSMEFT**2 - (clq31x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '(clq11x3x1x3*complex(0,1))/LambdaSMEFT**2 + (clq31x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '(clq11x3x2x1*complex(0,1))/LambdaSMEFT**2 - (clq31x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '(clq11x3x2x1*complex(0,1))/LambdaSMEFT**2 + (clq31x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_162 = Coupling(name = 'GC_162',
                  value = '(clq11x3x2x2*complex(0,1))/LambdaSMEFT**2 - (clq31x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_163 = Coupling(name = 'GC_163',
                  value = '(clq11x3x2x2*complex(0,1))/LambdaSMEFT**2 + (clq31x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_164 = Coupling(name = 'GC_164',
                  value = '(clq11x3x2x3*complex(0,1))/LambdaSMEFT**2 - (clq31x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_165 = Coupling(name = 'GC_165',
                  value = '(clq11x3x2x3*complex(0,1))/LambdaSMEFT**2 + (clq31x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_166 = Coupling(name = 'GC_166',
                  value = '(clq11x3x3x1*complex(0,1))/LambdaSMEFT**2 - (clq31x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_167 = Coupling(name = 'GC_167',
                  value = '(clq11x3x3x1*complex(0,1))/LambdaSMEFT**2 + (clq31x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_168 = Coupling(name = 'GC_168',
                  value = '(clq11x3x3x2*complex(0,1))/LambdaSMEFT**2 - (clq31x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_169 = Coupling(name = 'GC_169',
                  value = '(clq11x3x3x2*complex(0,1))/LambdaSMEFT**2 + (clq31x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_170 = Coupling(name = 'GC_170',
                  value = '(clq11x3x3x3*complex(0,1))/LambdaSMEFT**2 - (clq31x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = '(clq11x3x3x3*complex(0,1))/LambdaSMEFT**2 + (clq31x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_172 = Coupling(name = 'GC_172',
                  value = '(clq12x1x1x1*complex(0,1))/LambdaSMEFT**2 - (clq32x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_173 = Coupling(name = 'GC_173',
                  value = '(clq12x1x1x1*complex(0,1))/LambdaSMEFT**2 + (clq32x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_174 = Coupling(name = 'GC_174',
                  value = '(clq12x1x1x2*complex(0,1))/LambdaSMEFT**2 - (clq32x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_175 = Coupling(name = 'GC_175',
                  value = '(clq12x1x1x2*complex(0,1))/LambdaSMEFT**2 + (clq32x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_176 = Coupling(name = 'GC_176',
                  value = '(clq12x1x1x3*complex(0,1))/LambdaSMEFT**2 - (clq32x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = '(clq12x1x1x3*complex(0,1))/LambdaSMEFT**2 + (clq32x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_178 = Coupling(name = 'GC_178',
                  value = '(clq12x1x2x1*complex(0,1))/LambdaSMEFT**2 - (clq32x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_179 = Coupling(name = 'GC_179',
                  value = '(clq12x1x2x1*complex(0,1))/LambdaSMEFT**2 + (clq32x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_180 = Coupling(name = 'GC_180',
                  value = '(clq12x1x2x2*complex(0,1))/LambdaSMEFT**2 - (clq32x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_181 = Coupling(name = 'GC_181',
                  value = '(clq12x1x2x2*complex(0,1))/LambdaSMEFT**2 + (clq32x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_182 = Coupling(name = 'GC_182',
                  value = '(clq12x1x2x3*complex(0,1))/LambdaSMEFT**2 - (clq32x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_183 = Coupling(name = 'GC_183',
                  value = '(clq12x1x2x3*complex(0,1))/LambdaSMEFT**2 + (clq32x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_184 = Coupling(name = 'GC_184',
                  value = '(clq12x1x3x1*complex(0,1))/LambdaSMEFT**2 - (clq32x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_185 = Coupling(name = 'GC_185',
                  value = '(clq12x1x3x1*complex(0,1))/LambdaSMEFT**2 + (clq32x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_186 = Coupling(name = 'GC_186',
                  value = '(clq12x1x3x2*complex(0,1))/LambdaSMEFT**2 - (clq32x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_187 = Coupling(name = 'GC_187',
                  value = '(clq12x1x3x2*complex(0,1))/LambdaSMEFT**2 + (clq32x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_188 = Coupling(name = 'GC_188',
                  value = '(clq12x1x3x3*complex(0,1))/LambdaSMEFT**2 - (clq32x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '(clq12x1x3x3*complex(0,1))/LambdaSMEFT**2 + (clq32x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '(clq12x2x1x1*complex(0,1))/LambdaSMEFT**2 - (clq32x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_191 = Coupling(name = 'GC_191',
                  value = '(clq12x2x1x1*complex(0,1))/LambdaSMEFT**2 + (clq32x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_192 = Coupling(name = 'GC_192',
                  value = '(clq12x2x1x2*complex(0,1))/LambdaSMEFT**2 - (clq32x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_193 = Coupling(name = 'GC_193',
                  value = '(clq12x2x1x2*complex(0,1))/LambdaSMEFT**2 + (clq32x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_194 = Coupling(name = 'GC_194',
                  value = '(clq12x2x1x3*complex(0,1))/LambdaSMEFT**2 - (clq32x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_195 = Coupling(name = 'GC_195',
                  value = '(clq12x2x1x3*complex(0,1))/LambdaSMEFT**2 + (clq32x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_196 = Coupling(name = 'GC_196',
                  value = '(clq12x2x2x1*complex(0,1))/LambdaSMEFT**2 - (clq32x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_197 = Coupling(name = 'GC_197',
                  value = '(clq12x2x2x1*complex(0,1))/LambdaSMEFT**2 + (clq32x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_198 = Coupling(name = 'GC_198',
                  value = '(clq12x2x2x2*complex(0,1))/LambdaSMEFT**2 - (clq32x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_199 = Coupling(name = 'GC_199',
                  value = '(clq12x2x2x2*complex(0,1))/LambdaSMEFT**2 + (clq32x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_200 = Coupling(name = 'GC_200',
                  value = '(clq12x2x2x3*complex(0,1))/LambdaSMEFT**2 - (clq32x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_201 = Coupling(name = 'GC_201',
                  value = '(clq12x2x2x3*complex(0,1))/LambdaSMEFT**2 + (clq32x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_202 = Coupling(name = 'GC_202',
                  value = '(clq12x2x3x1*complex(0,1))/LambdaSMEFT**2 - (clq32x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_203 = Coupling(name = 'GC_203',
                  value = '(clq12x2x3x1*complex(0,1))/LambdaSMEFT**2 + (clq32x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_204 = Coupling(name = 'GC_204',
                  value = '(clq12x2x3x2*complex(0,1))/LambdaSMEFT**2 - (clq32x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_205 = Coupling(name = 'GC_205',
                  value = '(clq12x2x3x2*complex(0,1))/LambdaSMEFT**2 + (clq32x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_206 = Coupling(name = 'GC_206',
                  value = '(clq12x2x3x3*complex(0,1))/LambdaSMEFT**2 - (clq32x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_207 = Coupling(name = 'GC_207',
                  value = '(clq12x2x3x3*complex(0,1))/LambdaSMEFT**2 + (clq32x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_208 = Coupling(name = 'GC_208',
                  value = '(clq12x3x1x1*complex(0,1))/LambdaSMEFT**2 - (clq32x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_209 = Coupling(name = 'GC_209',
                  value = '(clq12x3x1x1*complex(0,1))/LambdaSMEFT**2 + (clq32x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = '(clq12x3x1x2*complex(0,1))/LambdaSMEFT**2 - (clq32x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_211 = Coupling(name = 'GC_211',
                  value = '(clq12x3x1x2*complex(0,1))/LambdaSMEFT**2 + (clq32x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_212 = Coupling(name = 'GC_212',
                  value = '(clq12x3x1x3*complex(0,1))/LambdaSMEFT**2 - (clq32x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_213 = Coupling(name = 'GC_213',
                  value = '(clq12x3x1x3*complex(0,1))/LambdaSMEFT**2 + (clq32x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_214 = Coupling(name = 'GC_214',
                  value = '(clq12x3x2x1*complex(0,1))/LambdaSMEFT**2 - (clq32x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_215 = Coupling(name = 'GC_215',
                  value = '(clq12x3x2x1*complex(0,1))/LambdaSMEFT**2 + (clq32x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_216 = Coupling(name = 'GC_216',
                  value = '(clq12x3x2x2*complex(0,1))/LambdaSMEFT**2 - (clq32x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_217 = Coupling(name = 'GC_217',
                  value = '(clq12x3x2x2*complex(0,1))/LambdaSMEFT**2 + (clq32x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_218 = Coupling(name = 'GC_218',
                  value = '(clq12x3x2x3*complex(0,1))/LambdaSMEFT**2 - (clq32x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_219 = Coupling(name = 'GC_219',
                  value = '(clq12x3x2x3*complex(0,1))/LambdaSMEFT**2 + (clq32x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_220 = Coupling(name = 'GC_220',
                  value = '(clq12x3x3x1*complex(0,1))/LambdaSMEFT**2 - (clq32x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_221 = Coupling(name = 'GC_221',
                  value = '(clq12x3x3x1*complex(0,1))/LambdaSMEFT**2 + (clq32x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_222 = Coupling(name = 'GC_222',
                  value = '(clq12x3x3x2*complex(0,1))/LambdaSMEFT**2 - (clq32x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_223 = Coupling(name = 'GC_223',
                  value = '(clq12x3x3x2*complex(0,1))/LambdaSMEFT**2 + (clq32x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_224 = Coupling(name = 'GC_224',
                  value = '(clq12x3x3x3*complex(0,1))/LambdaSMEFT**2 - (clq32x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_225 = Coupling(name = 'GC_225',
                  value = '(clq12x3x3x3*complex(0,1))/LambdaSMEFT**2 + (clq32x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_226 = Coupling(name = 'GC_226',
                  value = '(clq13x1x1x1*complex(0,1))/LambdaSMEFT**2 - (clq33x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_227 = Coupling(name = 'GC_227',
                  value = '(clq13x1x1x1*complex(0,1))/LambdaSMEFT**2 + (clq33x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_228 = Coupling(name = 'GC_228',
                  value = '(clq13x1x1x2*complex(0,1))/LambdaSMEFT**2 - (clq33x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_229 = Coupling(name = 'GC_229',
                  value = '(clq13x1x1x2*complex(0,1))/LambdaSMEFT**2 + (clq33x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_230 = Coupling(name = 'GC_230',
                  value = '(clq13x1x1x3*complex(0,1))/LambdaSMEFT**2 - (clq33x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_231 = Coupling(name = 'GC_231',
                  value = '(clq13x1x1x3*complex(0,1))/LambdaSMEFT**2 + (clq33x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_232 = Coupling(name = 'GC_232',
                  value = '(clq13x1x2x1*complex(0,1))/LambdaSMEFT**2 - (clq33x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_233 = Coupling(name = 'GC_233',
                  value = '(clq13x1x2x1*complex(0,1))/LambdaSMEFT**2 + (clq33x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_234 = Coupling(name = 'GC_234',
                  value = '(clq13x1x2x2*complex(0,1))/LambdaSMEFT**2 - (clq33x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_235 = Coupling(name = 'GC_235',
                  value = '(clq13x1x2x2*complex(0,1))/LambdaSMEFT**2 + (clq33x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_236 = Coupling(name = 'GC_236',
                  value = '(clq13x1x2x3*complex(0,1))/LambdaSMEFT**2 - (clq33x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_237 = Coupling(name = 'GC_237',
                  value = '(clq13x1x2x3*complex(0,1))/LambdaSMEFT**2 + (clq33x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_238 = Coupling(name = 'GC_238',
                  value = '(clq13x1x3x1*complex(0,1))/LambdaSMEFT**2 - (clq33x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_239 = Coupling(name = 'GC_239',
                  value = '(clq13x1x3x1*complex(0,1))/LambdaSMEFT**2 + (clq33x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_240 = Coupling(name = 'GC_240',
                  value = '(clq13x1x3x2*complex(0,1))/LambdaSMEFT**2 - (clq33x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_241 = Coupling(name = 'GC_241',
                  value = '(clq13x1x3x2*complex(0,1))/LambdaSMEFT**2 + (clq33x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_242 = Coupling(name = 'GC_242',
                  value = '(clq13x1x3x3*complex(0,1))/LambdaSMEFT**2 - (clq33x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_243 = Coupling(name = 'GC_243',
                  value = '(clq13x1x3x3*complex(0,1))/LambdaSMEFT**2 + (clq33x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_244 = Coupling(name = 'GC_244',
                  value = '(clq13x2x1x1*complex(0,1))/LambdaSMEFT**2 - (clq33x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_245 = Coupling(name = 'GC_245',
                  value = '(clq13x2x1x1*complex(0,1))/LambdaSMEFT**2 + (clq33x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_246 = Coupling(name = 'GC_246',
                  value = '(clq13x2x1x2*complex(0,1))/LambdaSMEFT**2 - (clq33x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_247 = Coupling(name = 'GC_247',
                  value = '(clq13x2x1x2*complex(0,1))/LambdaSMEFT**2 + (clq33x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_248 = Coupling(name = 'GC_248',
                  value = '(clq13x2x1x3*complex(0,1))/LambdaSMEFT**2 - (clq33x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_249 = Coupling(name = 'GC_249',
                  value = '(clq13x2x1x3*complex(0,1))/LambdaSMEFT**2 + (clq33x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_250 = Coupling(name = 'GC_250',
                  value = '(clq13x2x2x1*complex(0,1))/LambdaSMEFT**2 - (clq33x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_251 = Coupling(name = 'GC_251',
                  value = '(clq13x2x2x1*complex(0,1))/LambdaSMEFT**2 + (clq33x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_252 = Coupling(name = 'GC_252',
                  value = '(clq13x2x2x2*complex(0,1))/LambdaSMEFT**2 - (clq33x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_253 = Coupling(name = 'GC_253',
                  value = '(clq13x2x2x2*complex(0,1))/LambdaSMEFT**2 + (clq33x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_254 = Coupling(name = 'GC_254',
                  value = '(clq13x2x2x3*complex(0,1))/LambdaSMEFT**2 - (clq33x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_255 = Coupling(name = 'GC_255',
                  value = '(clq13x2x2x3*complex(0,1))/LambdaSMEFT**2 + (clq33x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_256 = Coupling(name = 'GC_256',
                  value = '(clq13x2x3x1*complex(0,1))/LambdaSMEFT**2 - (clq33x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '(clq13x2x3x1*complex(0,1))/LambdaSMEFT**2 + (clq33x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_258 = Coupling(name = 'GC_258',
                  value = '(clq13x2x3x2*complex(0,1))/LambdaSMEFT**2 - (clq33x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(clq13x2x3x2*complex(0,1))/LambdaSMEFT**2 + (clq33x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '(clq13x2x3x3*complex(0,1))/LambdaSMEFT**2 - (clq33x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_261 = Coupling(name = 'GC_261',
                  value = '(clq13x2x3x3*complex(0,1))/LambdaSMEFT**2 + (clq33x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_262 = Coupling(name = 'GC_262',
                  value = '(clq13x3x1x1*complex(0,1))/LambdaSMEFT**2 - (clq33x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_263 = Coupling(name = 'GC_263',
                  value = '(clq13x3x1x1*complex(0,1))/LambdaSMEFT**2 + (clq33x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_264 = Coupling(name = 'GC_264',
                  value = '(clq13x3x1x2*complex(0,1))/LambdaSMEFT**2 - (clq33x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_265 = Coupling(name = 'GC_265',
                  value = '(clq13x3x1x2*complex(0,1))/LambdaSMEFT**2 + (clq33x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_266 = Coupling(name = 'GC_266',
                  value = '(clq13x3x1x3*complex(0,1))/LambdaSMEFT**2 - (clq33x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_267 = Coupling(name = 'GC_267',
                  value = '(clq13x3x1x3*complex(0,1))/LambdaSMEFT**2 + (clq33x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_268 = Coupling(name = 'GC_268',
                  value = '(clq13x3x2x1*complex(0,1))/LambdaSMEFT**2 - (clq33x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_269 = Coupling(name = 'GC_269',
                  value = '(clq13x3x2x1*complex(0,1))/LambdaSMEFT**2 + (clq33x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_270 = Coupling(name = 'GC_270',
                  value = '(clq13x3x2x2*complex(0,1))/LambdaSMEFT**2 - (clq33x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_271 = Coupling(name = 'GC_271',
                  value = '(clq13x3x2x2*complex(0,1))/LambdaSMEFT**2 + (clq33x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_272 = Coupling(name = 'GC_272',
                  value = '(clq13x3x2x3*complex(0,1))/LambdaSMEFT**2 - (clq33x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_273 = Coupling(name = 'GC_273',
                  value = '(clq13x3x2x3*complex(0,1))/LambdaSMEFT**2 + (clq33x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_274 = Coupling(name = 'GC_274',
                  value = '(clq13x3x3x1*complex(0,1))/LambdaSMEFT**2 - (clq33x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_275 = Coupling(name = 'GC_275',
                  value = '(clq13x3x3x1*complex(0,1))/LambdaSMEFT**2 + (clq33x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_276 = Coupling(name = 'GC_276',
                  value = '(clq13x3x3x2*complex(0,1))/LambdaSMEFT**2 - (clq33x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_277 = Coupling(name = 'GC_277',
                  value = '(clq13x3x3x2*complex(0,1))/LambdaSMEFT**2 + (clq33x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_278 = Coupling(name = 'GC_278',
                  value = '(clq13x3x3x3*complex(0,1))/LambdaSMEFT**2 - (clq33x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_279 = Coupling(name = 'GC_279',
                  value = '(clq13x3x3x3*complex(0,1))/LambdaSMEFT**2 + (clq33x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_280 = Coupling(name = 'GC_280',
                  value = '(2*cqq11x1x1x1*complex(0,1))/LambdaSMEFT**2 - (2*cqq31x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '(2*cqq11x1x1x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq31x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_282 = Coupling(name = 'GC_282',
                  value = '(cqq11x1x1x2*complex(0,1))/LambdaSMEFT**2 + (cqq11x2x1x1*complex(0,1))/LambdaSMEFT**2 - (cqq31x1x1x2*complex(0,1))/LambdaSMEFT**2 - (cqq31x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_283 = Coupling(name = 'GC_283',
                  value = '(cqq11x1x1x2*complex(0,1))/LambdaSMEFT**2 + (cqq11x2x1x1*complex(0,1))/LambdaSMEFT**2 + (cqq31x1x1x2*complex(0,1))/LambdaSMEFT**2 + (cqq31x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_284 = Coupling(name = 'GC_284',
                  value = '(2*cqq31x1x1x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq31x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_285 = Coupling(name = 'GC_285',
                  value = '(2*cqq11x2x1x2*complex(0,1))/LambdaSMEFT**2 - (2*cqq31x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_286 = Coupling(name = 'GC_286',
                  value = '(2*cqq11x2x1x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq31x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_287 = Coupling(name = 'GC_287',
                  value = '(cqq11x1x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq11x3x1x1*complex(0,1))/LambdaSMEFT**2 - (cqq31x1x1x3*complex(0,1))/LambdaSMEFT**2 - (cqq31x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_288 = Coupling(name = 'GC_288',
                  value = '(cqq11x1x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq11x3x1x1*complex(0,1))/LambdaSMEFT**2 + (cqq31x1x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq31x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_289 = Coupling(name = 'GC_289',
                  value = '(2*cqq31x1x1x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq31x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_290 = Coupling(name = 'GC_290',
                  value = '(cqq11x2x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq11x3x1x2*complex(0,1))/LambdaSMEFT**2 - (cqq31x2x1x3*complex(0,1))/LambdaSMEFT**2 - (cqq31x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_291 = Coupling(name = 'GC_291',
                  value = '(cqq11x2x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq11x3x1x2*complex(0,1))/LambdaSMEFT**2 + (cqq31x2x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq31x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_292 = Coupling(name = 'GC_292',
                  value = '(2*cqq31x2x1x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq31x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_293 = Coupling(name = 'GC_293',
                  value = '(2*cqq11x3x1x3*complex(0,1))/LambdaSMEFT**2 - (2*cqq31x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_294 = Coupling(name = 'GC_294',
                  value = '(2*cqq11x3x1x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq31x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_295 = Coupling(name = 'GC_295',
                  value = '(cqq11x1x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq12x1x1x1*complex(0,1))/LambdaSMEFT**2 - (cqq31x1x2x1*complex(0,1))/LambdaSMEFT**2 - (cqq32x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_296 = Coupling(name = 'GC_296',
                  value = '(cqq11x1x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq12x1x1x1*complex(0,1))/LambdaSMEFT**2 + (cqq31x1x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq32x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_297 = Coupling(name = 'GC_297',
                  value = '(2*cqq31x1x2x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_298 = Coupling(name = 'GC_298',
                  value = '(cqq11x2x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq12x1x1x2*complex(0,1))/LambdaSMEFT**2 - (cqq31x2x2x1*complex(0,1))/LambdaSMEFT**2 - (cqq32x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_299 = Coupling(name = 'GC_299',
                  value = '(cqq11x2x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq12x1x1x2*complex(0,1))/LambdaSMEFT**2 + (cqq31x2x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq32x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_300 = Coupling(name = 'GC_300',
                  value = '(2*cqq31x2x2x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_301 = Coupling(name = 'GC_301',
                  value = '(cqq11x3x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq12x1x1x3*complex(0,1))/LambdaSMEFT**2 - (cqq31x3x2x1*complex(0,1))/LambdaSMEFT**2 - (cqq32x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_302 = Coupling(name = 'GC_302',
                  value = '(cqq11x3x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq12x1x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq31x3x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq32x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_303 = Coupling(name = 'GC_303',
                  value = '(2*cqq31x3x2x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_304 = Coupling(name = 'GC_304',
                  value = '(2*cqq12x1x2x1*complex(0,1))/LambdaSMEFT**2 - (2*cqq32x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_305 = Coupling(name = 'GC_305',
                  value = '(2*cqq12x1x2x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_306 = Coupling(name = 'GC_306',
                  value = '(cqq11x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq12x2x1x1*complex(0,1))/LambdaSMEFT**2 - (cqq31x1x2x2*complex(0,1))/LambdaSMEFT**2 - (cqq32x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_307 = Coupling(name = 'GC_307',
                  value = '(cqq11x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq12x2x1x1*complex(0,1))/LambdaSMEFT**2 + (cqq31x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq32x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_308 = Coupling(name = 'GC_308',
                  value = '(2*cqq31x1x2x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_309 = Coupling(name = 'GC_309',
                  value = '(cqq11x2x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq12x2x1x2*complex(0,1))/LambdaSMEFT**2 - (cqq31x2x2x2*complex(0,1))/LambdaSMEFT**2 - (cqq32x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_310 = Coupling(name = 'GC_310',
                  value = '(cqq11x2x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq12x2x1x2*complex(0,1))/LambdaSMEFT**2 + (cqq31x2x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq32x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_311 = Coupling(name = 'GC_311',
                  value = '(2*cqq31x2x2x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_312 = Coupling(name = 'GC_312',
                  value = '(cqq11x3x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq12x2x1x3*complex(0,1))/LambdaSMEFT**2 - (cqq31x3x2x2*complex(0,1))/LambdaSMEFT**2 - (cqq32x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_313 = Coupling(name = 'GC_313',
                  value = '(cqq11x3x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq12x2x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq31x3x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq32x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_314 = Coupling(name = 'GC_314',
                  value = '(2*cqq31x3x2x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_315 = Coupling(name = 'GC_315',
                  value = '(cqq12x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq12x2x2x1*complex(0,1))/LambdaSMEFT**2 - (cqq32x1x2x2*complex(0,1))/LambdaSMEFT**2 - (cqq32x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_316 = Coupling(name = 'GC_316',
                  value = '(cqq12x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq12x2x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq32x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq32x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_317 = Coupling(name = 'GC_317',
                  value = '(2*cqq32x1x2x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_318 = Coupling(name = 'GC_318',
                  value = '(2*cqq12x2x2x2*complex(0,1))/LambdaSMEFT**2 - (2*cqq32x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_319 = Coupling(name = 'GC_319',
                  value = '(2*cqq12x2x2x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_320 = Coupling(name = 'GC_320',
                  value = '(cqq11x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq12x3x1x1*complex(0,1))/LambdaSMEFT**2 - (cqq31x1x2x3*complex(0,1))/LambdaSMEFT**2 - (cqq32x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_321 = Coupling(name = 'GC_321',
                  value = '(cqq11x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq12x3x1x1*complex(0,1))/LambdaSMEFT**2 + (cqq31x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq32x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_322 = Coupling(name = 'GC_322',
                  value = '(2*cqq31x1x2x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_323 = Coupling(name = 'GC_323',
                  value = '(cqq11x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq12x3x1x2*complex(0,1))/LambdaSMEFT**2 - (cqq31x2x2x3*complex(0,1))/LambdaSMEFT**2 - (cqq32x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_324 = Coupling(name = 'GC_324',
                  value = '(cqq11x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq12x3x1x2*complex(0,1))/LambdaSMEFT**2 + (cqq31x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq32x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_325 = Coupling(name = 'GC_325',
                  value = '(2*cqq31x2x2x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_326 = Coupling(name = 'GC_326',
                  value = '(cqq11x3x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq12x3x1x3*complex(0,1))/LambdaSMEFT**2 - (cqq31x3x2x3*complex(0,1))/LambdaSMEFT**2 - (cqq32x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_327 = Coupling(name = 'GC_327',
                  value = '(cqq11x3x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq12x3x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq31x3x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq32x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_328 = Coupling(name = 'GC_328',
                  value = '(2*cqq31x3x2x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_329 = Coupling(name = 'GC_329',
                  value = '(cqq12x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq12x3x2x1*complex(0,1))/LambdaSMEFT**2 - (cqq32x1x2x3*complex(0,1))/LambdaSMEFT**2 - (cqq32x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_330 = Coupling(name = 'GC_330',
                  value = '(cqq12x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq12x3x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq32x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq32x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_331 = Coupling(name = 'GC_331',
                  value = '(2*cqq32x1x2x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_332 = Coupling(name = 'GC_332',
                  value = '(cqq12x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq12x3x2x2*complex(0,1))/LambdaSMEFT**2 - (cqq32x2x2x3*complex(0,1))/LambdaSMEFT**2 - (cqq32x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_333 = Coupling(name = 'GC_333',
                  value = '(cqq12x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq12x3x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq32x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq32x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_334 = Coupling(name = 'GC_334',
                  value = '(2*cqq32x2x2x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_335 = Coupling(name = 'GC_335',
                  value = '(2*cqq12x3x2x3*complex(0,1))/LambdaSMEFT**2 - (2*cqq32x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_336 = Coupling(name = 'GC_336',
                  value = '(2*cqq12x3x2x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq32x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_337 = Coupling(name = 'GC_337',
                  value = '(cqq11x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x1x1*complex(0,1))/LambdaSMEFT**2 - (cqq31x1x3x1*complex(0,1))/LambdaSMEFT**2 - (cqq33x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_338 = Coupling(name = 'GC_338',
                  value = '(cqq11x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x1x1*complex(0,1))/LambdaSMEFT**2 + (cqq31x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq33x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_339 = Coupling(name = 'GC_339',
                  value = '(2*cqq31x1x3x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_340 = Coupling(name = 'GC_340',
                  value = '(cqq11x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x1x2*complex(0,1))/LambdaSMEFT**2 - (cqq31x2x3x1*complex(0,1))/LambdaSMEFT**2 - (cqq33x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_341 = Coupling(name = 'GC_341',
                  value = '(cqq11x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x1x2*complex(0,1))/LambdaSMEFT**2 + (cqq31x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq33x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_342 = Coupling(name = 'GC_342',
                  value = '(2*cqq31x2x3x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_343 = Coupling(name = 'GC_343',
                  value = '(cqq11x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x1x3*complex(0,1))/LambdaSMEFT**2 - (cqq31x3x3x1*complex(0,1))/LambdaSMEFT**2 - (cqq33x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_344 = Coupling(name = 'GC_344',
                  value = '(cqq11x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq31x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq33x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_345 = Coupling(name = 'GC_345',
                  value = '(2*cqq31x3x3x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_346 = Coupling(name = 'GC_346',
                  value = '(cqq12x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x2x1*complex(0,1))/LambdaSMEFT**2 - (cqq32x1x3x1*complex(0,1))/LambdaSMEFT**2 - (cqq33x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_347 = Coupling(name = 'GC_347',
                  value = '(cqq12x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq32x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq33x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_348 = Coupling(name = 'GC_348',
                  value = '(2*cqq32x1x3x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_349 = Coupling(name = 'GC_349',
                  value = '(cqq12x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x2x2*complex(0,1))/LambdaSMEFT**2 - (cqq32x2x3x1*complex(0,1))/LambdaSMEFT**2 - (cqq33x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_350 = Coupling(name = 'GC_350',
                  value = '(cqq12x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq32x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq33x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_351 = Coupling(name = 'GC_351',
                  value = '(2*cqq32x2x3x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_352 = Coupling(name = 'GC_352',
                  value = '(cqq12x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x2x3*complex(0,1))/LambdaSMEFT**2 - (cqq32x3x3x1*complex(0,1))/LambdaSMEFT**2 - (cqq33x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_353 = Coupling(name = 'GC_353',
                  value = '(cqq12x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq13x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq32x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq33x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_354 = Coupling(name = 'GC_354',
                  value = '(2*cqq32x3x3x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_355 = Coupling(name = 'GC_355',
                  value = '(2*cqq13x1x3x1*complex(0,1))/LambdaSMEFT**2 - (2*cqq33x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_356 = Coupling(name = 'GC_356',
                  value = '(2*cqq13x1x3x1*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_357 = Coupling(name = 'GC_357',
                  value = '(cqq11x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x1x1*complex(0,1))/LambdaSMEFT**2 - (cqq31x1x3x2*complex(0,1))/LambdaSMEFT**2 - (cqq33x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_358 = Coupling(name = 'GC_358',
                  value = '(cqq11x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x1x1*complex(0,1))/LambdaSMEFT**2 + (cqq31x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq33x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_359 = Coupling(name = 'GC_359',
                  value = '(2*cqq31x1x3x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_360 = Coupling(name = 'GC_360',
                  value = '(cqq11x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x1x2*complex(0,1))/LambdaSMEFT**2 - (cqq31x2x3x2*complex(0,1))/LambdaSMEFT**2 - (cqq33x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_361 = Coupling(name = 'GC_361',
                  value = '(cqq11x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x1x2*complex(0,1))/LambdaSMEFT**2 + (cqq31x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq33x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_362 = Coupling(name = 'GC_362',
                  value = '(2*cqq31x2x3x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_363 = Coupling(name = 'GC_363',
                  value = '(cqq11x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x1x3*complex(0,1))/LambdaSMEFT**2 - (cqq31x3x3x2*complex(0,1))/LambdaSMEFT**2 - (cqq33x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_364 = Coupling(name = 'GC_364',
                  value = '(cqq11x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq31x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq33x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_365 = Coupling(name = 'GC_365',
                  value = '(2*cqq31x3x3x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_366 = Coupling(name = 'GC_366',
                  value = '(cqq12x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x2x1*complex(0,1))/LambdaSMEFT**2 - (cqq32x1x3x2*complex(0,1))/LambdaSMEFT**2 - (cqq33x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_367 = Coupling(name = 'GC_367',
                  value = '(cqq12x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq32x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq33x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_368 = Coupling(name = 'GC_368',
                  value = '(2*cqq32x1x3x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_369 = Coupling(name = 'GC_369',
                  value = '(cqq12x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x2x2*complex(0,1))/LambdaSMEFT**2 - (cqq32x2x3x2*complex(0,1))/LambdaSMEFT**2 - (cqq33x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_370 = Coupling(name = 'GC_370',
                  value = '(cqq12x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq32x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq33x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_371 = Coupling(name = 'GC_371',
                  value = '(2*cqq32x2x3x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_372 = Coupling(name = 'GC_372',
                  value = '(cqq12x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x2x3*complex(0,1))/LambdaSMEFT**2 - (cqq32x3x3x2*complex(0,1))/LambdaSMEFT**2 - (cqq33x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_373 = Coupling(name = 'GC_373',
                  value = '(cqq12x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq32x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq33x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_374 = Coupling(name = 'GC_374',
                  value = '(2*cqq32x3x3x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_375 = Coupling(name = 'GC_375',
                  value = '(cqq13x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x3x1*complex(0,1))/LambdaSMEFT**2 - (cqq33x1x3x2*complex(0,1))/LambdaSMEFT**2 - (cqq33x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_376 = Coupling(name = 'GC_376',
                  value = '(cqq13x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq13x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq33x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq33x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_377 = Coupling(name = 'GC_377',
                  value = '(2*cqq33x1x3x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_378 = Coupling(name = 'GC_378',
                  value = '(2*cqq13x2x3x2*complex(0,1))/LambdaSMEFT**2 - (2*cqq33x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_379 = Coupling(name = 'GC_379',
                  value = '(2*cqq13x2x3x2*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_380 = Coupling(name = 'GC_380',
                  value = '(cqq11x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x1x1*complex(0,1))/LambdaSMEFT**2 - (cqq31x1x3x3*complex(0,1))/LambdaSMEFT**2 - (cqq33x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_381 = Coupling(name = 'GC_381',
                  value = '(cqq11x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x1x1*complex(0,1))/LambdaSMEFT**2 + (cqq31x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq33x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_382 = Coupling(name = 'GC_382',
                  value = '(2*cqq31x1x3x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_383 = Coupling(name = 'GC_383',
                  value = '(cqq11x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x1x2*complex(0,1))/LambdaSMEFT**2 - (cqq31x2x3x3*complex(0,1))/LambdaSMEFT**2 - (cqq33x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_384 = Coupling(name = 'GC_384',
                  value = '(cqq11x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x1x2*complex(0,1))/LambdaSMEFT**2 + (cqq31x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq33x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_385 = Coupling(name = 'GC_385',
                  value = '(2*cqq31x2x3x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_386 = Coupling(name = 'GC_386',
                  value = '(cqq11x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x1x3*complex(0,1))/LambdaSMEFT**2 - (cqq31x3x3x3*complex(0,1))/LambdaSMEFT**2 - (cqq33x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_387 = Coupling(name = 'GC_387',
                  value = '(cqq11x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x1x3*complex(0,1))/LambdaSMEFT**2 + (cqq31x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq33x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_388 = Coupling(name = 'GC_388',
                  value = '(2*cqq31x3x3x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_389 = Coupling(name = 'GC_389',
                  value = '(cqq12x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x2x1*complex(0,1))/LambdaSMEFT**2 - (cqq32x1x3x3*complex(0,1))/LambdaSMEFT**2 - (cqq33x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_390 = Coupling(name = 'GC_390',
                  value = '(cqq12x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x2x1*complex(0,1))/LambdaSMEFT**2 + (cqq32x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq33x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_391 = Coupling(name = 'GC_391',
                  value = '(2*cqq32x1x3x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_392 = Coupling(name = 'GC_392',
                  value = '(cqq12x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x2x2*complex(0,1))/LambdaSMEFT**2 - (cqq32x2x3x3*complex(0,1))/LambdaSMEFT**2 - (cqq33x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_393 = Coupling(name = 'GC_393',
                  value = '(cqq12x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x2x2*complex(0,1))/LambdaSMEFT**2 + (cqq32x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq33x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_394 = Coupling(name = 'GC_394',
                  value = '(2*cqq32x2x3x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_395 = Coupling(name = 'GC_395',
                  value = '(cqq12x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x2x3*complex(0,1))/LambdaSMEFT**2 - (cqq32x3x3x3*complex(0,1))/LambdaSMEFT**2 - (cqq33x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_396 = Coupling(name = 'GC_396',
                  value = '(cqq12x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x2x3*complex(0,1))/LambdaSMEFT**2 + (cqq32x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq33x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_397 = Coupling(name = 'GC_397',
                  value = '(2*cqq32x3x3x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_398 = Coupling(name = 'GC_398',
                  value = '(cqq13x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x3x1*complex(0,1))/LambdaSMEFT**2 - (cqq33x1x3x3*complex(0,1))/LambdaSMEFT**2 - (cqq33x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_399 = Coupling(name = 'GC_399',
                  value = '(cqq13x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cqq33x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq33x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_400 = Coupling(name = 'GC_400',
                  value = '(2*cqq33x1x3x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_401 = Coupling(name = 'GC_401',
                  value = '(cqq13x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x3x2*complex(0,1))/LambdaSMEFT**2 - (cqq33x2x3x3*complex(0,1))/LambdaSMEFT**2 - (cqq33x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_402 = Coupling(name = 'GC_402',
                  value = '(cqq13x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq13x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cqq33x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cqq33x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_403 = Coupling(name = 'GC_403',
                  value = '(2*cqq33x2x3x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_404 = Coupling(name = 'GC_404',
                  value = '(2*cqq13x3x3x3*complex(0,1))/LambdaSMEFT**2 - (2*cqq33x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_405 = Coupling(name = 'GC_405',
                  value = '(2*cqq13x3x3x3*complex(0,1))/LambdaSMEFT**2 + (2*cqq33x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_406 = Coupling(name = 'GC_406',
                  value = '(cuu1x1x1x2*complex(0,1))/LambdaSMEFT**2 + (cuu1x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_407 = Coupling(name = 'GC_407',
                  value = '(cuu1x1x1x3*complex(0,1))/LambdaSMEFT**2 + (cuu1x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_408 = Coupling(name = 'GC_408',
                  value = '(cuu1x2x1x3*complex(0,1))/LambdaSMEFT**2 + (cuu1x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_409 = Coupling(name = 'GC_409',
                  value = '(cuu1x1x2x1*complex(0,1))/LambdaSMEFT**2 + (cuu2x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_410 = Coupling(name = 'GC_410',
                  value = '(cuu1x2x2x1*complex(0,1))/LambdaSMEFT**2 + (cuu2x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_411 = Coupling(name = 'GC_411',
                  value = '(cuu1x3x2x1*complex(0,1))/LambdaSMEFT**2 + (cuu2x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_412 = Coupling(name = 'GC_412',
                  value = '(cuu1x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cuu2x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_413 = Coupling(name = 'GC_413',
                  value = '(cuu1x2x2x2*complex(0,1))/LambdaSMEFT**2 + (cuu2x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_414 = Coupling(name = 'GC_414',
                  value = '(cuu1x3x2x2*complex(0,1))/LambdaSMEFT**2 + (cuu2x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_415 = Coupling(name = 'GC_415',
                  value = '(cuu2x1x2x2*complex(0,1))/LambdaSMEFT**2 + (cuu2x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_416 = Coupling(name = 'GC_416',
                  value = '(cuu1x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cuu2x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_417 = Coupling(name = 'GC_417',
                  value = '(cuu1x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cuu2x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_418 = Coupling(name = 'GC_418',
                  value = '(cuu1x3x2x3*complex(0,1))/LambdaSMEFT**2 + (cuu2x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_419 = Coupling(name = 'GC_419',
                  value = '(cuu2x1x2x3*complex(0,1))/LambdaSMEFT**2 + (cuu2x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_420 = Coupling(name = 'GC_420',
                  value = '(cuu2x2x2x3*complex(0,1))/LambdaSMEFT**2 + (cuu2x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_421 = Coupling(name = 'GC_421',
                  value = '(cuu1x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cuu3x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_422 = Coupling(name = 'GC_422',
                  value = '(cuu1x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cuu3x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_423 = Coupling(name = 'GC_423',
                  value = '(cuu1x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cuu3x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_424 = Coupling(name = 'GC_424',
                  value = '(cuu2x1x3x1*complex(0,1))/LambdaSMEFT**2 + (cuu3x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_425 = Coupling(name = 'GC_425',
                  value = '(cuu2x2x3x1*complex(0,1))/LambdaSMEFT**2 + (cuu3x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_426 = Coupling(name = 'GC_426',
                  value = '(cuu2x3x3x1*complex(0,1))/LambdaSMEFT**2 + (cuu3x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_427 = Coupling(name = 'GC_427',
                  value = '(cuu1x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cuu3x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_428 = Coupling(name = 'GC_428',
                  value = '(cuu1x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cuu3x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_429 = Coupling(name = 'GC_429',
                  value = '(cuu1x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cuu3x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_430 = Coupling(name = 'GC_430',
                  value = '(cuu2x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cuu3x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_431 = Coupling(name = 'GC_431',
                  value = '(cuu2x2x3x2*complex(0,1))/LambdaSMEFT**2 + (cuu3x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_432 = Coupling(name = 'GC_432',
                  value = '(cuu2x3x3x2*complex(0,1))/LambdaSMEFT**2 + (cuu3x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_433 = Coupling(name = 'GC_433',
                  value = '(cuu3x1x3x2*complex(0,1))/LambdaSMEFT**2 + (cuu3x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_434 = Coupling(name = 'GC_434',
                  value = '(cuu1x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cuu3x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_435 = Coupling(name = 'GC_435',
                  value = '(cuu1x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cuu3x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_436 = Coupling(name = 'GC_436',
                  value = '(cuu1x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cuu3x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_437 = Coupling(name = 'GC_437',
                  value = '(cuu2x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cuu3x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_438 = Coupling(name = 'GC_438',
                  value = '(cuu2x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cuu3x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_439 = Coupling(name = 'GC_439',
                  value = '(cuu2x3x3x3*complex(0,1))/LambdaSMEFT**2 + (cuu3x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_440 = Coupling(name = 'GC_440',
                  value = '(cuu3x1x3x3*complex(0,1))/LambdaSMEFT**2 + (cuu3x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_441 = Coupling(name = 'GC_441',
                  value = '(cuu3x2x3x3*complex(0,1))/LambdaSMEFT**2 + (cuu3x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_442 = Coupling(name = 'GC_442',
                  value = '(2*cdd1x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_443 = Coupling(name = 'GC_443',
                  value = '(2*cdd1x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_444 = Coupling(name = 'GC_444',
                  value = '(2*cdd1x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_445 = Coupling(name = 'GC_445',
                  value = '(2*cdd2x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_446 = Coupling(name = 'GC_446',
                  value = '(2*cdd2x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_447 = Coupling(name = 'GC_447',
                  value = '(2*cdd2x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_448 = Coupling(name = 'GC_448',
                  value = '(2*cdd3x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_449 = Coupling(name = 'GC_449',
                  value = '(2*cdd3x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_450 = Coupling(name = 'GC_450',
                  value = '(2*cdd3x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_451 = Coupling(name = 'GC_451',
                  value = '(cdG1x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_452 = Coupling(name = 'GC_452',
                  value = '(cdG1x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_453 = Coupling(name = 'GC_453',
                  value = '(cdG1x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_454 = Coupling(name = 'GC_454',
                  value = '(cdG2x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_455 = Coupling(name = 'GC_455',
                  value = '(cdG2x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_456 = Coupling(name = 'GC_456',
                  value = '(cdG2x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_457 = Coupling(name = 'GC_457',
                  value = '(cdG3x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_458 = Coupling(name = 'GC_458',
                  value = '(cdG3x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_459 = Coupling(name = 'GC_459',
                  value = '(cdG3x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_460 = Coupling(name = 'GC_460',
                  value = '(cdW1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_461 = Coupling(name = 'GC_461',
                  value = '(cdW1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_462 = Coupling(name = 'GC_462',
                  value = '(cdW1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_463 = Coupling(name = 'GC_463',
                  value = '(cdW2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_464 = Coupling(name = 'GC_464',
                  value = '(cdW2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_465 = Coupling(name = 'GC_465',
                  value = '(cdW2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_466 = Coupling(name = 'GC_466',
                  value = '(cdW3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_467 = Coupling(name = 'GC_467',
                  value = '(cdW3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_468 = Coupling(name = 'GC_468',
                  value = '(cdW3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_469 = Coupling(name = 'GC_469',
                  value = '(ced1x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_470 = Coupling(name = 'GC_470',
                  value = '(ced1x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_471 = Coupling(name = 'GC_471',
                  value = '(ced1x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_472 = Coupling(name = 'GC_472',
                  value = '(ced1x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_473 = Coupling(name = 'GC_473',
                  value = '(ced1x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_474 = Coupling(name = 'GC_474',
                  value = '(ced1x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_475 = Coupling(name = 'GC_475',
                  value = '(ced1x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_476 = Coupling(name = 'GC_476',
                  value = '(ced1x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_477 = Coupling(name = 'GC_477',
                  value = '(ced1x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_478 = Coupling(name = 'GC_478',
                  value = '(ced1x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_479 = Coupling(name = 'GC_479',
                  value = '(ced1x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_480 = Coupling(name = 'GC_480',
                  value = '(ced1x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_481 = Coupling(name = 'GC_481',
                  value = '(ced1x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_482 = Coupling(name = 'GC_482',
                  value = '(ced1x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_483 = Coupling(name = 'GC_483',
                  value = '(ced1x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_484 = Coupling(name = 'GC_484',
                  value = '(ced1x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_485 = Coupling(name = 'GC_485',
                  value = '(ced1x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_486 = Coupling(name = 'GC_486',
                  value = '(ced1x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_487 = Coupling(name = 'GC_487',
                  value = '(ced1x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_488 = Coupling(name = 'GC_488',
                  value = '(ced1x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_489 = Coupling(name = 'GC_489',
                  value = '(ced1x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_490 = Coupling(name = 'GC_490',
                  value = '(ced1x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_491 = Coupling(name = 'GC_491',
                  value = '(ced1x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_492 = Coupling(name = 'GC_492',
                  value = '(ced1x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_493 = Coupling(name = 'GC_493',
                  value = '(ced1x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_494 = Coupling(name = 'GC_494',
                  value = '(ced1x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_495 = Coupling(name = 'GC_495',
                  value = '(ced1x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_496 = Coupling(name = 'GC_496',
                  value = '(ced2x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_497 = Coupling(name = 'GC_497',
                  value = '(ced2x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_498 = Coupling(name = 'GC_498',
                  value = '(ced2x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_499 = Coupling(name = 'GC_499',
                  value = '(ced2x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_500 = Coupling(name = 'GC_500',
                  value = '(ced2x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_501 = Coupling(name = 'GC_501',
                  value = '(ced2x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_502 = Coupling(name = 'GC_502',
                  value = '(ced2x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_503 = Coupling(name = 'GC_503',
                  value = '(ced2x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_504 = Coupling(name = 'GC_504',
                  value = '(ced2x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_505 = Coupling(name = 'GC_505',
                  value = '(ced2x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_506 = Coupling(name = 'GC_506',
                  value = '(ced2x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_507 = Coupling(name = 'GC_507',
                  value = '(ced2x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_508 = Coupling(name = 'GC_508',
                  value = '(ced2x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_509 = Coupling(name = 'GC_509',
                  value = '(ced2x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_510 = Coupling(name = 'GC_510',
                  value = '(ced2x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_511 = Coupling(name = 'GC_511',
                  value = '(ced2x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_512 = Coupling(name = 'GC_512',
                  value = '(ced2x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_513 = Coupling(name = 'GC_513',
                  value = '(ced2x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_514 = Coupling(name = 'GC_514',
                  value = '(ced2x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_515 = Coupling(name = 'GC_515',
                  value = '(ced2x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_516 = Coupling(name = 'GC_516',
                  value = '(ced2x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_517 = Coupling(name = 'GC_517',
                  value = '(ced2x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_518 = Coupling(name = 'GC_518',
                  value = '(ced2x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_519 = Coupling(name = 'GC_519',
                  value = '(ced2x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_520 = Coupling(name = 'GC_520',
                  value = '(ced2x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_521 = Coupling(name = 'GC_521',
                  value = '(ced2x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_522 = Coupling(name = 'GC_522',
                  value = '(ced2x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_523 = Coupling(name = 'GC_523',
                  value = '(ced3x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_524 = Coupling(name = 'GC_524',
                  value = '(ced3x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_525 = Coupling(name = 'GC_525',
                  value = '(ced3x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_526 = Coupling(name = 'GC_526',
                  value = '(ced3x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_527 = Coupling(name = 'GC_527',
                  value = '(ced3x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_528 = Coupling(name = 'GC_528',
                  value = '(ced3x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_529 = Coupling(name = 'GC_529',
                  value = '(ced3x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_530 = Coupling(name = 'GC_530',
                  value = '(ced3x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_531 = Coupling(name = 'GC_531',
                  value = '(ced3x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_532 = Coupling(name = 'GC_532',
                  value = '(ced3x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_533 = Coupling(name = 'GC_533',
                  value = '(ced3x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_534 = Coupling(name = 'GC_534',
                  value = '(ced3x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_535 = Coupling(name = 'GC_535',
                  value = '(ced3x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_536 = Coupling(name = 'GC_536',
                  value = '(ced3x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_537 = Coupling(name = 'GC_537',
                  value = '(ced3x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_538 = Coupling(name = 'GC_538',
                  value = '(ced3x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_539 = Coupling(name = 'GC_539',
                  value = '(ced3x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_540 = Coupling(name = 'GC_540',
                  value = '(ced3x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_541 = Coupling(name = 'GC_541',
                  value = '(ced3x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_542 = Coupling(name = 'GC_542',
                  value = '(ced3x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_543 = Coupling(name = 'GC_543',
                  value = '(ced3x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_544 = Coupling(name = 'GC_544',
                  value = '(ced3x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_545 = Coupling(name = 'GC_545',
                  value = '(ced3x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_546 = Coupling(name = 'GC_546',
                  value = '(ced3x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_547 = Coupling(name = 'GC_547',
                  value = '(ced3x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_548 = Coupling(name = 'GC_548',
                  value = '(ced3x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_549 = Coupling(name = 'GC_549',
                  value = '(ced3x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_550 = Coupling(name = 'GC_550',
                  value = '(2*cee1x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_551 = Coupling(name = 'GC_551',
                  value = '(2*cee1x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_552 = Coupling(name = 'GC_552',
                  value = '(2*cee1x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_553 = Coupling(name = 'GC_553',
                  value = '(2*cee2x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_554 = Coupling(name = 'GC_554',
                  value = '(2*cee2x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_555 = Coupling(name = 'GC_555',
                  value = '(2*cee2x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_556 = Coupling(name = 'GC_556',
                  value = '(2*cee3x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_557 = Coupling(name = 'GC_557',
                  value = '(2*cee3x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_558 = Coupling(name = 'GC_558',
                  value = '(2*cee3x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_559 = Coupling(name = 'GC_559',
                  value = '(ceu1x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_560 = Coupling(name = 'GC_560',
                  value = '(ceu1x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_561 = Coupling(name = 'GC_561',
                  value = '(ceu1x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_562 = Coupling(name = 'GC_562',
                  value = '(ceu1x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_563 = Coupling(name = 'GC_563',
                  value = '(ceu1x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_564 = Coupling(name = 'GC_564',
                  value = '(ceu1x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_565 = Coupling(name = 'GC_565',
                  value = '(ceu1x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_566 = Coupling(name = 'GC_566',
                  value = '(ceu1x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_567 = Coupling(name = 'GC_567',
                  value = '(ceu1x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_568 = Coupling(name = 'GC_568',
                  value = '(ceu1x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_569 = Coupling(name = 'GC_569',
                  value = '(ceu1x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_570 = Coupling(name = 'GC_570',
                  value = '(ceu1x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_571 = Coupling(name = 'GC_571',
                  value = '(ceu1x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_572 = Coupling(name = 'GC_572',
                  value = '(ceu1x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_573 = Coupling(name = 'GC_573',
                  value = '(ceu1x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_574 = Coupling(name = 'GC_574',
                  value = '(ceu1x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_575 = Coupling(name = 'GC_575',
                  value = '(ceu1x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_576 = Coupling(name = 'GC_576',
                  value = '(ceu1x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_577 = Coupling(name = 'GC_577',
                  value = '(ceu1x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_578 = Coupling(name = 'GC_578',
                  value = '(ceu1x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_579 = Coupling(name = 'GC_579',
                  value = '(ceu1x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_580 = Coupling(name = 'GC_580',
                  value = '(ceu1x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_581 = Coupling(name = 'GC_581',
                  value = '(ceu1x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_582 = Coupling(name = 'GC_582',
                  value = '(ceu1x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_583 = Coupling(name = 'GC_583',
                  value = '(ceu1x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_584 = Coupling(name = 'GC_584',
                  value = '(ceu1x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_585 = Coupling(name = 'GC_585',
                  value = '(ceu1x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_586 = Coupling(name = 'GC_586',
                  value = '(ceu2x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_587 = Coupling(name = 'GC_587',
                  value = '(ceu2x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_588 = Coupling(name = 'GC_588',
                  value = '(ceu2x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_589 = Coupling(name = 'GC_589',
                  value = '(ceu2x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_590 = Coupling(name = 'GC_590',
                  value = '(ceu2x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_591 = Coupling(name = 'GC_591',
                  value = '(ceu2x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_592 = Coupling(name = 'GC_592',
                  value = '(ceu2x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_593 = Coupling(name = 'GC_593',
                  value = '(ceu2x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_594 = Coupling(name = 'GC_594',
                  value = '(ceu2x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_595 = Coupling(name = 'GC_595',
                  value = '(ceu2x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_596 = Coupling(name = 'GC_596',
                  value = '(ceu2x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_597 = Coupling(name = 'GC_597',
                  value = '(ceu2x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_598 = Coupling(name = 'GC_598',
                  value = '(ceu2x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_599 = Coupling(name = 'GC_599',
                  value = '(ceu2x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_600 = Coupling(name = 'GC_600',
                  value = '(ceu2x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_601 = Coupling(name = 'GC_601',
                  value = '(ceu2x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_602 = Coupling(name = 'GC_602',
                  value = '(ceu2x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_603 = Coupling(name = 'GC_603',
                  value = '(ceu2x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_604 = Coupling(name = 'GC_604',
                  value = '(ceu2x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_605 = Coupling(name = 'GC_605',
                  value = '(ceu2x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_606 = Coupling(name = 'GC_606',
                  value = '(ceu2x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_607 = Coupling(name = 'GC_607',
                  value = '(ceu2x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_608 = Coupling(name = 'GC_608',
                  value = '(ceu2x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_609 = Coupling(name = 'GC_609',
                  value = '(ceu2x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_610 = Coupling(name = 'GC_610',
                  value = '(ceu2x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_611 = Coupling(name = 'GC_611',
                  value = '(ceu2x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_612 = Coupling(name = 'GC_612',
                  value = '(ceu2x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_613 = Coupling(name = 'GC_613',
                  value = '(ceu3x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_614 = Coupling(name = 'GC_614',
                  value = '(ceu3x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_615 = Coupling(name = 'GC_615',
                  value = '(ceu3x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_616 = Coupling(name = 'GC_616',
                  value = '(ceu3x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_617 = Coupling(name = 'GC_617',
                  value = '(ceu3x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_618 = Coupling(name = 'GC_618',
                  value = '(ceu3x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_619 = Coupling(name = 'GC_619',
                  value = '(ceu3x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_620 = Coupling(name = 'GC_620',
                  value = '(ceu3x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_621 = Coupling(name = 'GC_621',
                  value = '(ceu3x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_622 = Coupling(name = 'GC_622',
                  value = '(ceu3x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_623 = Coupling(name = 'GC_623',
                  value = '(ceu3x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_624 = Coupling(name = 'GC_624',
                  value = '(ceu3x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_625 = Coupling(name = 'GC_625',
                  value = '(ceu3x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_626 = Coupling(name = 'GC_626',
                  value = '(ceu3x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_627 = Coupling(name = 'GC_627',
                  value = '(ceu3x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_628 = Coupling(name = 'GC_628',
                  value = '(ceu3x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_629 = Coupling(name = 'GC_629',
                  value = '(ceu3x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_630 = Coupling(name = 'GC_630',
                  value = '(ceu3x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_631 = Coupling(name = 'GC_631',
                  value = '(ceu3x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_632 = Coupling(name = 'GC_632',
                  value = '(ceu3x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_633 = Coupling(name = 'GC_633',
                  value = '(ceu3x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_634 = Coupling(name = 'GC_634',
                  value = '(ceu3x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_635 = Coupling(name = 'GC_635',
                  value = '(ceu3x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_636 = Coupling(name = 'GC_636',
                  value = '(ceu3x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_637 = Coupling(name = 'GC_637',
                  value = '(ceu3x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_638 = Coupling(name = 'GC_638',
                  value = '(ceu3x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_639 = Coupling(name = 'GC_639',
                  value = '(ceu3x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_640 = Coupling(name = 'GC_640',
                  value = '(ceW1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_641 = Coupling(name = 'GC_641',
                  value = '(ceW1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_642 = Coupling(name = 'GC_642',
                  value = '(ceW1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_643 = Coupling(name = 'GC_643',
                  value = '(ceW2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_644 = Coupling(name = 'GC_644',
                  value = '(ceW2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_645 = Coupling(name = 'GC_645',
                  value = '(ceW2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_646 = Coupling(name = 'GC_646',
                  value = '(ceW3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_647 = Coupling(name = 'GC_647',
                  value = '(ceW3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_648 = Coupling(name = 'GC_648',
                  value = '(ceW3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_649 = Coupling(name = 'GC_649',
                  value = '(-6*cG)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_650 = Coupling(name = 'GC_650',
                  value = 'cGtil/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_651 = Coupling(name = 'GC_651',
                  value = '(-3*cHbox*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_652 = Coupling(name = 'GC_652',
                  value = '-((cHDD*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_653 = Coupling(name = 'GC_653',
                  value = '(4*cHG*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_654 = Coupling(name = 'GC_654',
                  value = '(-2*cHGtil*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_655 = Coupling(name = 'GC_655',
                  value = '(4*cHW*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_656 = Coupling(name = 'GC_656',
                  value = '(4*cHWtil*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_657 = Coupling(name = 'GC_657',
                  value = '(cld1x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_658 = Coupling(name = 'GC_658',
                  value = '(cld1x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_659 = Coupling(name = 'GC_659',
                  value = '(cld1x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_660 = Coupling(name = 'GC_660',
                  value = '(cld1x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_661 = Coupling(name = 'GC_661',
                  value = '(cld1x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_662 = Coupling(name = 'GC_662',
                  value = '(cld1x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_663 = Coupling(name = 'GC_663',
                  value = '(cld1x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_664 = Coupling(name = 'GC_664',
                  value = '(cld1x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_665 = Coupling(name = 'GC_665',
                  value = '(cld1x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_666 = Coupling(name = 'GC_666',
                  value = '(cld1x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_667 = Coupling(name = 'GC_667',
                  value = '(cld1x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_668 = Coupling(name = 'GC_668',
                  value = '(cld1x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_669 = Coupling(name = 'GC_669',
                  value = '(cld1x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_670 = Coupling(name = 'GC_670',
                  value = '(cld1x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_671 = Coupling(name = 'GC_671',
                  value = '(cld1x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_672 = Coupling(name = 'GC_672',
                  value = '(cld1x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_673 = Coupling(name = 'GC_673',
                  value = '(cld1x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_674 = Coupling(name = 'GC_674',
                  value = '(cld1x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_675 = Coupling(name = 'GC_675',
                  value = '(cld1x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_676 = Coupling(name = 'GC_676',
                  value = '(cld1x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_677 = Coupling(name = 'GC_677',
                  value = '(cld1x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_678 = Coupling(name = 'GC_678',
                  value = '(cld1x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_679 = Coupling(name = 'GC_679',
                  value = '(cld1x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_680 = Coupling(name = 'GC_680',
                  value = '(cld1x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_681 = Coupling(name = 'GC_681',
                  value = '(cld1x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_682 = Coupling(name = 'GC_682',
                  value = '(cld1x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_683 = Coupling(name = 'GC_683',
                  value = '(cld1x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_684 = Coupling(name = 'GC_684',
                  value = '(cld2x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_685 = Coupling(name = 'GC_685',
                  value = '(cld2x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_686 = Coupling(name = 'GC_686',
                  value = '(cld2x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_687 = Coupling(name = 'GC_687',
                  value = '(cld2x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_688 = Coupling(name = 'GC_688',
                  value = '(cld2x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_689 = Coupling(name = 'GC_689',
                  value = '(cld2x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_690 = Coupling(name = 'GC_690',
                  value = '(cld2x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_691 = Coupling(name = 'GC_691',
                  value = '(cld2x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_692 = Coupling(name = 'GC_692',
                  value = '(cld2x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_693 = Coupling(name = 'GC_693',
                  value = '(cld2x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_694 = Coupling(name = 'GC_694',
                  value = '(cld2x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_695 = Coupling(name = 'GC_695',
                  value = '(cld2x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_696 = Coupling(name = 'GC_696',
                  value = '(cld2x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_697 = Coupling(name = 'GC_697',
                  value = '(cld2x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_698 = Coupling(name = 'GC_698',
                  value = '(cld2x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_699 = Coupling(name = 'GC_699',
                  value = '(cld2x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_700 = Coupling(name = 'GC_700',
                  value = '(cld2x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_701 = Coupling(name = 'GC_701',
                  value = '(cld2x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_702 = Coupling(name = 'GC_702',
                  value = '(cld2x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_703 = Coupling(name = 'GC_703',
                  value = '(cld2x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_704 = Coupling(name = 'GC_704',
                  value = '(cld2x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_705 = Coupling(name = 'GC_705',
                  value = '(cld2x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_706 = Coupling(name = 'GC_706',
                  value = '(cld2x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_707 = Coupling(name = 'GC_707',
                  value = '(cld2x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_708 = Coupling(name = 'GC_708',
                  value = '(cld2x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_709 = Coupling(name = 'GC_709',
                  value = '(cld2x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_710 = Coupling(name = 'GC_710',
                  value = '(cld2x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_711 = Coupling(name = 'GC_711',
                  value = '(cld3x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_712 = Coupling(name = 'GC_712',
                  value = '(cld3x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_713 = Coupling(name = 'GC_713',
                  value = '(cld3x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_714 = Coupling(name = 'GC_714',
                  value = '(cld3x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_715 = Coupling(name = 'GC_715',
                  value = '(cld3x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_716 = Coupling(name = 'GC_716',
                  value = '(cld3x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_717 = Coupling(name = 'GC_717',
                  value = '(cld3x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_718 = Coupling(name = 'GC_718',
                  value = '(cld3x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_719 = Coupling(name = 'GC_719',
                  value = '(cld3x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_720 = Coupling(name = 'GC_720',
                  value = '(cld3x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_721 = Coupling(name = 'GC_721',
                  value = '(cld3x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_722 = Coupling(name = 'GC_722',
                  value = '(cld3x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_723 = Coupling(name = 'GC_723',
                  value = '(cld3x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_724 = Coupling(name = 'GC_724',
                  value = '(cld3x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_725 = Coupling(name = 'GC_725',
                  value = '(cld3x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_726 = Coupling(name = 'GC_726',
                  value = '(cld3x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_727 = Coupling(name = 'GC_727',
                  value = '(cld3x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_728 = Coupling(name = 'GC_728',
                  value = '(cld3x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_729 = Coupling(name = 'GC_729',
                  value = '(cld3x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_730 = Coupling(name = 'GC_730',
                  value = '(cld3x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_731 = Coupling(name = 'GC_731',
                  value = '(cld3x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_732 = Coupling(name = 'GC_732',
                  value = '(cld3x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_733 = Coupling(name = 'GC_733',
                  value = '(cld3x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_734 = Coupling(name = 'GC_734',
                  value = '(cld3x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_735 = Coupling(name = 'GC_735',
                  value = '(cld3x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_736 = Coupling(name = 'GC_736',
                  value = '(cld3x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_737 = Coupling(name = 'GC_737',
                  value = '(cld3x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_738 = Coupling(name = 'GC_738',
                  value = '(cle1x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_739 = Coupling(name = 'GC_739',
                  value = '(cle1x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_740 = Coupling(name = 'GC_740',
                  value = '(cle1x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_741 = Coupling(name = 'GC_741',
                  value = '(cle1x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_742 = Coupling(name = 'GC_742',
                  value = '(cle1x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_743 = Coupling(name = 'GC_743',
                  value = '(cle1x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_744 = Coupling(name = 'GC_744',
                  value = '(cle1x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_745 = Coupling(name = 'GC_745',
                  value = '(cle1x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_746 = Coupling(name = 'GC_746',
                  value = '(cle1x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_747 = Coupling(name = 'GC_747',
                  value = '(cle1x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_748 = Coupling(name = 'GC_748',
                  value = '(cle1x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_749 = Coupling(name = 'GC_749',
                  value = '(cle1x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_750 = Coupling(name = 'GC_750',
                  value = '(cle1x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_751 = Coupling(name = 'GC_751',
                  value = '(cle1x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_752 = Coupling(name = 'GC_752',
                  value = '(cle1x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_753 = Coupling(name = 'GC_753',
                  value = '(cle1x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_754 = Coupling(name = 'GC_754',
                  value = '(cle1x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_755 = Coupling(name = 'GC_755',
                  value = '(cle1x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_756 = Coupling(name = 'GC_756',
                  value = '(cle1x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_757 = Coupling(name = 'GC_757',
                  value = '(cle1x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_758 = Coupling(name = 'GC_758',
                  value = '(cle1x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_759 = Coupling(name = 'GC_759',
                  value = '(cle1x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_760 = Coupling(name = 'GC_760',
                  value = '(cle1x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_761 = Coupling(name = 'GC_761',
                  value = '(cle1x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_762 = Coupling(name = 'GC_762',
                  value = '(cle1x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_763 = Coupling(name = 'GC_763',
                  value = '(cle1x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_764 = Coupling(name = 'GC_764',
                  value = '(cle1x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_765 = Coupling(name = 'GC_765',
                  value = '(cle2x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_766 = Coupling(name = 'GC_766',
                  value = '(cle2x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_767 = Coupling(name = 'GC_767',
                  value = '(cle2x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_768 = Coupling(name = 'GC_768',
                  value = '(cle2x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_769 = Coupling(name = 'GC_769',
                  value = '(cle2x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_770 = Coupling(name = 'GC_770',
                  value = '(cle2x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_771 = Coupling(name = 'GC_771',
                  value = '(cle2x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_772 = Coupling(name = 'GC_772',
                  value = '(cle2x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_773 = Coupling(name = 'GC_773',
                  value = '(cle2x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_774 = Coupling(name = 'GC_774',
                  value = '(cle2x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_775 = Coupling(name = 'GC_775',
                  value = '(cle2x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_776 = Coupling(name = 'GC_776',
                  value = '(cle2x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_777 = Coupling(name = 'GC_777',
                  value = '(cle2x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_778 = Coupling(name = 'GC_778',
                  value = '(cle2x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_779 = Coupling(name = 'GC_779',
                  value = '(cle2x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_780 = Coupling(name = 'GC_780',
                  value = '(cle2x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_781 = Coupling(name = 'GC_781',
                  value = '(cle2x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_782 = Coupling(name = 'GC_782',
                  value = '(cle2x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_783 = Coupling(name = 'GC_783',
                  value = '(cle2x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_784 = Coupling(name = 'GC_784',
                  value = '(cle2x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_785 = Coupling(name = 'GC_785',
                  value = '(cle2x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_786 = Coupling(name = 'GC_786',
                  value = '(cle2x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_787 = Coupling(name = 'GC_787',
                  value = '(cle2x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_788 = Coupling(name = 'GC_788',
                  value = '(cle2x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_789 = Coupling(name = 'GC_789',
                  value = '(cle2x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_790 = Coupling(name = 'GC_790',
                  value = '(cle2x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_791 = Coupling(name = 'GC_791',
                  value = '(cle2x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_792 = Coupling(name = 'GC_792',
                  value = '(cle3x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_793 = Coupling(name = 'GC_793',
                  value = '(cle3x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_794 = Coupling(name = 'GC_794',
                  value = '(cle3x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_795 = Coupling(name = 'GC_795',
                  value = '(cle3x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_796 = Coupling(name = 'GC_796',
                  value = '(cle3x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_797 = Coupling(name = 'GC_797',
                  value = '(cle3x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_798 = Coupling(name = 'GC_798',
                  value = '(cle3x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_799 = Coupling(name = 'GC_799',
                  value = '(cle3x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_800 = Coupling(name = 'GC_800',
                  value = '(cle3x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_801 = Coupling(name = 'GC_801',
                  value = '(cle3x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_802 = Coupling(name = 'GC_802',
                  value = '(cle3x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_803 = Coupling(name = 'GC_803',
                  value = '(cle3x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_804 = Coupling(name = 'GC_804',
                  value = '(cle3x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_805 = Coupling(name = 'GC_805',
                  value = '(cle3x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_806 = Coupling(name = 'GC_806',
                  value = '(cle3x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_807 = Coupling(name = 'GC_807',
                  value = '(cle3x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_808 = Coupling(name = 'GC_808',
                  value = '(cle3x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_809 = Coupling(name = 'GC_809',
                  value = '(cle3x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_810 = Coupling(name = 'GC_810',
                  value = '(cle3x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_811 = Coupling(name = 'GC_811',
                  value = '(cle3x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_812 = Coupling(name = 'GC_812',
                  value = '(cle3x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_813 = Coupling(name = 'GC_813',
                  value = '(cle3x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_814 = Coupling(name = 'GC_814',
                  value = '(cle3x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_815 = Coupling(name = 'GC_815',
                  value = '(cle3x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_816 = Coupling(name = 'GC_816',
                  value = '(cle3x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_817 = Coupling(name = 'GC_817',
                  value = '(cle3x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_818 = Coupling(name = 'GC_818',
                  value = '(cle3x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_819 = Coupling(name = 'GC_819',
                  value = '(cledq1x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_820 = Coupling(name = 'GC_820',
                  value = '(cledq1x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_821 = Coupling(name = 'GC_821',
                  value = '(cledq1x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_822 = Coupling(name = 'GC_822',
                  value = '(cledq1x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_823 = Coupling(name = 'GC_823',
                  value = '(cledq1x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_824 = Coupling(name = 'GC_824',
                  value = '(cledq1x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_825 = Coupling(name = 'GC_825',
                  value = '(cledq1x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_826 = Coupling(name = 'GC_826',
                  value = '(cledq1x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_827 = Coupling(name = 'GC_827',
                  value = '(cledq1x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_828 = Coupling(name = 'GC_828',
                  value = '(cledq1x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_829 = Coupling(name = 'GC_829',
                  value = '(cledq1x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_830 = Coupling(name = 'GC_830',
                  value = '(cledq1x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_831 = Coupling(name = 'GC_831',
                  value = '(cledq1x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_832 = Coupling(name = 'GC_832',
                  value = '(cledq1x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_833 = Coupling(name = 'GC_833',
                  value = '(cledq1x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_834 = Coupling(name = 'GC_834',
                  value = '(cledq1x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_835 = Coupling(name = 'GC_835',
                  value = '(cledq1x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_836 = Coupling(name = 'GC_836',
                  value = '(cledq1x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_837 = Coupling(name = 'GC_837',
                  value = '(cledq1x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_838 = Coupling(name = 'GC_838',
                  value = '(cledq1x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_839 = Coupling(name = 'GC_839',
                  value = '(cledq1x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_840 = Coupling(name = 'GC_840',
                  value = '(cledq1x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_841 = Coupling(name = 'GC_841',
                  value = '(cledq1x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_842 = Coupling(name = 'GC_842',
                  value = '(cledq1x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_843 = Coupling(name = 'GC_843',
                  value = '(cledq1x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_844 = Coupling(name = 'GC_844',
                  value = '(cledq1x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_845 = Coupling(name = 'GC_845',
                  value = '(cledq1x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_846 = Coupling(name = 'GC_846',
                  value = '(cledq2x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_847 = Coupling(name = 'GC_847',
                  value = '(cledq2x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_848 = Coupling(name = 'GC_848',
                  value = '(cledq2x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_849 = Coupling(name = 'GC_849',
                  value = '(cledq2x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_850 = Coupling(name = 'GC_850',
                  value = '(cledq2x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_851 = Coupling(name = 'GC_851',
                  value = '(cledq2x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_852 = Coupling(name = 'GC_852',
                  value = '(cledq2x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_853 = Coupling(name = 'GC_853',
                  value = '(cledq2x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_854 = Coupling(name = 'GC_854',
                  value = '(cledq2x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_855 = Coupling(name = 'GC_855',
                  value = '(cledq2x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_856 = Coupling(name = 'GC_856',
                  value = '(cledq2x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_857 = Coupling(name = 'GC_857',
                  value = '(cledq2x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_858 = Coupling(name = 'GC_858',
                  value = '(cledq2x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_859 = Coupling(name = 'GC_859',
                  value = '(cledq2x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_860 = Coupling(name = 'GC_860',
                  value = '(cledq2x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_861 = Coupling(name = 'GC_861',
                  value = '(cledq2x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_862 = Coupling(name = 'GC_862',
                  value = '(cledq2x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_863 = Coupling(name = 'GC_863',
                  value = '(cledq2x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_864 = Coupling(name = 'GC_864',
                  value = '(cledq2x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_865 = Coupling(name = 'GC_865',
                  value = '(cledq2x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_866 = Coupling(name = 'GC_866',
                  value = '(cledq2x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_867 = Coupling(name = 'GC_867',
                  value = '(cledq2x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_868 = Coupling(name = 'GC_868',
                  value = '(cledq2x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_869 = Coupling(name = 'GC_869',
                  value = '(cledq2x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_870 = Coupling(name = 'GC_870',
                  value = '(cledq2x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_871 = Coupling(name = 'GC_871',
                  value = '(cledq2x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_872 = Coupling(name = 'GC_872',
                  value = '(cledq2x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_873 = Coupling(name = 'GC_873',
                  value = '(cledq3x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_874 = Coupling(name = 'GC_874',
                  value = '(cledq3x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_875 = Coupling(name = 'GC_875',
                  value = '(cledq3x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_876 = Coupling(name = 'GC_876',
                  value = '(cledq3x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_877 = Coupling(name = 'GC_877',
                  value = '(cledq3x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_878 = Coupling(name = 'GC_878',
                  value = '(cledq3x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_879 = Coupling(name = 'GC_879',
                  value = '(cledq3x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_880 = Coupling(name = 'GC_880',
                  value = '(cledq3x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_881 = Coupling(name = 'GC_881',
                  value = '(cledq3x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_882 = Coupling(name = 'GC_882',
                  value = '(cledq3x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_883 = Coupling(name = 'GC_883',
                  value = '(cledq3x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_884 = Coupling(name = 'GC_884',
                  value = '(cledq3x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_885 = Coupling(name = 'GC_885',
                  value = '(cledq3x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_886 = Coupling(name = 'GC_886',
                  value = '(cledq3x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_887 = Coupling(name = 'GC_887',
                  value = '(cledq3x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_888 = Coupling(name = 'GC_888',
                  value = '(cledq3x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_889 = Coupling(name = 'GC_889',
                  value = '(cledq3x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_890 = Coupling(name = 'GC_890',
                  value = '(cledq3x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_891 = Coupling(name = 'GC_891',
                  value = '(cledq3x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_892 = Coupling(name = 'GC_892',
                  value = '(cledq3x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_893 = Coupling(name = 'GC_893',
                  value = '(cledq3x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_894 = Coupling(name = 'GC_894',
                  value = '(cledq3x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_895 = Coupling(name = 'GC_895',
                  value = '(cledq3x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_896 = Coupling(name = 'GC_896',
                  value = '(cledq3x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_897 = Coupling(name = 'GC_897',
                  value = '(cledq3x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_898 = Coupling(name = 'GC_898',
                  value = '(cledq3x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_899 = Coupling(name = 'GC_899',
                  value = '(cledq3x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_900 = Coupling(name = 'GC_900',
                  value = '-((clequ11x1x1x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_901 = Coupling(name = 'GC_901',
                  value = '(clequ11x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_902 = Coupling(name = 'GC_902',
                  value = '-((clequ11x1x1x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_903 = Coupling(name = 'GC_903',
                  value = '(clequ11x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_904 = Coupling(name = 'GC_904',
                  value = '-((clequ11x1x1x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_905 = Coupling(name = 'GC_905',
                  value = '(clequ11x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_906 = Coupling(name = 'GC_906',
                  value = '-((clequ11x1x2x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_907 = Coupling(name = 'GC_907',
                  value = '(clequ11x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_908 = Coupling(name = 'GC_908',
                  value = '-((clequ11x1x2x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_909 = Coupling(name = 'GC_909',
                  value = '(clequ11x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_910 = Coupling(name = 'GC_910',
                  value = '-((clequ11x1x2x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_911 = Coupling(name = 'GC_911',
                  value = '(clequ11x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_912 = Coupling(name = 'GC_912',
                  value = '-((clequ11x1x3x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_913 = Coupling(name = 'GC_913',
                  value = '(clequ11x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_914 = Coupling(name = 'GC_914',
                  value = '-((clequ11x1x3x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_915 = Coupling(name = 'GC_915',
                  value = '(clequ11x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_916 = Coupling(name = 'GC_916',
                  value = '-((clequ11x1x3x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_917 = Coupling(name = 'GC_917',
                  value = '(clequ11x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_918 = Coupling(name = 'GC_918',
                  value = '-((clequ11x2x1x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_919 = Coupling(name = 'GC_919',
                  value = '(clequ11x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_920 = Coupling(name = 'GC_920',
                  value = '-((clequ11x2x1x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_921 = Coupling(name = 'GC_921',
                  value = '(clequ11x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_922 = Coupling(name = 'GC_922',
                  value = '-((clequ11x2x1x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_923 = Coupling(name = 'GC_923',
                  value = '(clequ11x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_924 = Coupling(name = 'GC_924',
                  value = '-((clequ11x2x2x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_925 = Coupling(name = 'GC_925',
                  value = '(clequ11x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_926 = Coupling(name = 'GC_926',
                  value = '-((clequ11x2x2x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_927 = Coupling(name = 'GC_927',
                  value = '(clequ11x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_928 = Coupling(name = 'GC_928',
                  value = '-((clequ11x2x2x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_929 = Coupling(name = 'GC_929',
                  value = '(clequ11x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_930 = Coupling(name = 'GC_930',
                  value = '-((clequ11x2x3x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_931 = Coupling(name = 'GC_931',
                  value = '(clequ11x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_932 = Coupling(name = 'GC_932',
                  value = '-((clequ11x2x3x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_933 = Coupling(name = 'GC_933',
                  value = '(clequ11x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_934 = Coupling(name = 'GC_934',
                  value = '-((clequ11x2x3x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_935 = Coupling(name = 'GC_935',
                  value = '(clequ11x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_936 = Coupling(name = 'GC_936',
                  value = '-((clequ11x3x1x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_937 = Coupling(name = 'GC_937',
                  value = '(clequ11x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_938 = Coupling(name = 'GC_938',
                  value = '-((clequ11x3x1x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_939 = Coupling(name = 'GC_939',
                  value = '(clequ11x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_940 = Coupling(name = 'GC_940',
                  value = '-((clequ11x3x1x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_941 = Coupling(name = 'GC_941',
                  value = '(clequ11x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_942 = Coupling(name = 'GC_942',
                  value = '-((clequ11x3x2x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_943 = Coupling(name = 'GC_943',
                  value = '(clequ11x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_944 = Coupling(name = 'GC_944',
                  value = '-((clequ11x3x2x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_945 = Coupling(name = 'GC_945',
                  value = '(clequ11x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_946 = Coupling(name = 'GC_946',
                  value = '-((clequ11x3x2x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_947 = Coupling(name = 'GC_947',
                  value = '(clequ11x3x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_948 = Coupling(name = 'GC_948',
                  value = '-((clequ11x3x3x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_949 = Coupling(name = 'GC_949',
                  value = '(clequ11x3x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_950 = Coupling(name = 'GC_950',
                  value = '-((clequ11x3x3x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_951 = Coupling(name = 'GC_951',
                  value = '(clequ11x3x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_952 = Coupling(name = 'GC_952',
                  value = '-((clequ11x3x3x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_953 = Coupling(name = 'GC_953',
                  value = '(clequ11x3x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_954 = Coupling(name = 'GC_954',
                  value = '-((clequ12x1x1x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_955 = Coupling(name = 'GC_955',
                  value = '(clequ12x1x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_956 = Coupling(name = 'GC_956',
                  value = '-((clequ12x1x1x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_957 = Coupling(name = 'GC_957',
                  value = '(clequ12x1x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_958 = Coupling(name = 'GC_958',
                  value = '-((clequ12x1x1x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_959 = Coupling(name = 'GC_959',
                  value = '(clequ12x1x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_960 = Coupling(name = 'GC_960',
                  value = '-((clequ12x1x2x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_961 = Coupling(name = 'GC_961',
                  value = '(clequ12x1x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_962 = Coupling(name = 'GC_962',
                  value = '-((clequ12x1x2x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_963 = Coupling(name = 'GC_963',
                  value = '(clequ12x1x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_964 = Coupling(name = 'GC_964',
                  value = '-((clequ12x1x2x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_965 = Coupling(name = 'GC_965',
                  value = '(clequ12x1x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_966 = Coupling(name = 'GC_966',
                  value = '-((clequ12x1x3x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_967 = Coupling(name = 'GC_967',
                  value = '(clequ12x1x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_968 = Coupling(name = 'GC_968',
                  value = '-((clequ12x1x3x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_969 = Coupling(name = 'GC_969',
                  value = '(clequ12x1x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_970 = Coupling(name = 'GC_970',
                  value = '-((clequ12x1x3x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_971 = Coupling(name = 'GC_971',
                  value = '(clequ12x1x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_972 = Coupling(name = 'GC_972',
                  value = '-((clequ12x2x1x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_973 = Coupling(name = 'GC_973',
                  value = '(clequ12x2x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_974 = Coupling(name = 'GC_974',
                  value = '-((clequ12x2x1x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_975 = Coupling(name = 'GC_975',
                  value = '(clequ12x2x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_976 = Coupling(name = 'GC_976',
                  value = '-((clequ12x2x1x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_977 = Coupling(name = 'GC_977',
                  value = '(clequ12x2x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_978 = Coupling(name = 'GC_978',
                  value = '-((clequ12x2x2x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_979 = Coupling(name = 'GC_979',
                  value = '(clequ12x2x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_980 = Coupling(name = 'GC_980',
                  value = '-((clequ12x2x2x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_981 = Coupling(name = 'GC_981',
                  value = '(clequ12x2x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_982 = Coupling(name = 'GC_982',
                  value = '-((clequ12x2x2x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_983 = Coupling(name = 'GC_983',
                  value = '(clequ12x2x2x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_984 = Coupling(name = 'GC_984',
                  value = '-((clequ12x2x3x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_985 = Coupling(name = 'GC_985',
                  value = '(clequ12x2x3x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_986 = Coupling(name = 'GC_986',
                  value = '-((clequ12x2x3x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_987 = Coupling(name = 'GC_987',
                  value = '(clequ12x2x3x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_988 = Coupling(name = 'GC_988',
                  value = '-((clequ12x2x3x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_989 = Coupling(name = 'GC_989',
                  value = '(clequ12x2x3x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_990 = Coupling(name = 'GC_990',
                  value = '-((clequ12x3x1x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_991 = Coupling(name = 'GC_991',
                  value = '(clequ12x3x1x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_992 = Coupling(name = 'GC_992',
                  value = '-((clequ12x3x1x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_993 = Coupling(name = 'GC_993',
                  value = '(clequ12x3x1x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_994 = Coupling(name = 'GC_994',
                  value = '-((clequ12x3x1x3*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_995 = Coupling(name = 'GC_995',
                  value = '(clequ12x3x1x3*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_996 = Coupling(name = 'GC_996',
                  value = '-((clequ12x3x2x1*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_997 = Coupling(name = 'GC_997',
                  value = '(clequ12x3x2x1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_998 = Coupling(name = 'GC_998',
                  value = '-((clequ12x3x2x2*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_999 = Coupling(name = 'GC_999',
                  value = '(clequ12x3x2x2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '-((clequ12x3x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '(clequ12x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '-((clequ12x3x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '(clequ12x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '-((clequ12x3x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '(clequ12x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '-((clequ12x3x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '(clequ12x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '-((clequ13x1x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '(clequ13x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '-((clequ13x1x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '(clequ13x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '-((clequ13x1x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '(clequ13x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '-((clequ13x1x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '(clequ13x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '-((clequ13x1x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '(clequ13x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '-((clequ13x1x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '(clequ13x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '-((clequ13x1x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '(clequ13x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '-((clequ13x1x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '(clequ13x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '-((clequ13x1x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '(clequ13x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '-((clequ13x2x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '(clequ13x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '-((clequ13x2x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '(clequ13x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '-((clequ13x2x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '(clequ13x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '-((clequ13x2x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '(clequ13x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '-((clequ13x2x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '(clequ13x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '-((clequ13x2x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '(clequ13x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '-((clequ13x2x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '(clequ13x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '-((clequ13x2x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '(clequ13x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '-((clequ13x2x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '(clequ13x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '-((clequ13x3x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '(clequ13x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '-((clequ13x3x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '(clequ13x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '-((clequ13x3x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '(clequ13x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '-((clequ13x3x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '(clequ13x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-((clequ13x3x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '(clequ13x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '-((clequ13x3x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '(clequ13x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '-((clequ13x3x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '(clequ13x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '-((clequ13x3x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '(clequ13x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '-((clequ13x3x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '(clequ13x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '-(clequ31x1x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '(clequ31x1x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '-(clequ31x1x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '(clequ31x1x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '-(clequ31x1x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '(clequ31x1x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '-(clequ31x1x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '(clequ31x1x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '-(clequ31x1x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '(clequ31x1x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '-(clequ31x1x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '(clequ31x1x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '-(clequ31x1x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '(clequ31x1x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '-(clequ31x1x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '(clequ31x1x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '-(clequ31x1x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '(clequ31x1x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '-(clequ31x1x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '(clequ31x1x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '-(clequ31x1x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '(clequ31x1x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '-(clequ31x1x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '(clequ31x1x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '-(clequ31x1x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '(clequ31x1x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '-(clequ31x1x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '(clequ31x1x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '-(clequ31x1x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '(clequ31x1x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '-(clequ31x1x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '(clequ31x1x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '-(clequ31x1x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '(clequ31x1x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '-(clequ31x1x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '(clequ31x1x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '-(clequ31x2x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '(clequ31x2x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '-(clequ31x2x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '(clequ31x2x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '-(clequ31x2x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '(clequ31x2x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '-(clequ31x2x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '(clequ31x2x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '-(clequ31x2x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '(clequ31x2x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '-(clequ31x2x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '(clequ31x2x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '-(clequ31x2x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '(clequ31x2x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '-(clequ31x2x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '(clequ31x2x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '-(clequ31x2x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '(clequ31x2x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '-(clequ31x2x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '(clequ31x2x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '-(clequ31x2x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '(clequ31x2x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '-(clequ31x2x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '(clequ31x2x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '-(clequ31x2x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '(clequ31x2x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '-(clequ31x2x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '(clequ31x2x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '-(clequ31x2x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1127 = Coupling(name = 'GC_1127',
                   value = '(clequ31x2x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '-(clequ31x2x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '(clequ31x2x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '-(clequ31x2x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '(clequ31x2x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '-(clequ31x2x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '(clequ31x2x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '-(clequ31x3x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '(clequ31x3x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '-(clequ31x3x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '(clequ31x3x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '-(clequ31x3x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '(clequ31x3x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '-(clequ31x3x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '(clequ31x3x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '-(clequ31x3x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '(clequ31x3x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '-(clequ31x3x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '(clequ31x3x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '-(clequ31x3x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '(clequ31x3x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '-(clequ31x3x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '(clequ31x3x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '-(clequ31x3x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '(clequ31x3x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '-(clequ31x3x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '(clequ31x3x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1154 = Coupling(name = 'GC_1154',
                   value = '-(clequ31x3x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '(clequ31x3x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '-(clequ31x3x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '(clequ31x3x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '-(clequ31x3x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '(clequ31x3x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '-(clequ31x3x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1161 = Coupling(name = 'GC_1161',
                   value = '(clequ31x3x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1162 = Coupling(name = 'GC_1162',
                   value = '-(clequ31x3x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1163 = Coupling(name = 'GC_1163',
                   value = '(clequ31x3x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1164 = Coupling(name = 'GC_1164',
                   value = '-(clequ31x3x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1165 = Coupling(name = 'GC_1165',
                   value = '(clequ31x3x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1166 = Coupling(name = 'GC_1166',
                   value = '-(clequ31x3x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1167 = Coupling(name = 'GC_1167',
                   value = '(clequ31x3x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1168 = Coupling(name = 'GC_1168',
                   value = '-(clequ31x3x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1169 = Coupling(name = 'GC_1169',
                   value = '(clequ31x3x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1170 = Coupling(name = 'GC_1170',
                   value = '-(clequ32x1x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1171 = Coupling(name = 'GC_1171',
                   value = '(clequ32x1x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1172 = Coupling(name = 'GC_1172',
                   value = '-(clequ32x1x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1173 = Coupling(name = 'GC_1173',
                   value = '(clequ32x1x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1174 = Coupling(name = 'GC_1174',
                   value = '-(clequ32x1x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1175 = Coupling(name = 'GC_1175',
                   value = '(clequ32x1x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1176 = Coupling(name = 'GC_1176',
                   value = '-(clequ32x1x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1177 = Coupling(name = 'GC_1177',
                   value = '(clequ32x1x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1178 = Coupling(name = 'GC_1178',
                   value = '-(clequ32x1x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1179 = Coupling(name = 'GC_1179',
                   value = '(clequ32x1x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1180 = Coupling(name = 'GC_1180',
                   value = '-(clequ32x1x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1181 = Coupling(name = 'GC_1181',
                   value = '(clequ32x1x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1182 = Coupling(name = 'GC_1182',
                   value = '-(clequ32x1x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1183 = Coupling(name = 'GC_1183',
                   value = '(clequ32x1x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1184 = Coupling(name = 'GC_1184',
                   value = '-(clequ32x1x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1185 = Coupling(name = 'GC_1185',
                   value = '(clequ32x1x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1186 = Coupling(name = 'GC_1186',
                   value = '-(clequ32x1x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1187 = Coupling(name = 'GC_1187',
                   value = '(clequ32x1x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1188 = Coupling(name = 'GC_1188',
                   value = '-(clequ32x1x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1189 = Coupling(name = 'GC_1189',
                   value = '(clequ32x1x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1190 = Coupling(name = 'GC_1190',
                   value = '-(clequ32x1x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1191 = Coupling(name = 'GC_1191',
                   value = '(clequ32x1x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1192 = Coupling(name = 'GC_1192',
                   value = '-(clequ32x1x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1193 = Coupling(name = 'GC_1193',
                   value = '(clequ32x1x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1194 = Coupling(name = 'GC_1194',
                   value = '-(clequ32x1x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1195 = Coupling(name = 'GC_1195',
                   value = '(clequ32x1x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1196 = Coupling(name = 'GC_1196',
                   value = '-(clequ32x1x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1197 = Coupling(name = 'GC_1197',
                   value = '(clequ32x1x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1198 = Coupling(name = 'GC_1198',
                   value = '-(clequ32x1x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1199 = Coupling(name = 'GC_1199',
                   value = '(clequ32x1x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1200 = Coupling(name = 'GC_1200',
                   value = '-(clequ32x1x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1201 = Coupling(name = 'GC_1201',
                   value = '(clequ32x1x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1202 = Coupling(name = 'GC_1202',
                   value = '-(clequ32x1x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1203 = Coupling(name = 'GC_1203',
                   value = '(clequ32x1x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1204 = Coupling(name = 'GC_1204',
                   value = '-(clequ32x1x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1205 = Coupling(name = 'GC_1205',
                   value = '(clequ32x1x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1206 = Coupling(name = 'GC_1206',
                   value = '-(clequ32x2x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1207 = Coupling(name = 'GC_1207',
                   value = '(clequ32x2x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1208 = Coupling(name = 'GC_1208',
                   value = '-(clequ32x2x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1209 = Coupling(name = 'GC_1209',
                   value = '(clequ32x2x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1210 = Coupling(name = 'GC_1210',
                   value = '-(clequ32x2x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1211 = Coupling(name = 'GC_1211',
                   value = '(clequ32x2x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1212 = Coupling(name = 'GC_1212',
                   value = '-(clequ32x2x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1213 = Coupling(name = 'GC_1213',
                   value = '(clequ32x2x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1214 = Coupling(name = 'GC_1214',
                   value = '-(clequ32x2x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1215 = Coupling(name = 'GC_1215',
                   value = '(clequ32x2x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1216 = Coupling(name = 'GC_1216',
                   value = '-(clequ32x2x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1217 = Coupling(name = 'GC_1217',
                   value = '(clequ32x2x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1218 = Coupling(name = 'GC_1218',
                   value = '-(clequ32x2x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1219 = Coupling(name = 'GC_1219',
                   value = '(clequ32x2x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1220 = Coupling(name = 'GC_1220',
                   value = '-(clequ32x2x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1221 = Coupling(name = 'GC_1221',
                   value = '(clequ32x2x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1222 = Coupling(name = 'GC_1222',
                   value = '-(clequ32x2x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1223 = Coupling(name = 'GC_1223',
                   value = '(clequ32x2x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1224 = Coupling(name = 'GC_1224',
                   value = '-(clequ32x2x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1225 = Coupling(name = 'GC_1225',
                   value = '(clequ32x2x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1226 = Coupling(name = 'GC_1226',
                   value = '-(clequ32x2x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1227 = Coupling(name = 'GC_1227',
                   value = '(clequ32x2x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1228 = Coupling(name = 'GC_1228',
                   value = '-(clequ32x2x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1229 = Coupling(name = 'GC_1229',
                   value = '(clequ32x2x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1230 = Coupling(name = 'GC_1230',
                   value = '-(clequ32x2x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1231 = Coupling(name = 'GC_1231',
                   value = '(clequ32x2x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1232 = Coupling(name = 'GC_1232',
                   value = '-(clequ32x2x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1233 = Coupling(name = 'GC_1233',
                   value = '(clequ32x2x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1234 = Coupling(name = 'GC_1234',
                   value = '-(clequ32x2x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1235 = Coupling(name = 'GC_1235',
                   value = '(clequ32x2x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1236 = Coupling(name = 'GC_1236',
                   value = '-(clequ32x2x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1237 = Coupling(name = 'GC_1237',
                   value = '(clequ32x2x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1238 = Coupling(name = 'GC_1238',
                   value = '-(clequ32x2x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1239 = Coupling(name = 'GC_1239',
                   value = '(clequ32x2x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1240 = Coupling(name = 'GC_1240',
                   value = '-(clequ32x2x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1241 = Coupling(name = 'GC_1241',
                   value = '(clequ32x2x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1242 = Coupling(name = 'GC_1242',
                   value = '-(clequ32x3x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1243 = Coupling(name = 'GC_1243',
                   value = '(clequ32x3x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1244 = Coupling(name = 'GC_1244',
                   value = '-(clequ32x3x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1245 = Coupling(name = 'GC_1245',
                   value = '(clequ32x3x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1246 = Coupling(name = 'GC_1246',
                   value = '-(clequ32x3x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1247 = Coupling(name = 'GC_1247',
                   value = '(clequ32x3x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1248 = Coupling(name = 'GC_1248',
                   value = '-(clequ32x3x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1249 = Coupling(name = 'GC_1249',
                   value = '(clequ32x3x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1250 = Coupling(name = 'GC_1250',
                   value = '-(clequ32x3x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1251 = Coupling(name = 'GC_1251',
                   value = '(clequ32x3x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1252 = Coupling(name = 'GC_1252',
                   value = '-(clequ32x3x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1253 = Coupling(name = 'GC_1253',
                   value = '(clequ32x3x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1254 = Coupling(name = 'GC_1254',
                   value = '-(clequ32x3x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1255 = Coupling(name = 'GC_1255',
                   value = '(clequ32x3x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1256 = Coupling(name = 'GC_1256',
                   value = '-(clequ32x3x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1257 = Coupling(name = 'GC_1257',
                   value = '(clequ32x3x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1258 = Coupling(name = 'GC_1258',
                   value = '-(clequ32x3x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1259 = Coupling(name = 'GC_1259',
                   value = '(clequ32x3x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1260 = Coupling(name = 'GC_1260',
                   value = '-(clequ32x3x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1261 = Coupling(name = 'GC_1261',
                   value = '(clequ32x3x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1262 = Coupling(name = 'GC_1262',
                   value = '-(clequ32x3x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1263 = Coupling(name = 'GC_1263',
                   value = '(clequ32x3x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1264 = Coupling(name = 'GC_1264',
                   value = '-(clequ32x3x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1265 = Coupling(name = 'GC_1265',
                   value = '(clequ32x3x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1266 = Coupling(name = 'GC_1266',
                   value = '-(clequ32x3x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1267 = Coupling(name = 'GC_1267',
                   value = '(clequ32x3x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1268 = Coupling(name = 'GC_1268',
                   value = '-(clequ32x3x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1269 = Coupling(name = 'GC_1269',
                   value = '(clequ32x3x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1270 = Coupling(name = 'GC_1270',
                   value = '-(clequ32x3x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1271 = Coupling(name = 'GC_1271',
                   value = '(clequ32x3x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1272 = Coupling(name = 'GC_1272',
                   value = '-(clequ32x3x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1273 = Coupling(name = 'GC_1273',
                   value = '(clequ32x3x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1274 = Coupling(name = 'GC_1274',
                   value = '-(clequ32x3x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1275 = Coupling(name = 'GC_1275',
                   value = '(clequ32x3x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1276 = Coupling(name = 'GC_1276',
                   value = '-(clequ32x3x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1277 = Coupling(name = 'GC_1277',
                   value = '(clequ32x3x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1278 = Coupling(name = 'GC_1278',
                   value = '-(clequ33x1x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1279 = Coupling(name = 'GC_1279',
                   value = '(clequ33x1x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1280 = Coupling(name = 'GC_1280',
                   value = '-(clequ33x1x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1281 = Coupling(name = 'GC_1281',
                   value = '(clequ33x1x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1282 = Coupling(name = 'GC_1282',
                   value = '-(clequ33x1x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1283 = Coupling(name = 'GC_1283',
                   value = '(clequ33x1x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1284 = Coupling(name = 'GC_1284',
                   value = '-(clequ33x1x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1285 = Coupling(name = 'GC_1285',
                   value = '(clequ33x1x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1286 = Coupling(name = 'GC_1286',
                   value = '-(clequ33x1x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1287 = Coupling(name = 'GC_1287',
                   value = '(clequ33x1x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1288 = Coupling(name = 'GC_1288',
                   value = '-(clequ33x1x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1289 = Coupling(name = 'GC_1289',
                   value = '(clequ33x1x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1290 = Coupling(name = 'GC_1290',
                   value = '-(clequ33x1x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1291 = Coupling(name = 'GC_1291',
                   value = '(clequ33x1x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1292 = Coupling(name = 'GC_1292',
                   value = '-(clequ33x1x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1293 = Coupling(name = 'GC_1293',
                   value = '(clequ33x1x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1294 = Coupling(name = 'GC_1294',
                   value = '-(clequ33x1x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1295 = Coupling(name = 'GC_1295',
                   value = '(clequ33x1x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1296 = Coupling(name = 'GC_1296',
                   value = '-(clequ33x1x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1297 = Coupling(name = 'GC_1297',
                   value = '(clequ33x1x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1298 = Coupling(name = 'GC_1298',
                   value = '-(clequ33x1x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1299 = Coupling(name = 'GC_1299',
                   value = '(clequ33x1x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1300 = Coupling(name = 'GC_1300',
                   value = '-(clequ33x1x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1301 = Coupling(name = 'GC_1301',
                   value = '(clequ33x1x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1302 = Coupling(name = 'GC_1302',
                   value = '-(clequ33x1x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1303 = Coupling(name = 'GC_1303',
                   value = '(clequ33x1x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1304 = Coupling(name = 'GC_1304',
                   value = '-(clequ33x1x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1305 = Coupling(name = 'GC_1305',
                   value = '(clequ33x1x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1306 = Coupling(name = 'GC_1306',
                   value = '-(clequ33x1x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1307 = Coupling(name = 'GC_1307',
                   value = '(clequ33x1x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1308 = Coupling(name = 'GC_1308',
                   value = '-(clequ33x1x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1309 = Coupling(name = 'GC_1309',
                   value = '(clequ33x1x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1310 = Coupling(name = 'GC_1310',
                   value = '-(clequ33x1x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1311 = Coupling(name = 'GC_1311',
                   value = '(clequ33x1x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1312 = Coupling(name = 'GC_1312',
                   value = '-(clequ33x1x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1313 = Coupling(name = 'GC_1313',
                   value = '(clequ33x1x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1314 = Coupling(name = 'GC_1314',
                   value = '-(clequ33x2x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1315 = Coupling(name = 'GC_1315',
                   value = '(clequ33x2x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1316 = Coupling(name = 'GC_1316',
                   value = '-(clequ33x2x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1317 = Coupling(name = 'GC_1317',
                   value = '(clequ33x2x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1318 = Coupling(name = 'GC_1318',
                   value = '-(clequ33x2x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1319 = Coupling(name = 'GC_1319',
                   value = '(clequ33x2x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1320 = Coupling(name = 'GC_1320',
                   value = '-(clequ33x2x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1321 = Coupling(name = 'GC_1321',
                   value = '(clequ33x2x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1322 = Coupling(name = 'GC_1322',
                   value = '-(clequ33x2x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1323 = Coupling(name = 'GC_1323',
                   value = '(clequ33x2x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1324 = Coupling(name = 'GC_1324',
                   value = '-(clequ33x2x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1325 = Coupling(name = 'GC_1325',
                   value = '(clequ33x2x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1326 = Coupling(name = 'GC_1326',
                   value = '-(clequ33x2x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1327 = Coupling(name = 'GC_1327',
                   value = '(clequ33x2x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1328 = Coupling(name = 'GC_1328',
                   value = '-(clequ33x2x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1329 = Coupling(name = 'GC_1329',
                   value = '(clequ33x2x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1330 = Coupling(name = 'GC_1330',
                   value = '-(clequ33x2x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1331 = Coupling(name = 'GC_1331',
                   value = '(clequ33x2x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1332 = Coupling(name = 'GC_1332',
                   value = '-(clequ33x2x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1333 = Coupling(name = 'GC_1333',
                   value = '(clequ33x2x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1334 = Coupling(name = 'GC_1334',
                   value = '-(clequ33x2x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1335 = Coupling(name = 'GC_1335',
                   value = '(clequ33x2x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1336 = Coupling(name = 'GC_1336',
                   value = '-(clequ33x2x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1337 = Coupling(name = 'GC_1337',
                   value = '(clequ33x2x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1338 = Coupling(name = 'GC_1338',
                   value = '-(clequ33x2x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1339 = Coupling(name = 'GC_1339',
                   value = '(clequ33x2x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1340 = Coupling(name = 'GC_1340',
                   value = '-(clequ33x2x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1341 = Coupling(name = 'GC_1341',
                   value = '(clequ33x2x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1342 = Coupling(name = 'GC_1342',
                   value = '-(clequ33x2x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1343 = Coupling(name = 'GC_1343',
                   value = '(clequ33x2x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1344 = Coupling(name = 'GC_1344',
                   value = '-(clequ33x2x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1345 = Coupling(name = 'GC_1345',
                   value = '(clequ33x2x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1346 = Coupling(name = 'GC_1346',
                   value = '-(clequ33x2x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1347 = Coupling(name = 'GC_1347',
                   value = '(clequ33x2x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1348 = Coupling(name = 'GC_1348',
                   value = '-(clequ33x2x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1349 = Coupling(name = 'GC_1349',
                   value = '(clequ33x2x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1350 = Coupling(name = 'GC_1350',
                   value = '-(clequ33x3x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1351 = Coupling(name = 'GC_1351',
                   value = '(clequ33x3x1x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1352 = Coupling(name = 'GC_1352',
                   value = '-(clequ33x3x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1353 = Coupling(name = 'GC_1353',
                   value = '(clequ33x3x1x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1354 = Coupling(name = 'GC_1354',
                   value = '-(clequ33x3x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1355 = Coupling(name = 'GC_1355',
                   value = '(clequ33x3x1x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1356 = Coupling(name = 'GC_1356',
                   value = '-(clequ33x3x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1357 = Coupling(name = 'GC_1357',
                   value = '(clequ33x3x1x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1358 = Coupling(name = 'GC_1358',
                   value = '-(clequ33x3x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1359 = Coupling(name = 'GC_1359',
                   value = '(clequ33x3x1x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1360 = Coupling(name = 'GC_1360',
                   value = '-(clequ33x3x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1361 = Coupling(name = 'GC_1361',
                   value = '(clequ33x3x1x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1362 = Coupling(name = 'GC_1362',
                   value = '-(clequ33x3x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1363 = Coupling(name = 'GC_1363',
                   value = '(clequ33x3x2x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1364 = Coupling(name = 'GC_1364',
                   value = '-(clequ33x3x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1365 = Coupling(name = 'GC_1365',
                   value = '(clequ33x3x2x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1366 = Coupling(name = 'GC_1366',
                   value = '-(clequ33x3x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1367 = Coupling(name = 'GC_1367',
                   value = '(clequ33x3x2x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1368 = Coupling(name = 'GC_1368',
                   value = '-(clequ33x3x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1369 = Coupling(name = 'GC_1369',
                   value = '(clequ33x3x2x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1370 = Coupling(name = 'GC_1370',
                   value = '-(clequ33x3x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1371 = Coupling(name = 'GC_1371',
                   value = '(clequ33x3x2x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1372 = Coupling(name = 'GC_1372',
                   value = '-(clequ33x3x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1373 = Coupling(name = 'GC_1373',
                   value = '(clequ33x3x2x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1374 = Coupling(name = 'GC_1374',
                   value = '-(clequ33x3x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1375 = Coupling(name = 'GC_1375',
                   value = '(clequ33x3x3x1*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1376 = Coupling(name = 'GC_1376',
                   value = '-(clequ33x3x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1377 = Coupling(name = 'GC_1377',
                   value = '(clequ33x3x3x1*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1378 = Coupling(name = 'GC_1378',
                   value = '-(clequ33x3x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1379 = Coupling(name = 'GC_1379',
                   value = '(clequ33x3x3x2*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1380 = Coupling(name = 'GC_1380',
                   value = '-(clequ33x3x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1381 = Coupling(name = 'GC_1381',
                   value = '(clequ33x3x3x2*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1382 = Coupling(name = 'GC_1382',
                   value = '-(clequ33x3x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1383 = Coupling(name = 'GC_1383',
                   value = '(clequ33x3x3x3*complex(0,1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1384 = Coupling(name = 'GC_1384',
                   value = '-(clequ33x3x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1385 = Coupling(name = 'GC_1385',
                   value = '(clequ33x3x3x3*complex(0,1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1386 = Coupling(name = 'GC_1386',
                   value = '(2*cll1x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1387 = Coupling(name = 'GC_1387',
                   value = '(2*cll1x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1388 = Coupling(name = 'GC_1388',
                   value = '(2*cll1x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1389 = Coupling(name = 'GC_1389',
                   value = '(2*cll2x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1390 = Coupling(name = 'GC_1390',
                   value = '(2*cll2x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1391 = Coupling(name = 'GC_1391',
                   value = '(2*cll2x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1392 = Coupling(name = 'GC_1392',
                   value = '(2*cll3x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1393 = Coupling(name = 'GC_1393',
                   value = '(2*cll3x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1394 = Coupling(name = 'GC_1394',
                   value = '(2*cll3x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1395 = Coupling(name = 'GC_1395',
                   value = '(2*clq31x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1396 = Coupling(name = 'GC_1396',
                   value = '(2*clq31x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1397 = Coupling(name = 'GC_1397',
                   value = '(2*clq31x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1398 = Coupling(name = 'GC_1398',
                   value = '(2*clq31x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1399 = Coupling(name = 'GC_1399',
                   value = '(2*clq31x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1400 = Coupling(name = 'GC_1400',
                   value = '(2*clq31x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1401 = Coupling(name = 'GC_1401',
                   value = '(2*clq31x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1402 = Coupling(name = 'GC_1402',
                   value = '(2*clq31x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1403 = Coupling(name = 'GC_1403',
                   value = '(2*clq31x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1404 = Coupling(name = 'GC_1404',
                   value = '(2*clq31x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1405 = Coupling(name = 'GC_1405',
                   value = '(2*clq31x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1406 = Coupling(name = 'GC_1406',
                   value = '(2*clq31x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1407 = Coupling(name = 'GC_1407',
                   value = '(2*clq31x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1408 = Coupling(name = 'GC_1408',
                   value = '(2*clq31x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1409 = Coupling(name = 'GC_1409',
                   value = '(2*clq31x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1410 = Coupling(name = 'GC_1410',
                   value = '(2*clq31x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1411 = Coupling(name = 'GC_1411',
                   value = '(2*clq31x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1412 = Coupling(name = 'GC_1412',
                   value = '(2*clq31x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1413 = Coupling(name = 'GC_1413',
                   value = '(2*clq31x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1414 = Coupling(name = 'GC_1414',
                   value = '(2*clq31x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1415 = Coupling(name = 'GC_1415',
                   value = '(2*clq31x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1416 = Coupling(name = 'GC_1416',
                   value = '(2*clq31x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1417 = Coupling(name = 'GC_1417',
                   value = '(2*clq31x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1418 = Coupling(name = 'GC_1418',
                   value = '(2*clq31x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1419 = Coupling(name = 'GC_1419',
                   value = '(2*clq31x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1420 = Coupling(name = 'GC_1420',
                   value = '(2*clq31x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1421 = Coupling(name = 'GC_1421',
                   value = '(2*clq31x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1422 = Coupling(name = 'GC_1422',
                   value = '(2*clq32x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1423 = Coupling(name = 'GC_1423',
                   value = '(2*clq32x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1424 = Coupling(name = 'GC_1424',
                   value = '(2*clq32x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1425 = Coupling(name = 'GC_1425',
                   value = '(2*clq32x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1426 = Coupling(name = 'GC_1426',
                   value = '(2*clq32x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1427 = Coupling(name = 'GC_1427',
                   value = '(2*clq32x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1428 = Coupling(name = 'GC_1428',
                   value = '(2*clq32x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1429 = Coupling(name = 'GC_1429',
                   value = '(2*clq32x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1430 = Coupling(name = 'GC_1430',
                   value = '(2*clq32x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1431 = Coupling(name = 'GC_1431',
                   value = '(2*clq32x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1432 = Coupling(name = 'GC_1432',
                   value = '(2*clq32x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1433 = Coupling(name = 'GC_1433',
                   value = '(2*clq32x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1434 = Coupling(name = 'GC_1434',
                   value = '(2*clq32x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1435 = Coupling(name = 'GC_1435',
                   value = '(2*clq32x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1436 = Coupling(name = 'GC_1436',
                   value = '(2*clq32x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1437 = Coupling(name = 'GC_1437',
                   value = '(2*clq32x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1438 = Coupling(name = 'GC_1438',
                   value = '(2*clq32x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1439 = Coupling(name = 'GC_1439',
                   value = '(2*clq32x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1440 = Coupling(name = 'GC_1440',
                   value = '(2*clq32x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1441 = Coupling(name = 'GC_1441',
                   value = '(2*clq32x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1442 = Coupling(name = 'GC_1442',
                   value = '(2*clq32x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1443 = Coupling(name = 'GC_1443',
                   value = '(2*clq32x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1444 = Coupling(name = 'GC_1444',
                   value = '(2*clq32x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1445 = Coupling(name = 'GC_1445',
                   value = '(2*clq32x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1446 = Coupling(name = 'GC_1446',
                   value = '(2*clq32x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1447 = Coupling(name = 'GC_1447',
                   value = '(2*clq32x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1448 = Coupling(name = 'GC_1448',
                   value = '(2*clq32x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1449 = Coupling(name = 'GC_1449',
                   value = '(2*clq33x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1450 = Coupling(name = 'GC_1450',
                   value = '(2*clq33x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1451 = Coupling(name = 'GC_1451',
                   value = '(2*clq33x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1452 = Coupling(name = 'GC_1452',
                   value = '(2*clq33x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1453 = Coupling(name = 'GC_1453',
                   value = '(2*clq33x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1454 = Coupling(name = 'GC_1454',
                   value = '(2*clq33x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1455 = Coupling(name = 'GC_1455',
                   value = '(2*clq33x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1456 = Coupling(name = 'GC_1456',
                   value = '(2*clq33x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1457 = Coupling(name = 'GC_1457',
                   value = '(2*clq33x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1458 = Coupling(name = 'GC_1458',
                   value = '(2*clq33x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1459 = Coupling(name = 'GC_1459',
                   value = '(2*clq33x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1460 = Coupling(name = 'GC_1460',
                   value = '(2*clq33x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1461 = Coupling(name = 'GC_1461',
                   value = '(2*clq33x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1462 = Coupling(name = 'GC_1462',
                   value = '(2*clq33x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1463 = Coupling(name = 'GC_1463',
                   value = '(2*clq33x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1464 = Coupling(name = 'GC_1464',
                   value = '(2*clq33x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1465 = Coupling(name = 'GC_1465',
                   value = '(2*clq33x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1466 = Coupling(name = 'GC_1466',
                   value = '(2*clq33x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1467 = Coupling(name = 'GC_1467',
                   value = '(2*clq33x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1468 = Coupling(name = 'GC_1468',
                   value = '(2*clq33x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1469 = Coupling(name = 'GC_1469',
                   value = '(2*clq33x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1470 = Coupling(name = 'GC_1470',
                   value = '(2*clq33x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1471 = Coupling(name = 'GC_1471',
                   value = '(2*clq33x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1472 = Coupling(name = 'GC_1472',
                   value = '(2*clq33x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1473 = Coupling(name = 'GC_1473',
                   value = '(2*clq33x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1474 = Coupling(name = 'GC_1474',
                   value = '(2*clq33x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1475 = Coupling(name = 'GC_1475',
                   value = '(2*clq33x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1476 = Coupling(name = 'GC_1476',
                   value = '(clu1x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1477 = Coupling(name = 'GC_1477',
                   value = '(clu1x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1478 = Coupling(name = 'GC_1478',
                   value = '(clu1x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1479 = Coupling(name = 'GC_1479',
                   value = '(clu1x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1480 = Coupling(name = 'GC_1480',
                   value = '(clu1x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1481 = Coupling(name = 'GC_1481',
                   value = '(clu1x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1482 = Coupling(name = 'GC_1482',
                   value = '(clu1x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1483 = Coupling(name = 'GC_1483',
                   value = '(clu1x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1484 = Coupling(name = 'GC_1484',
                   value = '(clu1x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1485 = Coupling(name = 'GC_1485',
                   value = '(clu1x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1486 = Coupling(name = 'GC_1486',
                   value = '(clu1x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1487 = Coupling(name = 'GC_1487',
                   value = '(clu1x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1488 = Coupling(name = 'GC_1488',
                   value = '(clu1x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1489 = Coupling(name = 'GC_1489',
                   value = '(clu1x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1490 = Coupling(name = 'GC_1490',
                   value = '(clu1x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1491 = Coupling(name = 'GC_1491',
                   value = '(clu1x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1492 = Coupling(name = 'GC_1492',
                   value = '(clu1x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1493 = Coupling(name = 'GC_1493',
                   value = '(clu1x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1494 = Coupling(name = 'GC_1494',
                   value = '(clu1x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1495 = Coupling(name = 'GC_1495',
                   value = '(clu1x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1496 = Coupling(name = 'GC_1496',
                   value = '(clu1x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1497 = Coupling(name = 'GC_1497',
                   value = '(clu1x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1498 = Coupling(name = 'GC_1498',
                   value = '(clu1x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1499 = Coupling(name = 'GC_1499',
                   value = '(clu1x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1500 = Coupling(name = 'GC_1500',
                   value = '(clu1x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1501 = Coupling(name = 'GC_1501',
                   value = '(clu1x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1502 = Coupling(name = 'GC_1502',
                   value = '(clu1x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1503 = Coupling(name = 'GC_1503',
                   value = '(clu2x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1504 = Coupling(name = 'GC_1504',
                   value = '(clu2x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1505 = Coupling(name = 'GC_1505',
                   value = '(clu2x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1506 = Coupling(name = 'GC_1506',
                   value = '(clu2x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1507 = Coupling(name = 'GC_1507',
                   value = '(clu2x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1508 = Coupling(name = 'GC_1508',
                   value = '(clu2x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1509 = Coupling(name = 'GC_1509',
                   value = '(clu2x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1510 = Coupling(name = 'GC_1510',
                   value = '(clu2x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1511 = Coupling(name = 'GC_1511',
                   value = '(clu2x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1512 = Coupling(name = 'GC_1512',
                   value = '(clu2x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1513 = Coupling(name = 'GC_1513',
                   value = '(clu2x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1514 = Coupling(name = 'GC_1514',
                   value = '(clu2x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1515 = Coupling(name = 'GC_1515',
                   value = '(clu2x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1516 = Coupling(name = 'GC_1516',
                   value = '(clu2x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1517 = Coupling(name = 'GC_1517',
                   value = '(clu2x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1518 = Coupling(name = 'GC_1518',
                   value = '(clu2x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1519 = Coupling(name = 'GC_1519',
                   value = '(clu2x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1520 = Coupling(name = 'GC_1520',
                   value = '(clu2x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1521 = Coupling(name = 'GC_1521',
                   value = '(clu2x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1522 = Coupling(name = 'GC_1522',
                   value = '(clu2x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1523 = Coupling(name = 'GC_1523',
                   value = '(clu2x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1524 = Coupling(name = 'GC_1524',
                   value = '(clu2x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1525 = Coupling(name = 'GC_1525',
                   value = '(clu2x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1526 = Coupling(name = 'GC_1526',
                   value = '(clu2x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1527 = Coupling(name = 'GC_1527',
                   value = '(clu2x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1528 = Coupling(name = 'GC_1528',
                   value = '(clu2x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1529 = Coupling(name = 'GC_1529',
                   value = '(clu2x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1530 = Coupling(name = 'GC_1530',
                   value = '(clu3x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1531 = Coupling(name = 'GC_1531',
                   value = '(clu3x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1532 = Coupling(name = 'GC_1532',
                   value = '(clu3x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1533 = Coupling(name = 'GC_1533',
                   value = '(clu3x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1534 = Coupling(name = 'GC_1534',
                   value = '(clu3x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1535 = Coupling(name = 'GC_1535',
                   value = '(clu3x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1536 = Coupling(name = 'GC_1536',
                   value = '(clu3x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1537 = Coupling(name = 'GC_1537',
                   value = '(clu3x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1538 = Coupling(name = 'GC_1538',
                   value = '(clu3x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1539 = Coupling(name = 'GC_1539',
                   value = '(clu3x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1540 = Coupling(name = 'GC_1540',
                   value = '(clu3x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1541 = Coupling(name = 'GC_1541',
                   value = '(clu3x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1542 = Coupling(name = 'GC_1542',
                   value = '(clu3x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1543 = Coupling(name = 'GC_1543',
                   value = '(clu3x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1544 = Coupling(name = 'GC_1544',
                   value = '(clu3x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1545 = Coupling(name = 'GC_1545',
                   value = '(clu3x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1546 = Coupling(name = 'GC_1546',
                   value = '(clu3x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1547 = Coupling(name = 'GC_1547',
                   value = '(clu3x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1548 = Coupling(name = 'GC_1548',
                   value = '(clu3x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1549 = Coupling(name = 'GC_1549',
                   value = '(clu3x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1550 = Coupling(name = 'GC_1550',
                   value = '(clu3x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1551 = Coupling(name = 'GC_1551',
                   value = '(clu3x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1552 = Coupling(name = 'GC_1552',
                   value = '(clu3x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1553 = Coupling(name = 'GC_1553',
                   value = '(clu3x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1554 = Coupling(name = 'GC_1554',
                   value = '(clu3x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1555 = Coupling(name = 'GC_1555',
                   value = '(clu3x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1556 = Coupling(name = 'GC_1556',
                   value = '(clu3x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1557 = Coupling(name = 'GC_1557',
                   value = '(cqd11x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1558 = Coupling(name = 'GC_1558',
                   value = '(cqd11x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1559 = Coupling(name = 'GC_1559',
                   value = '(cqd11x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1560 = Coupling(name = 'GC_1560',
                   value = '(cqd11x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1561 = Coupling(name = 'GC_1561',
                   value = '(cqd11x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1562 = Coupling(name = 'GC_1562',
                   value = '(cqd11x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1563 = Coupling(name = 'GC_1563',
                   value = '(cqd11x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1564 = Coupling(name = 'GC_1564',
                   value = '(cqd11x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1565 = Coupling(name = 'GC_1565',
                   value = '(cqd11x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1566 = Coupling(name = 'GC_1566',
                   value = '(cqd11x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1567 = Coupling(name = 'GC_1567',
                   value = '(cqd11x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1568 = Coupling(name = 'GC_1568',
                   value = '(cqd11x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1569 = Coupling(name = 'GC_1569',
                   value = '(cqd11x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1570 = Coupling(name = 'GC_1570',
                   value = '(cqd11x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1571 = Coupling(name = 'GC_1571',
                   value = '(cqd11x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1572 = Coupling(name = 'GC_1572',
                   value = '(cqd11x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1573 = Coupling(name = 'GC_1573',
                   value = '(cqd11x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1574 = Coupling(name = 'GC_1574',
                   value = '(cqd11x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1575 = Coupling(name = 'GC_1575',
                   value = '(cqd11x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1576 = Coupling(name = 'GC_1576',
                   value = '(cqd11x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1577 = Coupling(name = 'GC_1577',
                   value = '(cqd11x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1578 = Coupling(name = 'GC_1578',
                   value = '(cqd11x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1579 = Coupling(name = 'GC_1579',
                   value = '(cqd11x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1580 = Coupling(name = 'GC_1580',
                   value = '(cqd11x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1581 = Coupling(name = 'GC_1581',
                   value = '(cqd11x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1582 = Coupling(name = 'GC_1582',
                   value = '(cqd11x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1583 = Coupling(name = 'GC_1583',
                   value = '(cqd11x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1584 = Coupling(name = 'GC_1584',
                   value = '(cqd12x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1585 = Coupling(name = 'GC_1585',
                   value = '(cqd12x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1586 = Coupling(name = 'GC_1586',
                   value = '(cqd12x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1587 = Coupling(name = 'GC_1587',
                   value = '(cqd12x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1588 = Coupling(name = 'GC_1588',
                   value = '(cqd12x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1589 = Coupling(name = 'GC_1589',
                   value = '(cqd12x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1590 = Coupling(name = 'GC_1590',
                   value = '(cqd12x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1591 = Coupling(name = 'GC_1591',
                   value = '(cqd12x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1592 = Coupling(name = 'GC_1592',
                   value = '(cqd12x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1593 = Coupling(name = 'GC_1593',
                   value = '(cqd12x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1594 = Coupling(name = 'GC_1594',
                   value = '(cqd12x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1595 = Coupling(name = 'GC_1595',
                   value = '(cqd12x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1596 = Coupling(name = 'GC_1596',
                   value = '(cqd12x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1597 = Coupling(name = 'GC_1597',
                   value = '(cqd12x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1598 = Coupling(name = 'GC_1598',
                   value = '(cqd12x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1599 = Coupling(name = 'GC_1599',
                   value = '(cqd12x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1600 = Coupling(name = 'GC_1600',
                   value = '(cqd12x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1601 = Coupling(name = 'GC_1601',
                   value = '(cqd12x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1602 = Coupling(name = 'GC_1602',
                   value = '(cqd12x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1603 = Coupling(name = 'GC_1603',
                   value = '(cqd12x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1604 = Coupling(name = 'GC_1604',
                   value = '(cqd12x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1605 = Coupling(name = 'GC_1605',
                   value = '(cqd12x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1606 = Coupling(name = 'GC_1606',
                   value = '(cqd12x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1607 = Coupling(name = 'GC_1607',
                   value = '(cqd12x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1608 = Coupling(name = 'GC_1608',
                   value = '(cqd12x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1609 = Coupling(name = 'GC_1609',
                   value = '(cqd12x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1610 = Coupling(name = 'GC_1610',
                   value = '(cqd12x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1611 = Coupling(name = 'GC_1611',
                   value = '(cqd13x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1612 = Coupling(name = 'GC_1612',
                   value = '(cqd13x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1613 = Coupling(name = 'GC_1613',
                   value = '(cqd13x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1614 = Coupling(name = 'GC_1614',
                   value = '(cqd13x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1615 = Coupling(name = 'GC_1615',
                   value = '(cqd13x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1616 = Coupling(name = 'GC_1616',
                   value = '(cqd13x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1617 = Coupling(name = 'GC_1617',
                   value = '(cqd13x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1618 = Coupling(name = 'GC_1618',
                   value = '(cqd13x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1619 = Coupling(name = 'GC_1619',
                   value = '(cqd13x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1620 = Coupling(name = 'GC_1620',
                   value = '(cqd13x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1621 = Coupling(name = 'GC_1621',
                   value = '(cqd13x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1622 = Coupling(name = 'GC_1622',
                   value = '(cqd13x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1623 = Coupling(name = 'GC_1623',
                   value = '(cqd13x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1624 = Coupling(name = 'GC_1624',
                   value = '(cqd13x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1625 = Coupling(name = 'GC_1625',
                   value = '(cqd13x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1626 = Coupling(name = 'GC_1626',
                   value = '(cqd13x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1627 = Coupling(name = 'GC_1627',
                   value = '(cqd13x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1628 = Coupling(name = 'GC_1628',
                   value = '(cqd13x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1629 = Coupling(name = 'GC_1629',
                   value = '(cqd13x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1630 = Coupling(name = 'GC_1630',
                   value = '(cqd13x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1631 = Coupling(name = 'GC_1631',
                   value = '(cqd13x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1632 = Coupling(name = 'GC_1632',
                   value = '(cqd13x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1633 = Coupling(name = 'GC_1633',
                   value = '(cqd13x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1634 = Coupling(name = 'GC_1634',
                   value = '(cqd13x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1635 = Coupling(name = 'GC_1635',
                   value = '(cqd13x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1636 = Coupling(name = 'GC_1636',
                   value = '(cqd13x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1637 = Coupling(name = 'GC_1637',
                   value = '(cqd13x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1638 = Coupling(name = 'GC_1638',
                   value = '(cqd81x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1639 = Coupling(name = 'GC_1639',
                   value = '(cqd81x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1640 = Coupling(name = 'GC_1640',
                   value = '(cqd81x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1641 = Coupling(name = 'GC_1641',
                   value = '(cqd81x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1642 = Coupling(name = 'GC_1642',
                   value = '(cqd81x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1643 = Coupling(name = 'GC_1643',
                   value = '(cqd81x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1644 = Coupling(name = 'GC_1644',
                   value = '(cqd81x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1645 = Coupling(name = 'GC_1645',
                   value = '(cqd81x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1646 = Coupling(name = 'GC_1646',
                   value = '(cqd81x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1647 = Coupling(name = 'GC_1647',
                   value = '(cqd81x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1648 = Coupling(name = 'GC_1648',
                   value = '(cqd81x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1649 = Coupling(name = 'GC_1649',
                   value = '(cqd81x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1650 = Coupling(name = 'GC_1650',
                   value = '(cqd81x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1651 = Coupling(name = 'GC_1651',
                   value = '(cqd81x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1652 = Coupling(name = 'GC_1652',
                   value = '(cqd81x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1653 = Coupling(name = 'GC_1653',
                   value = '(cqd81x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1654 = Coupling(name = 'GC_1654',
                   value = '(cqd81x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1655 = Coupling(name = 'GC_1655',
                   value = '(cqd81x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1656 = Coupling(name = 'GC_1656',
                   value = '(cqd81x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1657 = Coupling(name = 'GC_1657',
                   value = '(cqd81x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1658 = Coupling(name = 'GC_1658',
                   value = '(cqd81x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1659 = Coupling(name = 'GC_1659',
                   value = '(cqd81x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1660 = Coupling(name = 'GC_1660',
                   value = '(cqd81x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1661 = Coupling(name = 'GC_1661',
                   value = '(cqd81x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1662 = Coupling(name = 'GC_1662',
                   value = '(cqd81x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1663 = Coupling(name = 'GC_1663',
                   value = '(cqd81x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1664 = Coupling(name = 'GC_1664',
                   value = '(cqd81x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1665 = Coupling(name = 'GC_1665',
                   value = '(cqd82x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1666 = Coupling(name = 'GC_1666',
                   value = '(cqd82x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1667 = Coupling(name = 'GC_1667',
                   value = '(cqd82x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1668 = Coupling(name = 'GC_1668',
                   value = '(cqd82x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1669 = Coupling(name = 'GC_1669',
                   value = '(cqd82x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1670 = Coupling(name = 'GC_1670',
                   value = '(cqd82x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1671 = Coupling(name = 'GC_1671',
                   value = '(cqd82x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1672 = Coupling(name = 'GC_1672',
                   value = '(cqd82x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1673 = Coupling(name = 'GC_1673',
                   value = '(cqd82x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1674 = Coupling(name = 'GC_1674',
                   value = '(cqd82x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1675 = Coupling(name = 'GC_1675',
                   value = '(cqd82x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1676 = Coupling(name = 'GC_1676',
                   value = '(cqd82x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1677 = Coupling(name = 'GC_1677',
                   value = '(cqd82x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1678 = Coupling(name = 'GC_1678',
                   value = '(cqd82x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1679 = Coupling(name = 'GC_1679',
                   value = '(cqd82x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1680 = Coupling(name = 'GC_1680',
                   value = '(cqd82x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1681 = Coupling(name = 'GC_1681',
                   value = '(cqd82x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1682 = Coupling(name = 'GC_1682',
                   value = '(cqd82x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1683 = Coupling(name = 'GC_1683',
                   value = '(cqd82x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1684 = Coupling(name = 'GC_1684',
                   value = '(cqd82x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1685 = Coupling(name = 'GC_1685',
                   value = '(cqd82x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1686 = Coupling(name = 'GC_1686',
                   value = '(cqd82x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1687 = Coupling(name = 'GC_1687',
                   value = '(cqd82x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1688 = Coupling(name = 'GC_1688',
                   value = '(cqd82x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1689 = Coupling(name = 'GC_1689',
                   value = '(cqd82x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1690 = Coupling(name = 'GC_1690',
                   value = '(cqd82x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1691 = Coupling(name = 'GC_1691',
                   value = '(cqd82x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1692 = Coupling(name = 'GC_1692',
                   value = '(cqd83x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1693 = Coupling(name = 'GC_1693',
                   value = '(cqd83x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1694 = Coupling(name = 'GC_1694',
                   value = '(cqd83x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1695 = Coupling(name = 'GC_1695',
                   value = '(cqd83x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1696 = Coupling(name = 'GC_1696',
                   value = '(cqd83x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1697 = Coupling(name = 'GC_1697',
                   value = '(cqd83x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1698 = Coupling(name = 'GC_1698',
                   value = '(cqd83x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1699 = Coupling(name = 'GC_1699',
                   value = '(cqd83x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1700 = Coupling(name = 'GC_1700',
                   value = '(cqd83x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1701 = Coupling(name = 'GC_1701',
                   value = '(cqd83x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1702 = Coupling(name = 'GC_1702',
                   value = '(cqd83x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1703 = Coupling(name = 'GC_1703',
                   value = '(cqd83x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1704 = Coupling(name = 'GC_1704',
                   value = '(cqd83x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1705 = Coupling(name = 'GC_1705',
                   value = '(cqd83x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1706 = Coupling(name = 'GC_1706',
                   value = '(cqd83x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1707 = Coupling(name = 'GC_1707',
                   value = '(cqd83x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1708 = Coupling(name = 'GC_1708',
                   value = '(cqd83x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1709 = Coupling(name = 'GC_1709',
                   value = '(cqd83x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1710 = Coupling(name = 'GC_1710',
                   value = '(cqd83x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1711 = Coupling(name = 'GC_1711',
                   value = '(cqd83x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1712 = Coupling(name = 'GC_1712',
                   value = '(cqd83x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1713 = Coupling(name = 'GC_1713',
                   value = '(cqd83x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1714 = Coupling(name = 'GC_1714',
                   value = '(cqd83x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1715 = Coupling(name = 'GC_1715',
                   value = '(cqd83x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1716 = Coupling(name = 'GC_1716',
                   value = '(cqd83x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1717 = Coupling(name = 'GC_1717',
                   value = '(cqd83x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1718 = Coupling(name = 'GC_1718',
                   value = '(cqd83x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1719 = Coupling(name = 'GC_1719',
                   value = '(cqe1x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1720 = Coupling(name = 'GC_1720',
                   value = '(cqe1x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1721 = Coupling(name = 'GC_1721',
                   value = '(cqe1x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1722 = Coupling(name = 'GC_1722',
                   value = '(cqe1x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1723 = Coupling(name = 'GC_1723',
                   value = '(cqe1x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1724 = Coupling(name = 'GC_1724',
                   value = '(cqe1x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1725 = Coupling(name = 'GC_1725',
                   value = '(cqe1x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1726 = Coupling(name = 'GC_1726',
                   value = '(cqe1x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1727 = Coupling(name = 'GC_1727',
                   value = '(cqe1x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1728 = Coupling(name = 'GC_1728',
                   value = '(cqe1x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1729 = Coupling(name = 'GC_1729',
                   value = '(cqe1x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1730 = Coupling(name = 'GC_1730',
                   value = '(cqe1x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1731 = Coupling(name = 'GC_1731',
                   value = '(cqe1x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1732 = Coupling(name = 'GC_1732',
                   value = '(cqe1x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1733 = Coupling(name = 'GC_1733',
                   value = '(cqe1x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1734 = Coupling(name = 'GC_1734',
                   value = '(cqe1x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1735 = Coupling(name = 'GC_1735',
                   value = '(cqe1x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1736 = Coupling(name = 'GC_1736',
                   value = '(cqe1x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1737 = Coupling(name = 'GC_1737',
                   value = '(cqe1x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1738 = Coupling(name = 'GC_1738',
                   value = '(cqe1x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1739 = Coupling(name = 'GC_1739',
                   value = '(cqe1x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1740 = Coupling(name = 'GC_1740',
                   value = '(cqe1x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1741 = Coupling(name = 'GC_1741',
                   value = '(cqe1x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1742 = Coupling(name = 'GC_1742',
                   value = '(cqe1x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1743 = Coupling(name = 'GC_1743',
                   value = '(cqe1x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1744 = Coupling(name = 'GC_1744',
                   value = '(cqe1x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1745 = Coupling(name = 'GC_1745',
                   value = '(cqe1x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1746 = Coupling(name = 'GC_1746',
                   value = '(cqe2x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1747 = Coupling(name = 'GC_1747',
                   value = '(cqe2x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1748 = Coupling(name = 'GC_1748',
                   value = '(cqe2x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1749 = Coupling(name = 'GC_1749',
                   value = '(cqe2x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1750 = Coupling(name = 'GC_1750',
                   value = '(cqe2x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1751 = Coupling(name = 'GC_1751',
                   value = '(cqe2x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1752 = Coupling(name = 'GC_1752',
                   value = '(cqe2x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1753 = Coupling(name = 'GC_1753',
                   value = '(cqe2x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1754 = Coupling(name = 'GC_1754',
                   value = '(cqe2x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1755 = Coupling(name = 'GC_1755',
                   value = '(cqe2x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1756 = Coupling(name = 'GC_1756',
                   value = '(cqe2x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1757 = Coupling(name = 'GC_1757',
                   value = '(cqe2x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1758 = Coupling(name = 'GC_1758',
                   value = '(cqe2x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1759 = Coupling(name = 'GC_1759',
                   value = '(cqe2x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1760 = Coupling(name = 'GC_1760',
                   value = '(cqe2x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1761 = Coupling(name = 'GC_1761',
                   value = '(cqe2x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1762 = Coupling(name = 'GC_1762',
                   value = '(cqe2x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1763 = Coupling(name = 'GC_1763',
                   value = '(cqe2x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1764 = Coupling(name = 'GC_1764',
                   value = '(cqe2x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1765 = Coupling(name = 'GC_1765',
                   value = '(cqe2x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1766 = Coupling(name = 'GC_1766',
                   value = '(cqe2x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1767 = Coupling(name = 'GC_1767',
                   value = '(cqe2x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1768 = Coupling(name = 'GC_1768',
                   value = '(cqe2x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1769 = Coupling(name = 'GC_1769',
                   value = '(cqe2x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1770 = Coupling(name = 'GC_1770',
                   value = '(cqe2x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1771 = Coupling(name = 'GC_1771',
                   value = '(cqe2x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1772 = Coupling(name = 'GC_1772',
                   value = '(cqe2x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1773 = Coupling(name = 'GC_1773',
                   value = '(cqe3x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1774 = Coupling(name = 'GC_1774',
                   value = '(cqe3x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1775 = Coupling(name = 'GC_1775',
                   value = '(cqe3x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1776 = Coupling(name = 'GC_1776',
                   value = '(cqe3x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1777 = Coupling(name = 'GC_1777',
                   value = '(cqe3x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1778 = Coupling(name = 'GC_1778',
                   value = '(cqe3x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1779 = Coupling(name = 'GC_1779',
                   value = '(cqe3x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1780 = Coupling(name = 'GC_1780',
                   value = '(cqe3x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1781 = Coupling(name = 'GC_1781',
                   value = '(cqe3x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1782 = Coupling(name = 'GC_1782',
                   value = '(cqe3x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1783 = Coupling(name = 'GC_1783',
                   value = '(cqe3x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1784 = Coupling(name = 'GC_1784',
                   value = '(cqe3x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1785 = Coupling(name = 'GC_1785',
                   value = '(cqe3x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1786 = Coupling(name = 'GC_1786',
                   value = '(cqe3x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1787 = Coupling(name = 'GC_1787',
                   value = '(cqe3x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1788 = Coupling(name = 'GC_1788',
                   value = '(cqe3x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1789 = Coupling(name = 'GC_1789',
                   value = '(cqe3x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1790 = Coupling(name = 'GC_1790',
                   value = '(cqe3x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1791 = Coupling(name = 'GC_1791',
                   value = '(cqe3x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1792 = Coupling(name = 'GC_1792',
                   value = '(cqe3x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1793 = Coupling(name = 'GC_1793',
                   value = '(cqe3x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1794 = Coupling(name = 'GC_1794',
                   value = '(cqe3x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1795 = Coupling(name = 'GC_1795',
                   value = '(cqe3x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1796 = Coupling(name = 'GC_1796',
                   value = '(cqe3x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1797 = Coupling(name = 'GC_1797',
                   value = '(cqe3x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1798 = Coupling(name = 'GC_1798',
                   value = '(cqe3x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1799 = Coupling(name = 'GC_1799',
                   value = '(cqe3x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1800 = Coupling(name = 'GC_1800',
                   value = '(4*cqq31x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1801 = Coupling(name = 'GC_1801',
                   value = '(4*cqq31x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1802 = Coupling(name = 'GC_1802',
                   value = '(4*cqq31x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1803 = Coupling(name = 'GC_1803',
                   value = '(4*cqq32x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1804 = Coupling(name = 'GC_1804',
                   value = '(4*cqq32x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1805 = Coupling(name = 'GC_1805',
                   value = '(4*cqq32x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1806 = Coupling(name = 'GC_1806',
                   value = '(4*cqq33x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1807 = Coupling(name = 'GC_1807',
                   value = '(4*cqq33x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1808 = Coupling(name = 'GC_1808',
                   value = '(4*cqq33x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1809 = Coupling(name = 'GC_1809',
                   value = '(cqu11x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1810 = Coupling(name = 'GC_1810',
                   value = '(cqu11x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1811 = Coupling(name = 'GC_1811',
                   value = '(cqu11x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1812 = Coupling(name = 'GC_1812',
                   value = '(cqu11x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1813 = Coupling(name = 'GC_1813',
                   value = '(cqu11x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1814 = Coupling(name = 'GC_1814',
                   value = '(cqu11x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1815 = Coupling(name = 'GC_1815',
                   value = '(cqu11x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1816 = Coupling(name = 'GC_1816',
                   value = '(cqu11x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1817 = Coupling(name = 'GC_1817',
                   value = '(cqu11x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1818 = Coupling(name = 'GC_1818',
                   value = '(cqu11x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1819 = Coupling(name = 'GC_1819',
                   value = '(cqu11x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1820 = Coupling(name = 'GC_1820',
                   value = '(cqu11x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1821 = Coupling(name = 'GC_1821',
                   value = '(cqu11x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1822 = Coupling(name = 'GC_1822',
                   value = '(cqu11x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1823 = Coupling(name = 'GC_1823',
                   value = '(cqu11x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1824 = Coupling(name = 'GC_1824',
                   value = '(cqu11x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1825 = Coupling(name = 'GC_1825',
                   value = '(cqu11x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1826 = Coupling(name = 'GC_1826',
                   value = '(cqu11x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1827 = Coupling(name = 'GC_1827',
                   value = '(cqu11x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1828 = Coupling(name = 'GC_1828',
                   value = '(cqu11x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1829 = Coupling(name = 'GC_1829',
                   value = '(cqu11x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1830 = Coupling(name = 'GC_1830',
                   value = '(cqu11x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1831 = Coupling(name = 'GC_1831',
                   value = '(cqu11x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1832 = Coupling(name = 'GC_1832',
                   value = '(cqu11x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1833 = Coupling(name = 'GC_1833',
                   value = '(cqu11x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1834 = Coupling(name = 'GC_1834',
                   value = '(cqu11x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1835 = Coupling(name = 'GC_1835',
                   value = '(cqu11x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1836 = Coupling(name = 'GC_1836',
                   value = '(cqu12x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1837 = Coupling(name = 'GC_1837',
                   value = '(cqu12x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1838 = Coupling(name = 'GC_1838',
                   value = '(cqu12x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1839 = Coupling(name = 'GC_1839',
                   value = '(cqu12x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1840 = Coupling(name = 'GC_1840',
                   value = '(cqu12x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1841 = Coupling(name = 'GC_1841',
                   value = '(cqu12x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1842 = Coupling(name = 'GC_1842',
                   value = '(cqu12x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1843 = Coupling(name = 'GC_1843',
                   value = '(cqu12x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1844 = Coupling(name = 'GC_1844',
                   value = '(cqu12x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1845 = Coupling(name = 'GC_1845',
                   value = '(cqu12x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1846 = Coupling(name = 'GC_1846',
                   value = '(cqu12x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1847 = Coupling(name = 'GC_1847',
                   value = '(cqu12x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1848 = Coupling(name = 'GC_1848',
                   value = '(cqu12x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1849 = Coupling(name = 'GC_1849',
                   value = '(cqu12x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1850 = Coupling(name = 'GC_1850',
                   value = '(cqu12x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1851 = Coupling(name = 'GC_1851',
                   value = '(cqu12x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1852 = Coupling(name = 'GC_1852',
                   value = '(cqu12x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1853 = Coupling(name = 'GC_1853',
                   value = '(cqu12x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1854 = Coupling(name = 'GC_1854',
                   value = '(cqu12x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1855 = Coupling(name = 'GC_1855',
                   value = '(cqu12x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1856 = Coupling(name = 'GC_1856',
                   value = '(cqu12x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1857 = Coupling(name = 'GC_1857',
                   value = '(cqu12x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1858 = Coupling(name = 'GC_1858',
                   value = '(cqu12x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1859 = Coupling(name = 'GC_1859',
                   value = '(cqu12x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1860 = Coupling(name = 'GC_1860',
                   value = '(cqu12x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1861 = Coupling(name = 'GC_1861',
                   value = '(cqu12x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1862 = Coupling(name = 'GC_1862',
                   value = '(cqu12x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1863 = Coupling(name = 'GC_1863',
                   value = '(cqu13x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1864 = Coupling(name = 'GC_1864',
                   value = '(cqu13x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1865 = Coupling(name = 'GC_1865',
                   value = '(cqu13x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1866 = Coupling(name = 'GC_1866',
                   value = '(cqu13x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1867 = Coupling(name = 'GC_1867',
                   value = '(cqu13x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1868 = Coupling(name = 'GC_1868',
                   value = '(cqu13x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1869 = Coupling(name = 'GC_1869',
                   value = '(cqu13x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1870 = Coupling(name = 'GC_1870',
                   value = '(cqu13x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1871 = Coupling(name = 'GC_1871',
                   value = '(cqu13x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1872 = Coupling(name = 'GC_1872',
                   value = '(cqu13x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1873 = Coupling(name = 'GC_1873',
                   value = '(cqu13x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1874 = Coupling(name = 'GC_1874',
                   value = '(cqu13x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1875 = Coupling(name = 'GC_1875',
                   value = '(cqu13x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1876 = Coupling(name = 'GC_1876',
                   value = '(cqu13x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1877 = Coupling(name = 'GC_1877',
                   value = '(cqu13x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1878 = Coupling(name = 'GC_1878',
                   value = '(cqu13x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1879 = Coupling(name = 'GC_1879',
                   value = '(cqu13x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1880 = Coupling(name = 'GC_1880',
                   value = '(cqu13x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1881 = Coupling(name = 'GC_1881',
                   value = '(cqu13x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1882 = Coupling(name = 'GC_1882',
                   value = '(cqu13x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1883 = Coupling(name = 'GC_1883',
                   value = '(cqu13x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1884 = Coupling(name = 'GC_1884',
                   value = '(cqu13x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1885 = Coupling(name = 'GC_1885',
                   value = '(cqu13x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1886 = Coupling(name = 'GC_1886',
                   value = '(cqu13x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1887 = Coupling(name = 'GC_1887',
                   value = '(cqu13x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1888 = Coupling(name = 'GC_1888',
                   value = '(cqu13x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1889 = Coupling(name = 'GC_1889',
                   value = '(cqu13x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1890 = Coupling(name = 'GC_1890',
                   value = '(cqu81x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1891 = Coupling(name = 'GC_1891',
                   value = '(cqu81x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1892 = Coupling(name = 'GC_1892',
                   value = '(cqu81x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1893 = Coupling(name = 'GC_1893',
                   value = '(cqu81x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1894 = Coupling(name = 'GC_1894',
                   value = '(cqu81x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1895 = Coupling(name = 'GC_1895',
                   value = '(cqu81x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1896 = Coupling(name = 'GC_1896',
                   value = '(cqu81x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1897 = Coupling(name = 'GC_1897',
                   value = '(cqu81x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1898 = Coupling(name = 'GC_1898',
                   value = '(cqu81x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1899 = Coupling(name = 'GC_1899',
                   value = '(cqu81x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1900 = Coupling(name = 'GC_1900',
                   value = '(cqu81x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1901 = Coupling(name = 'GC_1901',
                   value = '(cqu81x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1902 = Coupling(name = 'GC_1902',
                   value = '(cqu81x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1903 = Coupling(name = 'GC_1903',
                   value = '(cqu81x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1904 = Coupling(name = 'GC_1904',
                   value = '(cqu81x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1905 = Coupling(name = 'GC_1905',
                   value = '(cqu81x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1906 = Coupling(name = 'GC_1906',
                   value = '(cqu81x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1907 = Coupling(name = 'GC_1907',
                   value = '(cqu81x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1908 = Coupling(name = 'GC_1908',
                   value = '(cqu81x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1909 = Coupling(name = 'GC_1909',
                   value = '(cqu81x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1910 = Coupling(name = 'GC_1910',
                   value = '(cqu81x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1911 = Coupling(name = 'GC_1911',
                   value = '(cqu81x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1912 = Coupling(name = 'GC_1912',
                   value = '(cqu81x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1913 = Coupling(name = 'GC_1913',
                   value = '(cqu81x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1914 = Coupling(name = 'GC_1914',
                   value = '(cqu81x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1915 = Coupling(name = 'GC_1915',
                   value = '(cqu81x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1916 = Coupling(name = 'GC_1916',
                   value = '(cqu81x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1917 = Coupling(name = 'GC_1917',
                   value = '(cqu82x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1918 = Coupling(name = 'GC_1918',
                   value = '(cqu82x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1919 = Coupling(name = 'GC_1919',
                   value = '(cqu82x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1920 = Coupling(name = 'GC_1920',
                   value = '(cqu82x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1921 = Coupling(name = 'GC_1921',
                   value = '(cqu82x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1922 = Coupling(name = 'GC_1922',
                   value = '(cqu82x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1923 = Coupling(name = 'GC_1923',
                   value = '(cqu82x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1924 = Coupling(name = 'GC_1924',
                   value = '(cqu82x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1925 = Coupling(name = 'GC_1925',
                   value = '(cqu82x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1926 = Coupling(name = 'GC_1926',
                   value = '(cqu82x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1927 = Coupling(name = 'GC_1927',
                   value = '(cqu82x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1928 = Coupling(name = 'GC_1928',
                   value = '(cqu82x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1929 = Coupling(name = 'GC_1929',
                   value = '(cqu82x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1930 = Coupling(name = 'GC_1930',
                   value = '(cqu82x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1931 = Coupling(name = 'GC_1931',
                   value = '(cqu82x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1932 = Coupling(name = 'GC_1932',
                   value = '(cqu82x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1933 = Coupling(name = 'GC_1933',
                   value = '(cqu82x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1934 = Coupling(name = 'GC_1934',
                   value = '(cqu82x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1935 = Coupling(name = 'GC_1935',
                   value = '(cqu82x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1936 = Coupling(name = 'GC_1936',
                   value = '(cqu82x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1937 = Coupling(name = 'GC_1937',
                   value = '(cqu82x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1938 = Coupling(name = 'GC_1938',
                   value = '(cqu82x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1939 = Coupling(name = 'GC_1939',
                   value = '(cqu82x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1940 = Coupling(name = 'GC_1940',
                   value = '(cqu82x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1941 = Coupling(name = 'GC_1941',
                   value = '(cqu82x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1942 = Coupling(name = 'GC_1942',
                   value = '(cqu82x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1943 = Coupling(name = 'GC_1943',
                   value = '(cqu82x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1944 = Coupling(name = 'GC_1944',
                   value = '(cqu83x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1945 = Coupling(name = 'GC_1945',
                   value = '(cqu83x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1946 = Coupling(name = 'GC_1946',
                   value = '(cqu83x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1947 = Coupling(name = 'GC_1947',
                   value = '(cqu83x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1948 = Coupling(name = 'GC_1948',
                   value = '(cqu83x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1949 = Coupling(name = 'GC_1949',
                   value = '(cqu83x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1950 = Coupling(name = 'GC_1950',
                   value = '(cqu83x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1951 = Coupling(name = 'GC_1951',
                   value = '(cqu83x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1952 = Coupling(name = 'GC_1952',
                   value = '(cqu83x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1953 = Coupling(name = 'GC_1953',
                   value = '(cqu83x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1954 = Coupling(name = 'GC_1954',
                   value = '(cqu83x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1955 = Coupling(name = 'GC_1955',
                   value = '(cqu83x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1956 = Coupling(name = 'GC_1956',
                   value = '(cqu83x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1957 = Coupling(name = 'GC_1957',
                   value = '(cqu83x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1958 = Coupling(name = 'GC_1958',
                   value = '(cqu83x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1959 = Coupling(name = 'GC_1959',
                   value = '(cqu83x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1960 = Coupling(name = 'GC_1960',
                   value = '(cqu83x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1961 = Coupling(name = 'GC_1961',
                   value = '(cqu83x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1962 = Coupling(name = 'GC_1962',
                   value = '(cqu83x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1963 = Coupling(name = 'GC_1963',
                   value = '(cqu83x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1964 = Coupling(name = 'GC_1964',
                   value = '(cqu83x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1965 = Coupling(name = 'GC_1965',
                   value = '(cqu83x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1966 = Coupling(name = 'GC_1966',
                   value = '(cqu83x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1967 = Coupling(name = 'GC_1967',
                   value = '(cqu83x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1968 = Coupling(name = 'GC_1968',
                   value = '(cqu83x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1969 = Coupling(name = 'GC_1969',
                   value = '(cqu83x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1970 = Coupling(name = 'GC_1970',
                   value = '(cqu83x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1971 = Coupling(name = 'GC_1971',
                   value = '-((cquqd11x1x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1972 = Coupling(name = 'GC_1972',
                   value = '(cquqd11x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1973 = Coupling(name = 'GC_1973',
                   value = '-((cquqd11x1x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1974 = Coupling(name = 'GC_1974',
                   value = '(cquqd11x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1975 = Coupling(name = 'GC_1975',
                   value = '-((cquqd11x1x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1976 = Coupling(name = 'GC_1976',
                   value = '(cquqd11x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1977 = Coupling(name = 'GC_1977',
                   value = '-((cquqd11x1x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1978 = Coupling(name = 'GC_1978',
                   value = '(cquqd11x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1979 = Coupling(name = 'GC_1979',
                   value = '-((cquqd11x1x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1980 = Coupling(name = 'GC_1980',
                   value = '(cquqd11x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1981 = Coupling(name = 'GC_1981',
                   value = '-((cquqd11x1x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1982 = Coupling(name = 'GC_1982',
                   value = '(cquqd11x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1983 = Coupling(name = 'GC_1983',
                   value = '-((cquqd11x1x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1984 = Coupling(name = 'GC_1984',
                   value = '(cquqd11x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1985 = Coupling(name = 'GC_1985',
                   value = '-((cquqd11x1x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1986 = Coupling(name = 'GC_1986',
                   value = '(cquqd11x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1987 = Coupling(name = 'GC_1987',
                   value = '-((cquqd11x1x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1988 = Coupling(name = 'GC_1988',
                   value = '(cquqd11x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1989 = Coupling(name = 'GC_1989',
                   value = '-((cquqd11x2x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1990 = Coupling(name = 'GC_1990',
                   value = '(cquqd11x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1991 = Coupling(name = 'GC_1991',
                   value = '-((cquqd11x2x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1992 = Coupling(name = 'GC_1992',
                   value = '(cquqd11x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1993 = Coupling(name = 'GC_1993',
                   value = '-((cquqd11x2x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1994 = Coupling(name = 'GC_1994',
                   value = '(cquqd11x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1995 = Coupling(name = 'GC_1995',
                   value = '-((cquqd11x2x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1996 = Coupling(name = 'GC_1996',
                   value = '(cquqd11x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1997 = Coupling(name = 'GC_1997',
                   value = '-((cquqd11x2x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_1998 = Coupling(name = 'GC_1998',
                   value = '(cquqd11x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1999 = Coupling(name = 'GC_1999',
                   value = '-((cquqd11x2x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2000 = Coupling(name = 'GC_2000',
                   value = '(cquqd11x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2001 = Coupling(name = 'GC_2001',
                   value = '-((cquqd11x2x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2002 = Coupling(name = 'GC_2002',
                   value = '(cquqd11x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2003 = Coupling(name = 'GC_2003',
                   value = '-((cquqd11x2x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2004 = Coupling(name = 'GC_2004',
                   value = '(cquqd11x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2005 = Coupling(name = 'GC_2005',
                   value = '-((cquqd11x2x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2006 = Coupling(name = 'GC_2006',
                   value = '(cquqd11x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2007 = Coupling(name = 'GC_2007',
                   value = '-((cquqd11x3x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2008 = Coupling(name = 'GC_2008',
                   value = '(cquqd11x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2009 = Coupling(name = 'GC_2009',
                   value = '-((cquqd11x3x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2010 = Coupling(name = 'GC_2010',
                   value = '(cquqd11x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2011 = Coupling(name = 'GC_2011',
                   value = '-((cquqd11x3x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2012 = Coupling(name = 'GC_2012',
                   value = '(cquqd11x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2013 = Coupling(name = 'GC_2013',
                   value = '-((cquqd11x3x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2014 = Coupling(name = 'GC_2014',
                   value = '(cquqd11x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2015 = Coupling(name = 'GC_2015',
                   value = '-((cquqd11x3x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2016 = Coupling(name = 'GC_2016',
                   value = '(cquqd11x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2017 = Coupling(name = 'GC_2017',
                   value = '-((cquqd11x3x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2018 = Coupling(name = 'GC_2018',
                   value = '(cquqd11x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2019 = Coupling(name = 'GC_2019',
                   value = '-((cquqd11x3x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2020 = Coupling(name = 'GC_2020',
                   value = '(cquqd11x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2021 = Coupling(name = 'GC_2021',
                   value = '-((cquqd11x3x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2022 = Coupling(name = 'GC_2022',
                   value = '(cquqd11x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2023 = Coupling(name = 'GC_2023',
                   value = '-((cquqd11x3x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2024 = Coupling(name = 'GC_2024',
                   value = '(cquqd11x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2025 = Coupling(name = 'GC_2025',
                   value = '-((cquqd12x1x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2026 = Coupling(name = 'GC_2026',
                   value = '(cquqd12x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2027 = Coupling(name = 'GC_2027',
                   value = '-((cquqd12x1x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2028 = Coupling(name = 'GC_2028',
                   value = '(cquqd12x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2029 = Coupling(name = 'GC_2029',
                   value = '-((cquqd12x1x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2030 = Coupling(name = 'GC_2030',
                   value = '(cquqd12x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2031 = Coupling(name = 'GC_2031',
                   value = '-((cquqd12x1x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2032 = Coupling(name = 'GC_2032',
                   value = '(cquqd12x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2033 = Coupling(name = 'GC_2033',
                   value = '-((cquqd12x1x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2034 = Coupling(name = 'GC_2034',
                   value = '(cquqd12x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2035 = Coupling(name = 'GC_2035',
                   value = '-((cquqd12x1x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2036 = Coupling(name = 'GC_2036',
                   value = '(cquqd12x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2037 = Coupling(name = 'GC_2037',
                   value = '-((cquqd12x1x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2038 = Coupling(name = 'GC_2038',
                   value = '(cquqd12x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2039 = Coupling(name = 'GC_2039',
                   value = '-((cquqd12x1x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2040 = Coupling(name = 'GC_2040',
                   value = '(cquqd12x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2041 = Coupling(name = 'GC_2041',
                   value = '-((cquqd12x1x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2042 = Coupling(name = 'GC_2042',
                   value = '(cquqd12x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2043 = Coupling(name = 'GC_2043',
                   value = '-((cquqd12x2x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2044 = Coupling(name = 'GC_2044',
                   value = '(cquqd12x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2045 = Coupling(name = 'GC_2045',
                   value = '-((cquqd12x2x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2046 = Coupling(name = 'GC_2046',
                   value = '(cquqd12x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2047 = Coupling(name = 'GC_2047',
                   value = '-((cquqd12x2x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2048 = Coupling(name = 'GC_2048',
                   value = '(cquqd12x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2049 = Coupling(name = 'GC_2049',
                   value = '-((cquqd12x2x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2050 = Coupling(name = 'GC_2050',
                   value = '(cquqd12x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2051 = Coupling(name = 'GC_2051',
                   value = '-((cquqd12x2x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2052 = Coupling(name = 'GC_2052',
                   value = '(cquqd12x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2053 = Coupling(name = 'GC_2053',
                   value = '-((cquqd12x2x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2054 = Coupling(name = 'GC_2054',
                   value = '(cquqd12x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2055 = Coupling(name = 'GC_2055',
                   value = '-((cquqd12x2x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2056 = Coupling(name = 'GC_2056',
                   value = '(cquqd12x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2057 = Coupling(name = 'GC_2057',
                   value = '-((cquqd12x2x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2058 = Coupling(name = 'GC_2058',
                   value = '(cquqd12x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2059 = Coupling(name = 'GC_2059',
                   value = '-((cquqd12x2x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2060 = Coupling(name = 'GC_2060',
                   value = '(cquqd12x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2061 = Coupling(name = 'GC_2061',
                   value = '-((cquqd12x3x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2062 = Coupling(name = 'GC_2062',
                   value = '(cquqd12x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2063 = Coupling(name = 'GC_2063',
                   value = '-((cquqd12x3x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2064 = Coupling(name = 'GC_2064',
                   value = '(cquqd12x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2065 = Coupling(name = 'GC_2065',
                   value = '-((cquqd12x3x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2066 = Coupling(name = 'GC_2066',
                   value = '(cquqd12x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2067 = Coupling(name = 'GC_2067',
                   value = '-((cquqd12x3x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2068 = Coupling(name = 'GC_2068',
                   value = '(cquqd12x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2069 = Coupling(name = 'GC_2069',
                   value = '-((cquqd12x3x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2070 = Coupling(name = 'GC_2070',
                   value = '(cquqd12x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2071 = Coupling(name = 'GC_2071',
                   value = '-((cquqd12x3x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2072 = Coupling(name = 'GC_2072',
                   value = '(cquqd12x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2073 = Coupling(name = 'GC_2073',
                   value = '-((cquqd12x3x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2074 = Coupling(name = 'GC_2074',
                   value = '(cquqd12x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2075 = Coupling(name = 'GC_2075',
                   value = '-((cquqd12x3x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2076 = Coupling(name = 'GC_2076',
                   value = '(cquqd12x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2077 = Coupling(name = 'GC_2077',
                   value = '-((cquqd12x3x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2078 = Coupling(name = 'GC_2078',
                   value = '(cquqd12x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2079 = Coupling(name = 'GC_2079',
                   value = '-((cquqd13x1x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2080 = Coupling(name = 'GC_2080',
                   value = '(cquqd13x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2081 = Coupling(name = 'GC_2081',
                   value = '-((cquqd13x1x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2082 = Coupling(name = 'GC_2082',
                   value = '(cquqd13x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2083 = Coupling(name = 'GC_2083',
                   value = '-((cquqd13x1x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2084 = Coupling(name = 'GC_2084',
                   value = '(cquqd13x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2085 = Coupling(name = 'GC_2085',
                   value = '-((cquqd13x1x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2086 = Coupling(name = 'GC_2086',
                   value = '(cquqd13x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2087 = Coupling(name = 'GC_2087',
                   value = '-((cquqd13x1x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2088 = Coupling(name = 'GC_2088',
                   value = '(cquqd13x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2089 = Coupling(name = 'GC_2089',
                   value = '-((cquqd13x1x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2090 = Coupling(name = 'GC_2090',
                   value = '(cquqd13x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2091 = Coupling(name = 'GC_2091',
                   value = '-((cquqd13x1x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2092 = Coupling(name = 'GC_2092',
                   value = '(cquqd13x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2093 = Coupling(name = 'GC_2093',
                   value = '-((cquqd13x1x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2094 = Coupling(name = 'GC_2094',
                   value = '(cquqd13x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2095 = Coupling(name = 'GC_2095',
                   value = '-((cquqd13x1x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2096 = Coupling(name = 'GC_2096',
                   value = '(cquqd13x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2097 = Coupling(name = 'GC_2097',
                   value = '-((cquqd13x2x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2098 = Coupling(name = 'GC_2098',
                   value = '(cquqd13x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2099 = Coupling(name = 'GC_2099',
                   value = '-((cquqd13x2x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2100 = Coupling(name = 'GC_2100',
                   value = '(cquqd13x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2101 = Coupling(name = 'GC_2101',
                   value = '-((cquqd13x2x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2102 = Coupling(name = 'GC_2102',
                   value = '(cquqd13x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2103 = Coupling(name = 'GC_2103',
                   value = '-((cquqd13x2x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2104 = Coupling(name = 'GC_2104',
                   value = '(cquqd13x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2105 = Coupling(name = 'GC_2105',
                   value = '-((cquqd13x2x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2106 = Coupling(name = 'GC_2106',
                   value = '(cquqd13x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2107 = Coupling(name = 'GC_2107',
                   value = '-((cquqd13x2x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2108 = Coupling(name = 'GC_2108',
                   value = '(cquqd13x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2109 = Coupling(name = 'GC_2109',
                   value = '-((cquqd13x2x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2110 = Coupling(name = 'GC_2110',
                   value = '(cquqd13x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2111 = Coupling(name = 'GC_2111',
                   value = '-((cquqd13x2x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2112 = Coupling(name = 'GC_2112',
                   value = '(cquqd13x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2113 = Coupling(name = 'GC_2113',
                   value = '-((cquqd13x2x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2114 = Coupling(name = 'GC_2114',
                   value = '(cquqd13x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2115 = Coupling(name = 'GC_2115',
                   value = '-((cquqd13x3x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2116 = Coupling(name = 'GC_2116',
                   value = '(cquqd13x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2117 = Coupling(name = 'GC_2117',
                   value = '-((cquqd13x3x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2118 = Coupling(name = 'GC_2118',
                   value = '(cquqd13x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2119 = Coupling(name = 'GC_2119',
                   value = '-((cquqd13x3x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2120 = Coupling(name = 'GC_2120',
                   value = '(cquqd13x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2121 = Coupling(name = 'GC_2121',
                   value = '-((cquqd13x3x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2122 = Coupling(name = 'GC_2122',
                   value = '(cquqd13x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2123 = Coupling(name = 'GC_2123',
                   value = '-((cquqd13x3x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2124 = Coupling(name = 'GC_2124',
                   value = '(cquqd13x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2125 = Coupling(name = 'GC_2125',
                   value = '-((cquqd13x3x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2126 = Coupling(name = 'GC_2126',
                   value = '(cquqd13x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2127 = Coupling(name = 'GC_2127',
                   value = '-((cquqd13x3x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2128 = Coupling(name = 'GC_2128',
                   value = '(cquqd13x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2129 = Coupling(name = 'GC_2129',
                   value = '-((cquqd13x3x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2130 = Coupling(name = 'GC_2130',
                   value = '(cquqd13x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2131 = Coupling(name = 'GC_2131',
                   value = '-((cquqd13x3x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2132 = Coupling(name = 'GC_2132',
                   value = '(cquqd13x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2133 = Coupling(name = 'GC_2133',
                   value = '-((cquqd81x1x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2134 = Coupling(name = 'GC_2134',
                   value = '(cquqd81x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2135 = Coupling(name = 'GC_2135',
                   value = '-((cquqd81x1x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2136 = Coupling(name = 'GC_2136',
                   value = '(cquqd81x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2137 = Coupling(name = 'GC_2137',
                   value = '-((cquqd81x1x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2138 = Coupling(name = 'GC_2138',
                   value = '(cquqd81x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2139 = Coupling(name = 'GC_2139',
                   value = '-((cquqd81x1x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2140 = Coupling(name = 'GC_2140',
                   value = '(cquqd81x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2141 = Coupling(name = 'GC_2141',
                   value = '-((cquqd81x1x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2142 = Coupling(name = 'GC_2142',
                   value = '(cquqd81x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2143 = Coupling(name = 'GC_2143',
                   value = '-((cquqd81x1x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2144 = Coupling(name = 'GC_2144',
                   value = '(cquqd81x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2145 = Coupling(name = 'GC_2145',
                   value = '-((cquqd81x1x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2146 = Coupling(name = 'GC_2146',
                   value = '(cquqd81x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2147 = Coupling(name = 'GC_2147',
                   value = '-((cquqd81x1x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2148 = Coupling(name = 'GC_2148',
                   value = '(cquqd81x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2149 = Coupling(name = 'GC_2149',
                   value = '-((cquqd81x1x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2150 = Coupling(name = 'GC_2150',
                   value = '(cquqd81x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2151 = Coupling(name = 'GC_2151',
                   value = '-((cquqd81x2x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2152 = Coupling(name = 'GC_2152',
                   value = '(cquqd81x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2153 = Coupling(name = 'GC_2153',
                   value = '-((cquqd81x2x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2154 = Coupling(name = 'GC_2154',
                   value = '(cquqd81x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2155 = Coupling(name = 'GC_2155',
                   value = '-((cquqd81x2x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2156 = Coupling(name = 'GC_2156',
                   value = '(cquqd81x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2157 = Coupling(name = 'GC_2157',
                   value = '-((cquqd81x2x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2158 = Coupling(name = 'GC_2158',
                   value = '(cquqd81x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2159 = Coupling(name = 'GC_2159',
                   value = '-((cquqd81x2x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2160 = Coupling(name = 'GC_2160',
                   value = '(cquqd81x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2161 = Coupling(name = 'GC_2161',
                   value = '-((cquqd81x2x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2162 = Coupling(name = 'GC_2162',
                   value = '(cquqd81x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2163 = Coupling(name = 'GC_2163',
                   value = '-((cquqd81x2x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2164 = Coupling(name = 'GC_2164',
                   value = '(cquqd81x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2165 = Coupling(name = 'GC_2165',
                   value = '-((cquqd81x2x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2166 = Coupling(name = 'GC_2166',
                   value = '(cquqd81x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2167 = Coupling(name = 'GC_2167',
                   value = '-((cquqd81x2x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2168 = Coupling(name = 'GC_2168',
                   value = '(cquqd81x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2169 = Coupling(name = 'GC_2169',
                   value = '-((cquqd81x3x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2170 = Coupling(name = 'GC_2170',
                   value = '(cquqd81x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2171 = Coupling(name = 'GC_2171',
                   value = '-((cquqd81x3x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2172 = Coupling(name = 'GC_2172',
                   value = '(cquqd81x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2173 = Coupling(name = 'GC_2173',
                   value = '-((cquqd81x3x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2174 = Coupling(name = 'GC_2174',
                   value = '(cquqd81x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2175 = Coupling(name = 'GC_2175',
                   value = '-((cquqd81x3x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2176 = Coupling(name = 'GC_2176',
                   value = '(cquqd81x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2177 = Coupling(name = 'GC_2177',
                   value = '-((cquqd81x3x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2178 = Coupling(name = 'GC_2178',
                   value = '(cquqd81x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2179 = Coupling(name = 'GC_2179',
                   value = '-((cquqd81x3x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2180 = Coupling(name = 'GC_2180',
                   value = '(cquqd81x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2181 = Coupling(name = 'GC_2181',
                   value = '-((cquqd81x3x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2182 = Coupling(name = 'GC_2182',
                   value = '(cquqd81x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2183 = Coupling(name = 'GC_2183',
                   value = '-((cquqd81x3x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2184 = Coupling(name = 'GC_2184',
                   value = '(cquqd81x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2185 = Coupling(name = 'GC_2185',
                   value = '-((cquqd81x3x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2186 = Coupling(name = 'GC_2186',
                   value = '(cquqd81x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2187 = Coupling(name = 'GC_2187',
                   value = '-((cquqd82x1x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2188 = Coupling(name = 'GC_2188',
                   value = '(cquqd82x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2189 = Coupling(name = 'GC_2189',
                   value = '-((cquqd82x1x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2190 = Coupling(name = 'GC_2190',
                   value = '(cquqd82x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2191 = Coupling(name = 'GC_2191',
                   value = '-((cquqd82x1x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2192 = Coupling(name = 'GC_2192',
                   value = '(cquqd82x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2193 = Coupling(name = 'GC_2193',
                   value = '-((cquqd82x1x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2194 = Coupling(name = 'GC_2194',
                   value = '(cquqd82x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2195 = Coupling(name = 'GC_2195',
                   value = '-((cquqd82x1x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2196 = Coupling(name = 'GC_2196',
                   value = '(cquqd82x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2197 = Coupling(name = 'GC_2197',
                   value = '-((cquqd82x1x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2198 = Coupling(name = 'GC_2198',
                   value = '(cquqd82x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2199 = Coupling(name = 'GC_2199',
                   value = '-((cquqd82x1x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2200 = Coupling(name = 'GC_2200',
                   value = '(cquqd82x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2201 = Coupling(name = 'GC_2201',
                   value = '-((cquqd82x1x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2202 = Coupling(name = 'GC_2202',
                   value = '(cquqd82x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2203 = Coupling(name = 'GC_2203',
                   value = '-((cquqd82x1x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2204 = Coupling(name = 'GC_2204',
                   value = '(cquqd82x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2205 = Coupling(name = 'GC_2205',
                   value = '-((cquqd82x2x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2206 = Coupling(name = 'GC_2206',
                   value = '(cquqd82x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2207 = Coupling(name = 'GC_2207',
                   value = '-((cquqd82x2x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2208 = Coupling(name = 'GC_2208',
                   value = '(cquqd82x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2209 = Coupling(name = 'GC_2209',
                   value = '-((cquqd82x2x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2210 = Coupling(name = 'GC_2210',
                   value = '(cquqd82x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2211 = Coupling(name = 'GC_2211',
                   value = '-((cquqd82x2x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2212 = Coupling(name = 'GC_2212',
                   value = '(cquqd82x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2213 = Coupling(name = 'GC_2213',
                   value = '-((cquqd82x2x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2214 = Coupling(name = 'GC_2214',
                   value = '(cquqd82x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2215 = Coupling(name = 'GC_2215',
                   value = '-((cquqd82x2x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2216 = Coupling(name = 'GC_2216',
                   value = '(cquqd82x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2217 = Coupling(name = 'GC_2217',
                   value = '-((cquqd82x2x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2218 = Coupling(name = 'GC_2218',
                   value = '(cquqd82x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2219 = Coupling(name = 'GC_2219',
                   value = '-((cquqd82x2x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2220 = Coupling(name = 'GC_2220',
                   value = '(cquqd82x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2221 = Coupling(name = 'GC_2221',
                   value = '-((cquqd82x2x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2222 = Coupling(name = 'GC_2222',
                   value = '(cquqd82x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2223 = Coupling(name = 'GC_2223',
                   value = '-((cquqd82x3x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2224 = Coupling(name = 'GC_2224',
                   value = '(cquqd82x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2225 = Coupling(name = 'GC_2225',
                   value = '-((cquqd82x3x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2226 = Coupling(name = 'GC_2226',
                   value = '(cquqd82x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2227 = Coupling(name = 'GC_2227',
                   value = '-((cquqd82x3x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2228 = Coupling(name = 'GC_2228',
                   value = '(cquqd82x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2229 = Coupling(name = 'GC_2229',
                   value = '-((cquqd82x3x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2230 = Coupling(name = 'GC_2230',
                   value = '(cquqd82x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2231 = Coupling(name = 'GC_2231',
                   value = '-((cquqd82x3x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2232 = Coupling(name = 'GC_2232',
                   value = '(cquqd82x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2233 = Coupling(name = 'GC_2233',
                   value = '-((cquqd82x3x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2234 = Coupling(name = 'GC_2234',
                   value = '(cquqd82x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2235 = Coupling(name = 'GC_2235',
                   value = '-((cquqd82x3x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2236 = Coupling(name = 'GC_2236',
                   value = '(cquqd82x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2237 = Coupling(name = 'GC_2237',
                   value = '-((cquqd82x3x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2238 = Coupling(name = 'GC_2238',
                   value = '(cquqd82x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2239 = Coupling(name = 'GC_2239',
                   value = '-((cquqd82x3x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2240 = Coupling(name = 'GC_2240',
                   value = '(cquqd82x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2241 = Coupling(name = 'GC_2241',
                   value = '-((cquqd83x1x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2242 = Coupling(name = 'GC_2242',
                   value = '(cquqd83x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2243 = Coupling(name = 'GC_2243',
                   value = '-((cquqd83x1x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2244 = Coupling(name = 'GC_2244',
                   value = '(cquqd83x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2245 = Coupling(name = 'GC_2245',
                   value = '-((cquqd83x1x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2246 = Coupling(name = 'GC_2246',
                   value = '(cquqd83x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2247 = Coupling(name = 'GC_2247',
                   value = '-((cquqd83x1x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2248 = Coupling(name = 'GC_2248',
                   value = '(cquqd83x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2249 = Coupling(name = 'GC_2249',
                   value = '-((cquqd83x1x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2250 = Coupling(name = 'GC_2250',
                   value = '(cquqd83x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2251 = Coupling(name = 'GC_2251',
                   value = '-((cquqd83x1x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2252 = Coupling(name = 'GC_2252',
                   value = '(cquqd83x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2253 = Coupling(name = 'GC_2253',
                   value = '-((cquqd83x1x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2254 = Coupling(name = 'GC_2254',
                   value = '(cquqd83x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2255 = Coupling(name = 'GC_2255',
                   value = '-((cquqd83x1x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2256 = Coupling(name = 'GC_2256',
                   value = '(cquqd83x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2257 = Coupling(name = 'GC_2257',
                   value = '-((cquqd83x1x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2258 = Coupling(name = 'GC_2258',
                   value = '(cquqd83x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2259 = Coupling(name = 'GC_2259',
                   value = '-((cquqd83x2x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2260 = Coupling(name = 'GC_2260',
                   value = '(cquqd83x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2261 = Coupling(name = 'GC_2261',
                   value = '-((cquqd83x2x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2262 = Coupling(name = 'GC_2262',
                   value = '(cquqd83x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2263 = Coupling(name = 'GC_2263',
                   value = '-((cquqd83x2x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2264 = Coupling(name = 'GC_2264',
                   value = '(cquqd83x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2265 = Coupling(name = 'GC_2265',
                   value = '-((cquqd83x2x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2266 = Coupling(name = 'GC_2266',
                   value = '(cquqd83x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2267 = Coupling(name = 'GC_2267',
                   value = '-((cquqd83x2x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2268 = Coupling(name = 'GC_2268',
                   value = '(cquqd83x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2269 = Coupling(name = 'GC_2269',
                   value = '-((cquqd83x2x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2270 = Coupling(name = 'GC_2270',
                   value = '(cquqd83x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2271 = Coupling(name = 'GC_2271',
                   value = '-((cquqd83x2x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2272 = Coupling(name = 'GC_2272',
                   value = '(cquqd83x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2273 = Coupling(name = 'GC_2273',
                   value = '-((cquqd83x2x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2274 = Coupling(name = 'GC_2274',
                   value = '(cquqd83x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2275 = Coupling(name = 'GC_2275',
                   value = '-((cquqd83x2x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2276 = Coupling(name = 'GC_2276',
                   value = '(cquqd83x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2277 = Coupling(name = 'GC_2277',
                   value = '-((cquqd83x3x1x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2278 = Coupling(name = 'GC_2278',
                   value = '(cquqd83x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2279 = Coupling(name = 'GC_2279',
                   value = '-((cquqd83x3x1x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2280 = Coupling(name = 'GC_2280',
                   value = '(cquqd83x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2281 = Coupling(name = 'GC_2281',
                   value = '-((cquqd83x3x1x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2282 = Coupling(name = 'GC_2282',
                   value = '(cquqd83x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2283 = Coupling(name = 'GC_2283',
                   value = '-((cquqd83x3x2x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2284 = Coupling(name = 'GC_2284',
                   value = '(cquqd83x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2285 = Coupling(name = 'GC_2285',
                   value = '-((cquqd83x3x2x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2286 = Coupling(name = 'GC_2286',
                   value = '(cquqd83x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2287 = Coupling(name = 'GC_2287',
                   value = '-((cquqd83x3x2x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2288 = Coupling(name = 'GC_2288',
                   value = '(cquqd83x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2289 = Coupling(name = 'GC_2289',
                   value = '-((cquqd83x3x3x1*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2290 = Coupling(name = 'GC_2290',
                   value = '(cquqd83x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2291 = Coupling(name = 'GC_2291',
                   value = '-((cquqd83x3x3x2*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2292 = Coupling(name = 'GC_2292',
                   value = '(cquqd83x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2293 = Coupling(name = 'GC_2293',
                   value = '-((cquqd83x3x3x3*complex(0,1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2294 = Coupling(name = 'GC_2294',
                   value = '(cquqd83x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2295 = Coupling(name = 'GC_2295',
                   value = '(cud11x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2296 = Coupling(name = 'GC_2296',
                   value = '(cud11x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2297 = Coupling(name = 'GC_2297',
                   value = '(cud11x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2298 = Coupling(name = 'GC_2298',
                   value = '(cud11x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2299 = Coupling(name = 'GC_2299',
                   value = '(cud11x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2300 = Coupling(name = 'GC_2300',
                   value = '(cud11x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2301 = Coupling(name = 'GC_2301',
                   value = '(cud11x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2302 = Coupling(name = 'GC_2302',
                   value = '(cud11x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2303 = Coupling(name = 'GC_2303',
                   value = '(cud11x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2304 = Coupling(name = 'GC_2304',
                   value = '(cud11x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2305 = Coupling(name = 'GC_2305',
                   value = '(cud11x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2306 = Coupling(name = 'GC_2306',
                   value = '(cud11x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2307 = Coupling(name = 'GC_2307',
                   value = '(cud11x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2308 = Coupling(name = 'GC_2308',
                   value = '(cud11x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2309 = Coupling(name = 'GC_2309',
                   value = '(cud11x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2310 = Coupling(name = 'GC_2310',
                   value = '(cud11x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2311 = Coupling(name = 'GC_2311',
                   value = '(cud11x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2312 = Coupling(name = 'GC_2312',
                   value = '(cud11x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2313 = Coupling(name = 'GC_2313',
                   value = '(cud11x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2314 = Coupling(name = 'GC_2314',
                   value = '(cud11x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2315 = Coupling(name = 'GC_2315',
                   value = '(cud11x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2316 = Coupling(name = 'GC_2316',
                   value = '(cud11x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2317 = Coupling(name = 'GC_2317',
                   value = '(cud11x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2318 = Coupling(name = 'GC_2318',
                   value = '(cud11x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2319 = Coupling(name = 'GC_2319',
                   value = '(cud11x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2320 = Coupling(name = 'GC_2320',
                   value = '(cud11x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2321 = Coupling(name = 'GC_2321',
                   value = '(cud11x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2322 = Coupling(name = 'GC_2322',
                   value = '(cud12x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2323 = Coupling(name = 'GC_2323',
                   value = '(cud12x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2324 = Coupling(name = 'GC_2324',
                   value = '(cud12x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2325 = Coupling(name = 'GC_2325',
                   value = '(cud12x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2326 = Coupling(name = 'GC_2326',
                   value = '(cud12x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2327 = Coupling(name = 'GC_2327',
                   value = '(cud12x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2328 = Coupling(name = 'GC_2328',
                   value = '(cud12x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2329 = Coupling(name = 'GC_2329',
                   value = '(cud12x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2330 = Coupling(name = 'GC_2330',
                   value = '(cud12x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2331 = Coupling(name = 'GC_2331',
                   value = '(cud12x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2332 = Coupling(name = 'GC_2332',
                   value = '(cud12x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2333 = Coupling(name = 'GC_2333',
                   value = '(cud12x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2334 = Coupling(name = 'GC_2334',
                   value = '(cud12x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2335 = Coupling(name = 'GC_2335',
                   value = '(cud12x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2336 = Coupling(name = 'GC_2336',
                   value = '(cud12x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2337 = Coupling(name = 'GC_2337',
                   value = '(cud12x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2338 = Coupling(name = 'GC_2338',
                   value = '(cud12x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2339 = Coupling(name = 'GC_2339',
                   value = '(cud12x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2340 = Coupling(name = 'GC_2340',
                   value = '(cud12x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2341 = Coupling(name = 'GC_2341',
                   value = '(cud12x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2342 = Coupling(name = 'GC_2342',
                   value = '(cud12x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2343 = Coupling(name = 'GC_2343',
                   value = '(cud12x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2344 = Coupling(name = 'GC_2344',
                   value = '(cud12x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2345 = Coupling(name = 'GC_2345',
                   value = '(cud12x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2346 = Coupling(name = 'GC_2346',
                   value = '(cud12x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2347 = Coupling(name = 'GC_2347',
                   value = '(cud12x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2348 = Coupling(name = 'GC_2348',
                   value = '(cud12x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2349 = Coupling(name = 'GC_2349',
                   value = '(cud13x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2350 = Coupling(name = 'GC_2350',
                   value = '(cud13x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2351 = Coupling(name = 'GC_2351',
                   value = '(cud13x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2352 = Coupling(name = 'GC_2352',
                   value = '(cud13x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2353 = Coupling(name = 'GC_2353',
                   value = '(cud13x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2354 = Coupling(name = 'GC_2354',
                   value = '(cud13x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2355 = Coupling(name = 'GC_2355',
                   value = '(cud13x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2356 = Coupling(name = 'GC_2356',
                   value = '(cud13x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2357 = Coupling(name = 'GC_2357',
                   value = '(cud13x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2358 = Coupling(name = 'GC_2358',
                   value = '(cud13x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2359 = Coupling(name = 'GC_2359',
                   value = '(cud13x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2360 = Coupling(name = 'GC_2360',
                   value = '(cud13x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2361 = Coupling(name = 'GC_2361',
                   value = '(cud13x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2362 = Coupling(name = 'GC_2362',
                   value = '(cud13x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2363 = Coupling(name = 'GC_2363',
                   value = '(cud13x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2364 = Coupling(name = 'GC_2364',
                   value = '(cud13x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2365 = Coupling(name = 'GC_2365',
                   value = '(cud13x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2366 = Coupling(name = 'GC_2366',
                   value = '(cud13x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2367 = Coupling(name = 'GC_2367',
                   value = '(cud13x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2368 = Coupling(name = 'GC_2368',
                   value = '(cud13x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2369 = Coupling(name = 'GC_2369',
                   value = '(cud13x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2370 = Coupling(name = 'GC_2370',
                   value = '(cud13x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2371 = Coupling(name = 'GC_2371',
                   value = '(cud13x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2372 = Coupling(name = 'GC_2372',
                   value = '(cud13x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2373 = Coupling(name = 'GC_2373',
                   value = '(cud13x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2374 = Coupling(name = 'GC_2374',
                   value = '(cud13x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2375 = Coupling(name = 'GC_2375',
                   value = '(cud13x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2376 = Coupling(name = 'GC_2376',
                   value = '(cud81x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2377 = Coupling(name = 'GC_2377',
                   value = '(cud81x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2378 = Coupling(name = 'GC_2378',
                   value = '(cud81x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2379 = Coupling(name = 'GC_2379',
                   value = '(cud81x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2380 = Coupling(name = 'GC_2380',
                   value = '(cud81x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2381 = Coupling(name = 'GC_2381',
                   value = '(cud81x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2382 = Coupling(name = 'GC_2382',
                   value = '(cud81x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2383 = Coupling(name = 'GC_2383',
                   value = '(cud81x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2384 = Coupling(name = 'GC_2384',
                   value = '(cud81x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2385 = Coupling(name = 'GC_2385',
                   value = '(cud81x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2386 = Coupling(name = 'GC_2386',
                   value = '(cud81x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2387 = Coupling(name = 'GC_2387',
                   value = '(cud81x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2388 = Coupling(name = 'GC_2388',
                   value = '(cud81x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2389 = Coupling(name = 'GC_2389',
                   value = '(cud81x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2390 = Coupling(name = 'GC_2390',
                   value = '(cud81x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2391 = Coupling(name = 'GC_2391',
                   value = '(cud81x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2392 = Coupling(name = 'GC_2392',
                   value = '(cud81x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2393 = Coupling(name = 'GC_2393',
                   value = '(cud81x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2394 = Coupling(name = 'GC_2394',
                   value = '(cud81x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2395 = Coupling(name = 'GC_2395',
                   value = '(cud81x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2396 = Coupling(name = 'GC_2396',
                   value = '(cud81x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2397 = Coupling(name = 'GC_2397',
                   value = '(cud81x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2398 = Coupling(name = 'GC_2398',
                   value = '(cud81x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2399 = Coupling(name = 'GC_2399',
                   value = '(cud81x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2400 = Coupling(name = 'GC_2400',
                   value = '(cud81x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2401 = Coupling(name = 'GC_2401',
                   value = '(cud81x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2402 = Coupling(name = 'GC_2402',
                   value = '(cud81x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2403 = Coupling(name = 'GC_2403',
                   value = '(cud82x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2404 = Coupling(name = 'GC_2404',
                   value = '(cud82x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2405 = Coupling(name = 'GC_2405',
                   value = '(cud82x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2406 = Coupling(name = 'GC_2406',
                   value = '(cud82x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2407 = Coupling(name = 'GC_2407',
                   value = '(cud82x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2408 = Coupling(name = 'GC_2408',
                   value = '(cud82x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2409 = Coupling(name = 'GC_2409',
                   value = '(cud82x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2410 = Coupling(name = 'GC_2410',
                   value = '(cud82x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2411 = Coupling(name = 'GC_2411',
                   value = '(cud82x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2412 = Coupling(name = 'GC_2412',
                   value = '(cud82x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2413 = Coupling(name = 'GC_2413',
                   value = '(cud82x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2414 = Coupling(name = 'GC_2414',
                   value = '(cud82x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2415 = Coupling(name = 'GC_2415',
                   value = '(cud82x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2416 = Coupling(name = 'GC_2416',
                   value = '(cud82x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2417 = Coupling(name = 'GC_2417',
                   value = '(cud82x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2418 = Coupling(name = 'GC_2418',
                   value = '(cud82x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2419 = Coupling(name = 'GC_2419',
                   value = '(cud82x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2420 = Coupling(name = 'GC_2420',
                   value = '(cud82x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2421 = Coupling(name = 'GC_2421',
                   value = '(cud82x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2422 = Coupling(name = 'GC_2422',
                   value = '(cud82x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2423 = Coupling(name = 'GC_2423',
                   value = '(cud82x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2424 = Coupling(name = 'GC_2424',
                   value = '(cud82x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2425 = Coupling(name = 'GC_2425',
                   value = '(cud82x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2426 = Coupling(name = 'GC_2426',
                   value = '(cud82x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2427 = Coupling(name = 'GC_2427',
                   value = '(cud82x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2428 = Coupling(name = 'GC_2428',
                   value = '(cud82x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2429 = Coupling(name = 'GC_2429',
                   value = '(cud82x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2430 = Coupling(name = 'GC_2430',
                   value = '(cud83x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2431 = Coupling(name = 'GC_2431',
                   value = '(cud83x1x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2432 = Coupling(name = 'GC_2432',
                   value = '(cud83x1x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2433 = Coupling(name = 'GC_2433',
                   value = '(cud83x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2434 = Coupling(name = 'GC_2434',
                   value = '(cud83x1x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2435 = Coupling(name = 'GC_2435',
                   value = '(cud83x1x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2436 = Coupling(name = 'GC_2436',
                   value = '(cud83x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2437 = Coupling(name = 'GC_2437',
                   value = '(cud83x1x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2438 = Coupling(name = 'GC_2438',
                   value = '(cud83x1x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2439 = Coupling(name = 'GC_2439',
                   value = '(cud83x2x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2440 = Coupling(name = 'GC_2440',
                   value = '(cud83x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2441 = Coupling(name = 'GC_2441',
                   value = '(cud83x2x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2442 = Coupling(name = 'GC_2442',
                   value = '(cud83x2x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2443 = Coupling(name = 'GC_2443',
                   value = '(cud83x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2444 = Coupling(name = 'GC_2444',
                   value = '(cud83x2x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2445 = Coupling(name = 'GC_2445',
                   value = '(cud83x2x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2446 = Coupling(name = 'GC_2446',
                   value = '(cud83x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2447 = Coupling(name = 'GC_2447',
                   value = '(cud83x2x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2448 = Coupling(name = 'GC_2448',
                   value = '(cud83x3x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2449 = Coupling(name = 'GC_2449',
                   value = '(cud83x3x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2450 = Coupling(name = 'GC_2450',
                   value = '(cud83x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2451 = Coupling(name = 'GC_2451',
                   value = '(cud83x3x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2452 = Coupling(name = 'GC_2452',
                   value = '(cud83x3x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2453 = Coupling(name = 'GC_2453',
                   value = '(cud83x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2454 = Coupling(name = 'GC_2454',
                   value = '(cud83x3x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2455 = Coupling(name = 'GC_2455',
                   value = '(cud83x3x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2456 = Coupling(name = 'GC_2456',
                   value = '(cud83x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2457 = Coupling(name = 'GC_2457',
                   value = '(cuG1x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2458 = Coupling(name = 'GC_2458',
                   value = '(cuG1x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2459 = Coupling(name = 'GC_2459',
                   value = '(cuG1x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2460 = Coupling(name = 'GC_2460',
                   value = '(cuG2x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2461 = Coupling(name = 'GC_2461',
                   value = '(cuG2x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2462 = Coupling(name = 'GC_2462',
                   value = '(cuG2x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2463 = Coupling(name = 'GC_2463',
                   value = '(cuG3x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2464 = Coupling(name = 'GC_2464',
                   value = '(cuG3x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2465 = Coupling(name = 'GC_2465',
                   value = '(cuG3x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2466 = Coupling(name = 'GC_2466',
                   value = '(2*cuu1x1x1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2467 = Coupling(name = 'GC_2467',
                   value = '(2*cuu1x2x1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2468 = Coupling(name = 'GC_2468',
                   value = '(2*cuu1x3x1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2469 = Coupling(name = 'GC_2469',
                   value = '(2*cuu2x1x2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2470 = Coupling(name = 'GC_2470',
                   value = '(2*cuu2x2x2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2471 = Coupling(name = 'GC_2471',
                   value = '(2*cuu2x3x2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2472 = Coupling(name = 'GC_2472',
                   value = '(2*cuu3x1x3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2473 = Coupling(name = 'GC_2473',
                   value = '(2*cuu3x2x3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2474 = Coupling(name = 'GC_2474',
                   value = '(2*cuu3x3x3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2475 = Coupling(name = 'GC_2475',
                   value = '(cuW1x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2476 = Coupling(name = 'GC_2476',
                   value = '(cuW1x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2477 = Coupling(name = 'GC_2477',
                   value = '(cuW1x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2478 = Coupling(name = 'GC_2478',
                   value = '(cuW2x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2479 = Coupling(name = 'GC_2479',
                   value = '(cuW2x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2480 = Coupling(name = 'GC_2480',
                   value = '(cuW2x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2481 = Coupling(name = 'GC_2481',
                   value = '(cuW3x1*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2482 = Coupling(name = 'GC_2482',
                   value = '(cuW3x2*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2483 = Coupling(name = 'GC_2483',
                   value = '(cuW3x3*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2484 = Coupling(name = 'GC_2484',
                   value = '(6*cth*cW*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2485 = Coupling(name = 'GC_2485',
                   value = '(2*cth*cWtil*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2486 = Coupling(name = 'GC_2486',
                   value = '(6*cth*cW*ee*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_2487 = Coupling(name = 'GC_2487',
                   value = '(-2*cth*cWtil*ee*complex(0,1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_2488 = Coupling(name = 'GC_2488',
                   value = '(-6*cG*complex(0,1)*G)/LambdaSMEFT**2',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_2489 = Coupling(name = 'GC_2489',
                   value = '(cGtil*complex(0,1)*G)/LambdaSMEFT**2',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_2490 = Coupling(name = 'GC_2490',
                   value = '(ee**2*complex(0,1))/(2.*sth**2)',
                   order = {'QED':2})

GC_2491 = Coupling(name = 'GC_2491',
                   value = '-((ee**2*complex(0,1))/sth**2)',
                   order = {'QED':2})

GC_2492 = Coupling(name = 'GC_2492',
                   value = '(cth**2*ee**2*complex(0,1))/sth**2',
                   order = {'QED':2})

GC_2493 = Coupling(name = 'GC_2493',
                   value = '(-2*dgw*ee**2*complex(0,1))/sth**2',
                   order = {'NP':1,'QED':2})

GC_2494 = Coupling(name = 'GC_2494',
                   value = '-((ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2495 = Coupling(name = 'GC_2495',
                   value = '-((CKM1x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2496 = Coupling(name = 'GC_2496',
                   value = '-((CKM1x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2497 = Coupling(name = 'GC_2497',
                   value = '-((CKM1x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2498 = Coupling(name = 'GC_2498',
                   value = '-((CKM2x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2499 = Coupling(name = 'GC_2499',
                   value = '-((CKM2x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2500 = Coupling(name = 'GC_2500',
                   value = '-((CKM2x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2501 = Coupling(name = 'GC_2501',
                   value = '-((CKM3x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2502 = Coupling(name = 'GC_2502',
                   value = '-((CKM3x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2503 = Coupling(name = 'GC_2503',
                   value = '-((CKM3x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_2504 = Coupling(name = 'GC_2504',
                   value = '-(cth*ee*complex(0,1))/(2.*sth)',
                   order = {'QED':1})

GC_2505 = Coupling(name = 'GC_2505',
                   value = '(cth*ee*complex(0,1))/(2.*sth)',
                   order = {'QED':1})

GC_2506 = Coupling(name = 'GC_2506',
                   value = '-((cth*ee*complex(0,1))/sth)',
                   order = {'QED':1})

GC_2507 = Coupling(name = 'GC_2507',
                   value = '(-2*cth*ee**2*complex(0,1))/sth',
                   order = {'QED':2})

GC_2508 = Coupling(name = 'GC_2508',
                   value = '(6*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_2509 = Coupling(name = 'GC_2509',
                   value = '(-6*cth**2*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_2510 = Coupling(name = 'GC_2510',
                   value = '(-2*cWtil*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_2511 = Coupling(name = 'GC_2511',
                   value = '(2*cth**2*cWtil*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_2512 = Coupling(name = 'GC_2512',
                   value = '(ee*complex(0,1)*sth)/(6.*cth)',
                   order = {'QED':1})

GC_2513 = Coupling(name = 'GC_2513',
                   value = '-(ee*complex(0,1)*sth)/(2.*cth)',
                   order = {'QED':1})

GC_2514 = Coupling(name = 'GC_2514',
                   value = '(6*cW*complex(0,1)*sth)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2515 = Coupling(name = 'GC_2515',
                   value = '(2*cWtil*complex(0,1)*sth)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2516 = Coupling(name = 'GC_2516',
                   value = '(-6*cW*ee*complex(0,1)*sth)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_2517 = Coupling(name = 'GC_2517',
                   value = '(2*cWtil*ee*complex(0,1)*sth)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_2518 = Coupling(name = 'GC_2518',
                   value = '-(cth*ee*complex(0,1))/(2.*sth) - (ee*complex(0,1)*sth)/(2.*cth)',
                   order = {'QED':1})

GC_2519 = Coupling(name = 'GC_2519',
                   value = '-((cdW1x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB1x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2520 = Coupling(name = 'GC_2520',
                   value = '-((cdW1x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB1x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2521 = Coupling(name = 'GC_2521',
                   value = '-((cdW1x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB1x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2522 = Coupling(name = 'GC_2522',
                   value = '-((cdW2x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB2x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2523 = Coupling(name = 'GC_2523',
                   value = '-((cdW2x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB2x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2524 = Coupling(name = 'GC_2524',
                   value = '-((cdW2x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB2x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2525 = Coupling(name = 'GC_2525',
                   value = '-((cdW3x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB3x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2526 = Coupling(name = 'GC_2526',
                   value = '-((cdW3x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB3x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2527 = Coupling(name = 'GC_2527',
                   value = '-((cdW3x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB3x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2528 = Coupling(name = 'GC_2528',
                   value = '(cdB1x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW1x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2529 = Coupling(name = 'GC_2529',
                   value = '(cdB1x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW1x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2530 = Coupling(name = 'GC_2530',
                   value = '(cdB1x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW1x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2531 = Coupling(name = 'GC_2531',
                   value = '(cdB2x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW2x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2532 = Coupling(name = 'GC_2532',
                   value = '(cdB2x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW2x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2533 = Coupling(name = 'GC_2533',
                   value = '(cdB2x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW2x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2534 = Coupling(name = 'GC_2534',
                   value = '(cdB3x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW3x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2535 = Coupling(name = 'GC_2535',
                   value = '(cdB3x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW3x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2536 = Coupling(name = 'GC_2536',
                   value = '(cdB3x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW3x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2537 = Coupling(name = 'GC_2537',
                   value = '-((ceW1x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB1x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2538 = Coupling(name = 'GC_2538',
                   value = '-((ceW1x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB1x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2539 = Coupling(name = 'GC_2539',
                   value = '-((ceW1x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB1x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2540 = Coupling(name = 'GC_2540',
                   value = '-((ceW2x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB2x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2541 = Coupling(name = 'GC_2541',
                   value = '-((ceW2x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB2x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2542 = Coupling(name = 'GC_2542',
                   value = '-((ceW2x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB2x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2543 = Coupling(name = 'GC_2543',
                   value = '-((ceW3x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB3x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2544 = Coupling(name = 'GC_2544',
                   value = '-((ceW3x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB3x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2545 = Coupling(name = 'GC_2545',
                   value = '-((ceW3x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB3x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2546 = Coupling(name = 'GC_2546',
                   value = '(ceB1x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW1x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2547 = Coupling(name = 'GC_2547',
                   value = '(ceB1x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW1x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2548 = Coupling(name = 'GC_2548',
                   value = '(ceB1x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW1x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2549 = Coupling(name = 'GC_2549',
                   value = '(ceB2x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW2x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2550 = Coupling(name = 'GC_2550',
                   value = '(ceB2x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW2x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2551 = Coupling(name = 'GC_2551',
                   value = '(ceB2x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW2x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2552 = Coupling(name = 'GC_2552',
                   value = '(ceB3x1*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW3x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2553 = Coupling(name = 'GC_2553',
                   value = '(ceB3x2*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW3x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2554 = Coupling(name = 'GC_2554',
                   value = '(ceB3x3*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW3x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2555 = Coupling(name = 'GC_2555',
                   value = '(cth*cuW1x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB1x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2556 = Coupling(name = 'GC_2556',
                   value = '(cth*cuW1x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB1x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2557 = Coupling(name = 'GC_2557',
                   value = '(cth*cuW1x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB1x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2558 = Coupling(name = 'GC_2558',
                   value = '(cth*cuW2x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB2x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2559 = Coupling(name = 'GC_2559',
                   value = '(cth*cuW2x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB2x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2560 = Coupling(name = 'GC_2560',
                   value = '(cth*cuW2x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB2x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2561 = Coupling(name = 'GC_2561',
                   value = '(cth*cuW3x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB3x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2562 = Coupling(name = 'GC_2562',
                   value = '(cth*cuW3x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB3x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2563 = Coupling(name = 'GC_2563',
                   value = '(cth*cuW3x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB3x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2564 = Coupling(name = 'GC_2564',
                   value = '(cth*cuB1x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW1x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2565 = Coupling(name = 'GC_2565',
                   value = '(cth*cuB1x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW1x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2566 = Coupling(name = 'GC_2566',
                   value = '(cth*cuB1x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW1x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2567 = Coupling(name = 'GC_2567',
                   value = '(cth*cuB2x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW2x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2568 = Coupling(name = 'GC_2568',
                   value = '(cth*cuB2x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW2x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2569 = Coupling(name = 'GC_2569',
                   value = '(cth*cuB2x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW2x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2570 = Coupling(name = 'GC_2570',
                   value = '(cth*cuB3x1*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW3x1*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2571 = Coupling(name = 'GC_2571',
                   value = '(cth*cuB3x2*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW3x2*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2572 = Coupling(name = 'GC_2572',
                   value = '(cth*cuB3x3*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW3x3*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2573 = Coupling(name = 'GC_2573',
                   value = 'ee**2*complex(0,1) + (cth**2*ee**2*complex(0,1))/(2.*sth**2) + (ee**2*complex(0,1)*sth**2)/(2.*cth**2)',
                   order = {'QED':2})

GC_2574 = Coupling(name = 'GC_2574',
                   value = '(4*cHW*cth**2*complex(0,1))/LambdaSMEFT**2 + (4*cHWB*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (4*cHB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2575 = Coupling(name = 'GC_2575',
                   value = '(-2*cHWtil*cth**2*complex(0,1))/LambdaSMEFT**2 - (2*cHWBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2 - (2*cHBtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2576 = Coupling(name = 'GC_2576',
                   value = '(4*cHB*cth**2*complex(0,1))/LambdaSMEFT**2 - (4*cHWB*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (4*cHW*complex(0,1)*sth**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2577 = Coupling(name = 'GC_2577',
                   value = '(-2*cHWB*cth**2*complex(0,1))/LambdaSMEFT**2 - (4*cHB*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (4*cHW*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (2*cHWB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2578 = Coupling(name = 'GC_2578',
                   value = '(-2*cHWBtil*cth**2*complex(0,1))/LambdaSMEFT**2 - (4*cHBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (4*cHWtil*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (2*cHWBtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2579 = Coupling(name = 'GC_2579',
                   value = '(-2*cHBtil*cth**2*complex(0,1))/LambdaSMEFT**2 + (2*cHWBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2 - (2*cHWtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2580 = Coupling(name = 'GC_2580',
                   value = '(4*complex(0,1)*gHaa)/vevhat',
                   order = {'QED':3,'SMHLOOP':1})

GC_2581 = Coupling(name = 'GC_2581',
                   value = '(4*complex(0,1)*gHgg)/vevhat',
                   order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_2582 = Coupling(name = 'GC_2582',
                   value = '(2*complex(0,1)*gHza)/vevhat',
                   order = {'QED':3,'SMHLOOP':1})

GC_2583 = Coupling(name = 'GC_2583',
                   value = '-6*complex(0,1)*lam*vevhat',
                   order = {'QED':1})

GC_2584 = Coupling(name = 'GC_2584',
                   value = '(cdG1x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2585 = Coupling(name = 'GC_2585',
                   value = '(cdG1x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2586 = Coupling(name = 'GC_2586',
                   value = '(cdG1x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2587 = Coupling(name = 'GC_2587',
                   value = '(cdG2x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2588 = Coupling(name = 'GC_2588',
                   value = '(cdG2x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2589 = Coupling(name = 'GC_2589',
                   value = '(cdG2x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2590 = Coupling(name = 'GC_2590',
                   value = '(cdG3x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2591 = Coupling(name = 'GC_2591',
                   value = '(cdG3x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2592 = Coupling(name = 'GC_2592',
                   value = '(cdG3x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2593 = Coupling(name = 'GC_2593',
                   value = '(3*cdH1x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2594 = Coupling(name = 'GC_2594',
                   value = '(3*cdH1x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2595 = Coupling(name = 'GC_2595',
                   value = '(3*cdH1x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2596 = Coupling(name = 'GC_2596',
                   value = '(3*cdH2x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2597 = Coupling(name = 'GC_2597',
                   value = '(3*cdH2x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2598 = Coupling(name = 'GC_2598',
                   value = '(3*cdH2x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2599 = Coupling(name = 'GC_2599',
                   value = '(3*cdH3x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2600 = Coupling(name = 'GC_2600',
                   value = '(3*cdH3x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2601 = Coupling(name = 'GC_2601',
                   value = '(3*cdH3x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2602 = Coupling(name = 'GC_2602',
                   value = '(cdW1x1*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2603 = Coupling(name = 'GC_2603',
                   value = '(cdW1x2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2604 = Coupling(name = 'GC_2604',
                   value = '(cdW1x3*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2605 = Coupling(name = 'GC_2605',
                   value = '(cdW2x1*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2606 = Coupling(name = 'GC_2606',
                   value = '(cdW2x2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2607 = Coupling(name = 'GC_2607',
                   value = '(cdW2x3*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2608 = Coupling(name = 'GC_2608',
                   value = '(cdW3x1*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2609 = Coupling(name = 'GC_2609',
                   value = '(cdW3x2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2610 = Coupling(name = 'GC_2610',
                   value = '(cdW3x3*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2611 = Coupling(name = 'GC_2611',
                   value = '(3*ceH1x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2612 = Coupling(name = 'GC_2612',
                   value = '(3*ceH1x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2613 = Coupling(name = 'GC_2613',
                   value = '(3*ceH1x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2614 = Coupling(name = 'GC_2614',
                   value = '(3*ceH2x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2615 = Coupling(name = 'GC_2615',
                   value = '(3*ceH2x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2616 = Coupling(name = 'GC_2616',
                   value = '(3*ceH2x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2617 = Coupling(name = 'GC_2617',
                   value = '(3*ceH3x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2618 = Coupling(name = 'GC_2618',
                   value = '(3*ceH3x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2619 = Coupling(name = 'GC_2619',
                   value = '(3*ceH3x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2620 = Coupling(name = 'GC_2620',
                   value = '(ceW1x1*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2621 = Coupling(name = 'GC_2621',
                   value = '(ceW1x2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2622 = Coupling(name = 'GC_2622',
                   value = '(ceW1x3*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2623 = Coupling(name = 'GC_2623',
                   value = '(ceW2x1*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2624 = Coupling(name = 'GC_2624',
                   value = '(ceW2x2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2625 = Coupling(name = 'GC_2625',
                   value = '(ceW2x3*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2626 = Coupling(name = 'GC_2626',
                   value = '(ceW3x1*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2627 = Coupling(name = 'GC_2627',
                   value = '(ceW3x2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2628 = Coupling(name = 'GC_2628',
                   value = '(ceW3x3*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2629 = Coupling(name = 'GC_2629',
                   value = '(-3*cHbox*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2630 = Coupling(name = 'GC_2630',
                   value = '-((cHDD*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2631 = Coupling(name = 'GC_2631',
                   value = '(4*cHG*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2632 = Coupling(name = 'GC_2632',
                   value = '(-2*cHGtil*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2633 = Coupling(name = 'GC_2633',
                   value = '(4*cHW*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2634 = Coupling(name = 'GC_2634',
                   value = '(4*cHWtil*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2635 = Coupling(name = 'GC_2635',
                   value = '(cuG1x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2636 = Coupling(name = 'GC_2636',
                   value = '(cuG1x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2637 = Coupling(name = 'GC_2637',
                   value = '(cuG1x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2638 = Coupling(name = 'GC_2638',
                   value = '(cuG2x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2639 = Coupling(name = 'GC_2639',
                   value = '(cuG2x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2640 = Coupling(name = 'GC_2640',
                   value = '(cuG2x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2641 = Coupling(name = 'GC_2641',
                   value = '(cuG3x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2642 = Coupling(name = 'GC_2642',
                   value = '(cuG3x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2643 = Coupling(name = 'GC_2643',
                   value = '(cuG3x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2644 = Coupling(name = 'GC_2644',
                   value = '(3*cuH1x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2645 = Coupling(name = 'GC_2645',
                   value = '(3*cuH1x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2646 = Coupling(name = 'GC_2646',
                   value = '(3*cuH1x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2647 = Coupling(name = 'GC_2647',
                   value = '(3*cuH2x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2648 = Coupling(name = 'GC_2648',
                   value = '(3*cuH2x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2649 = Coupling(name = 'GC_2649',
                   value = '(3*cuH2x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2650 = Coupling(name = 'GC_2650',
                   value = '(3*cuH3x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2651 = Coupling(name = 'GC_2651',
                   value = '(3*cuH3x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2652 = Coupling(name = 'GC_2652',
                   value = '(3*cuH3x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2653 = Coupling(name = 'GC_2653',
                   value = '(cuW1x1*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2654 = Coupling(name = 'GC_2654',
                   value = '(cuW1x2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2655 = Coupling(name = 'GC_2655',
                   value = '(cuW1x3*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2656 = Coupling(name = 'GC_2656',
                   value = '(cuW2x1*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2657 = Coupling(name = 'GC_2657',
                   value = '(cuW2x2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2658 = Coupling(name = 'GC_2658',
                   value = '(cuW2x3*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2659 = Coupling(name = 'GC_2659',
                   value = '(cuW3x1*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2660 = Coupling(name = 'GC_2660',
                   value = '(cuW3x2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2661 = Coupling(name = 'GC_2661',
                   value = '(cuW3x3*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2662 = Coupling(name = 'GC_2662',
                   value = '-((cdW1x1*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2663 = Coupling(name = 'GC_2663',
                   value = '-((cdW1x2*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2664 = Coupling(name = 'GC_2664',
                   value = '-((cdW1x3*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2665 = Coupling(name = 'GC_2665',
                   value = '-((cdW2x1*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2666 = Coupling(name = 'GC_2666',
                   value = '-((cdW2x2*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2667 = Coupling(name = 'GC_2667',
                   value = '-((cdW2x3*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2668 = Coupling(name = 'GC_2668',
                   value = '-((cdW3x1*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2669 = Coupling(name = 'GC_2669',
                   value = '-((cdW3x2*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2670 = Coupling(name = 'GC_2670',
                   value = '-((cdW3x3*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2671 = Coupling(name = 'GC_2671',
                   value = '-((ceW1x1*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2672 = Coupling(name = 'GC_2672',
                   value = '-((ceW1x2*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2673 = Coupling(name = 'GC_2673',
                   value = '-((ceW1x3*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2674 = Coupling(name = 'GC_2674',
                   value = '-((ceW2x1*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2675 = Coupling(name = 'GC_2675',
                   value = '-((ceW2x2*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2676 = Coupling(name = 'GC_2676',
                   value = '-((ceW2x3*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2677 = Coupling(name = 'GC_2677',
                   value = '-((ceW3x1*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2678 = Coupling(name = 'GC_2678',
                   value = '-((ceW3x2*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2679 = Coupling(name = 'GC_2679',
                   value = '-((ceW3x3*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2680 = Coupling(name = 'GC_2680',
                   value = '(4*cHW*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2681 = Coupling(name = 'GC_2681',
                   value = '(2*cHWB*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2682 = Coupling(name = 'GC_2682',
                   value = '(-2*cHWBtil*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2683 = Coupling(name = 'GC_2683',
                   value = '(-4*cHWtil*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2684 = Coupling(name = 'GC_2684',
                   value = '(cuW1x1*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2685 = Coupling(name = 'GC_2685',
                   value = '(cuW1x2*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2686 = Coupling(name = 'GC_2686',
                   value = '(cuW1x3*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2687 = Coupling(name = 'GC_2687',
                   value = '(cuW2x1*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2688 = Coupling(name = 'GC_2688',
                   value = '(cuW2x2*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2689 = Coupling(name = 'GC_2689',
                   value = '(cuW2x3*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2690 = Coupling(name = 'GC_2690',
                   value = '(cuW3x1*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2691 = Coupling(name = 'GC_2691',
                   value = '(cuW3x2*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2692 = Coupling(name = 'GC_2692',
                   value = '(cuW3x3*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2693 = Coupling(name = 'GC_2693',
                   value = '(cdG1x1*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2694 = Coupling(name = 'GC_2694',
                   value = '(cdG1x2*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2695 = Coupling(name = 'GC_2695',
                   value = '(cdG1x3*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2696 = Coupling(name = 'GC_2696',
                   value = '(cdG2x1*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2697 = Coupling(name = 'GC_2697',
                   value = '(cdG2x2*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2698 = Coupling(name = 'GC_2698',
                   value = '(cdG2x3*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2699 = Coupling(name = 'GC_2699',
                   value = '(cdG3x1*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2700 = Coupling(name = 'GC_2700',
                   value = '(cdG3x2*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2701 = Coupling(name = 'GC_2701',
                   value = '(cdG3x3*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2702 = Coupling(name = 'GC_2702',
                   value = '(-4*cHG*G*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2703 = Coupling(name = 'GC_2703',
                   value = '(4*cHGtil*G*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2704 = Coupling(name = 'GC_2704',
                   value = '(cuG1x1*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2705 = Coupling(name = 'GC_2705',
                   value = '(cuG1x2*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2706 = Coupling(name = 'GC_2706',
                   value = '(cuG1x3*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2707 = Coupling(name = 'GC_2707',
                   value = '(cuG2x1*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2708 = Coupling(name = 'GC_2708',
                   value = '(cuG2x2*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2709 = Coupling(name = 'GC_2709',
                   value = '(cuG2x3*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2710 = Coupling(name = 'GC_2710',
                   value = '(cuG3x1*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2711 = Coupling(name = 'GC_2711',
                   value = '(cuG3x2*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2712 = Coupling(name = 'GC_2712',
                   value = '(cuG3x3*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_2713 = Coupling(name = 'GC_2713',
                   value = '(ee**2*complex(0,1)*vevhat)/(2.*sth**2)',
                   order = {'QED':1})

GC_2714 = Coupling(name = 'GC_2714',
                   value = '(cdW1x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2715 = Coupling(name = 'GC_2715',
                   value = '(cdW1x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2716 = Coupling(name = 'GC_2716',
                   value = '(cdW1x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2717 = Coupling(name = 'GC_2717',
                   value = '(cdW2x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2718 = Coupling(name = 'GC_2718',
                   value = '(cdW2x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2719 = Coupling(name = 'GC_2719',
                   value = '(cdW2x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2720 = Coupling(name = 'GC_2720',
                   value = '(cdW3x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2721 = Coupling(name = 'GC_2721',
                   value = '(cdW3x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2722 = Coupling(name = 'GC_2722',
                   value = '(cdW3x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2723 = Coupling(name = 'GC_2723',
                   value = '(ceW1x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2724 = Coupling(name = 'GC_2724',
                   value = '(ceW1x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2725 = Coupling(name = 'GC_2725',
                   value = '(ceW1x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2726 = Coupling(name = 'GC_2726',
                   value = '(ceW2x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2727 = Coupling(name = 'GC_2727',
                   value = '(ceW2x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2728 = Coupling(name = 'GC_2728',
                   value = '(ceW2x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2729 = Coupling(name = 'GC_2729',
                   value = '(ceW3x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2730 = Coupling(name = 'GC_2730',
                   value = '(ceW3x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2731 = Coupling(name = 'GC_2731',
                   value = '(ceW3x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2732 = Coupling(name = 'GC_2732',
                   value = '-((cHl31x1*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2733 = Coupling(name = 'GC_2733',
                   value = '-((cHl31x2*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2734 = Coupling(name = 'GC_2734',
                   value = '-((cHl31x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2735 = Coupling(name = 'GC_2735',
                   value = '-((cHl32x2*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2736 = Coupling(name = 'GC_2736',
                   value = '-((cHl32x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2737 = Coupling(name = 'GC_2737',
                   value = '-((cHl33x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2738 = Coupling(name = 'GC_2738',
                   value = '-((cHq31x1*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2739 = Coupling(name = 'GC_2739',
                   value = '-((cHq31x2*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2740 = Coupling(name = 'GC_2740',
                   value = '-((cHq31x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2741 = Coupling(name = 'GC_2741',
                   value = '-((cHq32x2*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2742 = Coupling(name = 'GC_2742',
                   value = '-((cHq32x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2743 = Coupling(name = 'GC_2743',
                   value = '-((cHq33x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2744 = Coupling(name = 'GC_2744',
                   value = '(cHud1x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2745 = Coupling(name = 'GC_2745',
                   value = '(cHud1x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2746 = Coupling(name = 'GC_2746',
                   value = '(cHud1x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2747 = Coupling(name = 'GC_2747',
                   value = '(cHud2x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2748 = Coupling(name = 'GC_2748',
                   value = '(cHud2x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2749 = Coupling(name = 'GC_2749',
                   value = '(cHud2x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2750 = Coupling(name = 'GC_2750',
                   value = '(cHud3x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2751 = Coupling(name = 'GC_2751',
                   value = '(cHud3x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2752 = Coupling(name = 'GC_2752',
                   value = '(cHud3x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_2753 = Coupling(name = 'GC_2753',
                   value = '(cdW1x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2754 = Coupling(name = 'GC_2754',
                   value = '(cdW1x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2755 = Coupling(name = 'GC_2755',
                   value = '(cdW1x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2756 = Coupling(name = 'GC_2756',
                   value = '(cdW2x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2757 = Coupling(name = 'GC_2757',
                   value = '(cdW2x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2758 = Coupling(name = 'GC_2758',
                   value = '(cdW2x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2759 = Coupling(name = 'GC_2759',
                   value = '(cdW3x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2760 = Coupling(name = 'GC_2760',
                   value = '(cdW3x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2761 = Coupling(name = 'GC_2761',
                   value = '(cdW3x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2762 = Coupling(name = 'GC_2762',
                   value = '(ceW1x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2763 = Coupling(name = 'GC_2763',
                   value = '(ceW1x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2764 = Coupling(name = 'GC_2764',
                   value = '(ceW1x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2765 = Coupling(name = 'GC_2765',
                   value = '(ceW2x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2766 = Coupling(name = 'GC_2766',
                   value = '(ceW2x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2767 = Coupling(name = 'GC_2767',
                   value = '(ceW2x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2768 = Coupling(name = 'GC_2768',
                   value = '(ceW3x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2769 = Coupling(name = 'GC_2769',
                   value = '(ceW3x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2770 = Coupling(name = 'GC_2770',
                   value = '(ceW3x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2771 = Coupling(name = 'GC_2771',
                   value = '(4*cHW*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2772 = Coupling(name = 'GC_2772',
                   value = '(-2*cHWB*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2773 = Coupling(name = 'GC_2773',
                   value = '(2*cHWBtil*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2774 = Coupling(name = 'GC_2774',
                   value = '(-4*cHWtil*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_2775 = Coupling(name = 'GC_2775',
                   value = '-((cuW1x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_2776 = Coupling(name = 'GC_2776',
                   value = '-((cth*cuW1x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2777 = Coupling(name = 'GC_2777',
                   value = '-((cuW1x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_2778 = Coupling(name = 'GC_2778',
                   value = '-((cth*cuW1x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2779 = Coupling(name = 'GC_2779',
                   value = '-((cuW1x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_2780 = Coupling(name = 'GC_2780',
                   value = '-((cth*cuW1x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2781 = Coupling(name = 'GC_2781',
                   value = '-((cuW2x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_2782 = Coupling(name = 'GC_2782',
                   value = '-((cth*cuW2x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2783 = Coupling(name = 'GC_2783',
                   value = '-((cuW2x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_2784 = Coupling(name = 'GC_2784',
                   value = '-((cth*cuW2x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2785 = Coupling(name = 'GC_2785',
                   value = '-((cuW2x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_2786 = Coupling(name = 'GC_2786',
                   value = '-((cth*cuW2x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2787 = Coupling(name = 'GC_2787',
                   value = '-((cuW3x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_2788 = Coupling(name = 'GC_2788',
                   value = '-((cth*cuW3x1*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2789 = Coupling(name = 'GC_2789',
                   value = '-((cuW3x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_2790 = Coupling(name = 'GC_2790',
                   value = '-((cth*cuW3x2*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2791 = Coupling(name = 'GC_2791',
                   value = '-((cuW3x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_2792 = Coupling(name = 'GC_2792',
                   value = '-((cth*cuW3x3*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_2793 = Coupling(name = 'GC_2793',
                   value = '(cdH1x1*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2794 = Coupling(name = 'GC_2794',
                   value = '(cdH1x2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2795 = Coupling(name = 'GC_2795',
                   value = '(cdH1x3*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2796 = Coupling(name = 'GC_2796',
                   value = '(cdH2x1*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2797 = Coupling(name = 'GC_2797',
                   value = '(cdH2x2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2798 = Coupling(name = 'GC_2798',
                   value = '(cdH2x3*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2799 = Coupling(name = 'GC_2799',
                   value = '(cdH3x1*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2800 = Coupling(name = 'GC_2800',
                   value = '(cdH3x2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2801 = Coupling(name = 'GC_2801',
                   value = '(cdH3x3*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2802 = Coupling(name = 'GC_2802',
                   value = '(ceH1x1*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2803 = Coupling(name = 'GC_2803',
                   value = '(ceH1x2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2804 = Coupling(name = 'GC_2804',
                   value = '(ceH1x3*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2805 = Coupling(name = 'GC_2805',
                   value = '(ceH2x1*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2806 = Coupling(name = 'GC_2806',
                   value = '(ceH2x2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2807 = Coupling(name = 'GC_2807',
                   value = '(ceH2x3*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2808 = Coupling(name = 'GC_2808',
                   value = '(ceH3x1*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2809 = Coupling(name = 'GC_2809',
                   value = '(ceH3x2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2810 = Coupling(name = 'GC_2810',
                   value = '(ceH3x3*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2811 = Coupling(name = 'GC_2811',
                   value = '(45*cH*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1})

GC_2812 = Coupling(name = 'GC_2812',
                   value = '(cuH1x1*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2813 = Coupling(name = 'GC_2813',
                   value = '(cuH1x2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2814 = Coupling(name = 'GC_2814',
                   value = '(cuH1x3*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2815 = Coupling(name = 'GC_2815',
                   value = '(cuH2x1*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2816 = Coupling(name = 'GC_2816',
                   value = '(cuH2x2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2817 = Coupling(name = 'GC_2817',
                   value = '(cuH2x3*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2818 = Coupling(name = 'GC_2818',
                   value = '(cuH3x1*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2819 = Coupling(name = 'GC_2819',
                   value = '(cuH3x2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2820 = Coupling(name = 'GC_2820',
                   value = '(cuH3x3*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_2821 = Coupling(name = 'GC_2821',
                   value = '(cHWB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2822 = Coupling(name = 'GC_2822',
                   value = '-((cHWBtil*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2823 = Coupling(name = 'GC_2823',
                   value = '(-2*cHWtil*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2824 = Coupling(name = 'GC_2824',
                   value = '(2*cHGtil*G*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QCD':1})

GC_2825 = Coupling(name = 'GC_2825',
                   value = '-((cHl31x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':1})

GC_2826 = Coupling(name = 'GC_2826',
                   value = '-((cHl31x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':1})

GC_2827 = Coupling(name = 'GC_2827',
                   value = '-((cHl32x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':1})

GC_2828 = Coupling(name = 'GC_2828',
                   value = '(cHud1x1*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2829 = Coupling(name = 'GC_2829',
                   value = '(cHud1x2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2830 = Coupling(name = 'GC_2830',
                   value = '(cHud1x3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2831 = Coupling(name = 'GC_2831',
                   value = '(cHud2x1*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2832 = Coupling(name = 'GC_2832',
                   value = '(cHud2x2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2833 = Coupling(name = 'GC_2833',
                   value = '(cHud2x3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2834 = Coupling(name = 'GC_2834',
                   value = '(cHud3x1*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2835 = Coupling(name = 'GC_2835',
                   value = '(cHud3x2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2836 = Coupling(name = 'GC_2836',
                   value = '(cHud3x3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2837 = Coupling(name = 'GC_2837',
                   value = '-(cHWB*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':1})

GC_2838 = Coupling(name = 'GC_2838',
                   value = '(cHWBtil*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':1})

GC_2839 = Coupling(name = 'GC_2839',
                   value = '(-2*cHWtil*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':1})

GC_2840 = Coupling(name = 'GC_2840',
                   value = '(15*cH*complex(0,1)*vevhat**3)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':-1})

GC_2841 = Coupling(name = 'GC_2841',
                   value = '-((cdW1x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB1x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2842 = Coupling(name = 'GC_2842',
                   value = '-((cdW1x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB1x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2843 = Coupling(name = 'GC_2843',
                   value = '-((cdW1x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB1x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2844 = Coupling(name = 'GC_2844',
                   value = '-((cdW2x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB2x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2845 = Coupling(name = 'GC_2845',
                   value = '-((cdW2x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB2x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2846 = Coupling(name = 'GC_2846',
                   value = '-((cdW2x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB2x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2847 = Coupling(name = 'GC_2847',
                   value = '-((cdW3x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB3x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2848 = Coupling(name = 'GC_2848',
                   value = '-((cdW3x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB3x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2849 = Coupling(name = 'GC_2849',
                   value = '-((cdW3x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB3x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2850 = Coupling(name = 'GC_2850',
                   value = '(cdB1x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW1x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2851 = Coupling(name = 'GC_2851',
                   value = '(cdB1x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW1x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2852 = Coupling(name = 'GC_2852',
                   value = '(cdB1x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW1x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2853 = Coupling(name = 'GC_2853',
                   value = '(cdB2x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW2x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2854 = Coupling(name = 'GC_2854',
                   value = '(cdB2x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW2x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2855 = Coupling(name = 'GC_2855',
                   value = '(cdB2x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW2x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2856 = Coupling(name = 'GC_2856',
                   value = '(cdB3x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW3x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2857 = Coupling(name = 'GC_2857',
                   value = '(cdB3x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW3x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2858 = Coupling(name = 'GC_2858',
                   value = '(cdB3x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW3x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2859 = Coupling(name = 'GC_2859',
                   value = '-((ceW1x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB1x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2860 = Coupling(name = 'GC_2860',
                   value = '-((ceW1x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB1x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2861 = Coupling(name = 'GC_2861',
                   value = '-((ceW1x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB1x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2862 = Coupling(name = 'GC_2862',
                   value = '-((ceW2x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB2x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2863 = Coupling(name = 'GC_2863',
                   value = '-((ceW2x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB2x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2864 = Coupling(name = 'GC_2864',
                   value = '-((ceW2x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB2x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2865 = Coupling(name = 'GC_2865',
                   value = '-((ceW3x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB3x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2866 = Coupling(name = 'GC_2866',
                   value = '-((ceW3x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB3x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2867 = Coupling(name = 'GC_2867',
                   value = '-((ceW3x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB3x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2868 = Coupling(name = 'GC_2868',
                   value = '(ceB1x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW1x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2869 = Coupling(name = 'GC_2869',
                   value = '(ceB1x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW1x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2870 = Coupling(name = 'GC_2870',
                   value = '(ceB1x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW1x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2871 = Coupling(name = 'GC_2871',
                   value = '(ceB2x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW2x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2872 = Coupling(name = 'GC_2872',
                   value = '(ceB2x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW2x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2873 = Coupling(name = 'GC_2873',
                   value = '(ceB2x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW2x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2874 = Coupling(name = 'GC_2874',
                   value = '(ceB3x1*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW3x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2875 = Coupling(name = 'GC_2875',
                   value = '(ceB3x2*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW3x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2876 = Coupling(name = 'GC_2876',
                   value = '(ceB3x3*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW3x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2877 = Coupling(name = 'GC_2877',
                   value = '(cth*cuW1x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB1x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2878 = Coupling(name = 'GC_2878',
                   value = '(cth*cuW1x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB1x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2879 = Coupling(name = 'GC_2879',
                   value = '(cth*cuW1x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB1x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2880 = Coupling(name = 'GC_2880',
                   value = '(cth*cuW2x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB2x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2881 = Coupling(name = 'GC_2881',
                   value = '(cth*cuW2x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB2x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2882 = Coupling(name = 'GC_2882',
                   value = '(cth*cuW2x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB2x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2883 = Coupling(name = 'GC_2883',
                   value = '(cth*cuW3x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB3x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2884 = Coupling(name = 'GC_2884',
                   value = '(cth*cuW3x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB3x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2885 = Coupling(name = 'GC_2885',
                   value = '(cth*cuW3x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB3x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2886 = Coupling(name = 'GC_2886',
                   value = '(cth*cuB1x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW1x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2887 = Coupling(name = 'GC_2887',
                   value = '(cth*cuB1x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW1x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2888 = Coupling(name = 'GC_2888',
                   value = '(cth*cuB1x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW1x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2889 = Coupling(name = 'GC_2889',
                   value = '(cth*cuB2x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW2x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2890 = Coupling(name = 'GC_2890',
                   value = '(cth*cuB2x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW2x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2891 = Coupling(name = 'GC_2891',
                   value = '(cth*cuB2x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW2x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2892 = Coupling(name = 'GC_2892',
                   value = '(cth*cuB3x1*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW3x1*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2893 = Coupling(name = 'GC_2893',
                   value = '(cth*cuB3x2*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW3x2*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2894 = Coupling(name = 'GC_2894',
                   value = '(cth*cuB3x3*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW3x3*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2895 = Coupling(name = 'GC_2895',
                   value = '(cHd1x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHd1x1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2896 = Coupling(name = 'GC_2896',
                   value = '(cHd1x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHd1x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2897 = Coupling(name = 'GC_2897',
                   value = '(cHd1x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHd1x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2898 = Coupling(name = 'GC_2898',
                   value = '(cHd2x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHd2x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2899 = Coupling(name = 'GC_2899',
                   value = '(cHd2x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHd2x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2900 = Coupling(name = 'GC_2900',
                   value = '(cHd3x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHd3x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2901 = Coupling(name = 'GC_2901',
                   value = '(cHe1x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHe1x1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2902 = Coupling(name = 'GC_2902',
                   value = '(cHe1x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHe1x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2903 = Coupling(name = 'GC_2903',
                   value = '(cHe1x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHe1x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2904 = Coupling(name = 'GC_2904',
                   value = '(cHe2x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHe2x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2905 = Coupling(name = 'GC_2905',
                   value = '(cHe2x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHe2x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2906 = Coupling(name = 'GC_2906',
                   value = '(cHe3x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHe3x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2907 = Coupling(name = 'GC_2907',
                   value = '(cHl11x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHl31x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl11x1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHl31x1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2908 = Coupling(name = 'GC_2908',
                   value = '(cHl11x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl31x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl11x1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHl31x1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2909 = Coupling(name = 'GC_2909',
                   value = '(cHl11x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHl31x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl11x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHl31x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2910 = Coupling(name = 'GC_2910',
                   value = '(cHl11x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl31x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl11x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHl31x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2911 = Coupling(name = 'GC_2911',
                   value = '(cHl11x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHl31x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl11x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHl31x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2912 = Coupling(name = 'GC_2912',
                   value = '(cHl11x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl31x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl11x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHl31x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2913 = Coupling(name = 'GC_2913',
                   value = '(cHl12x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHl32x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl12x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHl32x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2914 = Coupling(name = 'GC_2914',
                   value = '(cHl12x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl32x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl12x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHl32x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2915 = Coupling(name = 'GC_2915',
                   value = '(cHl12x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHl32x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl12x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHl32x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2916 = Coupling(name = 'GC_2916',
                   value = '(cHl12x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl32x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl12x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHl32x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2917 = Coupling(name = 'GC_2917',
                   value = '(cHl13x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHl33x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl13x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHl33x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2918 = Coupling(name = 'GC_2918',
                   value = '(cHl13x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl33x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl13x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHl33x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2919 = Coupling(name = 'GC_2919',
                   value = '(cHq11x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHq31x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq11x1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHq31x1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2920 = Coupling(name = 'GC_2920',
                   value = '(cHq11x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq31x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq11x1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHq31x1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2921 = Coupling(name = 'GC_2921',
                   value = '(cHq11x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHq31x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq11x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHq31x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2922 = Coupling(name = 'GC_2922',
                   value = '(cHq11x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq31x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq11x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHq31x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2923 = Coupling(name = 'GC_2923',
                   value = '(cHq11x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHq31x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq11x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHq31x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2924 = Coupling(name = 'GC_2924',
                   value = '(cHq11x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq31x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq11x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHq31x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2925 = Coupling(name = 'GC_2925',
                   value = '(cHq12x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHq32x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq12x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHq32x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2926 = Coupling(name = 'GC_2926',
                   value = '(cHq12x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq32x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq12x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHq32x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2927 = Coupling(name = 'GC_2927',
                   value = '(cHq12x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHq32x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq12x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHq32x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2928 = Coupling(name = 'GC_2928',
                   value = '(cHq12x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq32x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq12x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHq32x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2929 = Coupling(name = 'GC_2929',
                   value = '(cHq13x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHq33x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq13x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHq33x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2930 = Coupling(name = 'GC_2930',
                   value = '(cHq13x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq33x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq13x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHq33x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2931 = Coupling(name = 'GC_2931',
                   value = '(cHu1x1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHu1x1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2932 = Coupling(name = 'GC_2932',
                   value = '(cHu1x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHu1x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2933 = Coupling(name = 'GC_2933',
                   value = '(cHu1x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHu1x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2934 = Coupling(name = 'GC_2934',
                   value = '(cHu2x2*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHu2x2*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2935 = Coupling(name = 'GC_2935',
                   value = '(cHu2x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHu2x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2936 = Coupling(name = 'GC_2936',
                   value = '(cHu3x3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHu3x3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_2937 = Coupling(name = 'GC_2937',
                   value = 'ee**2*complex(0,1)*vevhat + (cth**2*ee**2*complex(0,1)*vevhat)/(2.*sth**2) + (ee**2*complex(0,1)*sth**2*vevhat)/(2.*cth**2)',
                   order = {'QED':1})

GC_2938 = Coupling(name = 'GC_2938',
                   value = '(4*cHW*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 + (4*cHWB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (4*cHB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2939 = Coupling(name = 'GC_2939',
                   value = '(-2*cHWtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 - (2*cHWBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 - (2*cHBtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2940 = Coupling(name = 'GC_2940',
                   value = '(4*cHB*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 - (4*cHWB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (4*cHW*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2941 = Coupling(name = 'GC_2941',
                   value = '(-2*cHWB*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 - (4*cHB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (4*cHW*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (2*cHWB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2942 = Coupling(name = 'GC_2942',
                   value = '(-2*cHWBtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 - (4*cHBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (4*cHWtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (2*cHWBtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2943 = Coupling(name = 'GC_2943',
                   value = '(-2*cHBtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 + (2*cHWBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 - (2*cHWtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2944 = Coupling(name = 'GC_2944',
                   value = '-(dsth2*ee*complex(0,1))/(6.*cth*sth) - (cHWB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2945 = Coupling(name = 'GC_2945',
                   value = '(dsth2*ee*complex(0,1))/(3.*cth*sth) + (cHWB*ee*complex(0,1)*vevhat**2)/(3.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2946 = Coupling(name = 'GC_2946',
                   value = '-(dsth2*ee*complex(0,1))/(2.*cth*sth) - (cHWB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2947 = Coupling(name = 'GC_2947',
                   value = '(6*dMH2*complex(0,1)*lam)/MH**2 - (24*cHbox*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2 + (6*cHDD*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2 + 6*dGf*complex(0,1)*lam*cmath.sqrt(2)',
                   order = {'NP':1,'QED':2})

GC_2948 = Coupling(name = 'GC_2948',
                   value = '(dgw*ee**2*complex(0,1))/sth**2 + (cHbox*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) - (cHDD*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth**2)',
                   order = {'NP':1,'QED':2})

GC_2949 = Coupling(name = 'GC_2949',
                   value = '-((dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHl31x1*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2950 = Coupling(name = 'GC_2950',
                   value = '-((dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHl32x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2951 = Coupling(name = 'GC_2951',
                   value = '-((dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHl33x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2952 = Coupling(name = 'GC_2952',
                   value = '-((CKM1x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq31x1*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2953 = Coupling(name = 'GC_2953',
                   value = '-((CKM1x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq31x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2954 = Coupling(name = 'GC_2954',
                   value = '-((CKM1x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq31x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2955 = Coupling(name = 'GC_2955',
                   value = '-((CKM2x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq32x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2956 = Coupling(name = 'GC_2956',
                   value = '-((CKM2x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq32x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2957 = Coupling(name = 'GC_2957',
                   value = '-((CKM3x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq33x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2958 = Coupling(name = 'GC_2958',
                   value = '(cHd1x1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHd1x1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2959 = Coupling(name = 'GC_2959',
                   value = '(cHd1x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHd1x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2960 = Coupling(name = 'GC_2960',
                   value = '(cHd1x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHd1x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2961 = Coupling(name = 'GC_2961',
                   value = '(cHd2x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHd2x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2962 = Coupling(name = 'GC_2962',
                   value = '(cHd2x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHd2x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2963 = Coupling(name = 'GC_2963',
                   value = '(cHd3x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHd3x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2964 = Coupling(name = 'GC_2964',
                   value = '(cHe1x1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHe1x1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2965 = Coupling(name = 'GC_2965',
                   value = '(cHe1x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHe1x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2966 = Coupling(name = 'GC_2966',
                   value = '(cHe1x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHe1x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2967 = Coupling(name = 'GC_2967',
                   value = '(cHe2x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHe2x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2968 = Coupling(name = 'GC_2968',
                   value = '(cHe2x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHe2x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2969 = Coupling(name = 'GC_2969',
                   value = '(cHe3x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHe3x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2970 = Coupling(name = 'GC_2970',
                   value = '(cHl11x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHl31x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl11x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHl31x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2971 = Coupling(name = 'GC_2971',
                   value = '(cHl11x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl31x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl11x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl31x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2972 = Coupling(name = 'GC_2972',
                   value = '(cHl11x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHl31x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl11x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHl31x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2973 = Coupling(name = 'GC_2973',
                   value = '(cHl11x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl31x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl11x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl31x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2974 = Coupling(name = 'GC_2974',
                   value = '(cHl12x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHl32x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl12x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHl32x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2975 = Coupling(name = 'GC_2975',
                   value = '(cHl12x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl32x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl12x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl32x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2976 = Coupling(name = 'GC_2976',
                   value = '(cHq11x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHq31x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq11x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHq31x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2977 = Coupling(name = 'GC_2977',
                   value = '(cHq11x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq31x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq11x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHq31x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2978 = Coupling(name = 'GC_2978',
                   value = '(cHq11x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHq31x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq11x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHq31x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2979 = Coupling(name = 'GC_2979',
                   value = '(cHq11x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq31x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq11x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHq31x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2980 = Coupling(name = 'GC_2980',
                   value = '(cHq12x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHq32x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq12x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHq32x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2981 = Coupling(name = 'GC_2981',
                   value = '(cHq12x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq32x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq12x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHq32x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2982 = Coupling(name = 'GC_2982',
                   value = '(cHu1x1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHu1x1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2983 = Coupling(name = 'GC_2983',
                   value = '(cHu1x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHu1x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2984 = Coupling(name = 'GC_2984',
                   value = '(cHu1x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHu1x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2985 = Coupling(name = 'GC_2985',
                   value = '(cHu2x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHu2x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2986 = Coupling(name = 'GC_2986',
                   value = '(cHu2x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHu2x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2987 = Coupling(name = 'GC_2987',
                   value = '(cHu3x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHu3x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2988 = Coupling(name = 'GC_2988',
                   value = '(2*cth**2*dgw*ee**2*complex(0,1))/sth**2 - (dsth2*ee**2*complex(0,1))/sth**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (2*cHW*cth**4*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) - (cHWB*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHWB*cth**3*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_2989 = Coupling(name = 'GC_2989',
                   value = '-(dgw*ee*complex(0,1))/2. - (dsth2*ee*complex(0,1))/(4.*sth**2) + (cHW*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*cth*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth) - (cHW*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2990 = Coupling(name = 'GC_2990',
                   value = '(dgw*ee*complex(0,1))/2. + (dsth2*ee*complex(0,1))/(4.*sth**2) - (cHW*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHW*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*cth*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth) + (cHW*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2991 = Coupling(name = 'GC_2991',
                   value = '-(dgw*ee*complex(0,1)) - (dsth2*ee*complex(0,1))/(2.*sth**2) + (cHW*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (cHW*cth**2*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (cHW*ee*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_2992 = Coupling(name = 'GC_2992',
                   value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq11x1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHq31x1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq11x1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHq31x1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2993 = Coupling(name = 'GC_2993',
                   value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq12x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHq32x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq12x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHq32x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2994 = Coupling(name = 'GC_2994',
                   value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq13x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHq33x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq13x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHq33x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2995 = Coupling(name = 'GC_2995',
                   value = '(cth*dgw*ee*complex(0,1))/(2.*sth) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHl11x1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl31x1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl11x1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl31x1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2996 = Coupling(name = 'GC_2996',
                   value = '(cth*dgw*ee*complex(0,1))/(2.*sth) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHl12x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl32x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl12x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl32x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2997 = Coupling(name = 'GC_2997',
                   value = '(cth*dgw*ee*complex(0,1))/(2.*sth) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHl13x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl33x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl13x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl33x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2998 = Coupling(name = 'GC_2998',
                   value = '(cth*dgw*ee*complex(0,1))/(2.*sth) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq11x1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq31x1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq11x1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHq31x1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_2999 = Coupling(name = 'GC_2999',
                   value = '(cth*dgw*ee*complex(0,1))/(2.*sth) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq12x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq32x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq12x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHq32x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3000 = Coupling(name = 'GC_3000',
                   value = '(cth*dgw*ee*complex(0,1))/(2.*sth) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq13x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq33x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq13x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHq33x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3001 = Coupling(name = 'GC_3001',
                   value = '-((cth*dgw*ee*complex(0,1))/sth) + (dsth2*ee*complex(0,1))/(2.*cth*sth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHW*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3002 = Coupling(name = 'GC_3002',
                   value = '2*dgw*ee**2*complex(0,1) + (dsth2*ee**2*complex(0,1))/sth**2 - (2*cHW*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (cHWB*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHW*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3003 = Coupling(name = 'GC_3003',
                   value = '-((cth*dsth2*ee**2*complex(0,1))/sth**3) - (4*cth*dgw*ee**2*complex(0,1))/sth + (dsth2*ee**2*complex(0,1))/(cth*sth) + (cHWB*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (2*cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (4*cHW*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (4*cHW*cth**3*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (4*cHW*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 - (2*cHWB*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3004 = Coupling(name = 'GC_3004',
                   value = '(dg1*ee*complex(0,1)*sth)/(6.*cth) - (cHB*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2) + (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(6.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(6.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3005 = Coupling(name = 'GC_3005',
                   value = '-(dg1*ee*complex(0,1)*sth)/(2.*cth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3006 = Coupling(name = 'GC_3006',
                   value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) - (dg1*ee*complex(0,1)*sth)/(2.*cth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHl11x1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHl31x1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl11x1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHl31x1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3007 = Coupling(name = 'GC_3007',
                   value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) - (dg1*ee*complex(0,1)*sth)/(2.*cth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHl12x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHl32x2*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl12x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHl32x2*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3008 = Coupling(name = 'GC_3008',
                   value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) - (dg1*ee*complex(0,1)*sth)/(2.*cth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHl13x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHl33x3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl13x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHl33x3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3009 = Coupling(name = 'GC_3009',
                   value = '-(dg1*ee*complex(0,1))/6. + (dsth2*ee*complex(0,1))/(12.*cth**2) + (cHB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) - (cHB*cth**2*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth*vevhat**2)/(12.*cth*LambdaSMEFT**2) + (cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(6.*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**2*vevhat**2)/(6.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**3*vevhat**2)/(6.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3010 = Coupling(name = 'GC_3010',
                   value = '(dg1*ee*complex(0,1))/2. - (dsth2*ee*complex(0,1))/(4.*cth**2) - (cHB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth*vevhat**2)/(4.*cth*LambdaSMEFT**2) - (cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3011 = Coupling(name = 'GC_3011',
                   value = '(dg1*ee*complex(0,1))/2. - (dgw*ee*complex(0,1))/2. - (dsth2*ee*complex(0,1))/(4.*cth**2) - (dsth2*ee*complex(0,1))/(4.*sth**2) - (cHB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHW*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*cth*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth) + (cHWB*ee*complex(0,1)*sth*vevhat**2)/(4.*cth*LambdaSMEFT**2) - (cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3012 = Coupling(name = 'GC_3012',
                   value = 'dg1*ee**2*complex(0,1) + dgw*ee**2*complex(0,1) + (cth**2*dgw*ee**2*complex(0,1))/sth**2 + (dg1*ee**2*complex(0,1)*sth**2)/cth**2 - (cHB*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (2*cHbox*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (5*cHDD*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHB*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHbox*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (5*cHDD*cth**2*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth**2) - (cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (cHW*cth**4*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (cHWB*cth**3*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 + (2*cHB*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2 + (cHW*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2 - (cHB*ee**2*complex(0,1)*sth**2*vevhat**2)/(cth**2*LambdaSMEFT**2) + (cHbox*ee**2*complex(0,1)*sth**2*vevhat**2)/(cth**2*LambdaSMEFT**2) + (5*cHDD*ee**2*complex(0,1)*sth**2*vevhat**2)/(4.*cth**2*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**3*vevhat**2)/(cth*LambdaSMEFT**2) + (cHB*ee**2*complex(0,1)*sth**4*vevhat**2)/(cth**2*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3013 = Coupling(name = 'GC_3013',
                   value = '(cth*dsth2*ee**2*complex(0,1))/(4.*sth**3) - (cth*dg1*ee**2*complex(0,1))/(2.*sth) + (cth*dgw*ee**2*complex(0,1))/(2.*sth) + (dsth2*ee**2*complex(0,1))/(2.*cth*sth) - (dg1*ee**2*complex(0,1)*sth)/(2.*cth) + (dgw*ee**2*complex(0,1)*sth)/(2.*cth) + (dsth2*ee**2*complex(0,1)*sth)/(4.*cth**3) - (cHWB*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth**2) + (cHB*cth*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHB*cth**3*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee**2*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 + (cHW*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 + (cHWB*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2 - (cHWB*ee**2*complex(0,1)*sth**2*vevhat**2)/(4.*cth**2*LambdaSMEFT**2) - (cHB*ee**2*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHW*ee**2*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**4*vevhat**2)/(2.*cth**2*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3014 = Coupling(name = 'GC_3014',
                   value = '(6*dMH2*complex(0,1)*lam*vevhat)/MH**2 - (18*cHbox*complex(0,1)*lam*vevhat**3)/LambdaSMEFT**2 + (9*cHDD*complex(0,1)*lam*vevhat**3)/(2.*LambdaSMEFT**2) + 3*dGf*complex(0,1)*lam*vevhat*cmath.sqrt(2)',
                   order = {'NP':1,'QED':1})

GC_3015 = Coupling(name = 'GC_3015',
                   value = '(dgw*ee**2*complex(0,1)*vevhat)/sth**2 + (cHbox*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth**2) - (cHDD*ee**2*complex(0,1)*vevhat**3)/(8.*LambdaSMEFT**2*sth**2) + (dGf*ee**2*complex(0,1)*vevhat)/(2.*sth**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3016 = Coupling(name = 'GC_3016',
                   value = 'dg1*ee**2*complex(0,1)*vevhat + dgw*ee**2*complex(0,1)*vevhat + (cth**2*dgw*ee**2*complex(0,1)*vevhat)/sth**2 + (dg1*ee**2*complex(0,1)*sth**2*vevhat)/cth**2 - (cHB*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (cHbox*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (3*cHDD*ee**2*complex(0,1)*vevhat**3)/(4.*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (cHB*cth**2*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (cHbox*cth**2*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth**2) + (3*cHDD*cth**2*ee**2*complex(0,1)*vevhat**3)/(8.*LambdaSMEFT**2*sth**2) - (cHW*cth**2*ee**2*complex(0,1)*vevhat**3)/(LambdaSMEFT**2*sth**2) + (cHW*cth**4*ee**2*complex(0,1)*vevhat**3)/(LambdaSMEFT**2*sth**2) + (cHWB*cth**3*ee**2*complex(0,1)*vevhat**3)/(LambdaSMEFT**2*sth) + (2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**3)/LambdaSMEFT**2 + (2*cHB*ee**2*complex(0,1)*sth**2*vevhat**3)/LambdaSMEFT**2 + (cHW*ee**2*complex(0,1)*sth**2*vevhat**3)/LambdaSMEFT**2 - (cHB*ee**2*complex(0,1)*sth**2*vevhat**3)/(cth**2*LambdaSMEFT**2) + (cHbox*ee**2*complex(0,1)*sth**2*vevhat**3)/(2.*cth**2*LambdaSMEFT**2) + (3*cHDD*ee**2*complex(0,1)*sth**2*vevhat**3)/(8.*cth**2*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**3*vevhat**3)/(cth*LambdaSMEFT**2) + (cHB*ee**2*complex(0,1)*sth**4*vevhat**3)/(cth**2*LambdaSMEFT**2) + (dGf*ee**2*complex(0,1)*vevhat)/cmath.sqrt(2) + (cth**2*dGf*ee**2*complex(0,1)*vevhat)/(2.*sth**2*cmath.sqrt(2)) + (dGf*ee**2*complex(0,1)*sth**2*vevhat)/(2.*cth**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3017 = Coupling(name = 'GC_3017',
                   value = '(cth*dsth2*ee**2*complex(0,1)*vevhat)/(4.*sth**3) - (cth*dg1*ee**2*complex(0,1)*vevhat)/(2.*sth) + (cth*dgw*ee**2*complex(0,1)*vevhat)/(2.*sth) + (dsth2*ee**2*complex(0,1)*vevhat)/(2.*cth*sth) - (dg1*ee**2*complex(0,1)*sth*vevhat)/(2.*cth) + (dgw*ee**2*complex(0,1)*sth*vevhat)/(2.*cth) + (dsth2*ee**2*complex(0,1)*sth*vevhat)/(4.*cth**3) - (cHWB*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2) + (cHWB*cth**2*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2) - (cHWB*cth**2*ee**2*complex(0,1)*vevhat**3)/(4.*LambdaSMEFT**2*sth**2) + (cHB*cth*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) - (cHB*cth**3*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) + (cHB*ee**2*complex(0,1)*sth*vevhat**3)/(2.*cth*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*sth*vevhat**3)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee**2*complex(0,1)*sth*vevhat**3)/LambdaSMEFT**2 + (cHW*cth*ee**2*complex(0,1)*sth*vevhat**3)/LambdaSMEFT**2 + (cHWB*ee**2*complex(0,1)*sth**2*vevhat**3)/LambdaSMEFT**2 - (cHWB*ee**2*complex(0,1)*sth**2*vevhat**3)/(4.*cth**2*LambdaSMEFT**2) - (cHB*ee**2*complex(0,1)*sth**3*vevhat**3)/(2.*cth*LambdaSMEFT**2) + (cHW*ee**2*complex(0,1)*sth**3*vevhat**3)/(2.*cth*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**4*vevhat**3)/(2.*cth**2*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3018 = Coupling(name = 'GC_3018',
                   value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_3019 = Coupling(name = 'GC_3019',
                   value = '(dGf*complex(0,1)*yb)/2. - (cHbox*complex(0,1)*vevhat**2*yb)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yb)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3020 = Coupling(name = 'GC_3020',
                   value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_3021 = Coupling(name = 'GC_3021',
                   value = '(dGf*complex(0,1)*yc)/2. - (cHbox*complex(0,1)*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yc)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3022 = Coupling(name = 'GC_3022',
                   value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_3023 = Coupling(name = 'GC_3023',
                   value = '(dGf*complex(0,1)*ydo)/2. - (cHbox*complex(0,1)*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ydo)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3024 = Coupling(name = 'GC_3024',
                   value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_3025 = Coupling(name = 'GC_3025',
                   value = '(dGf*complex(0,1)*ye)/2. - (cHbox*complex(0,1)*vevhat**2*ye)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ye)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3026 = Coupling(name = 'GC_3026',
                   value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_3027 = Coupling(name = 'GC_3027',
                   value = '(dGf*complex(0,1)*ym)/2. - (cHbox*complex(0,1)*vevhat**2*ym)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ym)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3028 = Coupling(name = 'GC_3028',
                   value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_3029 = Coupling(name = 'GC_3029',
                   value = '(dGf*complex(0,1)*ys)/2. - (cHbox*complex(0,1)*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ys)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3030 = Coupling(name = 'GC_3030',
                   value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_3031 = Coupling(name = 'GC_3031',
                   value = '(dGf*complex(0,1)*yt)/2. - (cHbox*complex(0,1)*vevhat**2*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yt)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3032 = Coupling(name = 'GC_3032',
                   value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_3033 = Coupling(name = 'GC_3033',
                   value = '(dGf*complex(0,1)*ytau)/2. - (cHbox*complex(0,1)*vevhat**2*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ytau)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3034 = Coupling(name = 'GC_3034',
                   value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_3035 = Coupling(name = 'GC_3035',
                   value = '(dGf*complex(0,1)*yup)/2. - (cHbox*complex(0,1)*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yup)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3036 = Coupling(name = 'GC_3036',
                   value = '(complex(0,1)*complexconjugate(cdG1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3037 = Coupling(name = 'GC_3037',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdG1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3038 = Coupling(name = 'GC_3038',
                   value = '(G*vevhat*complexconjugate(cdG1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_3039 = Coupling(name = 'GC_3039',
                   value = '(complex(0,1)*complexconjugate(cdG1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3040 = Coupling(name = 'GC_3040',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdG1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3041 = Coupling(name = 'GC_3041',
                   value = '(G*vevhat*complexconjugate(cdG1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_3042 = Coupling(name = 'GC_3042',
                   value = '(complex(0,1)*complexconjugate(cdG1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3043 = Coupling(name = 'GC_3043',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdG1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3044 = Coupling(name = 'GC_3044',
                   value = '(G*vevhat*complexconjugate(cdG1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_3045 = Coupling(name = 'GC_3045',
                   value = '(complex(0,1)*complexconjugate(cdG2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3046 = Coupling(name = 'GC_3046',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdG2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3047 = Coupling(name = 'GC_3047',
                   value = '(G*vevhat*complexconjugate(cdG2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_3048 = Coupling(name = 'GC_3048',
                   value = '(complex(0,1)*complexconjugate(cdG2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3049 = Coupling(name = 'GC_3049',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdG2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3050 = Coupling(name = 'GC_3050',
                   value = '(G*vevhat*complexconjugate(cdG2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_3051 = Coupling(name = 'GC_3051',
                   value = '(complex(0,1)*complexconjugate(cdG2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3052 = Coupling(name = 'GC_3052',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdG2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3053 = Coupling(name = 'GC_3053',
                   value = '(G*vevhat*complexconjugate(cdG2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_3054 = Coupling(name = 'GC_3054',
                   value = '(complex(0,1)*complexconjugate(cdG3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3055 = Coupling(name = 'GC_3055',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdG3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3056 = Coupling(name = 'GC_3056',
                   value = '(G*vevhat*complexconjugate(cdG3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_3057 = Coupling(name = 'GC_3057',
                   value = '(complex(0,1)*complexconjugate(cdG3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3058 = Coupling(name = 'GC_3058',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdG3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3059 = Coupling(name = 'GC_3059',
                   value = '(G*vevhat*complexconjugate(cdG3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_3060 = Coupling(name = 'GC_3060',
                   value = '(complex(0,1)*complexconjugate(cdG3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3061 = Coupling(name = 'GC_3061',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdG3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3062 = Coupling(name = 'GC_3062',
                   value = '(G*vevhat*complexconjugate(cdG3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_3063 = Coupling(name = 'GC_3063',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cdH1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3064 = Coupling(name = 'GC_3064',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cdH1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3065 = Coupling(name = 'GC_3065',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cdH1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3066 = Coupling(name = 'GC_3066',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cdH1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3067 = Coupling(name = 'GC_3067',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cdH1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3068 = Coupling(name = 'GC_3068',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cdH1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3069 = Coupling(name = 'GC_3069',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cdH2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3070 = Coupling(name = 'GC_3070',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cdH2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3071 = Coupling(name = 'GC_3071',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cdH2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3072 = Coupling(name = 'GC_3072',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cdH2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3073 = Coupling(name = 'GC_3073',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cdH2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3074 = Coupling(name = 'GC_3074',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cdH2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3075 = Coupling(name = 'GC_3075',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cdH3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3076 = Coupling(name = 'GC_3076',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cdH3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3077 = Coupling(name = 'GC_3077',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cdH3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3078 = Coupling(name = 'GC_3078',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cdH3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3079 = Coupling(name = 'GC_3079',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cdH3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3080 = Coupling(name = 'GC_3080',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cdH3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3081 = Coupling(name = 'GC_3081',
                   value = '(complex(0,1)*complexconjugate(cdW1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3082 = Coupling(name = 'GC_3082',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdW1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3083 = Coupling(name = 'GC_3083',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3084 = Coupling(name = 'GC_3084',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW1x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3085 = Coupling(name = 'GC_3085',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(cdW1x1))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3086 = Coupling(name = 'GC_3086',
                   value = '-((complex(0,1)*sth*complexconjugate(cdB1x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(cdW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3087 = Coupling(name = 'GC_3087',
                   value = '(cth*complex(0,1)*complexconjugate(cdB1x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(cdW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3088 = Coupling(name = 'GC_3088',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cdB1x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(cdW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3089 = Coupling(name = 'GC_3089',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cdB1x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(cdW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3090 = Coupling(name = 'GC_3090',
                   value = '(complex(0,1)*complexconjugate(cdW1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3091 = Coupling(name = 'GC_3091',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdW1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3092 = Coupling(name = 'GC_3092',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3093 = Coupling(name = 'GC_3093',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW1x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3094 = Coupling(name = 'GC_3094',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(cdW1x2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3095 = Coupling(name = 'GC_3095',
                   value = '-((complex(0,1)*sth*complexconjugate(cdB1x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(cdW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3096 = Coupling(name = 'GC_3096',
                   value = '(cth*complex(0,1)*complexconjugate(cdB1x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(cdW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3097 = Coupling(name = 'GC_3097',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cdB1x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(cdW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3098 = Coupling(name = 'GC_3098',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cdB1x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(cdW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3099 = Coupling(name = 'GC_3099',
                   value = '(complex(0,1)*complexconjugate(cdW1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3100 = Coupling(name = 'GC_3100',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdW1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3101 = Coupling(name = 'GC_3101',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3102 = Coupling(name = 'GC_3102',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW1x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3103 = Coupling(name = 'GC_3103',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(cdW1x3))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3104 = Coupling(name = 'GC_3104',
                   value = '-((complex(0,1)*sth*complexconjugate(cdB1x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(cdW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3105 = Coupling(name = 'GC_3105',
                   value = '(cth*complex(0,1)*complexconjugate(cdB1x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(cdW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3106 = Coupling(name = 'GC_3106',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cdB1x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(cdW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3107 = Coupling(name = 'GC_3107',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cdB1x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(cdW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3108 = Coupling(name = 'GC_3108',
                   value = '(complex(0,1)*complexconjugate(cdW2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3109 = Coupling(name = 'GC_3109',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdW2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3110 = Coupling(name = 'GC_3110',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3111 = Coupling(name = 'GC_3111',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW2x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3112 = Coupling(name = 'GC_3112',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(cdW2x1))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3113 = Coupling(name = 'GC_3113',
                   value = '-((complex(0,1)*sth*complexconjugate(cdB2x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(cdW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3114 = Coupling(name = 'GC_3114',
                   value = '(cth*complex(0,1)*complexconjugate(cdB2x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(cdW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3115 = Coupling(name = 'GC_3115',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cdB2x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(cdW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3116 = Coupling(name = 'GC_3116',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cdB2x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(cdW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3117 = Coupling(name = 'GC_3117',
                   value = '(complex(0,1)*complexconjugate(cdW2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3118 = Coupling(name = 'GC_3118',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdW2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3119 = Coupling(name = 'GC_3119',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3120 = Coupling(name = 'GC_3120',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW2x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3121 = Coupling(name = 'GC_3121',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(cdW2x2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3122 = Coupling(name = 'GC_3122',
                   value = '-((complex(0,1)*sth*complexconjugate(cdB2x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(cdW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3123 = Coupling(name = 'GC_3123',
                   value = '(cth*complex(0,1)*complexconjugate(cdB2x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(cdW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3124 = Coupling(name = 'GC_3124',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cdB2x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(cdW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3125 = Coupling(name = 'GC_3125',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cdB2x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(cdW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3126 = Coupling(name = 'GC_3126',
                   value = '(complex(0,1)*complexconjugate(cdW2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3127 = Coupling(name = 'GC_3127',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdW2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3128 = Coupling(name = 'GC_3128',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3129 = Coupling(name = 'GC_3129',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW2x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3130 = Coupling(name = 'GC_3130',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(cdW2x3))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3131 = Coupling(name = 'GC_3131',
                   value = '-((complex(0,1)*sth*complexconjugate(cdB2x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(cdW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3132 = Coupling(name = 'GC_3132',
                   value = '(cth*complex(0,1)*complexconjugate(cdB2x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(cdW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3133 = Coupling(name = 'GC_3133',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cdB2x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(cdW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3134 = Coupling(name = 'GC_3134',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cdB2x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(cdW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3135 = Coupling(name = 'GC_3135',
                   value = '(complex(0,1)*complexconjugate(cdW3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3136 = Coupling(name = 'GC_3136',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdW3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3137 = Coupling(name = 'GC_3137',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3138 = Coupling(name = 'GC_3138',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW3x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3139 = Coupling(name = 'GC_3139',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(cdW3x1))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3140 = Coupling(name = 'GC_3140',
                   value = '-((complex(0,1)*sth*complexconjugate(cdB3x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(cdW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3141 = Coupling(name = 'GC_3141',
                   value = '(cth*complex(0,1)*complexconjugate(cdB3x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(cdW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3142 = Coupling(name = 'GC_3142',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cdB3x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(cdW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3143 = Coupling(name = 'GC_3143',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cdB3x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(cdW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3144 = Coupling(name = 'GC_3144',
                   value = '(complex(0,1)*complexconjugate(cdW3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3145 = Coupling(name = 'GC_3145',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdW3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3146 = Coupling(name = 'GC_3146',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3147 = Coupling(name = 'GC_3147',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW3x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3148 = Coupling(name = 'GC_3148',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(cdW3x2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3149 = Coupling(name = 'GC_3149',
                   value = '-((complex(0,1)*sth*complexconjugate(cdB3x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(cdW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3150 = Coupling(name = 'GC_3150',
                   value = '(cth*complex(0,1)*complexconjugate(cdB3x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(cdW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3151 = Coupling(name = 'GC_3151',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cdB3x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(cdW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3152 = Coupling(name = 'GC_3152',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cdB3x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(cdW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3153 = Coupling(name = 'GC_3153',
                   value = '(complex(0,1)*complexconjugate(cdW3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3154 = Coupling(name = 'GC_3154',
                   value = '(complex(0,1)*vevhat*complexconjugate(cdW3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3155 = Coupling(name = 'GC_3155',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3156 = Coupling(name = 'GC_3156',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cdW3x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3157 = Coupling(name = 'GC_3157',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(cdW3x3))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3158 = Coupling(name = 'GC_3158',
                   value = '-((complex(0,1)*sth*complexconjugate(cdB3x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(cdW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3159 = Coupling(name = 'GC_3159',
                   value = '(cth*complex(0,1)*complexconjugate(cdB3x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(cdW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3160 = Coupling(name = 'GC_3160',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cdB3x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(cdW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3161 = Coupling(name = 'GC_3161',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cdB3x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(cdW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3162 = Coupling(name = 'GC_3162',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(ceH1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3163 = Coupling(name = 'GC_3163',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(ceH1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3164 = Coupling(name = 'GC_3164',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(ceH1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3165 = Coupling(name = 'GC_3165',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(ceH1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3166 = Coupling(name = 'GC_3166',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(ceH1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3167 = Coupling(name = 'GC_3167',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(ceH1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3168 = Coupling(name = 'GC_3168',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(ceH2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3169 = Coupling(name = 'GC_3169',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(ceH2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3170 = Coupling(name = 'GC_3170',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(ceH2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3171 = Coupling(name = 'GC_3171',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(ceH2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3172 = Coupling(name = 'GC_3172',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(ceH2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3173 = Coupling(name = 'GC_3173',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(ceH2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3174 = Coupling(name = 'GC_3174',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(ceH3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3175 = Coupling(name = 'GC_3175',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(ceH3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3176 = Coupling(name = 'GC_3176',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(ceH3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3177 = Coupling(name = 'GC_3177',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(ceH3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3178 = Coupling(name = 'GC_3178',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(ceH3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3179 = Coupling(name = 'GC_3179',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(ceH3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_3180 = Coupling(name = 'GC_3180',
                   value = '(complex(0,1)*complexconjugate(ceW1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3181 = Coupling(name = 'GC_3181',
                   value = '(complex(0,1)*vevhat*complexconjugate(ceW1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3182 = Coupling(name = 'GC_3182',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3183 = Coupling(name = 'GC_3183',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW1x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3184 = Coupling(name = 'GC_3184',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(ceW1x1))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3185 = Coupling(name = 'GC_3185',
                   value = '-((complex(0,1)*sth*complexconjugate(ceB1x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(ceW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3186 = Coupling(name = 'GC_3186',
                   value = '(cth*complex(0,1)*complexconjugate(ceB1x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(ceW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3187 = Coupling(name = 'GC_3187',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(ceB1x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(ceW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3188 = Coupling(name = 'GC_3188',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(ceB1x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(ceW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3189 = Coupling(name = 'GC_3189',
                   value = '(complex(0,1)*complexconjugate(ceW1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3190 = Coupling(name = 'GC_3190',
                   value = '(complex(0,1)*vevhat*complexconjugate(ceW1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3191 = Coupling(name = 'GC_3191',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3192 = Coupling(name = 'GC_3192',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW1x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3193 = Coupling(name = 'GC_3193',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(ceW1x2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3194 = Coupling(name = 'GC_3194',
                   value = '-((complex(0,1)*sth*complexconjugate(ceB1x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(ceW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3195 = Coupling(name = 'GC_3195',
                   value = '(cth*complex(0,1)*complexconjugate(ceB1x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(ceW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3196 = Coupling(name = 'GC_3196',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(ceB1x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(ceW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3197 = Coupling(name = 'GC_3197',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(ceB1x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(ceW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3198 = Coupling(name = 'GC_3198',
                   value = '(complex(0,1)*complexconjugate(ceW1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3199 = Coupling(name = 'GC_3199',
                   value = '(complex(0,1)*vevhat*complexconjugate(ceW1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3200 = Coupling(name = 'GC_3200',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3201 = Coupling(name = 'GC_3201',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW1x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3202 = Coupling(name = 'GC_3202',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(ceW1x3))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3203 = Coupling(name = 'GC_3203',
                   value = '-((complex(0,1)*sth*complexconjugate(ceB1x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(ceW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3204 = Coupling(name = 'GC_3204',
                   value = '(cth*complex(0,1)*complexconjugate(ceB1x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(ceW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3205 = Coupling(name = 'GC_3205',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(ceB1x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(ceW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3206 = Coupling(name = 'GC_3206',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(ceB1x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(ceW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3207 = Coupling(name = 'GC_3207',
                   value = '(complex(0,1)*complexconjugate(ceW2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3208 = Coupling(name = 'GC_3208',
                   value = '(complex(0,1)*vevhat*complexconjugate(ceW2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3209 = Coupling(name = 'GC_3209',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3210 = Coupling(name = 'GC_3210',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW2x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3211 = Coupling(name = 'GC_3211',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(ceW2x1))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3212 = Coupling(name = 'GC_3212',
                   value = '-((complex(0,1)*sth*complexconjugate(ceB2x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(ceW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3213 = Coupling(name = 'GC_3213',
                   value = '(cth*complex(0,1)*complexconjugate(ceB2x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(ceW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3214 = Coupling(name = 'GC_3214',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(ceB2x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(ceW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3215 = Coupling(name = 'GC_3215',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(ceB2x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(ceW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3216 = Coupling(name = 'GC_3216',
                   value = '(complex(0,1)*complexconjugate(ceW2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3217 = Coupling(name = 'GC_3217',
                   value = '(complex(0,1)*vevhat*complexconjugate(ceW2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3218 = Coupling(name = 'GC_3218',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3219 = Coupling(name = 'GC_3219',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW2x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3220 = Coupling(name = 'GC_3220',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(ceW2x2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3221 = Coupling(name = 'GC_3221',
                   value = '-((complex(0,1)*sth*complexconjugate(ceB2x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(ceW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3222 = Coupling(name = 'GC_3222',
                   value = '(cth*complex(0,1)*complexconjugate(ceB2x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(ceW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3223 = Coupling(name = 'GC_3223',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(ceB2x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(ceW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3224 = Coupling(name = 'GC_3224',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(ceB2x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(ceW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3225 = Coupling(name = 'GC_3225',
                   value = '(complex(0,1)*complexconjugate(ceW2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3226 = Coupling(name = 'GC_3226',
                   value = '(complex(0,1)*vevhat*complexconjugate(ceW2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3227 = Coupling(name = 'GC_3227',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3228 = Coupling(name = 'GC_3228',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW2x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3229 = Coupling(name = 'GC_3229',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(ceW2x3))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3230 = Coupling(name = 'GC_3230',
                   value = '-((complex(0,1)*sth*complexconjugate(ceB2x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(ceW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3231 = Coupling(name = 'GC_3231',
                   value = '(cth*complex(0,1)*complexconjugate(ceB2x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(ceW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3232 = Coupling(name = 'GC_3232',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(ceB2x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(ceW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3233 = Coupling(name = 'GC_3233',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(ceB2x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(ceW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3234 = Coupling(name = 'GC_3234',
                   value = '(complex(0,1)*complexconjugate(ceW3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3235 = Coupling(name = 'GC_3235',
                   value = '(complex(0,1)*vevhat*complexconjugate(ceW3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3236 = Coupling(name = 'GC_3236',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3237 = Coupling(name = 'GC_3237',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW3x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3238 = Coupling(name = 'GC_3238',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(ceW3x1))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3239 = Coupling(name = 'GC_3239',
                   value = '-((complex(0,1)*sth*complexconjugate(ceB3x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(ceW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3240 = Coupling(name = 'GC_3240',
                   value = '(cth*complex(0,1)*complexconjugate(ceB3x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(ceW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3241 = Coupling(name = 'GC_3241',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(ceB3x1))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(ceW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3242 = Coupling(name = 'GC_3242',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(ceB3x1))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(ceW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3243 = Coupling(name = 'GC_3243',
                   value = '(complex(0,1)*complexconjugate(ceW3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3244 = Coupling(name = 'GC_3244',
                   value = '(complex(0,1)*vevhat*complexconjugate(ceW3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3245 = Coupling(name = 'GC_3245',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3246 = Coupling(name = 'GC_3246',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW3x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3247 = Coupling(name = 'GC_3247',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(ceW3x2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3248 = Coupling(name = 'GC_3248',
                   value = '-((complex(0,1)*sth*complexconjugate(ceB3x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(ceW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3249 = Coupling(name = 'GC_3249',
                   value = '(cth*complex(0,1)*complexconjugate(ceB3x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(ceW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3250 = Coupling(name = 'GC_3250',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(ceB3x2))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(ceW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3251 = Coupling(name = 'GC_3251',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(ceB3x2))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(ceW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3252 = Coupling(name = 'GC_3252',
                   value = '(complex(0,1)*complexconjugate(ceW3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3253 = Coupling(name = 'GC_3253',
                   value = '(complex(0,1)*vevhat*complexconjugate(ceW3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_3254 = Coupling(name = 'GC_3254',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3255 = Coupling(name = 'GC_3255',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(ceW3x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3256 = Coupling(name = 'GC_3256',
                   value = '-((cth*ee*complex(0,1)*vevhat*complexconjugate(ceW3x3))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3257 = Coupling(name = 'GC_3257',
                   value = '-((complex(0,1)*sth*complexconjugate(ceB3x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*complexconjugate(ceW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3258 = Coupling(name = 'GC_3258',
                   value = '(cth*complex(0,1)*complexconjugate(ceB3x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*complexconjugate(ceW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3259 = Coupling(name = 'GC_3259',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(ceB3x3))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*complexconjugate(ceW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3260 = Coupling(name = 'GC_3260',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(ceB3x3))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*complexconjugate(ceW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3261 = Coupling(name = 'GC_3261',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHd1x2))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHd1x2))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3262 = Coupling(name = 'GC_3262',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHd1x2))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHd1x2))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3263 = Coupling(name = 'GC_3263',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHd1x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHd1x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3264 = Coupling(name = 'GC_3264',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHd1x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHd1x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3265 = Coupling(name = 'GC_3265',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHd2x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHd2x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3266 = Coupling(name = 'GC_3266',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHd2x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHd2x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3267 = Coupling(name = 'GC_3267',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHe1x2))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHe1x2))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3268 = Coupling(name = 'GC_3268',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHe1x2))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHe1x2))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3269 = Coupling(name = 'GC_3269',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHe1x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHe1x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3270 = Coupling(name = 'GC_3270',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHe1x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHe1x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3271 = Coupling(name = 'GC_3271',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHe2x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHe2x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3272 = Coupling(name = 'GC_3272',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHe2x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHe2x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3273 = Coupling(name = 'GC_3273',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cHl31x2)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3274 = Coupling(name = 'GC_3274',
                   value = '-((ee*complex(0,1)*vevhat**2*complexconjugate(cHl31x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':1})

GC_3275 = Coupling(name = 'GC_3275',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHl11x2))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl11x2))/(cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat*complexconjugate(cHl31x2))/(LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl31x2))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3276 = Coupling(name = 'GC_3276',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHl11x2))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl11x2))/(cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat*complexconjugate(cHl31x2))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl31x2))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3277 = Coupling(name = 'GC_3277',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl11x2))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl11x2))/(2.*cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl31x2))/(2.*LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl31x2))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3278 = Coupling(name = 'GC_3278',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl11x2))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl11x2))/(2.*cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl31x2))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl31x2))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3279 = Coupling(name = 'GC_3279',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cHl31x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3280 = Coupling(name = 'GC_3280',
                   value = '-((ee*complex(0,1)*vevhat**2*complexconjugate(cHl31x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':1})

GC_3281 = Coupling(name = 'GC_3281',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHl11x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl11x3))/(cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat*complexconjugate(cHl31x3))/(LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl31x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3282 = Coupling(name = 'GC_3282',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHl11x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl11x3))/(cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat*complexconjugate(cHl31x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl31x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3283 = Coupling(name = 'GC_3283',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl11x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl11x3))/(2.*cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl31x3))/(2.*LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl31x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3284 = Coupling(name = 'GC_3284',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl11x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl11x3))/(2.*cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl31x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl31x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3285 = Coupling(name = 'GC_3285',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cHl32x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3286 = Coupling(name = 'GC_3286',
                   value = '-((ee*complex(0,1)*vevhat**2*complexconjugate(cHl32x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':1})

GC_3287 = Coupling(name = 'GC_3287',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHl12x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl12x3))/(cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat*complexconjugate(cHl32x3))/(LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl32x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3288 = Coupling(name = 'GC_3288',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHl12x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl12x3))/(cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat*complexconjugate(cHl32x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHl32x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3289 = Coupling(name = 'GC_3289',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl12x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl12x3))/(2.*cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl32x3))/(2.*LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl32x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3290 = Coupling(name = 'GC_3290',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl12x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl12x3))/(2.*cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHl32x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHl32x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3291 = Coupling(name = 'GC_3291',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cHq31x2)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3292 = Coupling(name = 'GC_3292',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHq11x2))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq11x2))/(cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat*complexconjugate(cHq31x2))/(LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq31x2))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3293 = Coupling(name = 'GC_3293',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHq11x2))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq11x2))/(cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat*complexconjugate(cHq31x2))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq31x2))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3294 = Coupling(name = 'GC_3294',
                   value = '-((CKM2x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (ee*complex(0,1)*vevhat**2*complexconjugate(cHq31x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3295 = Coupling(name = 'GC_3295',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq11x2))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq11x2))/(2.*cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq31x2))/(2.*LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq31x2))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3296 = Coupling(name = 'GC_3296',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq11x2))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq11x2))/(2.*cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq31x2))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq31x2))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3297 = Coupling(name = 'GC_3297',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cHq31x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3298 = Coupling(name = 'GC_3298',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHq11x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq11x3))/(cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat*complexconjugate(cHq31x3))/(LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq31x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3299 = Coupling(name = 'GC_3299',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHq11x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq11x3))/(cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat*complexconjugate(cHq31x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq31x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3300 = Coupling(name = 'GC_3300',
                   value = '-((CKM3x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (ee*complex(0,1)*vevhat**2*complexconjugate(cHq31x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3301 = Coupling(name = 'GC_3301',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq11x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq11x3))/(2.*cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq31x3))/(2.*LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq31x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3302 = Coupling(name = 'GC_3302',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq11x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq11x3))/(2.*cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq31x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq31x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3303 = Coupling(name = 'GC_3303',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cHq32x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'QED':2})

GC_3304 = Coupling(name = 'GC_3304',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHq12x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq12x3))/(cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat*complexconjugate(cHq32x3))/(LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq32x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3305 = Coupling(name = 'GC_3305',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHq12x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq12x3))/(cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat*complexconjugate(cHq32x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHq32x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3306 = Coupling(name = 'GC_3306',
                   value = '-((CKM3x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (ee*complex(0,1)*vevhat**2*complexconjugate(cHq32x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3307 = Coupling(name = 'GC_3307',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq12x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq12x3))/(2.*cth*LambdaSMEFT**2) - (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq32x3))/(2.*LambdaSMEFT**2*sth) - (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq32x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3308 = Coupling(name = 'GC_3308',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq12x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq12x3))/(2.*cth*LambdaSMEFT**2) + (cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHq32x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHq32x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3309 = Coupling(name = 'GC_3309',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHu1x2))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHu1x2))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3310 = Coupling(name = 'GC_3310',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHu1x2))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHu1x2))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3311 = Coupling(name = 'GC_3311',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHu1x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHu1x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3312 = Coupling(name = 'GC_3312',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHu1x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHu1x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3313 = Coupling(name = 'GC_3313',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cHu2x3))/(LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat*complexconjugate(cHu2x3))/(cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3314 = Coupling(name = 'GC_3314',
                   value = '(cth*ee*complex(0,1)*vevhat**2*complexconjugate(cHu2x3))/(2.*LambdaSMEFT**2*sth) + (ee*complex(0,1)*sth*vevhat**2*complexconjugate(cHu2x3))/(2.*cth*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':1})

GC_3315 = Coupling(name = 'GC_3315',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cHud1x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3316 = Coupling(name = 'GC_3316',
                   value = '(ee*complex(0,1)*vevhat**2*complexconjugate(cHud1x1))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3317 = Coupling(name = 'GC_3317',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cHud1x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3318 = Coupling(name = 'GC_3318',
                   value = '(ee*complex(0,1)*vevhat**2*complexconjugate(cHud1x2))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3319 = Coupling(name = 'GC_3319',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cHud1x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3320 = Coupling(name = 'GC_3320',
                   value = '(ee*complex(0,1)*vevhat**2*complexconjugate(cHud1x3))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3321 = Coupling(name = 'GC_3321',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cHud2x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3322 = Coupling(name = 'GC_3322',
                   value = '(ee*complex(0,1)*vevhat**2*complexconjugate(cHud2x1))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3323 = Coupling(name = 'GC_3323',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cHud2x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3324 = Coupling(name = 'GC_3324',
                   value = '(ee*complex(0,1)*vevhat**2*complexconjugate(cHud2x2))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3325 = Coupling(name = 'GC_3325',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cHud2x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3326 = Coupling(name = 'GC_3326',
                   value = '(ee*complex(0,1)*vevhat**2*complexconjugate(cHud2x3))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3327 = Coupling(name = 'GC_3327',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cHud3x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3328 = Coupling(name = 'GC_3328',
                   value = '(ee*complex(0,1)*vevhat**2*complexconjugate(cHud3x1))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3329 = Coupling(name = 'GC_3329',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cHud3x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3330 = Coupling(name = 'GC_3330',
                   value = '(ee*complex(0,1)*vevhat**2*complexconjugate(cHud3x2))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3331 = Coupling(name = 'GC_3331',
                   value = '(ee*complex(0,1)*vevhat*complexconjugate(cHud3x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_3332 = Coupling(name = 'GC_3332',
                   value = '(ee*complex(0,1)*vevhat**2*complexconjugate(cHud3x3))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3333 = Coupling(name = 'GC_3333',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM1x1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_3334 = Coupling(name = 'GC_3334',
                   value = '-((cHq31x1*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM1x1))/(sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3335 = Coupling(name = 'GC_3335',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM1x2))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_3336 = Coupling(name = 'GC_3336',
                   value = '-((ee*complex(0,1)*vevhat**2*complexconjugate(cHq31x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM1x2))/(sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3337 = Coupling(name = 'GC_3337',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM1x3))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_3338 = Coupling(name = 'GC_3338',
                   value = '-((ee*complex(0,1)*vevhat**2*complexconjugate(cHq31x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM1x3))/(sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3339 = Coupling(name = 'GC_3339',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM2x1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_3340 = Coupling(name = 'GC_3340',
                   value = '-((cHq31x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM2x1))/(sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3341 = Coupling(name = 'GC_3341',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM2x2))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_3342 = Coupling(name = 'GC_3342',
                   value = '-((cHq32x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM2x2))/(sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3343 = Coupling(name = 'GC_3343',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM2x3))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_3344 = Coupling(name = 'GC_3344',
                   value = '-((ee*complex(0,1)*vevhat**2*complexconjugate(cHq32x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM2x3))/(sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3345 = Coupling(name = 'GC_3345',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM3x1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_3346 = Coupling(name = 'GC_3346',
                   value = '-((cHq31x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM3x1))/(sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3347 = Coupling(name = 'GC_3347',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM3x2))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_3348 = Coupling(name = 'GC_3348',
                   value = '-((cHq32x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM3x2))/(sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3349 = Coupling(name = 'GC_3349',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM3x3))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_3350 = Coupling(name = 'GC_3350',
                   value = '-((cHq33x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM3x3))/(sth*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_3351 = Coupling(name = 'GC_3351',
                   value = '(complex(0,1)*complexconjugate(cledq1x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3352 = Coupling(name = 'GC_3352',
                   value = '(complex(0,1)*complexconjugate(cledq1x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3353 = Coupling(name = 'GC_3353',
                   value = '(complex(0,1)*complexconjugate(cledq1x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3354 = Coupling(name = 'GC_3354',
                   value = '(complex(0,1)*complexconjugate(cledq1x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3355 = Coupling(name = 'GC_3355',
                   value = '(complex(0,1)*complexconjugate(cledq1x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3356 = Coupling(name = 'GC_3356',
                   value = '(complex(0,1)*complexconjugate(cledq1x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3357 = Coupling(name = 'GC_3357',
                   value = '(complex(0,1)*complexconjugate(cledq1x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3358 = Coupling(name = 'GC_3358',
                   value = '(complex(0,1)*complexconjugate(cledq1x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3359 = Coupling(name = 'GC_3359',
                   value = '(complex(0,1)*complexconjugate(cledq1x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3360 = Coupling(name = 'GC_3360',
                   value = '(complex(0,1)*complexconjugate(cledq1x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3361 = Coupling(name = 'GC_3361',
                   value = '(complex(0,1)*complexconjugate(cledq1x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3362 = Coupling(name = 'GC_3362',
                   value = '(complex(0,1)*complexconjugate(cledq1x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3363 = Coupling(name = 'GC_3363',
                   value = '(complex(0,1)*complexconjugate(cledq1x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3364 = Coupling(name = 'GC_3364',
                   value = '(complex(0,1)*complexconjugate(cledq1x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3365 = Coupling(name = 'GC_3365',
                   value = '(complex(0,1)*complexconjugate(cledq1x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3366 = Coupling(name = 'GC_3366',
                   value = '(complex(0,1)*complexconjugate(cledq1x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3367 = Coupling(name = 'GC_3367',
                   value = '(complex(0,1)*complexconjugate(cledq1x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3368 = Coupling(name = 'GC_3368',
                   value = '(complex(0,1)*complexconjugate(cledq1x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3369 = Coupling(name = 'GC_3369',
                   value = '(complex(0,1)*complexconjugate(cledq1x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3370 = Coupling(name = 'GC_3370',
                   value = '(complex(0,1)*complexconjugate(cledq1x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3371 = Coupling(name = 'GC_3371',
                   value = '(complex(0,1)*complexconjugate(cledq1x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3372 = Coupling(name = 'GC_3372',
                   value = '(complex(0,1)*complexconjugate(cledq1x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3373 = Coupling(name = 'GC_3373',
                   value = '(complex(0,1)*complexconjugate(cledq1x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3374 = Coupling(name = 'GC_3374',
                   value = '(complex(0,1)*complexconjugate(cledq1x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3375 = Coupling(name = 'GC_3375',
                   value = '(complex(0,1)*complexconjugate(cledq1x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3376 = Coupling(name = 'GC_3376',
                   value = '(complex(0,1)*complexconjugate(cledq1x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3377 = Coupling(name = 'GC_3377',
                   value = '(complex(0,1)*complexconjugate(cledq1x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3378 = Coupling(name = 'GC_3378',
                   value = '(complex(0,1)*complexconjugate(cledq2x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3379 = Coupling(name = 'GC_3379',
                   value = '(complex(0,1)*complexconjugate(cledq2x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3380 = Coupling(name = 'GC_3380',
                   value = '(complex(0,1)*complexconjugate(cledq2x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3381 = Coupling(name = 'GC_3381',
                   value = '(complex(0,1)*complexconjugate(cledq2x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3382 = Coupling(name = 'GC_3382',
                   value = '(complex(0,1)*complexconjugate(cledq2x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3383 = Coupling(name = 'GC_3383',
                   value = '(complex(0,1)*complexconjugate(cledq2x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3384 = Coupling(name = 'GC_3384',
                   value = '(complex(0,1)*complexconjugate(cledq2x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3385 = Coupling(name = 'GC_3385',
                   value = '(complex(0,1)*complexconjugate(cledq2x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3386 = Coupling(name = 'GC_3386',
                   value = '(complex(0,1)*complexconjugate(cledq2x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3387 = Coupling(name = 'GC_3387',
                   value = '(complex(0,1)*complexconjugate(cledq2x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3388 = Coupling(name = 'GC_3388',
                   value = '(complex(0,1)*complexconjugate(cledq2x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3389 = Coupling(name = 'GC_3389',
                   value = '(complex(0,1)*complexconjugate(cledq2x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3390 = Coupling(name = 'GC_3390',
                   value = '(complex(0,1)*complexconjugate(cledq2x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3391 = Coupling(name = 'GC_3391',
                   value = '(complex(0,1)*complexconjugate(cledq2x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3392 = Coupling(name = 'GC_3392',
                   value = '(complex(0,1)*complexconjugate(cledq2x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3393 = Coupling(name = 'GC_3393',
                   value = '(complex(0,1)*complexconjugate(cledq2x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3394 = Coupling(name = 'GC_3394',
                   value = '(complex(0,1)*complexconjugate(cledq2x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3395 = Coupling(name = 'GC_3395',
                   value = '(complex(0,1)*complexconjugate(cledq2x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3396 = Coupling(name = 'GC_3396',
                   value = '(complex(0,1)*complexconjugate(cledq2x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3397 = Coupling(name = 'GC_3397',
                   value = '(complex(0,1)*complexconjugate(cledq2x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3398 = Coupling(name = 'GC_3398',
                   value = '(complex(0,1)*complexconjugate(cledq2x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3399 = Coupling(name = 'GC_3399',
                   value = '(complex(0,1)*complexconjugate(cledq2x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3400 = Coupling(name = 'GC_3400',
                   value = '(complex(0,1)*complexconjugate(cledq2x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3401 = Coupling(name = 'GC_3401',
                   value = '(complex(0,1)*complexconjugate(cledq2x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3402 = Coupling(name = 'GC_3402',
                   value = '(complex(0,1)*complexconjugate(cledq2x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3403 = Coupling(name = 'GC_3403',
                   value = '(complex(0,1)*complexconjugate(cledq2x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3404 = Coupling(name = 'GC_3404',
                   value = '(complex(0,1)*complexconjugate(cledq2x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3405 = Coupling(name = 'GC_3405',
                   value = '(complex(0,1)*complexconjugate(cledq3x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3406 = Coupling(name = 'GC_3406',
                   value = '(complex(0,1)*complexconjugate(cledq3x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3407 = Coupling(name = 'GC_3407',
                   value = '(complex(0,1)*complexconjugate(cledq3x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3408 = Coupling(name = 'GC_3408',
                   value = '(complex(0,1)*complexconjugate(cledq3x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3409 = Coupling(name = 'GC_3409',
                   value = '(complex(0,1)*complexconjugate(cledq3x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3410 = Coupling(name = 'GC_3410',
                   value = '(complex(0,1)*complexconjugate(cledq3x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3411 = Coupling(name = 'GC_3411',
                   value = '(complex(0,1)*complexconjugate(cledq3x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3412 = Coupling(name = 'GC_3412',
                   value = '(complex(0,1)*complexconjugate(cledq3x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3413 = Coupling(name = 'GC_3413',
                   value = '(complex(0,1)*complexconjugate(cledq3x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3414 = Coupling(name = 'GC_3414',
                   value = '(complex(0,1)*complexconjugate(cledq3x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3415 = Coupling(name = 'GC_3415',
                   value = '(complex(0,1)*complexconjugate(cledq3x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3416 = Coupling(name = 'GC_3416',
                   value = '(complex(0,1)*complexconjugate(cledq3x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3417 = Coupling(name = 'GC_3417',
                   value = '(complex(0,1)*complexconjugate(cledq3x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3418 = Coupling(name = 'GC_3418',
                   value = '(complex(0,1)*complexconjugate(cledq3x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3419 = Coupling(name = 'GC_3419',
                   value = '(complex(0,1)*complexconjugate(cledq3x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3420 = Coupling(name = 'GC_3420',
                   value = '(complex(0,1)*complexconjugate(cledq3x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3421 = Coupling(name = 'GC_3421',
                   value = '(complex(0,1)*complexconjugate(cledq3x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3422 = Coupling(name = 'GC_3422',
                   value = '(complex(0,1)*complexconjugate(cledq3x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3423 = Coupling(name = 'GC_3423',
                   value = '(complex(0,1)*complexconjugate(cledq3x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3424 = Coupling(name = 'GC_3424',
                   value = '(complex(0,1)*complexconjugate(cledq3x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3425 = Coupling(name = 'GC_3425',
                   value = '(complex(0,1)*complexconjugate(cledq3x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3426 = Coupling(name = 'GC_3426',
                   value = '(complex(0,1)*complexconjugate(cledq3x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3427 = Coupling(name = 'GC_3427',
                   value = '(complex(0,1)*complexconjugate(cledq3x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3428 = Coupling(name = 'GC_3428',
                   value = '(complex(0,1)*complexconjugate(cledq3x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3429 = Coupling(name = 'GC_3429',
                   value = '(complex(0,1)*complexconjugate(cledq3x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3430 = Coupling(name = 'GC_3430',
                   value = '(complex(0,1)*complexconjugate(cledq3x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3431 = Coupling(name = 'GC_3431',
                   value = '(complex(0,1)*complexconjugate(cledq3x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3432 = Coupling(name = 'GC_3432',
                   value = '-((complex(0,1)*complexconjugate(clequ11x1x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3433 = Coupling(name = 'GC_3433',
                   value = '(complex(0,1)*complexconjugate(clequ11x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3434 = Coupling(name = 'GC_3434',
                   value = '-((complex(0,1)*complexconjugate(clequ11x1x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3435 = Coupling(name = 'GC_3435',
                   value = '(complex(0,1)*complexconjugate(clequ11x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3436 = Coupling(name = 'GC_3436',
                   value = '-((complex(0,1)*complexconjugate(clequ11x1x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3437 = Coupling(name = 'GC_3437',
                   value = '(complex(0,1)*complexconjugate(clequ11x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3438 = Coupling(name = 'GC_3438',
                   value = '-((complex(0,1)*complexconjugate(clequ11x1x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3439 = Coupling(name = 'GC_3439',
                   value = '(complex(0,1)*complexconjugate(clequ11x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3440 = Coupling(name = 'GC_3440',
                   value = '-((complex(0,1)*complexconjugate(clequ11x1x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3441 = Coupling(name = 'GC_3441',
                   value = '(complex(0,1)*complexconjugate(clequ11x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3442 = Coupling(name = 'GC_3442',
                   value = '-((complex(0,1)*complexconjugate(clequ11x1x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3443 = Coupling(name = 'GC_3443',
                   value = '(complex(0,1)*complexconjugate(clequ11x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3444 = Coupling(name = 'GC_3444',
                   value = '-((complex(0,1)*complexconjugate(clequ11x1x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3445 = Coupling(name = 'GC_3445',
                   value = '(complex(0,1)*complexconjugate(clequ11x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3446 = Coupling(name = 'GC_3446',
                   value = '-((complex(0,1)*complexconjugate(clequ11x1x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3447 = Coupling(name = 'GC_3447',
                   value = '(complex(0,1)*complexconjugate(clequ11x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3448 = Coupling(name = 'GC_3448',
                   value = '-((complex(0,1)*complexconjugate(clequ11x1x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3449 = Coupling(name = 'GC_3449',
                   value = '(complex(0,1)*complexconjugate(clequ11x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3450 = Coupling(name = 'GC_3450',
                   value = '-((complex(0,1)*complexconjugate(clequ11x2x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3451 = Coupling(name = 'GC_3451',
                   value = '(complex(0,1)*complexconjugate(clequ11x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3452 = Coupling(name = 'GC_3452',
                   value = '-((complex(0,1)*complexconjugate(clequ11x2x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3453 = Coupling(name = 'GC_3453',
                   value = '(complex(0,1)*complexconjugate(clequ11x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3454 = Coupling(name = 'GC_3454',
                   value = '-((complex(0,1)*complexconjugate(clequ11x2x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3455 = Coupling(name = 'GC_3455',
                   value = '(complex(0,1)*complexconjugate(clequ11x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3456 = Coupling(name = 'GC_3456',
                   value = '-((complex(0,1)*complexconjugate(clequ11x2x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3457 = Coupling(name = 'GC_3457',
                   value = '(complex(0,1)*complexconjugate(clequ11x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3458 = Coupling(name = 'GC_3458',
                   value = '-((complex(0,1)*complexconjugate(clequ11x2x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3459 = Coupling(name = 'GC_3459',
                   value = '(complex(0,1)*complexconjugate(clequ11x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3460 = Coupling(name = 'GC_3460',
                   value = '-((complex(0,1)*complexconjugate(clequ11x2x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3461 = Coupling(name = 'GC_3461',
                   value = '(complex(0,1)*complexconjugate(clequ11x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3462 = Coupling(name = 'GC_3462',
                   value = '-((complex(0,1)*complexconjugate(clequ11x2x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3463 = Coupling(name = 'GC_3463',
                   value = '(complex(0,1)*complexconjugate(clequ11x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3464 = Coupling(name = 'GC_3464',
                   value = '-((complex(0,1)*complexconjugate(clequ11x2x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3465 = Coupling(name = 'GC_3465',
                   value = '(complex(0,1)*complexconjugate(clequ11x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3466 = Coupling(name = 'GC_3466',
                   value = '-((complex(0,1)*complexconjugate(clequ11x2x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3467 = Coupling(name = 'GC_3467',
                   value = '(complex(0,1)*complexconjugate(clequ11x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3468 = Coupling(name = 'GC_3468',
                   value = '-((complex(0,1)*complexconjugate(clequ11x3x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3469 = Coupling(name = 'GC_3469',
                   value = '(complex(0,1)*complexconjugate(clequ11x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3470 = Coupling(name = 'GC_3470',
                   value = '-((complex(0,1)*complexconjugate(clequ11x3x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3471 = Coupling(name = 'GC_3471',
                   value = '(complex(0,1)*complexconjugate(clequ11x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3472 = Coupling(name = 'GC_3472',
                   value = '-((complex(0,1)*complexconjugate(clequ11x3x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3473 = Coupling(name = 'GC_3473',
                   value = '(complex(0,1)*complexconjugate(clequ11x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3474 = Coupling(name = 'GC_3474',
                   value = '-((complex(0,1)*complexconjugate(clequ11x3x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3475 = Coupling(name = 'GC_3475',
                   value = '(complex(0,1)*complexconjugate(clequ11x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3476 = Coupling(name = 'GC_3476',
                   value = '-((complex(0,1)*complexconjugate(clequ11x3x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3477 = Coupling(name = 'GC_3477',
                   value = '(complex(0,1)*complexconjugate(clequ11x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3478 = Coupling(name = 'GC_3478',
                   value = '-((complex(0,1)*complexconjugate(clequ11x3x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3479 = Coupling(name = 'GC_3479',
                   value = '(complex(0,1)*complexconjugate(clequ11x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3480 = Coupling(name = 'GC_3480',
                   value = '-((complex(0,1)*complexconjugate(clequ11x3x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3481 = Coupling(name = 'GC_3481',
                   value = '(complex(0,1)*complexconjugate(clequ11x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3482 = Coupling(name = 'GC_3482',
                   value = '-((complex(0,1)*complexconjugate(clequ11x3x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3483 = Coupling(name = 'GC_3483',
                   value = '(complex(0,1)*complexconjugate(clequ11x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3484 = Coupling(name = 'GC_3484',
                   value = '-((complex(0,1)*complexconjugate(clequ11x3x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3485 = Coupling(name = 'GC_3485',
                   value = '(complex(0,1)*complexconjugate(clequ11x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3486 = Coupling(name = 'GC_3486',
                   value = '-((complex(0,1)*complexconjugate(clequ12x1x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3487 = Coupling(name = 'GC_3487',
                   value = '(complex(0,1)*complexconjugate(clequ12x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3488 = Coupling(name = 'GC_3488',
                   value = '-((complex(0,1)*complexconjugate(clequ12x1x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3489 = Coupling(name = 'GC_3489',
                   value = '(complex(0,1)*complexconjugate(clequ12x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3490 = Coupling(name = 'GC_3490',
                   value = '-((complex(0,1)*complexconjugate(clequ12x1x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3491 = Coupling(name = 'GC_3491',
                   value = '(complex(0,1)*complexconjugate(clequ12x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3492 = Coupling(name = 'GC_3492',
                   value = '-((complex(0,1)*complexconjugate(clequ12x1x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3493 = Coupling(name = 'GC_3493',
                   value = '(complex(0,1)*complexconjugate(clequ12x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3494 = Coupling(name = 'GC_3494',
                   value = '-((complex(0,1)*complexconjugate(clequ12x1x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3495 = Coupling(name = 'GC_3495',
                   value = '(complex(0,1)*complexconjugate(clequ12x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3496 = Coupling(name = 'GC_3496',
                   value = '-((complex(0,1)*complexconjugate(clequ12x1x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3497 = Coupling(name = 'GC_3497',
                   value = '(complex(0,1)*complexconjugate(clequ12x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3498 = Coupling(name = 'GC_3498',
                   value = '-((complex(0,1)*complexconjugate(clequ12x1x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3499 = Coupling(name = 'GC_3499',
                   value = '(complex(0,1)*complexconjugate(clequ12x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3500 = Coupling(name = 'GC_3500',
                   value = '-((complex(0,1)*complexconjugate(clequ12x1x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3501 = Coupling(name = 'GC_3501',
                   value = '(complex(0,1)*complexconjugate(clequ12x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3502 = Coupling(name = 'GC_3502',
                   value = '-((complex(0,1)*complexconjugate(clequ12x1x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3503 = Coupling(name = 'GC_3503',
                   value = '(complex(0,1)*complexconjugate(clequ12x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3504 = Coupling(name = 'GC_3504',
                   value = '-((complex(0,1)*complexconjugate(clequ12x2x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3505 = Coupling(name = 'GC_3505',
                   value = '(complex(0,1)*complexconjugate(clequ12x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3506 = Coupling(name = 'GC_3506',
                   value = '-((complex(0,1)*complexconjugate(clequ12x2x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3507 = Coupling(name = 'GC_3507',
                   value = '(complex(0,1)*complexconjugate(clequ12x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3508 = Coupling(name = 'GC_3508',
                   value = '-((complex(0,1)*complexconjugate(clequ12x2x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3509 = Coupling(name = 'GC_3509',
                   value = '(complex(0,1)*complexconjugate(clequ12x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3510 = Coupling(name = 'GC_3510',
                   value = '-((complex(0,1)*complexconjugate(clequ12x2x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3511 = Coupling(name = 'GC_3511',
                   value = '(complex(0,1)*complexconjugate(clequ12x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3512 = Coupling(name = 'GC_3512',
                   value = '-((complex(0,1)*complexconjugate(clequ12x2x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3513 = Coupling(name = 'GC_3513',
                   value = '(complex(0,1)*complexconjugate(clequ12x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3514 = Coupling(name = 'GC_3514',
                   value = '-((complex(0,1)*complexconjugate(clequ12x2x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3515 = Coupling(name = 'GC_3515',
                   value = '(complex(0,1)*complexconjugate(clequ12x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3516 = Coupling(name = 'GC_3516',
                   value = '-((complex(0,1)*complexconjugate(clequ12x2x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3517 = Coupling(name = 'GC_3517',
                   value = '(complex(0,1)*complexconjugate(clequ12x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3518 = Coupling(name = 'GC_3518',
                   value = '-((complex(0,1)*complexconjugate(clequ12x2x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3519 = Coupling(name = 'GC_3519',
                   value = '(complex(0,1)*complexconjugate(clequ12x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3520 = Coupling(name = 'GC_3520',
                   value = '-((complex(0,1)*complexconjugate(clequ12x2x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3521 = Coupling(name = 'GC_3521',
                   value = '(complex(0,1)*complexconjugate(clequ12x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3522 = Coupling(name = 'GC_3522',
                   value = '-((complex(0,1)*complexconjugate(clequ12x3x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3523 = Coupling(name = 'GC_3523',
                   value = '(complex(0,1)*complexconjugate(clequ12x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3524 = Coupling(name = 'GC_3524',
                   value = '-((complex(0,1)*complexconjugate(clequ12x3x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3525 = Coupling(name = 'GC_3525',
                   value = '(complex(0,1)*complexconjugate(clequ12x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3526 = Coupling(name = 'GC_3526',
                   value = '-((complex(0,1)*complexconjugate(clequ12x3x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3527 = Coupling(name = 'GC_3527',
                   value = '(complex(0,1)*complexconjugate(clequ12x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3528 = Coupling(name = 'GC_3528',
                   value = '-((complex(0,1)*complexconjugate(clequ12x3x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3529 = Coupling(name = 'GC_3529',
                   value = '(complex(0,1)*complexconjugate(clequ12x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3530 = Coupling(name = 'GC_3530',
                   value = '-((complex(0,1)*complexconjugate(clequ12x3x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3531 = Coupling(name = 'GC_3531',
                   value = '(complex(0,1)*complexconjugate(clequ12x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3532 = Coupling(name = 'GC_3532',
                   value = '-((complex(0,1)*complexconjugate(clequ12x3x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3533 = Coupling(name = 'GC_3533',
                   value = '(complex(0,1)*complexconjugate(clequ12x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3534 = Coupling(name = 'GC_3534',
                   value = '-((complex(0,1)*complexconjugate(clequ12x3x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3535 = Coupling(name = 'GC_3535',
                   value = '(complex(0,1)*complexconjugate(clequ12x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3536 = Coupling(name = 'GC_3536',
                   value = '-((complex(0,1)*complexconjugate(clequ12x3x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3537 = Coupling(name = 'GC_3537',
                   value = '(complex(0,1)*complexconjugate(clequ12x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3538 = Coupling(name = 'GC_3538',
                   value = '-((complex(0,1)*complexconjugate(clequ12x3x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3539 = Coupling(name = 'GC_3539',
                   value = '(complex(0,1)*complexconjugate(clequ12x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3540 = Coupling(name = 'GC_3540',
                   value = '-((complex(0,1)*complexconjugate(clequ13x1x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3541 = Coupling(name = 'GC_3541',
                   value = '(complex(0,1)*complexconjugate(clequ13x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3542 = Coupling(name = 'GC_3542',
                   value = '-((complex(0,1)*complexconjugate(clequ13x1x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3543 = Coupling(name = 'GC_3543',
                   value = '(complex(0,1)*complexconjugate(clequ13x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3544 = Coupling(name = 'GC_3544',
                   value = '-((complex(0,1)*complexconjugate(clequ13x1x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3545 = Coupling(name = 'GC_3545',
                   value = '(complex(0,1)*complexconjugate(clequ13x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3546 = Coupling(name = 'GC_3546',
                   value = '-((complex(0,1)*complexconjugate(clequ13x1x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3547 = Coupling(name = 'GC_3547',
                   value = '(complex(0,1)*complexconjugate(clequ13x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3548 = Coupling(name = 'GC_3548',
                   value = '-((complex(0,1)*complexconjugate(clequ13x1x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3549 = Coupling(name = 'GC_3549',
                   value = '(complex(0,1)*complexconjugate(clequ13x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3550 = Coupling(name = 'GC_3550',
                   value = '-((complex(0,1)*complexconjugate(clequ13x1x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3551 = Coupling(name = 'GC_3551',
                   value = '(complex(0,1)*complexconjugate(clequ13x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3552 = Coupling(name = 'GC_3552',
                   value = '-((complex(0,1)*complexconjugate(clequ13x1x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3553 = Coupling(name = 'GC_3553',
                   value = '(complex(0,1)*complexconjugate(clequ13x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3554 = Coupling(name = 'GC_3554',
                   value = '-((complex(0,1)*complexconjugate(clequ13x1x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3555 = Coupling(name = 'GC_3555',
                   value = '(complex(0,1)*complexconjugate(clequ13x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3556 = Coupling(name = 'GC_3556',
                   value = '-((complex(0,1)*complexconjugate(clequ13x1x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3557 = Coupling(name = 'GC_3557',
                   value = '(complex(0,1)*complexconjugate(clequ13x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3558 = Coupling(name = 'GC_3558',
                   value = '-((complex(0,1)*complexconjugate(clequ13x2x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3559 = Coupling(name = 'GC_3559',
                   value = '(complex(0,1)*complexconjugate(clequ13x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3560 = Coupling(name = 'GC_3560',
                   value = '-((complex(0,1)*complexconjugate(clequ13x2x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3561 = Coupling(name = 'GC_3561',
                   value = '(complex(0,1)*complexconjugate(clequ13x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3562 = Coupling(name = 'GC_3562',
                   value = '-((complex(0,1)*complexconjugate(clequ13x2x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3563 = Coupling(name = 'GC_3563',
                   value = '(complex(0,1)*complexconjugate(clequ13x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3564 = Coupling(name = 'GC_3564',
                   value = '-((complex(0,1)*complexconjugate(clequ13x2x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3565 = Coupling(name = 'GC_3565',
                   value = '(complex(0,1)*complexconjugate(clequ13x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3566 = Coupling(name = 'GC_3566',
                   value = '-((complex(0,1)*complexconjugate(clequ13x2x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3567 = Coupling(name = 'GC_3567',
                   value = '(complex(0,1)*complexconjugate(clequ13x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3568 = Coupling(name = 'GC_3568',
                   value = '-((complex(0,1)*complexconjugate(clequ13x2x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3569 = Coupling(name = 'GC_3569',
                   value = '(complex(0,1)*complexconjugate(clequ13x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3570 = Coupling(name = 'GC_3570',
                   value = '-((complex(0,1)*complexconjugate(clequ13x2x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3571 = Coupling(name = 'GC_3571',
                   value = '(complex(0,1)*complexconjugate(clequ13x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3572 = Coupling(name = 'GC_3572',
                   value = '-((complex(0,1)*complexconjugate(clequ13x2x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3573 = Coupling(name = 'GC_3573',
                   value = '(complex(0,1)*complexconjugate(clequ13x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3574 = Coupling(name = 'GC_3574',
                   value = '-((complex(0,1)*complexconjugate(clequ13x2x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3575 = Coupling(name = 'GC_3575',
                   value = '(complex(0,1)*complexconjugate(clequ13x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3576 = Coupling(name = 'GC_3576',
                   value = '-((complex(0,1)*complexconjugate(clequ13x3x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3577 = Coupling(name = 'GC_3577',
                   value = '(complex(0,1)*complexconjugate(clequ13x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3578 = Coupling(name = 'GC_3578',
                   value = '-((complex(0,1)*complexconjugate(clequ13x3x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3579 = Coupling(name = 'GC_3579',
                   value = '(complex(0,1)*complexconjugate(clequ13x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3580 = Coupling(name = 'GC_3580',
                   value = '-((complex(0,1)*complexconjugate(clequ13x3x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3581 = Coupling(name = 'GC_3581',
                   value = '(complex(0,1)*complexconjugate(clequ13x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3582 = Coupling(name = 'GC_3582',
                   value = '-((complex(0,1)*complexconjugate(clequ13x3x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3583 = Coupling(name = 'GC_3583',
                   value = '(complex(0,1)*complexconjugate(clequ13x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3584 = Coupling(name = 'GC_3584',
                   value = '-((complex(0,1)*complexconjugate(clequ13x3x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3585 = Coupling(name = 'GC_3585',
                   value = '(complex(0,1)*complexconjugate(clequ13x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3586 = Coupling(name = 'GC_3586',
                   value = '-((complex(0,1)*complexconjugate(clequ13x3x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3587 = Coupling(name = 'GC_3587',
                   value = '(complex(0,1)*complexconjugate(clequ13x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3588 = Coupling(name = 'GC_3588',
                   value = '-((complex(0,1)*complexconjugate(clequ13x3x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3589 = Coupling(name = 'GC_3589',
                   value = '(complex(0,1)*complexconjugate(clequ13x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3590 = Coupling(name = 'GC_3590',
                   value = '-((complex(0,1)*complexconjugate(clequ13x3x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3591 = Coupling(name = 'GC_3591',
                   value = '(complex(0,1)*complexconjugate(clequ13x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3592 = Coupling(name = 'GC_3592',
                   value = '-((complex(0,1)*complexconjugate(clequ13x3x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3593 = Coupling(name = 'GC_3593',
                   value = '(complex(0,1)*complexconjugate(clequ13x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3594 = Coupling(name = 'GC_3594',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3595 = Coupling(name = 'GC_3595',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3596 = Coupling(name = 'GC_3596',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3597 = Coupling(name = 'GC_3597',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3598 = Coupling(name = 'GC_3598',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3599 = Coupling(name = 'GC_3599',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3600 = Coupling(name = 'GC_3600',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3601 = Coupling(name = 'GC_3601',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3602 = Coupling(name = 'GC_3602',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3603 = Coupling(name = 'GC_3603',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3604 = Coupling(name = 'GC_3604',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3605 = Coupling(name = 'GC_3605',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3606 = Coupling(name = 'GC_3606',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3607 = Coupling(name = 'GC_3607',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3608 = Coupling(name = 'GC_3608',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3609 = Coupling(name = 'GC_3609',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3610 = Coupling(name = 'GC_3610',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3611 = Coupling(name = 'GC_3611',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3612 = Coupling(name = 'GC_3612',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3613 = Coupling(name = 'GC_3613',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3614 = Coupling(name = 'GC_3614',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3615 = Coupling(name = 'GC_3615',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3616 = Coupling(name = 'GC_3616',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3617 = Coupling(name = 'GC_3617',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3618 = Coupling(name = 'GC_3618',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3619 = Coupling(name = 'GC_3619',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3620 = Coupling(name = 'GC_3620',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3621 = Coupling(name = 'GC_3621',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3622 = Coupling(name = 'GC_3622',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3623 = Coupling(name = 'GC_3623',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3624 = Coupling(name = 'GC_3624',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3625 = Coupling(name = 'GC_3625',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3626 = Coupling(name = 'GC_3626',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3627 = Coupling(name = 'GC_3627',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3628 = Coupling(name = 'GC_3628',
                   value = '-(complex(0,1)*complexconjugate(clequ31x1x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3629 = Coupling(name = 'GC_3629',
                   value = '(complex(0,1)*complexconjugate(clequ31x1x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3630 = Coupling(name = 'GC_3630',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3631 = Coupling(name = 'GC_3631',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3632 = Coupling(name = 'GC_3632',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3633 = Coupling(name = 'GC_3633',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3634 = Coupling(name = 'GC_3634',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3635 = Coupling(name = 'GC_3635',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3636 = Coupling(name = 'GC_3636',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3637 = Coupling(name = 'GC_3637',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3638 = Coupling(name = 'GC_3638',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3639 = Coupling(name = 'GC_3639',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3640 = Coupling(name = 'GC_3640',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3641 = Coupling(name = 'GC_3641',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3642 = Coupling(name = 'GC_3642',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3643 = Coupling(name = 'GC_3643',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3644 = Coupling(name = 'GC_3644',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3645 = Coupling(name = 'GC_3645',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3646 = Coupling(name = 'GC_3646',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3647 = Coupling(name = 'GC_3647',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3648 = Coupling(name = 'GC_3648',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3649 = Coupling(name = 'GC_3649',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3650 = Coupling(name = 'GC_3650',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3651 = Coupling(name = 'GC_3651',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3652 = Coupling(name = 'GC_3652',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3653 = Coupling(name = 'GC_3653',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3654 = Coupling(name = 'GC_3654',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3655 = Coupling(name = 'GC_3655',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3656 = Coupling(name = 'GC_3656',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3657 = Coupling(name = 'GC_3657',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3658 = Coupling(name = 'GC_3658',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3659 = Coupling(name = 'GC_3659',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3660 = Coupling(name = 'GC_3660',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3661 = Coupling(name = 'GC_3661',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3662 = Coupling(name = 'GC_3662',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3663 = Coupling(name = 'GC_3663',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3664 = Coupling(name = 'GC_3664',
                   value = '-(complex(0,1)*complexconjugate(clequ31x2x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3665 = Coupling(name = 'GC_3665',
                   value = '(complex(0,1)*complexconjugate(clequ31x2x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3666 = Coupling(name = 'GC_3666',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3667 = Coupling(name = 'GC_3667',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3668 = Coupling(name = 'GC_3668',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3669 = Coupling(name = 'GC_3669',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3670 = Coupling(name = 'GC_3670',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3671 = Coupling(name = 'GC_3671',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3672 = Coupling(name = 'GC_3672',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3673 = Coupling(name = 'GC_3673',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3674 = Coupling(name = 'GC_3674',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3675 = Coupling(name = 'GC_3675',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3676 = Coupling(name = 'GC_3676',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3677 = Coupling(name = 'GC_3677',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3678 = Coupling(name = 'GC_3678',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3679 = Coupling(name = 'GC_3679',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3680 = Coupling(name = 'GC_3680',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3681 = Coupling(name = 'GC_3681',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3682 = Coupling(name = 'GC_3682',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3683 = Coupling(name = 'GC_3683',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3684 = Coupling(name = 'GC_3684',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3685 = Coupling(name = 'GC_3685',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3686 = Coupling(name = 'GC_3686',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3687 = Coupling(name = 'GC_3687',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3688 = Coupling(name = 'GC_3688',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3689 = Coupling(name = 'GC_3689',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3690 = Coupling(name = 'GC_3690',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3691 = Coupling(name = 'GC_3691',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3692 = Coupling(name = 'GC_3692',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3693 = Coupling(name = 'GC_3693',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3694 = Coupling(name = 'GC_3694',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3695 = Coupling(name = 'GC_3695',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3696 = Coupling(name = 'GC_3696',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3697 = Coupling(name = 'GC_3697',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3698 = Coupling(name = 'GC_3698',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3699 = Coupling(name = 'GC_3699',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3700 = Coupling(name = 'GC_3700',
                   value = '-(complex(0,1)*complexconjugate(clequ31x3x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3701 = Coupling(name = 'GC_3701',
                   value = '(complex(0,1)*complexconjugate(clequ31x3x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3702 = Coupling(name = 'GC_3702',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3703 = Coupling(name = 'GC_3703',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3704 = Coupling(name = 'GC_3704',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3705 = Coupling(name = 'GC_3705',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3706 = Coupling(name = 'GC_3706',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3707 = Coupling(name = 'GC_3707',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3708 = Coupling(name = 'GC_3708',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3709 = Coupling(name = 'GC_3709',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3710 = Coupling(name = 'GC_3710',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3711 = Coupling(name = 'GC_3711',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3712 = Coupling(name = 'GC_3712',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3713 = Coupling(name = 'GC_3713',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3714 = Coupling(name = 'GC_3714',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3715 = Coupling(name = 'GC_3715',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3716 = Coupling(name = 'GC_3716',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3717 = Coupling(name = 'GC_3717',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3718 = Coupling(name = 'GC_3718',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3719 = Coupling(name = 'GC_3719',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3720 = Coupling(name = 'GC_3720',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3721 = Coupling(name = 'GC_3721',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3722 = Coupling(name = 'GC_3722',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3723 = Coupling(name = 'GC_3723',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3724 = Coupling(name = 'GC_3724',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3725 = Coupling(name = 'GC_3725',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3726 = Coupling(name = 'GC_3726',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3727 = Coupling(name = 'GC_3727',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3728 = Coupling(name = 'GC_3728',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3729 = Coupling(name = 'GC_3729',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3730 = Coupling(name = 'GC_3730',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3731 = Coupling(name = 'GC_3731',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3732 = Coupling(name = 'GC_3732',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3733 = Coupling(name = 'GC_3733',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3734 = Coupling(name = 'GC_3734',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3735 = Coupling(name = 'GC_3735',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3736 = Coupling(name = 'GC_3736',
                   value = '-(complex(0,1)*complexconjugate(clequ32x1x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3737 = Coupling(name = 'GC_3737',
                   value = '(complex(0,1)*complexconjugate(clequ32x1x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3738 = Coupling(name = 'GC_3738',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3739 = Coupling(name = 'GC_3739',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3740 = Coupling(name = 'GC_3740',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3741 = Coupling(name = 'GC_3741',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3742 = Coupling(name = 'GC_3742',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3743 = Coupling(name = 'GC_3743',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3744 = Coupling(name = 'GC_3744',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3745 = Coupling(name = 'GC_3745',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3746 = Coupling(name = 'GC_3746',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3747 = Coupling(name = 'GC_3747',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3748 = Coupling(name = 'GC_3748',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3749 = Coupling(name = 'GC_3749',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3750 = Coupling(name = 'GC_3750',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3751 = Coupling(name = 'GC_3751',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3752 = Coupling(name = 'GC_3752',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3753 = Coupling(name = 'GC_3753',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3754 = Coupling(name = 'GC_3754',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3755 = Coupling(name = 'GC_3755',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3756 = Coupling(name = 'GC_3756',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3757 = Coupling(name = 'GC_3757',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3758 = Coupling(name = 'GC_3758',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3759 = Coupling(name = 'GC_3759',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3760 = Coupling(name = 'GC_3760',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3761 = Coupling(name = 'GC_3761',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3762 = Coupling(name = 'GC_3762',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3763 = Coupling(name = 'GC_3763',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3764 = Coupling(name = 'GC_3764',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3765 = Coupling(name = 'GC_3765',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3766 = Coupling(name = 'GC_3766',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3767 = Coupling(name = 'GC_3767',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3768 = Coupling(name = 'GC_3768',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3769 = Coupling(name = 'GC_3769',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3770 = Coupling(name = 'GC_3770',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3771 = Coupling(name = 'GC_3771',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3772 = Coupling(name = 'GC_3772',
                   value = '-(complex(0,1)*complexconjugate(clequ32x2x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3773 = Coupling(name = 'GC_3773',
                   value = '(complex(0,1)*complexconjugate(clequ32x2x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3774 = Coupling(name = 'GC_3774',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3775 = Coupling(name = 'GC_3775',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3776 = Coupling(name = 'GC_3776',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3777 = Coupling(name = 'GC_3777',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3778 = Coupling(name = 'GC_3778',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3779 = Coupling(name = 'GC_3779',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3780 = Coupling(name = 'GC_3780',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3781 = Coupling(name = 'GC_3781',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3782 = Coupling(name = 'GC_3782',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3783 = Coupling(name = 'GC_3783',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3784 = Coupling(name = 'GC_3784',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3785 = Coupling(name = 'GC_3785',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3786 = Coupling(name = 'GC_3786',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3787 = Coupling(name = 'GC_3787',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3788 = Coupling(name = 'GC_3788',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3789 = Coupling(name = 'GC_3789',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3790 = Coupling(name = 'GC_3790',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3791 = Coupling(name = 'GC_3791',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3792 = Coupling(name = 'GC_3792',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3793 = Coupling(name = 'GC_3793',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3794 = Coupling(name = 'GC_3794',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3795 = Coupling(name = 'GC_3795',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3796 = Coupling(name = 'GC_3796',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3797 = Coupling(name = 'GC_3797',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3798 = Coupling(name = 'GC_3798',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3799 = Coupling(name = 'GC_3799',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3800 = Coupling(name = 'GC_3800',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3801 = Coupling(name = 'GC_3801',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3802 = Coupling(name = 'GC_3802',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3803 = Coupling(name = 'GC_3803',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3804 = Coupling(name = 'GC_3804',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3805 = Coupling(name = 'GC_3805',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3806 = Coupling(name = 'GC_3806',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3807 = Coupling(name = 'GC_3807',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3808 = Coupling(name = 'GC_3808',
                   value = '-(complex(0,1)*complexconjugate(clequ32x3x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3809 = Coupling(name = 'GC_3809',
                   value = '(complex(0,1)*complexconjugate(clequ32x3x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3810 = Coupling(name = 'GC_3810',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3811 = Coupling(name = 'GC_3811',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3812 = Coupling(name = 'GC_3812',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3813 = Coupling(name = 'GC_3813',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3814 = Coupling(name = 'GC_3814',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3815 = Coupling(name = 'GC_3815',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3816 = Coupling(name = 'GC_3816',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3817 = Coupling(name = 'GC_3817',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3818 = Coupling(name = 'GC_3818',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3819 = Coupling(name = 'GC_3819',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3820 = Coupling(name = 'GC_3820',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3821 = Coupling(name = 'GC_3821',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3822 = Coupling(name = 'GC_3822',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3823 = Coupling(name = 'GC_3823',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3824 = Coupling(name = 'GC_3824',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3825 = Coupling(name = 'GC_3825',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3826 = Coupling(name = 'GC_3826',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3827 = Coupling(name = 'GC_3827',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3828 = Coupling(name = 'GC_3828',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3829 = Coupling(name = 'GC_3829',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3830 = Coupling(name = 'GC_3830',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3831 = Coupling(name = 'GC_3831',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3832 = Coupling(name = 'GC_3832',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3833 = Coupling(name = 'GC_3833',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3834 = Coupling(name = 'GC_3834',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3835 = Coupling(name = 'GC_3835',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3836 = Coupling(name = 'GC_3836',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3837 = Coupling(name = 'GC_3837',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3838 = Coupling(name = 'GC_3838',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3839 = Coupling(name = 'GC_3839',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3840 = Coupling(name = 'GC_3840',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3841 = Coupling(name = 'GC_3841',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3842 = Coupling(name = 'GC_3842',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3843 = Coupling(name = 'GC_3843',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3844 = Coupling(name = 'GC_3844',
                   value = '-(complex(0,1)*complexconjugate(clequ33x1x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3845 = Coupling(name = 'GC_3845',
                   value = '(complex(0,1)*complexconjugate(clequ33x1x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3846 = Coupling(name = 'GC_3846',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3847 = Coupling(name = 'GC_3847',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3848 = Coupling(name = 'GC_3848',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3849 = Coupling(name = 'GC_3849',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3850 = Coupling(name = 'GC_3850',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3851 = Coupling(name = 'GC_3851',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3852 = Coupling(name = 'GC_3852',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3853 = Coupling(name = 'GC_3853',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3854 = Coupling(name = 'GC_3854',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3855 = Coupling(name = 'GC_3855',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3856 = Coupling(name = 'GC_3856',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3857 = Coupling(name = 'GC_3857',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3858 = Coupling(name = 'GC_3858',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3859 = Coupling(name = 'GC_3859',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3860 = Coupling(name = 'GC_3860',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3861 = Coupling(name = 'GC_3861',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3862 = Coupling(name = 'GC_3862',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3863 = Coupling(name = 'GC_3863',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3864 = Coupling(name = 'GC_3864',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3865 = Coupling(name = 'GC_3865',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3866 = Coupling(name = 'GC_3866',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3867 = Coupling(name = 'GC_3867',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3868 = Coupling(name = 'GC_3868',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3869 = Coupling(name = 'GC_3869',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3870 = Coupling(name = 'GC_3870',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3871 = Coupling(name = 'GC_3871',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3872 = Coupling(name = 'GC_3872',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3873 = Coupling(name = 'GC_3873',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3874 = Coupling(name = 'GC_3874',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3875 = Coupling(name = 'GC_3875',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3876 = Coupling(name = 'GC_3876',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3877 = Coupling(name = 'GC_3877',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3878 = Coupling(name = 'GC_3878',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3879 = Coupling(name = 'GC_3879',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3880 = Coupling(name = 'GC_3880',
                   value = '-(complex(0,1)*complexconjugate(clequ33x2x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3881 = Coupling(name = 'GC_3881',
                   value = '(complex(0,1)*complexconjugate(clequ33x2x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3882 = Coupling(name = 'GC_3882',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3883 = Coupling(name = 'GC_3883',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x1x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3884 = Coupling(name = 'GC_3884',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3885 = Coupling(name = 'GC_3885',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x1x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3886 = Coupling(name = 'GC_3886',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3887 = Coupling(name = 'GC_3887',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x1x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3888 = Coupling(name = 'GC_3888',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3889 = Coupling(name = 'GC_3889',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x1x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3890 = Coupling(name = 'GC_3890',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3891 = Coupling(name = 'GC_3891',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x1x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3892 = Coupling(name = 'GC_3892',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3893 = Coupling(name = 'GC_3893',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x1x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3894 = Coupling(name = 'GC_3894',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3895 = Coupling(name = 'GC_3895',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x2x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3896 = Coupling(name = 'GC_3896',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3897 = Coupling(name = 'GC_3897',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x2x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3898 = Coupling(name = 'GC_3898',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3899 = Coupling(name = 'GC_3899',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x2x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3900 = Coupling(name = 'GC_3900',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3901 = Coupling(name = 'GC_3901',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x2x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3902 = Coupling(name = 'GC_3902',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3903 = Coupling(name = 'GC_3903',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x2x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3904 = Coupling(name = 'GC_3904',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3905 = Coupling(name = 'GC_3905',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x2x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3906 = Coupling(name = 'GC_3906',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3907 = Coupling(name = 'GC_3907',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x3x1))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3908 = Coupling(name = 'GC_3908',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3909 = Coupling(name = 'GC_3909',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x3x1))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3910 = Coupling(name = 'GC_3910',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3911 = Coupling(name = 'GC_3911',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x3x2))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3912 = Coupling(name = 'GC_3912',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3913 = Coupling(name = 'GC_3913',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x3x2))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3914 = Coupling(name = 'GC_3914',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3915 = Coupling(name = 'GC_3915',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x3x3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3916 = Coupling(name = 'GC_3916',
                   value = '-(complex(0,1)*complexconjugate(clequ33x3x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3917 = Coupling(name = 'GC_3917',
                   value = '(complex(0,1)*complexconjugate(clequ33x3x3x3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3918 = Coupling(name = 'GC_3918',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x1x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3919 = Coupling(name = 'GC_3919',
                   value = '(complex(0,1)*complexconjugate(cquqd11x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3920 = Coupling(name = 'GC_3920',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x1x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3921 = Coupling(name = 'GC_3921',
                   value = '(complex(0,1)*complexconjugate(cquqd11x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3922 = Coupling(name = 'GC_3922',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x1x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3923 = Coupling(name = 'GC_3923',
                   value = '(complex(0,1)*complexconjugate(cquqd11x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3924 = Coupling(name = 'GC_3924',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x1x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3925 = Coupling(name = 'GC_3925',
                   value = '(complex(0,1)*complexconjugate(cquqd11x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3926 = Coupling(name = 'GC_3926',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x1x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3927 = Coupling(name = 'GC_3927',
                   value = '(complex(0,1)*complexconjugate(cquqd11x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3928 = Coupling(name = 'GC_3928',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x1x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3929 = Coupling(name = 'GC_3929',
                   value = '(complex(0,1)*complexconjugate(cquqd11x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3930 = Coupling(name = 'GC_3930',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x1x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3931 = Coupling(name = 'GC_3931',
                   value = '(complex(0,1)*complexconjugate(cquqd11x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3932 = Coupling(name = 'GC_3932',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x1x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3933 = Coupling(name = 'GC_3933',
                   value = '(complex(0,1)*complexconjugate(cquqd11x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3934 = Coupling(name = 'GC_3934',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x1x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3935 = Coupling(name = 'GC_3935',
                   value = '(complex(0,1)*complexconjugate(cquqd11x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3936 = Coupling(name = 'GC_3936',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x2x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3937 = Coupling(name = 'GC_3937',
                   value = '(complex(0,1)*complexconjugate(cquqd11x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3938 = Coupling(name = 'GC_3938',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x2x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3939 = Coupling(name = 'GC_3939',
                   value = '(complex(0,1)*complexconjugate(cquqd11x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3940 = Coupling(name = 'GC_3940',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x2x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3941 = Coupling(name = 'GC_3941',
                   value = '(complex(0,1)*complexconjugate(cquqd11x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3942 = Coupling(name = 'GC_3942',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x2x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3943 = Coupling(name = 'GC_3943',
                   value = '(complex(0,1)*complexconjugate(cquqd11x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3944 = Coupling(name = 'GC_3944',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x2x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3945 = Coupling(name = 'GC_3945',
                   value = '(complex(0,1)*complexconjugate(cquqd11x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3946 = Coupling(name = 'GC_3946',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x2x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3947 = Coupling(name = 'GC_3947',
                   value = '(complex(0,1)*complexconjugate(cquqd11x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3948 = Coupling(name = 'GC_3948',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x2x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3949 = Coupling(name = 'GC_3949',
                   value = '(complex(0,1)*complexconjugate(cquqd11x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3950 = Coupling(name = 'GC_3950',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x2x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3951 = Coupling(name = 'GC_3951',
                   value = '(complex(0,1)*complexconjugate(cquqd11x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3952 = Coupling(name = 'GC_3952',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x2x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3953 = Coupling(name = 'GC_3953',
                   value = '(complex(0,1)*complexconjugate(cquqd11x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3954 = Coupling(name = 'GC_3954',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x3x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3955 = Coupling(name = 'GC_3955',
                   value = '(complex(0,1)*complexconjugate(cquqd11x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3956 = Coupling(name = 'GC_3956',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x3x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3957 = Coupling(name = 'GC_3957',
                   value = '(complex(0,1)*complexconjugate(cquqd11x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3958 = Coupling(name = 'GC_3958',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x3x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3959 = Coupling(name = 'GC_3959',
                   value = '(complex(0,1)*complexconjugate(cquqd11x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3960 = Coupling(name = 'GC_3960',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x3x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3961 = Coupling(name = 'GC_3961',
                   value = '(complex(0,1)*complexconjugate(cquqd11x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3962 = Coupling(name = 'GC_3962',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x3x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3963 = Coupling(name = 'GC_3963',
                   value = '(complex(0,1)*complexconjugate(cquqd11x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3964 = Coupling(name = 'GC_3964',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x3x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3965 = Coupling(name = 'GC_3965',
                   value = '(complex(0,1)*complexconjugate(cquqd11x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3966 = Coupling(name = 'GC_3966',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x3x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3967 = Coupling(name = 'GC_3967',
                   value = '(complex(0,1)*complexconjugate(cquqd11x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3968 = Coupling(name = 'GC_3968',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x3x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3969 = Coupling(name = 'GC_3969',
                   value = '(complex(0,1)*complexconjugate(cquqd11x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3970 = Coupling(name = 'GC_3970',
                   value = '-((complex(0,1)*complexconjugate(cquqd11x3x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3971 = Coupling(name = 'GC_3971',
                   value = '(complex(0,1)*complexconjugate(cquqd11x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3972 = Coupling(name = 'GC_3972',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x1x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3973 = Coupling(name = 'GC_3973',
                   value = '(complex(0,1)*complexconjugate(cquqd12x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3974 = Coupling(name = 'GC_3974',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x1x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3975 = Coupling(name = 'GC_3975',
                   value = '(complex(0,1)*complexconjugate(cquqd12x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3976 = Coupling(name = 'GC_3976',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x1x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3977 = Coupling(name = 'GC_3977',
                   value = '(complex(0,1)*complexconjugate(cquqd12x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3978 = Coupling(name = 'GC_3978',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x1x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3979 = Coupling(name = 'GC_3979',
                   value = '(complex(0,1)*complexconjugate(cquqd12x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3980 = Coupling(name = 'GC_3980',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x1x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3981 = Coupling(name = 'GC_3981',
                   value = '(complex(0,1)*complexconjugate(cquqd12x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3982 = Coupling(name = 'GC_3982',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x1x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3983 = Coupling(name = 'GC_3983',
                   value = '(complex(0,1)*complexconjugate(cquqd12x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3984 = Coupling(name = 'GC_3984',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x1x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3985 = Coupling(name = 'GC_3985',
                   value = '(complex(0,1)*complexconjugate(cquqd12x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3986 = Coupling(name = 'GC_3986',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x1x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3987 = Coupling(name = 'GC_3987',
                   value = '(complex(0,1)*complexconjugate(cquqd12x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3988 = Coupling(name = 'GC_3988',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x1x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3989 = Coupling(name = 'GC_3989',
                   value = '(complex(0,1)*complexconjugate(cquqd12x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3990 = Coupling(name = 'GC_3990',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x2x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3991 = Coupling(name = 'GC_3991',
                   value = '(complex(0,1)*complexconjugate(cquqd12x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3992 = Coupling(name = 'GC_3992',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x2x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3993 = Coupling(name = 'GC_3993',
                   value = '(complex(0,1)*complexconjugate(cquqd12x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3994 = Coupling(name = 'GC_3994',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x2x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3995 = Coupling(name = 'GC_3995',
                   value = '(complex(0,1)*complexconjugate(cquqd12x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3996 = Coupling(name = 'GC_3996',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x2x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3997 = Coupling(name = 'GC_3997',
                   value = '(complex(0,1)*complexconjugate(cquqd12x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_3998 = Coupling(name = 'GC_3998',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x2x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_3999 = Coupling(name = 'GC_3999',
                   value = '(complex(0,1)*complexconjugate(cquqd12x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4000 = Coupling(name = 'GC_4000',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x2x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4001 = Coupling(name = 'GC_4001',
                   value = '(complex(0,1)*complexconjugate(cquqd12x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4002 = Coupling(name = 'GC_4002',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x2x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4003 = Coupling(name = 'GC_4003',
                   value = '(complex(0,1)*complexconjugate(cquqd12x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4004 = Coupling(name = 'GC_4004',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x2x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4005 = Coupling(name = 'GC_4005',
                   value = '(complex(0,1)*complexconjugate(cquqd12x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4006 = Coupling(name = 'GC_4006',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x2x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4007 = Coupling(name = 'GC_4007',
                   value = '(complex(0,1)*complexconjugate(cquqd12x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4008 = Coupling(name = 'GC_4008',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x3x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4009 = Coupling(name = 'GC_4009',
                   value = '(complex(0,1)*complexconjugate(cquqd12x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4010 = Coupling(name = 'GC_4010',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x3x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4011 = Coupling(name = 'GC_4011',
                   value = '(complex(0,1)*complexconjugate(cquqd12x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4012 = Coupling(name = 'GC_4012',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x3x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4013 = Coupling(name = 'GC_4013',
                   value = '(complex(0,1)*complexconjugate(cquqd12x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4014 = Coupling(name = 'GC_4014',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x3x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4015 = Coupling(name = 'GC_4015',
                   value = '(complex(0,1)*complexconjugate(cquqd12x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4016 = Coupling(name = 'GC_4016',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x3x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4017 = Coupling(name = 'GC_4017',
                   value = '(complex(0,1)*complexconjugate(cquqd12x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4018 = Coupling(name = 'GC_4018',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x3x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4019 = Coupling(name = 'GC_4019',
                   value = '(complex(0,1)*complexconjugate(cquqd12x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4020 = Coupling(name = 'GC_4020',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x3x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4021 = Coupling(name = 'GC_4021',
                   value = '(complex(0,1)*complexconjugate(cquqd12x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4022 = Coupling(name = 'GC_4022',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x3x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4023 = Coupling(name = 'GC_4023',
                   value = '(complex(0,1)*complexconjugate(cquqd12x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4024 = Coupling(name = 'GC_4024',
                   value = '-((complex(0,1)*complexconjugate(cquqd12x3x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4025 = Coupling(name = 'GC_4025',
                   value = '(complex(0,1)*complexconjugate(cquqd12x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4026 = Coupling(name = 'GC_4026',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x1x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4027 = Coupling(name = 'GC_4027',
                   value = '(complex(0,1)*complexconjugate(cquqd13x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4028 = Coupling(name = 'GC_4028',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x1x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4029 = Coupling(name = 'GC_4029',
                   value = '(complex(0,1)*complexconjugate(cquqd13x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4030 = Coupling(name = 'GC_4030',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x1x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4031 = Coupling(name = 'GC_4031',
                   value = '(complex(0,1)*complexconjugate(cquqd13x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4032 = Coupling(name = 'GC_4032',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x1x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4033 = Coupling(name = 'GC_4033',
                   value = '(complex(0,1)*complexconjugate(cquqd13x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4034 = Coupling(name = 'GC_4034',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x1x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4035 = Coupling(name = 'GC_4035',
                   value = '(complex(0,1)*complexconjugate(cquqd13x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4036 = Coupling(name = 'GC_4036',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x1x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4037 = Coupling(name = 'GC_4037',
                   value = '(complex(0,1)*complexconjugate(cquqd13x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4038 = Coupling(name = 'GC_4038',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x1x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4039 = Coupling(name = 'GC_4039',
                   value = '(complex(0,1)*complexconjugate(cquqd13x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4040 = Coupling(name = 'GC_4040',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x1x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4041 = Coupling(name = 'GC_4041',
                   value = '(complex(0,1)*complexconjugate(cquqd13x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4042 = Coupling(name = 'GC_4042',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x1x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4043 = Coupling(name = 'GC_4043',
                   value = '(complex(0,1)*complexconjugate(cquqd13x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4044 = Coupling(name = 'GC_4044',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x2x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4045 = Coupling(name = 'GC_4045',
                   value = '(complex(0,1)*complexconjugate(cquqd13x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4046 = Coupling(name = 'GC_4046',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x2x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4047 = Coupling(name = 'GC_4047',
                   value = '(complex(0,1)*complexconjugate(cquqd13x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4048 = Coupling(name = 'GC_4048',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x2x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4049 = Coupling(name = 'GC_4049',
                   value = '(complex(0,1)*complexconjugate(cquqd13x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4050 = Coupling(name = 'GC_4050',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x2x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4051 = Coupling(name = 'GC_4051',
                   value = '(complex(0,1)*complexconjugate(cquqd13x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4052 = Coupling(name = 'GC_4052',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x2x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4053 = Coupling(name = 'GC_4053',
                   value = '(complex(0,1)*complexconjugate(cquqd13x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4054 = Coupling(name = 'GC_4054',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x2x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4055 = Coupling(name = 'GC_4055',
                   value = '(complex(0,1)*complexconjugate(cquqd13x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4056 = Coupling(name = 'GC_4056',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x2x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4057 = Coupling(name = 'GC_4057',
                   value = '(complex(0,1)*complexconjugate(cquqd13x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4058 = Coupling(name = 'GC_4058',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x2x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4059 = Coupling(name = 'GC_4059',
                   value = '(complex(0,1)*complexconjugate(cquqd13x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4060 = Coupling(name = 'GC_4060',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x2x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4061 = Coupling(name = 'GC_4061',
                   value = '(complex(0,1)*complexconjugate(cquqd13x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4062 = Coupling(name = 'GC_4062',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x3x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4063 = Coupling(name = 'GC_4063',
                   value = '(complex(0,1)*complexconjugate(cquqd13x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4064 = Coupling(name = 'GC_4064',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x3x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4065 = Coupling(name = 'GC_4065',
                   value = '(complex(0,1)*complexconjugate(cquqd13x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4066 = Coupling(name = 'GC_4066',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x3x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4067 = Coupling(name = 'GC_4067',
                   value = '(complex(0,1)*complexconjugate(cquqd13x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4068 = Coupling(name = 'GC_4068',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x3x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4069 = Coupling(name = 'GC_4069',
                   value = '(complex(0,1)*complexconjugate(cquqd13x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4070 = Coupling(name = 'GC_4070',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x3x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4071 = Coupling(name = 'GC_4071',
                   value = '(complex(0,1)*complexconjugate(cquqd13x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4072 = Coupling(name = 'GC_4072',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x3x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4073 = Coupling(name = 'GC_4073',
                   value = '(complex(0,1)*complexconjugate(cquqd13x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4074 = Coupling(name = 'GC_4074',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x3x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4075 = Coupling(name = 'GC_4075',
                   value = '(complex(0,1)*complexconjugate(cquqd13x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4076 = Coupling(name = 'GC_4076',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x3x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4077 = Coupling(name = 'GC_4077',
                   value = '(complex(0,1)*complexconjugate(cquqd13x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4078 = Coupling(name = 'GC_4078',
                   value = '-((complex(0,1)*complexconjugate(cquqd13x3x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4079 = Coupling(name = 'GC_4079',
                   value = '(complex(0,1)*complexconjugate(cquqd13x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4080 = Coupling(name = 'GC_4080',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x1x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4081 = Coupling(name = 'GC_4081',
                   value = '(complex(0,1)*complexconjugate(cquqd81x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4082 = Coupling(name = 'GC_4082',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x1x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4083 = Coupling(name = 'GC_4083',
                   value = '(complex(0,1)*complexconjugate(cquqd81x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4084 = Coupling(name = 'GC_4084',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x1x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4085 = Coupling(name = 'GC_4085',
                   value = '(complex(0,1)*complexconjugate(cquqd81x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4086 = Coupling(name = 'GC_4086',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x1x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4087 = Coupling(name = 'GC_4087',
                   value = '(complex(0,1)*complexconjugate(cquqd81x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4088 = Coupling(name = 'GC_4088',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x1x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4089 = Coupling(name = 'GC_4089',
                   value = '(complex(0,1)*complexconjugate(cquqd81x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4090 = Coupling(name = 'GC_4090',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x1x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4091 = Coupling(name = 'GC_4091',
                   value = '(complex(0,1)*complexconjugate(cquqd81x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4092 = Coupling(name = 'GC_4092',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x1x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4093 = Coupling(name = 'GC_4093',
                   value = '(complex(0,1)*complexconjugate(cquqd81x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4094 = Coupling(name = 'GC_4094',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x1x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4095 = Coupling(name = 'GC_4095',
                   value = '(complex(0,1)*complexconjugate(cquqd81x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4096 = Coupling(name = 'GC_4096',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x1x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4097 = Coupling(name = 'GC_4097',
                   value = '(complex(0,1)*complexconjugate(cquqd81x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4098 = Coupling(name = 'GC_4098',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x2x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4099 = Coupling(name = 'GC_4099',
                   value = '(complex(0,1)*complexconjugate(cquqd81x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4100 = Coupling(name = 'GC_4100',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x2x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4101 = Coupling(name = 'GC_4101',
                   value = '(complex(0,1)*complexconjugate(cquqd81x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4102 = Coupling(name = 'GC_4102',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x2x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4103 = Coupling(name = 'GC_4103',
                   value = '(complex(0,1)*complexconjugate(cquqd81x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4104 = Coupling(name = 'GC_4104',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x2x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4105 = Coupling(name = 'GC_4105',
                   value = '(complex(0,1)*complexconjugate(cquqd81x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4106 = Coupling(name = 'GC_4106',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x2x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4107 = Coupling(name = 'GC_4107',
                   value = '(complex(0,1)*complexconjugate(cquqd81x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4108 = Coupling(name = 'GC_4108',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x2x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4109 = Coupling(name = 'GC_4109',
                   value = '(complex(0,1)*complexconjugate(cquqd81x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4110 = Coupling(name = 'GC_4110',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x2x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4111 = Coupling(name = 'GC_4111',
                   value = '(complex(0,1)*complexconjugate(cquqd81x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4112 = Coupling(name = 'GC_4112',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x2x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4113 = Coupling(name = 'GC_4113',
                   value = '(complex(0,1)*complexconjugate(cquqd81x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4114 = Coupling(name = 'GC_4114',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x2x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4115 = Coupling(name = 'GC_4115',
                   value = '(complex(0,1)*complexconjugate(cquqd81x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4116 = Coupling(name = 'GC_4116',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x3x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4117 = Coupling(name = 'GC_4117',
                   value = '(complex(0,1)*complexconjugate(cquqd81x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4118 = Coupling(name = 'GC_4118',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x3x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4119 = Coupling(name = 'GC_4119',
                   value = '(complex(0,1)*complexconjugate(cquqd81x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4120 = Coupling(name = 'GC_4120',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x3x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4121 = Coupling(name = 'GC_4121',
                   value = '(complex(0,1)*complexconjugate(cquqd81x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4122 = Coupling(name = 'GC_4122',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x3x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4123 = Coupling(name = 'GC_4123',
                   value = '(complex(0,1)*complexconjugate(cquqd81x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4124 = Coupling(name = 'GC_4124',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x3x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4125 = Coupling(name = 'GC_4125',
                   value = '(complex(0,1)*complexconjugate(cquqd81x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4126 = Coupling(name = 'GC_4126',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x3x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4127 = Coupling(name = 'GC_4127',
                   value = '(complex(0,1)*complexconjugate(cquqd81x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4128 = Coupling(name = 'GC_4128',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x3x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4129 = Coupling(name = 'GC_4129',
                   value = '(complex(0,1)*complexconjugate(cquqd81x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4130 = Coupling(name = 'GC_4130',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x3x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4131 = Coupling(name = 'GC_4131',
                   value = '(complex(0,1)*complexconjugate(cquqd81x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4132 = Coupling(name = 'GC_4132',
                   value = '-((complex(0,1)*complexconjugate(cquqd81x3x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4133 = Coupling(name = 'GC_4133',
                   value = '(complex(0,1)*complexconjugate(cquqd81x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4134 = Coupling(name = 'GC_4134',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x1x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4135 = Coupling(name = 'GC_4135',
                   value = '(complex(0,1)*complexconjugate(cquqd82x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4136 = Coupling(name = 'GC_4136',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x1x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4137 = Coupling(name = 'GC_4137',
                   value = '(complex(0,1)*complexconjugate(cquqd82x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4138 = Coupling(name = 'GC_4138',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x1x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4139 = Coupling(name = 'GC_4139',
                   value = '(complex(0,1)*complexconjugate(cquqd82x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4140 = Coupling(name = 'GC_4140',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x1x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4141 = Coupling(name = 'GC_4141',
                   value = '(complex(0,1)*complexconjugate(cquqd82x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4142 = Coupling(name = 'GC_4142',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x1x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4143 = Coupling(name = 'GC_4143',
                   value = '(complex(0,1)*complexconjugate(cquqd82x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4144 = Coupling(name = 'GC_4144',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x1x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4145 = Coupling(name = 'GC_4145',
                   value = '(complex(0,1)*complexconjugate(cquqd82x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4146 = Coupling(name = 'GC_4146',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x1x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4147 = Coupling(name = 'GC_4147',
                   value = '(complex(0,1)*complexconjugate(cquqd82x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4148 = Coupling(name = 'GC_4148',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x1x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4149 = Coupling(name = 'GC_4149',
                   value = '(complex(0,1)*complexconjugate(cquqd82x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4150 = Coupling(name = 'GC_4150',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x1x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4151 = Coupling(name = 'GC_4151',
                   value = '(complex(0,1)*complexconjugate(cquqd82x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4152 = Coupling(name = 'GC_4152',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x2x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4153 = Coupling(name = 'GC_4153',
                   value = '(complex(0,1)*complexconjugate(cquqd82x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4154 = Coupling(name = 'GC_4154',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x2x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4155 = Coupling(name = 'GC_4155',
                   value = '(complex(0,1)*complexconjugate(cquqd82x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4156 = Coupling(name = 'GC_4156',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x2x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4157 = Coupling(name = 'GC_4157',
                   value = '(complex(0,1)*complexconjugate(cquqd82x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4158 = Coupling(name = 'GC_4158',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x2x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4159 = Coupling(name = 'GC_4159',
                   value = '(complex(0,1)*complexconjugate(cquqd82x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4160 = Coupling(name = 'GC_4160',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x2x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4161 = Coupling(name = 'GC_4161',
                   value = '(complex(0,1)*complexconjugate(cquqd82x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4162 = Coupling(name = 'GC_4162',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x2x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4163 = Coupling(name = 'GC_4163',
                   value = '(complex(0,1)*complexconjugate(cquqd82x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4164 = Coupling(name = 'GC_4164',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x2x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4165 = Coupling(name = 'GC_4165',
                   value = '(complex(0,1)*complexconjugate(cquqd82x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4166 = Coupling(name = 'GC_4166',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x2x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4167 = Coupling(name = 'GC_4167',
                   value = '(complex(0,1)*complexconjugate(cquqd82x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4168 = Coupling(name = 'GC_4168',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x2x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4169 = Coupling(name = 'GC_4169',
                   value = '(complex(0,1)*complexconjugate(cquqd82x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4170 = Coupling(name = 'GC_4170',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x3x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4171 = Coupling(name = 'GC_4171',
                   value = '(complex(0,1)*complexconjugate(cquqd82x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4172 = Coupling(name = 'GC_4172',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x3x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4173 = Coupling(name = 'GC_4173',
                   value = '(complex(0,1)*complexconjugate(cquqd82x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4174 = Coupling(name = 'GC_4174',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x3x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4175 = Coupling(name = 'GC_4175',
                   value = '(complex(0,1)*complexconjugate(cquqd82x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4176 = Coupling(name = 'GC_4176',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x3x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4177 = Coupling(name = 'GC_4177',
                   value = '(complex(0,1)*complexconjugate(cquqd82x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4178 = Coupling(name = 'GC_4178',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x3x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4179 = Coupling(name = 'GC_4179',
                   value = '(complex(0,1)*complexconjugate(cquqd82x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4180 = Coupling(name = 'GC_4180',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x3x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4181 = Coupling(name = 'GC_4181',
                   value = '(complex(0,1)*complexconjugate(cquqd82x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4182 = Coupling(name = 'GC_4182',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x3x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4183 = Coupling(name = 'GC_4183',
                   value = '(complex(0,1)*complexconjugate(cquqd82x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4184 = Coupling(name = 'GC_4184',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x3x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4185 = Coupling(name = 'GC_4185',
                   value = '(complex(0,1)*complexconjugate(cquqd82x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4186 = Coupling(name = 'GC_4186',
                   value = '-((complex(0,1)*complexconjugate(cquqd82x3x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4187 = Coupling(name = 'GC_4187',
                   value = '(complex(0,1)*complexconjugate(cquqd82x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4188 = Coupling(name = 'GC_4188',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x1x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4189 = Coupling(name = 'GC_4189',
                   value = '(complex(0,1)*complexconjugate(cquqd83x1x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4190 = Coupling(name = 'GC_4190',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x1x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4191 = Coupling(name = 'GC_4191',
                   value = '(complex(0,1)*complexconjugate(cquqd83x1x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4192 = Coupling(name = 'GC_4192',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x1x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4193 = Coupling(name = 'GC_4193',
                   value = '(complex(0,1)*complexconjugate(cquqd83x1x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4194 = Coupling(name = 'GC_4194',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x1x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4195 = Coupling(name = 'GC_4195',
                   value = '(complex(0,1)*complexconjugate(cquqd83x1x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4196 = Coupling(name = 'GC_4196',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x1x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4197 = Coupling(name = 'GC_4197',
                   value = '(complex(0,1)*complexconjugate(cquqd83x1x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4198 = Coupling(name = 'GC_4198',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x1x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4199 = Coupling(name = 'GC_4199',
                   value = '(complex(0,1)*complexconjugate(cquqd83x1x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4200 = Coupling(name = 'GC_4200',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x1x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4201 = Coupling(name = 'GC_4201',
                   value = '(complex(0,1)*complexconjugate(cquqd83x1x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4202 = Coupling(name = 'GC_4202',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x1x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4203 = Coupling(name = 'GC_4203',
                   value = '(complex(0,1)*complexconjugate(cquqd83x1x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4204 = Coupling(name = 'GC_4204',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x1x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4205 = Coupling(name = 'GC_4205',
                   value = '(complex(0,1)*complexconjugate(cquqd83x1x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4206 = Coupling(name = 'GC_4206',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x2x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4207 = Coupling(name = 'GC_4207',
                   value = '(complex(0,1)*complexconjugate(cquqd83x2x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4208 = Coupling(name = 'GC_4208',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x2x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4209 = Coupling(name = 'GC_4209',
                   value = '(complex(0,1)*complexconjugate(cquqd83x2x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4210 = Coupling(name = 'GC_4210',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x2x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4211 = Coupling(name = 'GC_4211',
                   value = '(complex(0,1)*complexconjugate(cquqd83x2x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4212 = Coupling(name = 'GC_4212',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x2x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4213 = Coupling(name = 'GC_4213',
                   value = '(complex(0,1)*complexconjugate(cquqd83x2x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4214 = Coupling(name = 'GC_4214',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x2x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4215 = Coupling(name = 'GC_4215',
                   value = '(complex(0,1)*complexconjugate(cquqd83x2x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4216 = Coupling(name = 'GC_4216',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x2x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4217 = Coupling(name = 'GC_4217',
                   value = '(complex(0,1)*complexconjugate(cquqd83x2x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4218 = Coupling(name = 'GC_4218',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x2x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4219 = Coupling(name = 'GC_4219',
                   value = '(complex(0,1)*complexconjugate(cquqd83x2x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4220 = Coupling(name = 'GC_4220',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x2x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4221 = Coupling(name = 'GC_4221',
                   value = '(complex(0,1)*complexconjugate(cquqd83x2x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4222 = Coupling(name = 'GC_4222',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x2x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4223 = Coupling(name = 'GC_4223',
                   value = '(complex(0,1)*complexconjugate(cquqd83x2x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4224 = Coupling(name = 'GC_4224',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x3x1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4225 = Coupling(name = 'GC_4225',
                   value = '(complex(0,1)*complexconjugate(cquqd83x3x1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4226 = Coupling(name = 'GC_4226',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x3x1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4227 = Coupling(name = 'GC_4227',
                   value = '(complex(0,1)*complexconjugate(cquqd83x3x1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4228 = Coupling(name = 'GC_4228',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x3x1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4229 = Coupling(name = 'GC_4229',
                   value = '(complex(0,1)*complexconjugate(cquqd83x3x1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4230 = Coupling(name = 'GC_4230',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x3x2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4231 = Coupling(name = 'GC_4231',
                   value = '(complex(0,1)*complexconjugate(cquqd83x3x2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4232 = Coupling(name = 'GC_4232',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x3x2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4233 = Coupling(name = 'GC_4233',
                   value = '(complex(0,1)*complexconjugate(cquqd83x3x2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4234 = Coupling(name = 'GC_4234',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x3x2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4235 = Coupling(name = 'GC_4235',
                   value = '(complex(0,1)*complexconjugate(cquqd83x3x2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4236 = Coupling(name = 'GC_4236',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x3x3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4237 = Coupling(name = 'GC_4237',
                   value = '(complex(0,1)*complexconjugate(cquqd83x3x3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4238 = Coupling(name = 'GC_4238',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x3x3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4239 = Coupling(name = 'GC_4239',
                   value = '(complex(0,1)*complexconjugate(cquqd83x3x3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4240 = Coupling(name = 'GC_4240',
                   value = '-((complex(0,1)*complexconjugate(cquqd83x3x3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4241 = Coupling(name = 'GC_4241',
                   value = '(complex(0,1)*complexconjugate(cquqd83x3x3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4242 = Coupling(name = 'GC_4242',
                   value = '(complex(0,1)*complexconjugate(cuG1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4243 = Coupling(name = 'GC_4243',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuG1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4244 = Coupling(name = 'GC_4244',
                   value = '(G*vevhat*complexconjugate(cuG1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_4245 = Coupling(name = 'GC_4245',
                   value = '(complex(0,1)*complexconjugate(cuG1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4246 = Coupling(name = 'GC_4246',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuG1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4247 = Coupling(name = 'GC_4247',
                   value = '(G*vevhat*complexconjugate(cuG1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_4248 = Coupling(name = 'GC_4248',
                   value = '(complex(0,1)*complexconjugate(cuG1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4249 = Coupling(name = 'GC_4249',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuG1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4250 = Coupling(name = 'GC_4250',
                   value = '(G*vevhat*complexconjugate(cuG1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_4251 = Coupling(name = 'GC_4251',
                   value = '(complex(0,1)*complexconjugate(cuG2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4252 = Coupling(name = 'GC_4252',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuG2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4253 = Coupling(name = 'GC_4253',
                   value = '(G*vevhat*complexconjugate(cuG2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_4254 = Coupling(name = 'GC_4254',
                   value = '(complex(0,1)*complexconjugate(cuG2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4255 = Coupling(name = 'GC_4255',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuG2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4256 = Coupling(name = 'GC_4256',
                   value = '(G*vevhat*complexconjugate(cuG2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_4257 = Coupling(name = 'GC_4257',
                   value = '(complex(0,1)*complexconjugate(cuG2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4258 = Coupling(name = 'GC_4258',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuG2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4259 = Coupling(name = 'GC_4259',
                   value = '(G*vevhat*complexconjugate(cuG2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_4260 = Coupling(name = 'GC_4260',
                   value = '(complex(0,1)*complexconjugate(cuG3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4261 = Coupling(name = 'GC_4261',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuG3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4262 = Coupling(name = 'GC_4262',
                   value = '(G*vevhat*complexconjugate(cuG3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_4263 = Coupling(name = 'GC_4263',
                   value = '(complex(0,1)*complexconjugate(cuG3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4264 = Coupling(name = 'GC_4264',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuG3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4265 = Coupling(name = 'GC_4265',
                   value = '(G*vevhat*complexconjugate(cuG3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_4266 = Coupling(name = 'GC_4266',
                   value = '(complex(0,1)*complexconjugate(cuG3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4267 = Coupling(name = 'GC_4267',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuG3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4268 = Coupling(name = 'GC_4268',
                   value = '(G*vevhat*complexconjugate(cuG3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_4269 = Coupling(name = 'GC_4269',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cuH1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4270 = Coupling(name = 'GC_4270',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cuH1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_4271 = Coupling(name = 'GC_4271',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cuH1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4272 = Coupling(name = 'GC_4272',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cuH1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_4273 = Coupling(name = 'GC_4273',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cuH1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4274 = Coupling(name = 'GC_4274',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cuH1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_4275 = Coupling(name = 'GC_4275',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cuH2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4276 = Coupling(name = 'GC_4276',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cuH2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_4277 = Coupling(name = 'GC_4277',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cuH2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4278 = Coupling(name = 'GC_4278',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cuH2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_4279 = Coupling(name = 'GC_4279',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cuH2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4280 = Coupling(name = 'GC_4280',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cuH2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_4281 = Coupling(name = 'GC_4281',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cuH3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4282 = Coupling(name = 'GC_4282',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cuH3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_4283 = Coupling(name = 'GC_4283',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cuH3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4284 = Coupling(name = 'GC_4284',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cuH3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_4285 = Coupling(name = 'GC_4285',
                   value = '(3*complex(0,1)*vevhat*complexconjugate(cuH3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4286 = Coupling(name = 'GC_4286',
                   value = '(complex(0,1)*vevhat**2*complexconjugate(cuH3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1})

GC_4287 = Coupling(name = 'GC_4287',
                   value = '(complex(0,1)*complexconjugate(cuW1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4288 = Coupling(name = 'GC_4288',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuW1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_4289 = Coupling(name = 'GC_4289',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW1x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4290 = Coupling(name = 'GC_4290',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW1x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_4291 = Coupling(name = 'GC_4291',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cuW1x1))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_4292 = Coupling(name = 'GC_4292',
                   value = '-((complex(0,1)*sth*complexconjugate(cuB1x1))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*complexconjugate(cuW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4293 = Coupling(name = 'GC_4293',
                   value = '(cth*complex(0,1)*complexconjugate(cuB1x1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*complexconjugate(cuW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4294 = Coupling(name = 'GC_4294',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cuB1x1))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*complexconjugate(cuW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4295 = Coupling(name = 'GC_4295',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cuB1x1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*complexconjugate(cuW1x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4296 = Coupling(name = 'GC_4296',
                   value = '(complex(0,1)*complexconjugate(cuW1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4297 = Coupling(name = 'GC_4297',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuW1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_4298 = Coupling(name = 'GC_4298',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW1x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4299 = Coupling(name = 'GC_4299',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW1x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_4300 = Coupling(name = 'GC_4300',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cuW1x2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_4301 = Coupling(name = 'GC_4301',
                   value = '-((complex(0,1)*sth*complexconjugate(cuB1x2))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*complexconjugate(cuW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4302 = Coupling(name = 'GC_4302',
                   value = '(cth*complex(0,1)*complexconjugate(cuB1x2))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*complexconjugate(cuW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4303 = Coupling(name = 'GC_4303',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cuB1x2))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*complexconjugate(cuW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4304 = Coupling(name = 'GC_4304',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cuB1x2))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*complexconjugate(cuW1x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4305 = Coupling(name = 'GC_4305',
                   value = '(complex(0,1)*complexconjugate(cuW1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4306 = Coupling(name = 'GC_4306',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuW1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_4307 = Coupling(name = 'GC_4307',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW1x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4308 = Coupling(name = 'GC_4308',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW1x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_4309 = Coupling(name = 'GC_4309',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cuW1x3))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_4310 = Coupling(name = 'GC_4310',
                   value = '-((complex(0,1)*sth*complexconjugate(cuB1x3))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*complexconjugate(cuW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4311 = Coupling(name = 'GC_4311',
                   value = '(cth*complex(0,1)*complexconjugate(cuB1x3))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*complexconjugate(cuW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4312 = Coupling(name = 'GC_4312',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cuB1x3))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*complexconjugate(cuW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4313 = Coupling(name = 'GC_4313',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cuB1x3))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*complexconjugate(cuW1x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4314 = Coupling(name = 'GC_4314',
                   value = '(complex(0,1)*complexconjugate(cuW2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4315 = Coupling(name = 'GC_4315',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuW2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_4316 = Coupling(name = 'GC_4316',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW2x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4317 = Coupling(name = 'GC_4317',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW2x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_4318 = Coupling(name = 'GC_4318',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cuW2x1))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_4319 = Coupling(name = 'GC_4319',
                   value = '-((complex(0,1)*sth*complexconjugate(cuB2x1))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*complexconjugate(cuW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4320 = Coupling(name = 'GC_4320',
                   value = '(cth*complex(0,1)*complexconjugate(cuB2x1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*complexconjugate(cuW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4321 = Coupling(name = 'GC_4321',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cuB2x1))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*complexconjugate(cuW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4322 = Coupling(name = 'GC_4322',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cuB2x1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*complexconjugate(cuW2x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4323 = Coupling(name = 'GC_4323',
                   value = '(complex(0,1)*complexconjugate(cuW2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4324 = Coupling(name = 'GC_4324',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuW2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_4325 = Coupling(name = 'GC_4325',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW2x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4326 = Coupling(name = 'GC_4326',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW2x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_4327 = Coupling(name = 'GC_4327',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cuW2x2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_4328 = Coupling(name = 'GC_4328',
                   value = '-((complex(0,1)*sth*complexconjugate(cuB2x2))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*complexconjugate(cuW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4329 = Coupling(name = 'GC_4329',
                   value = '(cth*complex(0,1)*complexconjugate(cuB2x2))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*complexconjugate(cuW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4330 = Coupling(name = 'GC_4330',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cuB2x2))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*complexconjugate(cuW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4331 = Coupling(name = 'GC_4331',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cuB2x2))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*complexconjugate(cuW2x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4332 = Coupling(name = 'GC_4332',
                   value = '(complex(0,1)*complexconjugate(cuW2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4333 = Coupling(name = 'GC_4333',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuW2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_4334 = Coupling(name = 'GC_4334',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW2x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4335 = Coupling(name = 'GC_4335',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW2x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_4336 = Coupling(name = 'GC_4336',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cuW2x3))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_4337 = Coupling(name = 'GC_4337',
                   value = '-((complex(0,1)*sth*complexconjugate(cuB2x3))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*complexconjugate(cuW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4338 = Coupling(name = 'GC_4338',
                   value = '(cth*complex(0,1)*complexconjugate(cuB2x3))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*complexconjugate(cuW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4339 = Coupling(name = 'GC_4339',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cuB2x3))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*complexconjugate(cuW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4340 = Coupling(name = 'GC_4340',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cuB2x3))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*complexconjugate(cuW2x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4341 = Coupling(name = 'GC_4341',
                   value = '(complex(0,1)*complexconjugate(cuW3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4342 = Coupling(name = 'GC_4342',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuW3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_4343 = Coupling(name = 'GC_4343',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW3x1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4344 = Coupling(name = 'GC_4344',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW3x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_4345 = Coupling(name = 'GC_4345',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cuW3x1))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_4346 = Coupling(name = 'GC_4346',
                   value = '-((complex(0,1)*sth*complexconjugate(cuB3x1))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*complexconjugate(cuW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4347 = Coupling(name = 'GC_4347',
                   value = '(cth*complex(0,1)*complexconjugate(cuB3x1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*complexconjugate(cuW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4348 = Coupling(name = 'GC_4348',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cuB3x1))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*complexconjugate(cuW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4349 = Coupling(name = 'GC_4349',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cuB3x1))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*complexconjugate(cuW3x1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4350 = Coupling(name = 'GC_4350',
                   value = '(complex(0,1)*complexconjugate(cuW3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4351 = Coupling(name = 'GC_4351',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuW3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_4352 = Coupling(name = 'GC_4352',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW3x2))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4353 = Coupling(name = 'GC_4353',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW3x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_4354 = Coupling(name = 'GC_4354',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cuW3x2))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_4355 = Coupling(name = 'GC_4355',
                   value = '-((complex(0,1)*sth*complexconjugate(cuB3x2))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*complexconjugate(cuW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4356 = Coupling(name = 'GC_4356',
                   value = '(cth*complex(0,1)*complexconjugate(cuB3x2))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*complexconjugate(cuW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4357 = Coupling(name = 'GC_4357',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cuB3x2))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*complexconjugate(cuW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4358 = Coupling(name = 'GC_4358',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cuB3x2))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*complexconjugate(cuW3x2))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4359 = Coupling(name = 'GC_4359',
                   value = '(complex(0,1)*complexconjugate(cuW3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_4360 = Coupling(name = 'GC_4360',
                   value = '(complex(0,1)*vevhat*complexconjugate(cuW3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':1})

GC_4361 = Coupling(name = 'GC_4361',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW3x3))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':2})

GC_4362 = Coupling(name = 'GC_4362',
                   value = '-((ee*complex(0,1)*vevhat*complexconjugate(cuW3x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_4363 = Coupling(name = 'GC_4363',
                   value = '(cth*ee*complex(0,1)*vevhat*complexconjugate(cuW3x3))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':2})

GC_4364 = Coupling(name = 'GC_4364',
                   value = '-((complex(0,1)*sth*complexconjugate(cuB3x3))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*complexconjugate(cuW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4365 = Coupling(name = 'GC_4365',
                   value = '(cth*complex(0,1)*complexconjugate(cuB3x3))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*complexconjugate(cuW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_4366 = Coupling(name = 'GC_4366',
                   value = '-((complex(0,1)*sth*vevhat*complexconjugate(cuB3x3))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*complexconjugate(cuW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_4367 = Coupling(name = 'GC_4367',
                   value = '(cth*complex(0,1)*vevhat*complexconjugate(cuB3x3))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*complexconjugate(cuW3x3))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

