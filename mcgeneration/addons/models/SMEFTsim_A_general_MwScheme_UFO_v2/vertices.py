# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Mon 5 Feb 2018 13:13:47


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1, L.SSSS2, L.SSSS3 ],
             couplings = {(0,0):C.GC_9,(0,2):C.GC_651,(0,1):C.GC_652})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_2947})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_2811})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1, L.SSS2, L.SSS3 ],
             couplings = {(0,0):C.GC_2583,(0,2):C.GC_2629,(0,1):C.GC_2630})

V_5 = Vertex(name = 'V_5',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_3014})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2840})

V_7 = Vertex(name = 'V_7',
             particles = [ P.a, P.a, P.H ],
             color = [ '1' ],
             lorentz = [ L.VVS2, L.VVS4 ],
             couplings = {(0,0):C.GC_2943,(0,1):C.GC_2580})

V_8 = Vertex(name = 'V_8',
             particles = [ P.a, P.a, P.H ],
             color = [ '1' ],
             lorentz = [ L.VVS4 ],
             couplings = {(0,0):C.GC_2940})

V_9 = Vertex(name = 'V_9',
             particles = [ P.a, P.a, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.VVSS2, L.VVSS4 ],
             couplings = {(0,0):C.GC_2579,(0,1):C.GC_2576})

V_10 = Vertex(name = 'V_10',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_2632,(0,1):C.GC_2581})

V_11 = Vertex(name = 'V_11',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_2631})

V_12 = Vertex(name = 'V_12',
              particles = [ P.g, P.g, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_654,(0,1):C.GC_653})

V_13 = Vertex(name = 'V_13',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_656,(0,2):C.GC_655,(0,1):C.GC_2490})

V_14 = Vertex(name = 'V_14',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_2948})

V_15 = Vertex(name = 'V_15',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_2634,(0,2):C.GC_2633,(0,1):C.GC_2713})

V_16 = Vertex(name = 'V_16',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_3015})

V_17 = Vertex(name = 'V_17',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1, L.VVV3, L.VVV5, L.VVV6, L.VVV7, L.VVV9 ],
              couplings = {(0,1):C.GC_2823,(0,0):C.GC_2838,(0,5):C.GC_2515,(0,4):C.GC_2514,(0,2):C.GC_3,(0,3):C.GC_2837})

V_18 = Vertex(name = 'V_18',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV5 ],
              couplings = {(0,0):C.GC_2991})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_2942,(0,2):C.GC_2582,(0,1):C.GC_3017})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_2941})

V_21 = Vertex(name = 'V_21',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_2578,(0,2):C.GC_2577,(0,1):C.GC_3013})

V_22 = Vertex(name = 'V_22',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_2575,(0,2):C.GC_2574,(0,1):C.GC_2573})

V_23 = Vertex(name = 'V_23',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_3012})

V_24 = Vertex(name = 'V_24',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_2939,(0,2):C.GC_2938,(0,1):C.GC_2937})

V_25 = Vertex(name = 'V_25',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_3016})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV7, L.VVV9 ],
              couplings = {(0,1):C.GC_2839,(0,0):C.GC_2822,(0,5):C.GC_2485,(0,4):C.GC_2484,(0,3):C.GC_2506,(0,2):C.GC_2821})

V_27 = Vertex(name = 'V_27',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV5 ],
              couplings = {(0,0):C.GC_3001})

V_28 = Vertex(name = 'V_28',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_7})

V_29 = Vertex(name = 'V_29',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV3, L.VVV5, L.VVV7, L.VVV8 ],
              couplings = {(0,0):C.GC_2824,(0,3):C.GC_650,(0,2):C.GC_649,(0,1):C.GC_7})

V_30 = Vertex(name = 'V_30',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS3, L.VVVS6 ],
              couplings = {(0,0):C.GC_2703,(0,1):C.GC_2702})

V_31 = Vertex(name = 'V_31',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV10, L.VVVV12, L.VVVV13, L.VVVV2, L.VVVV3, L.VVVV4, L.VVVV6, L.VVVV9 ],
              couplings = {(0,7):C.GC_2489,(1,6):C.GC_2489,(2,5):C.GC_2489,(0,4):C.GC_2488,(1,3):C.GC_2488,(2,2):C.GC_2488,(1,8):C.GC_8,(0,0):C.GC_8,(2,1):C.GC_8})

V_32 = Vertex(name = 'V_32',
              particles = [ P.d__tilde__, P.d, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3063,(0,1):C.GC_2593})

V_33 = Vertex(name = 'V_33',
              particles = [ P.s__tilde__, P.d, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3069,(0,1):C.GC_2594})

V_34 = Vertex(name = 'V_34',
              particles = [ P.b__tilde__, P.d, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3075,(0,1):C.GC_2595})

V_35 = Vertex(name = 'V_35',
              particles = [ P.d__tilde__, P.s, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3065,(0,1):C.GC_2596})

V_36 = Vertex(name = 'V_36',
              particles = [ P.s__tilde__, P.s, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3071,(0,1):C.GC_2597})

V_37 = Vertex(name = 'V_37',
              particles = [ P.b__tilde__, P.s, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3077,(0,1):C.GC_2598})

V_38 = Vertex(name = 'V_38',
              particles = [ P.d__tilde__, P.b, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3067,(0,1):C.GC_2599})

V_39 = Vertex(name = 'V_39',
              particles = [ P.s__tilde__, P.b, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3073,(0,1):C.GC_2600})

V_40 = Vertex(name = 'V_40',
              particles = [ P.b__tilde__, P.b, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3079,(0,1):C.GC_2601})

V_41 = Vertex(name = 'V_41',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_3022,(0,0):C.GC_3064,(0,1):C.GC_2793})

V_42 = Vertex(name = 'V_42',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_3023})

V_43 = Vertex(name = 'V_43',
              particles = [ P.s__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3070,(0,1):C.GC_2794})

V_44 = Vertex(name = 'V_44',
              particles = [ P.b__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3076,(0,1):C.GC_2795})

V_45 = Vertex(name = 'V_45',
              particles = [ P.d__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3066,(0,1):C.GC_2796})

V_46 = Vertex(name = 'V_46',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_3028,(0,0):C.GC_3072,(0,1):C.GC_2797})

V_47 = Vertex(name = 'V_47',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_3029})

V_48 = Vertex(name = 'V_48',
              particles = [ P.b__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3078,(0,1):C.GC_2798})

V_49 = Vertex(name = 'V_49',
              particles = [ P.d__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3068,(0,1):C.GC_2799})

V_50 = Vertex(name = 'V_50',
              particles = [ P.s__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3074,(0,1):C.GC_2800})

V_51 = Vertex(name = 'V_51',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_3018,(0,0):C.GC_3080,(0,1):C.GC_2801})

V_52 = Vertex(name = 'V_52',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_3019})

V_53 = Vertex(name = 'V_53',
              particles = [ P.e__plus__, P.e__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3162,(0,1):C.GC_2611})

V_54 = Vertex(name = 'V_54',
              particles = [ P.mu__plus__, P.e__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3168,(0,1):C.GC_2612})

V_55 = Vertex(name = 'V_55',
              particles = [ P.ta__plus__, P.e__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3174,(0,1):C.GC_2613})

V_56 = Vertex(name = 'V_56',
              particles = [ P.e__plus__, P.mu__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3164,(0,1):C.GC_2614})

V_57 = Vertex(name = 'V_57',
              particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3170,(0,1):C.GC_2615})

V_58 = Vertex(name = 'V_58',
              particles = [ P.ta__plus__, P.mu__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3176,(0,1):C.GC_2616})

V_59 = Vertex(name = 'V_59',
              particles = [ P.e__plus__, P.ta__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3166,(0,1):C.GC_2617})

V_60 = Vertex(name = 'V_60',
              particles = [ P.mu__plus__, P.ta__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3172,(0,1):C.GC_2618})

V_61 = Vertex(name = 'V_61',
              particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_3178,(0,1):C.GC_2619})

V_62 = Vertex(name = 'V_62',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_3024,(0,0):C.GC_3163,(0,1):C.GC_2802})

V_63 = Vertex(name = 'V_63',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_3025})

V_64 = Vertex(name = 'V_64',
              particles = [ P.mu__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3169,(0,1):C.GC_2803})

V_65 = Vertex(name = 'V_65',
              particles = [ P.ta__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3175,(0,1):C.GC_2804})

V_66 = Vertex(name = 'V_66',
              particles = [ P.e__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3165,(0,1):C.GC_2805})

V_67 = Vertex(name = 'V_67',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_3026,(0,0):C.GC_3171,(0,1):C.GC_2806})

V_68 = Vertex(name = 'V_68',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_3027})

V_69 = Vertex(name = 'V_69',
              particles = [ P.ta__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3177,(0,1):C.GC_2807})

V_70 = Vertex(name = 'V_70',
              particles = [ P.e__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3167,(0,1):C.GC_2808})

V_71 = Vertex(name = 'V_71',
              particles = [ P.mu__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_3173,(0,1):C.GC_2809})

V_72 = Vertex(name = 'V_72',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_3032,(0,0):C.GC_3179,(0,1):C.GC_2810})

V_73 = Vertex(name = 'V_73',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_3033})

V_74 = Vertex(name = 'V_74',
              particles = [ P.u__tilde__, P.u, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_4269,(0,1):C.GC_2644})

V_75 = Vertex(name = 'V_75',
              particles = [ P.c__tilde__, P.u, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_4275,(0,1):C.GC_2645})

V_76 = Vertex(name = 'V_76',
              particles = [ P.t__tilde__, P.u, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_4281,(0,1):C.GC_2646})

V_77 = Vertex(name = 'V_77',
              particles = [ P.u__tilde__, P.c, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_4271,(0,1):C.GC_2647})

V_78 = Vertex(name = 'V_78',
              particles = [ P.c__tilde__, P.c, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_4277,(0,1):C.GC_2648})

V_79 = Vertex(name = 'V_79',
              particles = [ P.t__tilde__, P.c, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_4283,(0,1):C.GC_2649})

V_80 = Vertex(name = 'V_80',
              particles = [ P.u__tilde__, P.t, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_4273,(0,1):C.GC_2650})

V_81 = Vertex(name = 'V_81',
              particles = [ P.c__tilde__, P.t, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_4279,(0,1):C.GC_2651})

V_82 = Vertex(name = 'V_82',
              particles = [ P.t__tilde__, P.t, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_4285,(0,1):C.GC_2652})

V_83 = Vertex(name = 'V_83',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_3034,(0,0):C.GC_4270,(0,1):C.GC_2812})

V_84 = Vertex(name = 'V_84',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_3035})

V_85 = Vertex(name = 'V_85',
              particles = [ P.c__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_4276,(0,1):C.GC_2813})

V_86 = Vertex(name = 'V_86',
              particles = [ P.t__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_4282,(0,1):C.GC_2814})

V_87 = Vertex(name = 'V_87',
              particles = [ P.u__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_4272,(0,1):C.GC_2815})

V_88 = Vertex(name = 'V_88',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_3020,(0,0):C.GC_4278,(0,1):C.GC_2816})

V_89 = Vertex(name = 'V_89',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_3021})

V_90 = Vertex(name = 'V_90',
              particles = [ P.t__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_4284,(0,1):C.GC_2817})

V_91 = Vertex(name = 'V_91',
              particles = [ P.u__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_4274,(0,1):C.GC_2818})

V_92 = Vertex(name = 'V_92',
              particles = [ P.c__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_4280,(0,1):C.GC_2819})

V_93 = Vertex(name = 'V_93',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_3030,(0,0):C.GC_4286,(0,1):C.GC_2820})

V_94 = Vertex(name = 'V_94',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_3031})

V_95 = Vertex(name = 'V_95',
              particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
              couplings = {(1,6):C.GC_280,(0,7):C.GC_1800,(1,0):C.GC_3919,(3,0):C.GC_4081,(0,5):C.GC_3918,(2,5):C.GC_4080,(1,4):C.GC_1557,(3,4):C.GC_1638,(1,2):C.GC_1809,(3,2):C.GC_1890,(1,3):C.GC_2295,(3,3):C.GC_2376,(1,8):C.GC_1972,(3,8):C.GC_2134,(0,1):C.GC_1971,(2,1):C.GC_2133})

V_96 = Vertex(name = 'V_96',
              particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
              couplings = {(1,6):C.GC_282,(0,7):C.GC_284,(1,0):C.GC_3973,(3,0):C.GC_4135,(0,5):C.GC_3924,(2,5):C.GC_4086,(1,4):C.GC_1566,(3,4):C.GC_1647,(1,2):C.GC_1810,(3,2):C.GC_1891,(1,3):C.GC_2304,(3,3):C.GC_2385,(1,8):C.GC_1990,(3,8):C.GC_2152,(0,1):C.GC_1989,(2,1):C.GC_2151})

V_97 = Vertex(name = 'V_97',
              particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
              couplings = {(1,6):C.GC_287,(0,7):C.GC_289,(1,0):C.GC_4027,(3,0):C.GC_4189,(0,5):C.GC_3930,(2,5):C.GC_4092,(1,4):C.GC_1575,(3,4):C.GC_1656,(1,2):C.GC_1811,(3,2):C.GC_1892,(1,3):C.GC_2313,(3,3):C.GC_2394,(1,8):C.GC_2008,(3,8):C.GC_2170,(0,1):C.GC_2007,(2,1):C.GC_2169})

V_98 = Vertex(name = 'V_98',
              particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
              couplings = {(1,6):C.GC_295,(0,7):C.GC_297,(1,0):C.GC_3937,(3,0):C.GC_4099,(0,5):C.GC_3936,(2,5):C.GC_4098,(1,4):C.GC_1584,(3,4):C.GC_1665,(1,2):C.GC_1812,(3,2):C.GC_1893,(1,3):C.GC_2322,(3,3):C.GC_2403,(1,8):C.GC_2026,(3,8):C.GC_2188,(0,1):C.GC_1977,(2,1):C.GC_2139})

V_99 = Vertex(name = 'V_99',
              particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
              couplings = {(1,6):C.GC_306,(0,7):C.GC_300,(1,0):C.GC_3991,(3,0):C.GC_4153,(0,5):C.GC_3942,(2,5):C.GC_4104,(1,4):C.GC_1593,(3,4):C.GC_1674,(1,2):C.GC_1813,(3,2):C.GC_1894,(1,3):C.GC_2331,(3,3):C.GC_2412,(1,8):C.GC_2044,(3,8):C.GC_2206,(0,1):C.GC_1995,(2,1):C.GC_2157})

V_100 = Vertex(name = 'V_100',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_320,(0,7):C.GC_303,(1,0):C.GC_4045,(3,0):C.GC_4207,(0,5):C.GC_3948,(2,5):C.GC_4110,(1,4):C.GC_1602,(3,4):C.GC_1683,(1,2):C.GC_1814,(3,2):C.GC_1895,(1,3):C.GC_2340,(3,3):C.GC_2421,(1,8):C.GC_2062,(3,8):C.GC_2224,(0,1):C.GC_2013,(2,1):C.GC_2175})

V_101 = Vertex(name = 'V_101',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_337,(0,7):C.GC_339,(1,0):C.GC_3955,(3,0):C.GC_4117,(0,5):C.GC_3954,(2,5):C.GC_4116,(1,4):C.GC_1611,(3,4):C.GC_1692,(1,2):C.GC_1815,(3,2):C.GC_1896,(1,3):C.GC_2349,(3,3):C.GC_2430,(1,8):C.GC_2080,(3,8):C.GC_2242,(0,1):C.GC_1983,(2,1):C.GC_2145})

V_102 = Vertex(name = 'V_102',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_357,(0,7):C.GC_342,(1,0):C.GC_4009,(3,0):C.GC_4171,(0,5):C.GC_3960,(2,5):C.GC_4122,(1,4):C.GC_1620,(3,4):C.GC_1701,(1,2):C.GC_1816,(3,2):C.GC_1897,(1,3):C.GC_2358,(3,3):C.GC_2439,(1,8):C.GC_2098,(3,8):C.GC_2260,(0,1):C.GC_2001,(2,1):C.GC_2163})

V_103 = Vertex(name = 'V_103',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_380,(0,7):C.GC_345,(1,0):C.GC_4063,(3,0):C.GC_4225,(0,5):C.GC_3966,(2,5):C.GC_4128,(1,4):C.GC_1629,(3,4):C.GC_1710,(1,2):C.GC_1817,(3,2):C.GC_1898,(1,3):C.GC_2367,(3,3):C.GC_2448,(1,8):C.GC_2116,(3,8):C.GC_2278,(0,1):C.GC_2019,(2,1):C.GC_2181})

V_104 = Vertex(name = 'V_104',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_282,(0,7):C.GC_284,(1,0):C.GC_3925,(3,0):C.GC_4087,(0,5):C.GC_3972,(2,5):C.GC_4134,(1,4):C.GC_1558,(3,4):C.GC_1639,(1,2):C.GC_1818,(3,2):C.GC_1899,(1,3):C.GC_2296,(3,3):C.GC_2377,(1,8):C.GC_1974,(3,8):C.GC_2136,(0,1):C.GC_1973,(2,1):C.GC_2135})

V_105 = Vertex(name = 'V_105',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_285,(0,7):C.GC_1801,(1,0):C.GC_3979,(3,0):C.GC_4141,(0,5):C.GC_3978,(2,5):C.GC_4140,(1,4):C.GC_1567,(3,4):C.GC_1648,(1,2):C.GC_1819,(3,2):C.GC_1900,(1,3):C.GC_2305,(3,3):C.GC_2386,(1,8):C.GC_1992,(3,8):C.GC_2154,(0,1):C.GC_1991,(2,1):C.GC_2153})

V_106 = Vertex(name = 'V_106',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_290,(0,7):C.GC_292,(1,0):C.GC_4033,(3,0):C.GC_4195,(0,5):C.GC_3984,(2,5):C.GC_4146,(1,4):C.GC_1576,(3,4):C.GC_1657,(1,2):C.GC_1820,(3,2):C.GC_1901,(1,3):C.GC_2314,(3,3):C.GC_2395,(1,8):C.GC_2010,(3,8):C.GC_2172,(0,1):C.GC_2009,(2,1):C.GC_2171})

V_107 = Vertex(name = 'V_107',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_298,(0,7):C.GC_308,(1,0):C.GC_3943,(3,0):C.GC_4105,(0,5):C.GC_3990,(2,5):C.GC_4152,(1,4):C.GC_1585,(3,4):C.GC_1666,(1,2):C.GC_1821,(3,2):C.GC_1902,(1,3):C.GC_2323,(3,3):C.GC_2404,(1,8):C.GC_2028,(3,8):C.GC_2190,(0,1):C.GC_1979,(2,1):C.GC_2141})

V_108 = Vertex(name = 'V_108',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_309,(0,7):C.GC_311,(1,0):C.GC_3997,(3,0):C.GC_4159,(0,5):C.GC_3996,(2,5):C.GC_4158,(1,4):C.GC_1594,(3,4):C.GC_1675,(1,2):C.GC_1822,(3,2):C.GC_1903,(1,3):C.GC_2332,(3,3):C.GC_2413,(1,8):C.GC_2046,(3,8):C.GC_2208,(0,1):C.GC_1997,(2,1):C.GC_2159})

V_109 = Vertex(name = 'V_109',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_323,(0,7):C.GC_314,(1,0):C.GC_4051,(3,0):C.GC_4213,(0,5):C.GC_4002,(2,5):C.GC_4164,(1,4):C.GC_1603,(3,4):C.GC_1684,(1,2):C.GC_1823,(3,2):C.GC_1904,(1,3):C.GC_2341,(3,3):C.GC_2422,(1,8):C.GC_2064,(3,8):C.GC_2226,(0,1):C.GC_2015,(2,1):C.GC_2177})

V_110 = Vertex(name = 'V_110',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_340,(0,7):C.GC_359,(1,0):C.GC_3961,(3,0):C.GC_4123,(0,5):C.GC_4008,(2,5):C.GC_4170,(1,4):C.GC_1612,(3,4):C.GC_1693,(1,2):C.GC_1824,(3,2):C.GC_1905,(1,3):C.GC_2350,(3,3):C.GC_2431,(1,8):C.GC_2082,(3,8):C.GC_2244,(0,1):C.GC_1985,(2,1):C.GC_2147})

V_111 = Vertex(name = 'V_111',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_360,(0,7):C.GC_362,(1,0):C.GC_4015,(3,0):C.GC_4177,(0,5):C.GC_4014,(2,5):C.GC_4176,(1,4):C.GC_1621,(3,4):C.GC_1702,(1,2):C.GC_1825,(3,2):C.GC_1906,(1,3):C.GC_2359,(3,3):C.GC_2440,(1,8):C.GC_2100,(3,8):C.GC_2262,(0,1):C.GC_2003,(2,1):C.GC_2165})

V_112 = Vertex(name = 'V_112',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_383,(0,7):C.GC_365,(1,0):C.GC_4069,(3,0):C.GC_4231,(0,5):C.GC_4020,(2,5):C.GC_4182,(1,4):C.GC_1630,(3,4):C.GC_1711,(1,2):C.GC_1826,(3,2):C.GC_1907,(1,3):C.GC_2368,(3,3):C.GC_2449,(1,8):C.GC_2118,(3,8):C.GC_2280,(0,1):C.GC_2021,(2,1):C.GC_2183})

V_113 = Vertex(name = 'V_113',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_287,(0,7):C.GC_289,(1,0):C.GC_3931,(3,0):C.GC_4093,(0,5):C.GC_4026,(2,5):C.GC_4188,(1,4):C.GC_1559,(3,4):C.GC_1640,(1,2):C.GC_1827,(3,2):C.GC_1908,(1,3):C.GC_2297,(3,3):C.GC_2378,(1,8):C.GC_1976,(3,8):C.GC_2138,(0,1):C.GC_1975,(2,1):C.GC_2137})

V_114 = Vertex(name = 'V_114',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_290,(0,7):C.GC_292,(1,0):C.GC_3985,(3,0):C.GC_4147,(0,5):C.GC_4032,(2,5):C.GC_4194,(1,4):C.GC_1568,(3,4):C.GC_1649,(1,2):C.GC_1828,(3,2):C.GC_1909,(1,3):C.GC_2306,(3,3):C.GC_2387,(1,8):C.GC_1994,(3,8):C.GC_2156,(0,1):C.GC_1993,(2,1):C.GC_2155})

V_115 = Vertex(name = 'V_115',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_293,(0,7):C.GC_1802,(1,0):C.GC_4039,(3,0):C.GC_4201,(0,5):C.GC_4038,(2,5):C.GC_4200,(1,4):C.GC_1577,(3,4):C.GC_1658,(1,2):C.GC_1829,(3,2):C.GC_1910,(1,3):C.GC_2315,(3,3):C.GC_2396,(1,8):C.GC_2012,(3,8):C.GC_2174,(0,1):C.GC_2011,(2,1):C.GC_2173})

V_116 = Vertex(name = 'V_116',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_301,(0,7):C.GC_322,(1,0):C.GC_3949,(3,0):C.GC_4111,(0,5):C.GC_4044,(2,5):C.GC_4206,(1,4):C.GC_1586,(3,4):C.GC_1667,(1,2):C.GC_1830,(3,2):C.GC_1911,(1,3):C.GC_2324,(3,3):C.GC_2405,(1,8):C.GC_2030,(3,8):C.GC_2192,(0,1):C.GC_1981,(2,1):C.GC_2143})

V_117 = Vertex(name = 'V_117',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_312,(0,7):C.GC_325,(1,0):C.GC_4003,(3,0):C.GC_4165,(0,5):C.GC_4050,(2,5):C.GC_4212,(1,4):C.GC_1595,(3,4):C.GC_1676,(1,2):C.GC_1831,(3,2):C.GC_1912,(1,3):C.GC_2333,(3,3):C.GC_2414,(1,8):C.GC_2048,(3,8):C.GC_2210,(0,1):C.GC_1999,(2,1):C.GC_2161})

V_118 = Vertex(name = 'V_118',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_326,(0,7):C.GC_328,(1,0):C.GC_4057,(3,0):C.GC_4219,(0,5):C.GC_4056,(2,5):C.GC_4218,(1,4):C.GC_1604,(3,4):C.GC_1685,(1,2):C.GC_1832,(3,2):C.GC_1913,(1,3):C.GC_2342,(3,3):C.GC_2423,(1,8):C.GC_2066,(3,8):C.GC_2228,(0,1):C.GC_2017,(2,1):C.GC_2179})

V_119 = Vertex(name = 'V_119',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_343,(0,7):C.GC_382,(1,0):C.GC_3967,(3,0):C.GC_4129,(0,5):C.GC_4062,(2,5):C.GC_4224,(1,4):C.GC_1613,(3,4):C.GC_1694,(1,2):C.GC_1833,(3,2):C.GC_1914,(1,3):C.GC_2351,(3,3):C.GC_2432,(1,8):C.GC_2084,(3,8):C.GC_2246,(0,1):C.GC_1987,(2,1):C.GC_2149})

V_120 = Vertex(name = 'V_120',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_363,(0,7):C.GC_385,(1,0):C.GC_4021,(3,0):C.GC_4183,(0,5):C.GC_4068,(2,5):C.GC_4230,(1,4):C.GC_1622,(3,4):C.GC_1703,(1,2):C.GC_1834,(3,2):C.GC_1915,(1,3):C.GC_2360,(3,3):C.GC_2441,(1,8):C.GC_2102,(3,8):C.GC_2264,(0,1):C.GC_2005,(2,1):C.GC_2167})

V_121 = Vertex(name = 'V_121',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_386,(0,7):C.GC_388,(1,0):C.GC_4075,(3,0):C.GC_4237,(0,5):C.GC_4074,(2,5):C.GC_4236,(1,4):C.GC_1631,(3,4):C.GC_1712,(1,2):C.GC_1835,(3,2):C.GC_1916,(1,3):C.GC_2369,(3,3):C.GC_2450,(1,8):C.GC_2120,(3,8):C.GC_2282,(0,1):C.GC_2023,(2,1):C.GC_2185})

V_122 = Vertex(name = 'V_122',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_295,(0,7):C.GC_297,(1,0):C.GC_3921,(3,0):C.GC_4083,(0,5):C.GC_3920,(2,5):C.GC_4082,(1,4):C.GC_1560,(3,4):C.GC_1641,(1,2):C.GC_1836,(3,2):C.GC_1917,(1,3):C.GC_2298,(3,3):C.GC_2379,(1,8):C.GC_1978,(3,8):C.GC_2140,(0,1):C.GC_2025,(2,1):C.GC_2187})

V_123 = Vertex(name = 'V_123',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_298,(0,7):C.GC_308,(1,0):C.GC_3975,(3,0):C.GC_4137,(0,5):C.GC_3926,(2,5):C.GC_4088,(1,4):C.GC_1569,(3,4):C.GC_1650,(1,2):C.GC_1837,(3,2):C.GC_1918,(1,3):C.GC_2307,(3,3):C.GC_2388,(1,8):C.GC_1996,(3,8):C.GC_2158,(0,1):C.GC_2043,(2,1):C.GC_2205})

V_124 = Vertex(name = 'V_124',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_301,(0,7):C.GC_322,(1,0):C.GC_4029,(3,0):C.GC_4191,(0,5):C.GC_3932,(2,5):C.GC_4094,(1,4):C.GC_1578,(3,4):C.GC_1659,(1,2):C.GC_1838,(3,2):C.GC_1919,(1,3):C.GC_2316,(3,3):C.GC_2397,(1,8):C.GC_2014,(3,8):C.GC_2176,(0,1):C.GC_2061,(2,1):C.GC_2223})

V_125 = Vertex(name = 'V_125',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_304,(0,7):C.GC_1803,(1,0):C.GC_3939,(3,0):C.GC_4101,(0,5):C.GC_3938,(2,5):C.GC_4100,(1,4):C.GC_1587,(3,4):C.GC_1668,(1,2):C.GC_1839,(3,2):C.GC_1920,(1,3):C.GC_2325,(3,3):C.GC_2406,(1,8):C.GC_2032,(3,8):C.GC_2194,(0,1):C.GC_2031,(2,1):C.GC_2193})

V_126 = Vertex(name = 'V_126',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_315,(0,7):C.GC_317,(1,0):C.GC_3993,(3,0):C.GC_4155,(0,5):C.GC_3944,(2,5):C.GC_4106,(1,4):C.GC_1596,(3,4):C.GC_1677,(1,2):C.GC_1840,(3,2):C.GC_1921,(1,3):C.GC_2334,(3,3):C.GC_2415,(1,8):C.GC_2050,(3,8):C.GC_2212,(0,1):C.GC_2049,(2,1):C.GC_2211})

V_127 = Vertex(name = 'V_127',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_329,(0,7):C.GC_331,(1,0):C.GC_4047,(3,0):C.GC_4209,(0,5):C.GC_3950,(2,5):C.GC_4112,(1,4):C.GC_1605,(3,4):C.GC_1686,(1,2):C.GC_1841,(3,2):C.GC_1922,(1,3):C.GC_2343,(3,3):C.GC_2424,(1,8):C.GC_2068,(3,8):C.GC_2230,(0,1):C.GC_2067,(2,1):C.GC_2229})

V_128 = Vertex(name = 'V_128',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_346,(0,7):C.GC_348,(1,0):C.GC_3957,(3,0):C.GC_4119,(0,5):C.GC_3956,(2,5):C.GC_4118,(1,4):C.GC_1614,(3,4):C.GC_1695,(1,2):C.GC_1842,(3,2):C.GC_1923,(1,3):C.GC_2352,(3,3):C.GC_2433,(1,8):C.GC_2086,(3,8):C.GC_2248,(0,1):C.GC_2037,(2,1):C.GC_2199})

V_129 = Vertex(name = 'V_129',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_366,(0,7):C.GC_351,(1,0):C.GC_4011,(3,0):C.GC_4173,(0,5):C.GC_3962,(2,5):C.GC_4124,(1,4):C.GC_1623,(3,4):C.GC_1704,(1,2):C.GC_1843,(3,2):C.GC_1924,(1,3):C.GC_2361,(3,3):C.GC_2442,(1,8):C.GC_2104,(3,8):C.GC_2266,(0,1):C.GC_2055,(2,1):C.GC_2217})

V_130 = Vertex(name = 'V_130',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_389,(0,7):C.GC_354,(1,0):C.GC_4065,(3,0):C.GC_4227,(0,5):C.GC_3968,(2,5):C.GC_4130,(1,4):C.GC_1632,(3,4):C.GC_1713,(1,2):C.GC_1844,(3,2):C.GC_1925,(1,3):C.GC_2370,(3,3):C.GC_2451,(1,8):C.GC_2122,(3,8):C.GC_2284,(0,1):C.GC_2073,(2,1):C.GC_2235})

V_131 = Vertex(name = 'V_131',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_306,(0,7):C.GC_300,(1,0):C.GC_3927,(3,0):C.GC_4089,(0,5):C.GC_3974,(2,5):C.GC_4136,(1,4):C.GC_1561,(3,4):C.GC_1642,(1,2):C.GC_1845,(3,2):C.GC_1926,(1,3):C.GC_2299,(3,3):C.GC_2380,(1,8):C.GC_1980,(3,8):C.GC_2142,(0,1):C.GC_2027,(2,1):C.GC_2189})

V_132 = Vertex(name = 'V_132',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_309,(0,7):C.GC_311,(1,0):C.GC_3981,(3,0):C.GC_4143,(0,5):C.GC_3980,(2,5):C.GC_4142,(1,4):C.GC_1570,(3,4):C.GC_1651,(1,2):C.GC_1846,(3,2):C.GC_1927,(1,3):C.GC_2308,(3,3):C.GC_2389,(1,8):C.GC_1998,(3,8):C.GC_2160,(0,1):C.GC_2045,(2,1):C.GC_2207})

V_133 = Vertex(name = 'V_133',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_312,(0,7):C.GC_325,(1,0):C.GC_4035,(3,0):C.GC_4197,(0,5):C.GC_3986,(2,5):C.GC_4148,(1,4):C.GC_1579,(3,4):C.GC_1660,(1,2):C.GC_1847,(3,2):C.GC_1928,(1,3):C.GC_2317,(3,3):C.GC_2398,(1,8):C.GC_2016,(3,8):C.GC_2178,(0,1):C.GC_2063,(2,1):C.GC_2225})

V_134 = Vertex(name = 'V_134',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_315,(0,7):C.GC_317,(1,0):C.GC_3945,(3,0):C.GC_4107,(0,5):C.GC_3992,(2,5):C.GC_4154,(1,4):C.GC_1588,(3,4):C.GC_1669,(1,2):C.GC_1848,(3,2):C.GC_1929,(1,3):C.GC_2326,(3,3):C.GC_2407,(1,8):C.GC_2034,(3,8):C.GC_2196,(0,1):C.GC_2033,(2,1):C.GC_2195})

V_135 = Vertex(name = 'V_135',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_318,(0,7):C.GC_1804,(1,0):C.GC_3999,(3,0):C.GC_4161,(0,5):C.GC_3998,(2,5):C.GC_4160,(1,4):C.GC_1597,(3,4):C.GC_1678,(1,2):C.GC_1849,(3,2):C.GC_1930,(1,3):C.GC_2335,(3,3):C.GC_2416,(1,8):C.GC_2052,(3,8):C.GC_2214,(0,1):C.GC_2051,(2,1):C.GC_2213})

V_136 = Vertex(name = 'V_136',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_332,(0,7):C.GC_334,(1,0):C.GC_4053,(3,0):C.GC_4215,(0,5):C.GC_4004,(2,5):C.GC_4166,(1,4):C.GC_1606,(3,4):C.GC_1687,(1,2):C.GC_1850,(3,2):C.GC_1931,(1,3):C.GC_2344,(3,3):C.GC_2425,(1,8):C.GC_2070,(3,8):C.GC_2232,(0,1):C.GC_2069,(2,1):C.GC_2231})

V_137 = Vertex(name = 'V_137',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_349,(0,7):C.GC_368,(1,0):C.GC_3963,(3,0):C.GC_4125,(0,5):C.GC_4010,(2,5):C.GC_4172,(1,4):C.GC_1615,(3,4):C.GC_1696,(1,2):C.GC_1851,(3,2):C.GC_1932,(1,3):C.GC_2353,(3,3):C.GC_2434,(1,8):C.GC_2088,(3,8):C.GC_2250,(0,1):C.GC_2039,(2,1):C.GC_2201})

V_138 = Vertex(name = 'V_138',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_369,(0,7):C.GC_371,(1,0):C.GC_4017,(3,0):C.GC_4179,(0,5):C.GC_4016,(2,5):C.GC_4178,(1,4):C.GC_1624,(3,4):C.GC_1705,(1,2):C.GC_1852,(3,2):C.GC_1933,(1,3):C.GC_2362,(3,3):C.GC_2443,(1,8):C.GC_2106,(3,8):C.GC_2268,(0,1):C.GC_2057,(2,1):C.GC_2219})

V_139 = Vertex(name = 'V_139',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_392,(0,7):C.GC_374,(1,0):C.GC_4071,(3,0):C.GC_4233,(0,5):C.GC_4022,(2,5):C.GC_4184,(1,4):C.GC_1633,(3,4):C.GC_1714,(1,2):C.GC_1853,(3,2):C.GC_1934,(1,3):C.GC_2371,(3,3):C.GC_2452,(1,8):C.GC_2124,(3,8):C.GC_2286,(0,1):C.GC_2075,(2,1):C.GC_2237})

V_140 = Vertex(name = 'V_140',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_320,(0,7):C.GC_303,(1,0):C.GC_3933,(3,0):C.GC_4095,(0,5):C.GC_4028,(2,5):C.GC_4190,(1,4):C.GC_1562,(3,4):C.GC_1643,(1,2):C.GC_1854,(3,2):C.GC_1935,(1,3):C.GC_2300,(3,3):C.GC_2381,(1,8):C.GC_1982,(3,8):C.GC_2144,(0,1):C.GC_2029,(2,1):C.GC_2191})

V_141 = Vertex(name = 'V_141',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_323,(0,7):C.GC_314,(1,0):C.GC_3987,(3,0):C.GC_4149,(0,5):C.GC_4034,(2,5):C.GC_4196,(1,4):C.GC_1571,(3,4):C.GC_1652,(1,2):C.GC_1855,(3,2):C.GC_1936,(1,3):C.GC_2309,(3,3):C.GC_2390,(1,8):C.GC_2000,(3,8):C.GC_2162,(0,1):C.GC_2047,(2,1):C.GC_2209})

V_142 = Vertex(name = 'V_142',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_326,(0,7):C.GC_328,(1,0):C.GC_4041,(3,0):C.GC_4203,(0,5):C.GC_4040,(2,5):C.GC_4202,(1,4):C.GC_1580,(3,4):C.GC_1661,(1,2):C.GC_1856,(3,2):C.GC_1937,(1,3):C.GC_2318,(3,3):C.GC_2399,(1,8):C.GC_2018,(3,8):C.GC_2180,(0,1):C.GC_2065,(2,1):C.GC_2227})

V_143 = Vertex(name = 'V_143',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_329,(0,7):C.GC_331,(1,0):C.GC_3951,(3,0):C.GC_4113,(0,5):C.GC_4046,(2,5):C.GC_4208,(1,4):C.GC_1589,(3,4):C.GC_1670,(1,2):C.GC_1857,(3,2):C.GC_1938,(1,3):C.GC_2327,(3,3):C.GC_2408,(1,8):C.GC_2036,(3,8):C.GC_2198,(0,1):C.GC_2035,(2,1):C.GC_2197})

V_144 = Vertex(name = 'V_144',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_332,(0,7):C.GC_334,(1,0):C.GC_4005,(3,0):C.GC_4167,(0,5):C.GC_4052,(2,5):C.GC_4214,(1,4):C.GC_1598,(3,4):C.GC_1679,(1,2):C.GC_1858,(3,2):C.GC_1939,(1,3):C.GC_2336,(3,3):C.GC_2417,(1,8):C.GC_2054,(3,8):C.GC_2216,(0,1):C.GC_2053,(2,1):C.GC_2215})

V_145 = Vertex(name = 'V_145',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_335,(0,7):C.GC_1805,(1,0):C.GC_4059,(3,0):C.GC_4221,(0,5):C.GC_4058,(2,5):C.GC_4220,(1,4):C.GC_1607,(3,4):C.GC_1688,(1,2):C.GC_1859,(3,2):C.GC_1940,(1,3):C.GC_2345,(3,3):C.GC_2426,(1,8):C.GC_2072,(3,8):C.GC_2234,(0,1):C.GC_2071,(2,1):C.GC_2233})

V_146 = Vertex(name = 'V_146',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_352,(0,7):C.GC_391,(1,0):C.GC_3969,(3,0):C.GC_4131,(0,5):C.GC_4064,(2,5):C.GC_4226,(1,4):C.GC_1616,(3,4):C.GC_1697,(1,2):C.GC_1860,(3,2):C.GC_1941,(1,3):C.GC_2354,(3,3):C.GC_2435,(1,8):C.GC_2090,(3,8):C.GC_2252,(0,1):C.GC_2041,(2,1):C.GC_2203})

V_147 = Vertex(name = 'V_147',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_372,(0,7):C.GC_394,(1,0):C.GC_4023,(3,0):C.GC_4185,(0,5):C.GC_4070,(2,5):C.GC_4232,(1,4):C.GC_1625,(3,4):C.GC_1706,(1,2):C.GC_1861,(3,2):C.GC_1942,(1,3):C.GC_2363,(3,3):C.GC_2444,(1,8):C.GC_2108,(3,8):C.GC_2270,(0,1):C.GC_2059,(2,1):C.GC_2221})

V_148 = Vertex(name = 'V_148',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_395,(0,7):C.GC_397,(1,0):C.GC_4077,(3,0):C.GC_4239,(0,5):C.GC_4076,(2,5):C.GC_4238,(1,4):C.GC_1634,(3,4):C.GC_1715,(1,2):C.GC_1862,(3,2):C.GC_1943,(1,3):C.GC_2372,(3,3):C.GC_2453,(1,8):C.GC_2126,(3,8):C.GC_2288,(0,1):C.GC_2077,(2,1):C.GC_2239})

V_149 = Vertex(name = 'V_149',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_337,(0,7):C.GC_339,(1,0):C.GC_3923,(3,0):C.GC_4085,(0,5):C.GC_3922,(2,5):C.GC_4084,(1,4):C.GC_1563,(3,4):C.GC_1644,(1,2):C.GC_1863,(3,2):C.GC_1944,(1,3):C.GC_2301,(3,3):C.GC_2382,(1,8):C.GC_1984,(3,8):C.GC_2146,(0,1):C.GC_2079,(2,1):C.GC_2241})

V_150 = Vertex(name = 'V_150',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_340,(0,7):C.GC_359,(1,0):C.GC_3977,(3,0):C.GC_4139,(0,5):C.GC_3928,(2,5):C.GC_4090,(1,4):C.GC_1572,(3,4):C.GC_1653,(1,2):C.GC_1864,(3,2):C.GC_1945,(1,3):C.GC_2310,(3,3):C.GC_2391,(1,8):C.GC_2002,(3,8):C.GC_2164,(0,1):C.GC_2097,(2,1):C.GC_2259})

V_151 = Vertex(name = 'V_151',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_343,(0,7):C.GC_382,(1,0):C.GC_4031,(3,0):C.GC_4193,(0,5):C.GC_3934,(2,5):C.GC_4096,(1,4):C.GC_1581,(3,4):C.GC_1662,(1,2):C.GC_1865,(3,2):C.GC_1946,(1,3):C.GC_2319,(3,3):C.GC_2400,(1,8):C.GC_2020,(3,8):C.GC_2182,(0,1):C.GC_2115,(2,1):C.GC_2277})

V_152 = Vertex(name = 'V_152',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_346,(0,7):C.GC_348,(1,0):C.GC_3941,(3,0):C.GC_4103,(0,5):C.GC_3940,(2,5):C.GC_4102,(1,4):C.GC_1590,(3,4):C.GC_1671,(1,2):C.GC_1866,(3,2):C.GC_1947,(1,3):C.GC_2328,(3,3):C.GC_2409,(1,8):C.GC_2038,(3,8):C.GC_2200,(0,1):C.GC_2085,(2,1):C.GC_2247})

V_153 = Vertex(name = 'V_153',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_349,(0,7):C.GC_368,(1,0):C.GC_3995,(3,0):C.GC_4157,(0,5):C.GC_3946,(2,5):C.GC_4108,(1,4):C.GC_1599,(3,4):C.GC_1680,(1,2):C.GC_1867,(3,2):C.GC_1948,(1,3):C.GC_2337,(3,3):C.GC_2418,(1,8):C.GC_2056,(3,8):C.GC_2218,(0,1):C.GC_2103,(2,1):C.GC_2265})

V_154 = Vertex(name = 'V_154',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_352,(0,7):C.GC_391,(1,0):C.GC_4049,(3,0):C.GC_4211,(0,5):C.GC_3952,(2,5):C.GC_4114,(1,4):C.GC_1608,(3,4):C.GC_1689,(1,2):C.GC_1868,(3,2):C.GC_1949,(1,3):C.GC_2346,(3,3):C.GC_2427,(1,8):C.GC_2074,(3,8):C.GC_2236,(0,1):C.GC_2121,(2,1):C.GC_2283})

V_155 = Vertex(name = 'V_155',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_355,(0,7):C.GC_1806,(1,0):C.GC_3959,(3,0):C.GC_4121,(0,5):C.GC_3958,(2,5):C.GC_4120,(1,4):C.GC_1617,(3,4):C.GC_1698,(1,2):C.GC_1869,(3,2):C.GC_1950,(1,3):C.GC_2355,(3,3):C.GC_2436,(1,8):C.GC_2092,(3,8):C.GC_2254,(0,1):C.GC_2091,(2,1):C.GC_2253})

V_156 = Vertex(name = 'V_156',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_375,(0,7):C.GC_377,(1,0):C.GC_4013,(3,0):C.GC_4175,(0,5):C.GC_3964,(2,5):C.GC_4126,(1,4):C.GC_1626,(3,4):C.GC_1707,(1,2):C.GC_1870,(3,2):C.GC_1951,(1,3):C.GC_2364,(3,3):C.GC_2445,(1,8):C.GC_2110,(3,8):C.GC_2272,(0,1):C.GC_2109,(2,1):C.GC_2271})

V_157 = Vertex(name = 'V_157',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_398,(0,7):C.GC_400,(1,0):C.GC_4067,(3,0):C.GC_4229,(0,5):C.GC_3970,(2,5):C.GC_4132,(1,4):C.GC_1635,(3,4):C.GC_1716,(1,2):C.GC_1871,(3,2):C.GC_1952,(1,3):C.GC_2373,(3,3):C.GC_2454,(1,8):C.GC_2128,(3,8):C.GC_2290,(0,1):C.GC_2127,(2,1):C.GC_2289})

V_158 = Vertex(name = 'V_158',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_357,(0,7):C.GC_342,(1,0):C.GC_3929,(3,0):C.GC_4091,(0,5):C.GC_3976,(2,5):C.GC_4138,(1,4):C.GC_1564,(3,4):C.GC_1645,(1,2):C.GC_1872,(3,2):C.GC_1953,(1,3):C.GC_2302,(3,3):C.GC_2383,(1,8):C.GC_1986,(3,8):C.GC_2148,(0,1):C.GC_2081,(2,1):C.GC_2243})

V_159 = Vertex(name = 'V_159',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_360,(0,7):C.GC_362,(1,0):C.GC_3983,(3,0):C.GC_4145,(0,5):C.GC_3982,(2,5):C.GC_4144,(1,4):C.GC_1573,(3,4):C.GC_1654,(1,2):C.GC_1873,(3,2):C.GC_1954,(1,3):C.GC_2311,(3,3):C.GC_2392,(1,8):C.GC_2004,(3,8):C.GC_2166,(0,1):C.GC_2099,(2,1):C.GC_2261})

V_160 = Vertex(name = 'V_160',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_363,(0,7):C.GC_385,(1,0):C.GC_4037,(3,0):C.GC_4199,(0,5):C.GC_3988,(2,5):C.GC_4150,(1,4):C.GC_1582,(3,4):C.GC_1663,(1,2):C.GC_1874,(3,2):C.GC_1955,(1,3):C.GC_2320,(3,3):C.GC_2401,(1,8):C.GC_2022,(3,8):C.GC_2184,(0,1):C.GC_2117,(2,1):C.GC_2279})

V_161 = Vertex(name = 'V_161',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_366,(0,7):C.GC_351,(1,0):C.GC_3947,(3,0):C.GC_4109,(0,5):C.GC_3994,(2,5):C.GC_4156,(1,4):C.GC_1591,(3,4):C.GC_1672,(1,2):C.GC_1875,(3,2):C.GC_1956,(1,3):C.GC_2329,(3,3):C.GC_2410,(1,8):C.GC_2040,(3,8):C.GC_2202,(0,1):C.GC_2087,(2,1):C.GC_2249})

V_162 = Vertex(name = 'V_162',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_369,(0,7):C.GC_371,(1,0):C.GC_4001,(3,0):C.GC_4163,(0,5):C.GC_4000,(2,5):C.GC_4162,(1,4):C.GC_1600,(3,4):C.GC_1681,(1,2):C.GC_1876,(3,2):C.GC_1957,(1,3):C.GC_2338,(3,3):C.GC_2419,(1,8):C.GC_2058,(3,8):C.GC_2220,(0,1):C.GC_2105,(2,1):C.GC_2267})

V_163 = Vertex(name = 'V_163',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_372,(0,7):C.GC_394,(1,0):C.GC_4055,(3,0):C.GC_4217,(0,5):C.GC_4006,(2,5):C.GC_4168,(1,4):C.GC_1609,(3,4):C.GC_1690,(1,2):C.GC_1877,(3,2):C.GC_1958,(1,3):C.GC_2347,(3,3):C.GC_2428,(1,8):C.GC_2076,(3,8):C.GC_2238,(0,1):C.GC_2123,(2,1):C.GC_2285})

V_164 = Vertex(name = 'V_164',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_375,(0,7):C.GC_377,(1,0):C.GC_3965,(3,0):C.GC_4127,(0,5):C.GC_4012,(2,5):C.GC_4174,(1,4):C.GC_1618,(3,4):C.GC_1699,(1,2):C.GC_1878,(3,2):C.GC_1959,(1,3):C.GC_2356,(3,3):C.GC_2437,(1,8):C.GC_2094,(3,8):C.GC_2256,(0,1):C.GC_2093,(2,1):C.GC_2255})

V_165 = Vertex(name = 'V_165',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_378,(0,7):C.GC_1807,(1,0):C.GC_4019,(3,0):C.GC_4181,(0,5):C.GC_4018,(2,5):C.GC_4180,(1,4):C.GC_1627,(3,4):C.GC_1708,(1,2):C.GC_1879,(3,2):C.GC_1960,(1,3):C.GC_2365,(3,3):C.GC_2446,(1,8):C.GC_2112,(3,8):C.GC_2274,(0,1):C.GC_2111,(2,1):C.GC_2273})

V_166 = Vertex(name = 'V_166',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_401,(0,7):C.GC_403,(1,0):C.GC_4073,(3,0):C.GC_4235,(0,5):C.GC_4024,(2,5):C.GC_4186,(1,4):C.GC_1636,(3,4):C.GC_1717,(1,2):C.GC_1880,(3,2):C.GC_1961,(1,3):C.GC_2374,(3,3):C.GC_2455,(1,8):C.GC_2130,(3,8):C.GC_2292,(0,1):C.GC_2129,(2,1):C.GC_2291})

V_167 = Vertex(name = 'V_167',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_380,(0,7):C.GC_345,(1,0):C.GC_3935,(3,0):C.GC_4097,(0,5):C.GC_4030,(2,5):C.GC_4192,(1,4):C.GC_1565,(3,4):C.GC_1646,(1,2):C.GC_1881,(3,2):C.GC_1962,(1,3):C.GC_2303,(3,3):C.GC_2384,(1,8):C.GC_1988,(3,8):C.GC_2150,(0,1):C.GC_2083,(2,1):C.GC_2245})

V_168 = Vertex(name = 'V_168',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_383,(0,7):C.GC_365,(1,0):C.GC_3989,(3,0):C.GC_4151,(0,5):C.GC_4036,(2,5):C.GC_4198,(1,4):C.GC_1574,(3,4):C.GC_1655,(1,2):C.GC_1882,(3,2):C.GC_1963,(1,3):C.GC_2312,(3,3):C.GC_2393,(1,8):C.GC_2006,(3,8):C.GC_2168,(0,1):C.GC_2101,(2,1):C.GC_2263})

V_169 = Vertex(name = 'V_169',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_386,(0,7):C.GC_388,(1,0):C.GC_4043,(3,0):C.GC_4205,(0,5):C.GC_4042,(2,5):C.GC_4204,(1,4):C.GC_1583,(3,4):C.GC_1664,(1,2):C.GC_1883,(3,2):C.GC_1964,(1,3):C.GC_2321,(3,3):C.GC_2402,(1,8):C.GC_2024,(3,8):C.GC_2186,(0,1):C.GC_2119,(2,1):C.GC_2281})

V_170 = Vertex(name = 'V_170',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_389,(0,7):C.GC_354,(1,0):C.GC_3953,(3,0):C.GC_4115,(0,5):C.GC_4048,(2,5):C.GC_4210,(1,4):C.GC_1592,(3,4):C.GC_1673,(1,2):C.GC_1884,(3,2):C.GC_1965,(1,3):C.GC_2330,(3,3):C.GC_2411,(1,8):C.GC_2042,(3,8):C.GC_2204,(0,1):C.GC_2089,(2,1):C.GC_2251})

V_171 = Vertex(name = 'V_171',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_392,(0,7):C.GC_374,(1,0):C.GC_4007,(3,0):C.GC_4169,(0,5):C.GC_4054,(2,5):C.GC_4216,(1,4):C.GC_1601,(3,4):C.GC_1682,(1,2):C.GC_1885,(3,2):C.GC_1966,(1,3):C.GC_2339,(3,3):C.GC_2420,(1,8):C.GC_2060,(3,8):C.GC_2222,(0,1):C.GC_2107,(2,1):C.GC_2269})

V_172 = Vertex(name = 'V_172',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_395,(0,7):C.GC_397,(1,0):C.GC_4061,(3,0):C.GC_4223,(0,5):C.GC_4060,(2,5):C.GC_4222,(1,4):C.GC_1610,(3,4):C.GC_1691,(1,2):C.GC_1886,(3,2):C.GC_1967,(1,3):C.GC_2348,(3,3):C.GC_2429,(1,8):C.GC_2078,(3,8):C.GC_2240,(0,1):C.GC_2125,(2,1):C.GC_2287})

V_173 = Vertex(name = 'V_173',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_398,(0,7):C.GC_400,(1,0):C.GC_3971,(3,0):C.GC_4133,(0,5):C.GC_4066,(2,5):C.GC_4228,(1,4):C.GC_1619,(3,4):C.GC_1700,(1,2):C.GC_1887,(3,2):C.GC_1968,(1,3):C.GC_2357,(3,3):C.GC_2438,(1,8):C.GC_2096,(3,8):C.GC_2258,(0,1):C.GC_2095,(2,1):C.GC_2257})

V_174 = Vertex(name = 'V_174',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_401,(0,7):C.GC_403,(1,0):C.GC_4025,(3,0):C.GC_4187,(0,5):C.GC_4072,(2,5):C.GC_4234,(1,4):C.GC_1628,(3,4):C.GC_1709,(1,2):C.GC_1888,(3,2):C.GC_1969,(1,3):C.GC_2366,(3,3):C.GC_2447,(1,8):C.GC_2114,(3,8):C.GC_2276,(0,1):C.GC_2113,(2,1):C.GC_2275})

V_175 = Vertex(name = 'V_175',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(1,6):C.GC_404,(0,7):C.GC_1808,(1,0):C.GC_4079,(3,0):C.GC_4241,(0,5):C.GC_4078,(2,5):C.GC_4240,(1,4):C.GC_1637,(3,4):C.GC_1718,(1,2):C.GC_1889,(3,2):C.GC_1970,(1,3):C.GC_2375,(3,3):C.GC_2456,(1,8):C.GC_2132,(3,8):C.GC_2294,(0,1):C.GC_2131,(2,1):C.GC_2293})

V_176 = Vertex(name = 'V_176',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_118,(0,11):C.GC_3597,(0,9):C.GC_3594,(0,10):C.GC_3594,(0,6):C.GC_3432,(0,1):C.GC_1719,(0,2):C.GC_1476,(0,3):C.GC_559,(0,7):C.GC_1065,(0,4):C.GC_1062,(0,5):C.GC_1062,(0,0):C.GC_900})

V_177 = Vertex(name = 'V_177',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_120,(0,11):C.GC_3609,(0,9):C.GC_3606,(0,10):C.GC_3606,(0,6):C.GC_3438,(0,1):C.GC_1728,(0,2):C.GC_1477,(0,3):C.GC_560,(0,7):C.GC_1069,(0,4):C.GC_1066,(0,5):C.GC_1066,(0,0):C.GC_902})

V_178 = Vertex(name = 'V_178',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_122,(0,11):C.GC_3621,(0,9):C.GC_3618,(0,10):C.GC_3618,(0,6):C.GC_3444,(0,1):C.GC_1737,(0,2):C.GC_1478,(0,3):C.GC_561,(0,7):C.GC_1073,(0,4):C.GC_1070,(0,5):C.GC_1070,(0,0):C.GC_904})

V_179 = Vertex(name = 'V_179',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_124,(0,11):C.GC_3601,(0,9):C.GC_3598,(0,10):C.GC_3598,(0,6):C.GC_3434,(0,1):C.GC_1746,(0,2):C.GC_1479,(0,3):C.GC_562,(0,7):C.GC_1077,(0,4):C.GC_1074,(0,5):C.GC_1074,(0,0):C.GC_906})

V_180 = Vertex(name = 'V_180',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_126,(0,11):C.GC_3613,(0,9):C.GC_3610,(0,10):C.GC_3610,(0,6):C.GC_3440,(0,1):C.GC_1755,(0,2):C.GC_1480,(0,3):C.GC_563,(0,7):C.GC_1081,(0,4):C.GC_1078,(0,5):C.GC_1078,(0,0):C.GC_908})

V_181 = Vertex(name = 'V_181',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_128,(0,11):C.GC_3625,(0,9):C.GC_3622,(0,10):C.GC_3622,(0,6):C.GC_3446,(0,1):C.GC_1764,(0,2):C.GC_1481,(0,3):C.GC_564,(0,7):C.GC_1085,(0,4):C.GC_1082,(0,5):C.GC_1082,(0,0):C.GC_910})

V_182 = Vertex(name = 'V_182',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_130,(0,11):C.GC_3605,(0,9):C.GC_3602,(0,10):C.GC_3602,(0,6):C.GC_3436,(0,1):C.GC_1773,(0,2):C.GC_1482,(0,3):C.GC_565,(0,7):C.GC_1089,(0,4):C.GC_1086,(0,5):C.GC_1086,(0,0):C.GC_912})

V_183 = Vertex(name = 'V_183',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_132,(0,11):C.GC_3617,(0,9):C.GC_3614,(0,10):C.GC_3614,(0,6):C.GC_3442,(0,1):C.GC_1782,(0,2):C.GC_1483,(0,3):C.GC_566,(0,7):C.GC_1093,(0,4):C.GC_1090,(0,5):C.GC_1090,(0,0):C.GC_914})

V_184 = Vertex(name = 'V_184',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_134,(0,11):C.GC_3629,(0,9):C.GC_3626,(0,10):C.GC_3626,(0,6):C.GC_3448,(0,1):C.GC_1791,(0,2):C.GC_1484,(0,3):C.GC_567,(0,7):C.GC_1097,(0,4):C.GC_1094,(0,5):C.GC_1094,(0,0):C.GC_916})

V_185 = Vertex(name = 'V_185',
               particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_136,(0,11):C.GC_3705,(0,9):C.GC_3702,(0,10):C.GC_3702,(0,6):C.GC_3486,(0,1):C.GC_1720,(0,2):C.GC_1485,(0,3):C.GC_568,(0,7):C.GC_1101,(0,4):C.GC_1098,(0,5):C.GC_1098,(0,0):C.GC_918})

V_186 = Vertex(name = 'V_186',
               particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_138,(0,11):C.GC_3717,(0,9):C.GC_3714,(0,10):C.GC_3714,(0,6):C.GC_3492,(0,1):C.GC_1729,(0,2):C.GC_1486,(0,3):C.GC_569,(0,7):C.GC_1105,(0,4):C.GC_1102,(0,5):C.GC_1102,(0,0):C.GC_920})

V_187 = Vertex(name = 'V_187',
               particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_140,(0,11):C.GC_3729,(0,9):C.GC_3726,(0,10):C.GC_3726,(0,6):C.GC_3498,(0,1):C.GC_1738,(0,2):C.GC_1487,(0,3):C.GC_570,(0,7):C.GC_1109,(0,4):C.GC_1106,(0,5):C.GC_1106,(0,0):C.GC_922})

V_188 = Vertex(name = 'V_188',
               particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_142,(0,11):C.GC_3709,(0,9):C.GC_3706,(0,10):C.GC_3706,(0,6):C.GC_3488,(0,1):C.GC_1747,(0,2):C.GC_1488,(0,3):C.GC_571,(0,7):C.GC_1113,(0,4):C.GC_1110,(0,5):C.GC_1110,(0,0):C.GC_924})

V_189 = Vertex(name = 'V_189',
               particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_144,(0,11):C.GC_3721,(0,9):C.GC_3718,(0,10):C.GC_3718,(0,6):C.GC_3494,(0,1):C.GC_1756,(0,2):C.GC_1489,(0,3):C.GC_572,(0,7):C.GC_1117,(0,4):C.GC_1114,(0,5):C.GC_1114,(0,0):C.GC_926})

V_190 = Vertex(name = 'V_190',
               particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_146,(0,11):C.GC_3733,(0,9):C.GC_3730,(0,10):C.GC_3730,(0,6):C.GC_3500,(0,1):C.GC_1765,(0,2):C.GC_1490,(0,3):C.GC_573,(0,7):C.GC_1121,(0,4):C.GC_1118,(0,5):C.GC_1118,(0,0):C.GC_928})

V_191 = Vertex(name = 'V_191',
               particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_148,(0,11):C.GC_3713,(0,9):C.GC_3710,(0,10):C.GC_3710,(0,6):C.GC_3490,(0,1):C.GC_1774,(0,2):C.GC_1491,(0,3):C.GC_574,(0,7):C.GC_1125,(0,4):C.GC_1122,(0,5):C.GC_1122,(0,0):C.GC_930})

V_192 = Vertex(name = 'V_192',
               particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_150,(0,11):C.GC_3725,(0,9):C.GC_3722,(0,10):C.GC_3722,(0,6):C.GC_3496,(0,1):C.GC_1783,(0,2):C.GC_1492,(0,3):C.GC_575,(0,7):C.GC_1129,(0,4):C.GC_1126,(0,5):C.GC_1126,(0,0):C.GC_932})

V_193 = Vertex(name = 'V_193',
               particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_152,(0,11):C.GC_3737,(0,9):C.GC_3734,(0,10):C.GC_3734,(0,6):C.GC_3502,(0,1):C.GC_1792,(0,2):C.GC_1493,(0,3):C.GC_576,(0,7):C.GC_1133,(0,4):C.GC_1130,(0,5):C.GC_1130,(0,0):C.GC_934})

V_194 = Vertex(name = 'V_194',
               particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_154,(0,11):C.GC_3813,(0,9):C.GC_3810,(0,10):C.GC_3810,(0,6):C.GC_3540,(0,1):C.GC_1721,(0,2):C.GC_1494,(0,3):C.GC_577,(0,7):C.GC_1137,(0,4):C.GC_1134,(0,5):C.GC_1134,(0,0):C.GC_936})

V_195 = Vertex(name = 'V_195',
               particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_156,(0,11):C.GC_3825,(0,9):C.GC_3822,(0,10):C.GC_3822,(0,6):C.GC_3546,(0,1):C.GC_1730,(0,2):C.GC_1495,(0,3):C.GC_578,(0,7):C.GC_1141,(0,4):C.GC_1138,(0,5):C.GC_1138,(0,0):C.GC_938})

V_196 = Vertex(name = 'V_196',
               particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_158,(0,11):C.GC_3837,(0,9):C.GC_3834,(0,10):C.GC_3834,(0,6):C.GC_3552,(0,1):C.GC_1739,(0,2):C.GC_1496,(0,3):C.GC_579,(0,7):C.GC_1145,(0,4):C.GC_1142,(0,5):C.GC_1142,(0,0):C.GC_940})

V_197 = Vertex(name = 'V_197',
               particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_160,(0,11):C.GC_3817,(0,9):C.GC_3814,(0,10):C.GC_3814,(0,6):C.GC_3542,(0,1):C.GC_1748,(0,2):C.GC_1497,(0,3):C.GC_580,(0,7):C.GC_1149,(0,4):C.GC_1146,(0,5):C.GC_1146,(0,0):C.GC_942})

V_198 = Vertex(name = 'V_198',
               particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_162,(0,11):C.GC_3829,(0,9):C.GC_3826,(0,10):C.GC_3826,(0,6):C.GC_3548,(0,1):C.GC_1757,(0,2):C.GC_1498,(0,3):C.GC_581,(0,7):C.GC_1153,(0,4):C.GC_1150,(0,5):C.GC_1150,(0,0):C.GC_944})

V_199 = Vertex(name = 'V_199',
               particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_164,(0,11):C.GC_3841,(0,9):C.GC_3838,(0,10):C.GC_3838,(0,6):C.GC_3554,(0,1):C.GC_1766,(0,2):C.GC_1499,(0,3):C.GC_582,(0,7):C.GC_1157,(0,4):C.GC_1154,(0,5):C.GC_1154,(0,0):C.GC_946})

V_200 = Vertex(name = 'V_200',
               particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_166,(0,11):C.GC_3821,(0,9):C.GC_3818,(0,10):C.GC_3818,(0,6):C.GC_3544,(0,1):C.GC_1775,(0,2):C.GC_1500,(0,3):C.GC_583,(0,7):C.GC_1161,(0,4):C.GC_1158,(0,5):C.GC_1158,(0,0):C.GC_948})

V_201 = Vertex(name = 'V_201',
               particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_168,(0,11):C.GC_3833,(0,9):C.GC_3830,(0,10):C.GC_3830,(0,6):C.GC_3550,(0,1):C.GC_1784,(0,2):C.GC_1501,(0,3):C.GC_584,(0,7):C.GC_1165,(0,4):C.GC_1162,(0,5):C.GC_1162,(0,0):C.GC_950})

V_202 = Vertex(name = 'V_202',
               particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_170,(0,11):C.GC_3845,(0,9):C.GC_3842,(0,10):C.GC_3842,(0,6):C.GC_3556,(0,1):C.GC_1793,(0,2):C.GC_1502,(0,3):C.GC_585,(0,7):C.GC_1169,(0,4):C.GC_1166,(0,5):C.GC_1166,(0,0):C.GC_952})

V_203 = Vertex(name = 'V_203',
               particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_172,(0,11):C.GC_3633,(0,9):C.GC_3630,(0,10):C.GC_3630,(0,6):C.GC_3450,(0,1):C.GC_1722,(0,2):C.GC_1503,(0,3):C.GC_586,(0,7):C.GC_1173,(0,4):C.GC_1170,(0,5):C.GC_1170,(0,0):C.GC_954})

V_204 = Vertex(name = 'V_204',
               particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_174,(0,11):C.GC_3645,(0,9):C.GC_3642,(0,10):C.GC_3642,(0,6):C.GC_3456,(0,1):C.GC_1731,(0,2):C.GC_1504,(0,3):C.GC_587,(0,7):C.GC_1177,(0,4):C.GC_1174,(0,5):C.GC_1174,(0,0):C.GC_956})

V_205 = Vertex(name = 'V_205',
               particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_176,(0,11):C.GC_3657,(0,9):C.GC_3654,(0,10):C.GC_3654,(0,6):C.GC_3462,(0,1):C.GC_1740,(0,2):C.GC_1505,(0,3):C.GC_588,(0,7):C.GC_1181,(0,4):C.GC_1178,(0,5):C.GC_1178,(0,0):C.GC_958})

V_206 = Vertex(name = 'V_206',
               particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_178,(0,11):C.GC_3637,(0,9):C.GC_3634,(0,10):C.GC_3634,(0,6):C.GC_3452,(0,1):C.GC_1749,(0,2):C.GC_1506,(0,3):C.GC_589,(0,7):C.GC_1185,(0,4):C.GC_1182,(0,5):C.GC_1182,(0,0):C.GC_960})

V_207 = Vertex(name = 'V_207',
               particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_180,(0,11):C.GC_3649,(0,9):C.GC_3646,(0,10):C.GC_3646,(0,6):C.GC_3458,(0,1):C.GC_1758,(0,2):C.GC_1507,(0,3):C.GC_590,(0,7):C.GC_1189,(0,4):C.GC_1186,(0,5):C.GC_1186,(0,0):C.GC_962})

V_208 = Vertex(name = 'V_208',
               particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_182,(0,11):C.GC_3661,(0,9):C.GC_3658,(0,10):C.GC_3658,(0,6):C.GC_3464,(0,1):C.GC_1767,(0,2):C.GC_1508,(0,3):C.GC_591,(0,7):C.GC_1193,(0,4):C.GC_1190,(0,5):C.GC_1190,(0,0):C.GC_964})

V_209 = Vertex(name = 'V_209',
               particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_184,(0,11):C.GC_3641,(0,9):C.GC_3638,(0,10):C.GC_3638,(0,6):C.GC_3454,(0,1):C.GC_1776,(0,2):C.GC_1509,(0,3):C.GC_592,(0,7):C.GC_1197,(0,4):C.GC_1194,(0,5):C.GC_1194,(0,0):C.GC_966})

V_210 = Vertex(name = 'V_210',
               particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_186,(0,11):C.GC_3653,(0,9):C.GC_3650,(0,10):C.GC_3650,(0,6):C.GC_3460,(0,1):C.GC_1785,(0,2):C.GC_1510,(0,3):C.GC_593,(0,7):C.GC_1201,(0,4):C.GC_1198,(0,5):C.GC_1198,(0,0):C.GC_968})

V_211 = Vertex(name = 'V_211',
               particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_188,(0,11):C.GC_3665,(0,9):C.GC_3662,(0,10):C.GC_3662,(0,6):C.GC_3466,(0,1):C.GC_1794,(0,2):C.GC_1511,(0,3):C.GC_594,(0,7):C.GC_1205,(0,4):C.GC_1202,(0,5):C.GC_1202,(0,0):C.GC_970})

V_212 = Vertex(name = 'V_212',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_190,(0,11):C.GC_3741,(0,9):C.GC_3738,(0,10):C.GC_3738,(0,6):C.GC_3504,(0,1):C.GC_1723,(0,2):C.GC_1512,(0,3):C.GC_595,(0,7):C.GC_1209,(0,4):C.GC_1206,(0,5):C.GC_1206,(0,0):C.GC_972})

V_213 = Vertex(name = 'V_213',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_192,(0,11):C.GC_3753,(0,9):C.GC_3750,(0,10):C.GC_3750,(0,6):C.GC_3510,(0,1):C.GC_1732,(0,2):C.GC_1513,(0,3):C.GC_596,(0,7):C.GC_1213,(0,4):C.GC_1210,(0,5):C.GC_1210,(0,0):C.GC_974})

V_214 = Vertex(name = 'V_214',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_194,(0,11):C.GC_3765,(0,9):C.GC_3762,(0,10):C.GC_3762,(0,6):C.GC_3516,(0,1):C.GC_1741,(0,2):C.GC_1514,(0,3):C.GC_597,(0,7):C.GC_1217,(0,4):C.GC_1214,(0,5):C.GC_1214,(0,0):C.GC_976})

V_215 = Vertex(name = 'V_215',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_196,(0,11):C.GC_3745,(0,9):C.GC_3742,(0,10):C.GC_3742,(0,6):C.GC_3506,(0,1):C.GC_1750,(0,2):C.GC_1515,(0,3):C.GC_598,(0,7):C.GC_1221,(0,4):C.GC_1218,(0,5):C.GC_1218,(0,0):C.GC_978})

V_216 = Vertex(name = 'V_216',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_198,(0,11):C.GC_3757,(0,9):C.GC_3754,(0,10):C.GC_3754,(0,6):C.GC_3512,(0,1):C.GC_1759,(0,2):C.GC_1516,(0,3):C.GC_599,(0,7):C.GC_1225,(0,4):C.GC_1222,(0,5):C.GC_1222,(0,0):C.GC_980})

V_217 = Vertex(name = 'V_217',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_200,(0,11):C.GC_3769,(0,9):C.GC_3766,(0,10):C.GC_3766,(0,6):C.GC_3518,(0,1):C.GC_1768,(0,2):C.GC_1517,(0,3):C.GC_600,(0,7):C.GC_1229,(0,4):C.GC_1226,(0,5):C.GC_1226,(0,0):C.GC_982})

V_218 = Vertex(name = 'V_218',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_202,(0,11):C.GC_3749,(0,9):C.GC_3746,(0,10):C.GC_3746,(0,6):C.GC_3508,(0,1):C.GC_1777,(0,2):C.GC_1518,(0,3):C.GC_601,(0,7):C.GC_1233,(0,4):C.GC_1230,(0,5):C.GC_1230,(0,0):C.GC_984})

V_219 = Vertex(name = 'V_219',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_204,(0,11):C.GC_3761,(0,9):C.GC_3758,(0,10):C.GC_3758,(0,6):C.GC_3514,(0,1):C.GC_1786,(0,2):C.GC_1519,(0,3):C.GC_602,(0,7):C.GC_1237,(0,4):C.GC_1234,(0,5):C.GC_1234,(0,0):C.GC_986})

V_220 = Vertex(name = 'V_220',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_206,(0,11):C.GC_3773,(0,9):C.GC_3770,(0,10):C.GC_3770,(0,6):C.GC_3520,(0,1):C.GC_1795,(0,2):C.GC_1520,(0,3):C.GC_603,(0,7):C.GC_1241,(0,4):C.GC_1238,(0,5):C.GC_1238,(0,0):C.GC_988})

V_221 = Vertex(name = 'V_221',
               particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_208,(0,11):C.GC_3849,(0,9):C.GC_3846,(0,10):C.GC_3846,(0,6):C.GC_3558,(0,1):C.GC_1724,(0,2):C.GC_1521,(0,3):C.GC_604,(0,7):C.GC_1245,(0,4):C.GC_1242,(0,5):C.GC_1242,(0,0):C.GC_990})

V_222 = Vertex(name = 'V_222',
               particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_210,(0,11):C.GC_3861,(0,9):C.GC_3858,(0,10):C.GC_3858,(0,6):C.GC_3564,(0,1):C.GC_1733,(0,2):C.GC_1522,(0,3):C.GC_605,(0,7):C.GC_1249,(0,4):C.GC_1246,(0,5):C.GC_1246,(0,0):C.GC_992})

V_223 = Vertex(name = 'V_223',
               particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_212,(0,11):C.GC_3873,(0,9):C.GC_3870,(0,10):C.GC_3870,(0,6):C.GC_3570,(0,1):C.GC_1742,(0,2):C.GC_1523,(0,3):C.GC_606,(0,7):C.GC_1253,(0,4):C.GC_1250,(0,5):C.GC_1250,(0,0):C.GC_994})

V_224 = Vertex(name = 'V_224',
               particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_214,(0,11):C.GC_3853,(0,9):C.GC_3850,(0,10):C.GC_3850,(0,6):C.GC_3560,(0,1):C.GC_1751,(0,2):C.GC_1524,(0,3):C.GC_607,(0,7):C.GC_1257,(0,4):C.GC_1254,(0,5):C.GC_1254,(0,0):C.GC_996})

V_225 = Vertex(name = 'V_225',
               particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_216,(0,11):C.GC_3865,(0,9):C.GC_3862,(0,10):C.GC_3862,(0,6):C.GC_3566,(0,1):C.GC_1760,(0,2):C.GC_1525,(0,3):C.GC_608,(0,7):C.GC_1261,(0,4):C.GC_1258,(0,5):C.GC_1258,(0,0):C.GC_998})

V_226 = Vertex(name = 'V_226',
               particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_218,(0,11):C.GC_3877,(0,9):C.GC_3874,(0,10):C.GC_3874,(0,6):C.GC_3572,(0,1):C.GC_1769,(0,2):C.GC_1526,(0,3):C.GC_609,(0,7):C.GC_1265,(0,4):C.GC_1262,(0,5):C.GC_1262,(0,0):C.GC_1000})

V_227 = Vertex(name = 'V_227',
               particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_220,(0,11):C.GC_3857,(0,9):C.GC_3854,(0,10):C.GC_3854,(0,6):C.GC_3562,(0,1):C.GC_1778,(0,2):C.GC_1527,(0,3):C.GC_610,(0,7):C.GC_1269,(0,4):C.GC_1266,(0,5):C.GC_1266,(0,0):C.GC_1002})

V_228 = Vertex(name = 'V_228',
               particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_222,(0,11):C.GC_3869,(0,9):C.GC_3866,(0,10):C.GC_3866,(0,6):C.GC_3568,(0,1):C.GC_1787,(0,2):C.GC_1528,(0,3):C.GC_611,(0,7):C.GC_1273,(0,4):C.GC_1270,(0,5):C.GC_1270,(0,0):C.GC_1004})

V_229 = Vertex(name = 'V_229',
               particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_224,(0,11):C.GC_3881,(0,9):C.GC_3878,(0,10):C.GC_3878,(0,6):C.GC_3574,(0,1):C.GC_1796,(0,2):C.GC_1529,(0,3):C.GC_612,(0,7):C.GC_1277,(0,4):C.GC_1274,(0,5):C.GC_1274,(0,0):C.GC_1006})

V_230 = Vertex(name = 'V_230',
               particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_226,(0,11):C.GC_3669,(0,9):C.GC_3666,(0,10):C.GC_3666,(0,6):C.GC_3468,(0,1):C.GC_1725,(0,2):C.GC_1530,(0,3):C.GC_613,(0,7):C.GC_1281,(0,4):C.GC_1278,(0,5):C.GC_1278,(0,0):C.GC_1008})

V_231 = Vertex(name = 'V_231',
               particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_228,(0,11):C.GC_3681,(0,9):C.GC_3678,(0,10):C.GC_3678,(0,6):C.GC_3474,(0,1):C.GC_1734,(0,2):C.GC_1531,(0,3):C.GC_614,(0,7):C.GC_1285,(0,4):C.GC_1282,(0,5):C.GC_1282,(0,0):C.GC_1010})

V_232 = Vertex(name = 'V_232',
               particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_230,(0,11):C.GC_3693,(0,9):C.GC_3690,(0,10):C.GC_3690,(0,6):C.GC_3480,(0,1):C.GC_1743,(0,2):C.GC_1532,(0,3):C.GC_615,(0,7):C.GC_1289,(0,4):C.GC_1286,(0,5):C.GC_1286,(0,0):C.GC_1012})

V_233 = Vertex(name = 'V_233',
               particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_232,(0,11):C.GC_3673,(0,9):C.GC_3670,(0,10):C.GC_3670,(0,6):C.GC_3470,(0,1):C.GC_1752,(0,2):C.GC_1533,(0,3):C.GC_616,(0,7):C.GC_1293,(0,4):C.GC_1290,(0,5):C.GC_1290,(0,0):C.GC_1014})

V_234 = Vertex(name = 'V_234',
               particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_234,(0,11):C.GC_3685,(0,9):C.GC_3682,(0,10):C.GC_3682,(0,6):C.GC_3476,(0,1):C.GC_1761,(0,2):C.GC_1534,(0,3):C.GC_617,(0,7):C.GC_1297,(0,4):C.GC_1294,(0,5):C.GC_1294,(0,0):C.GC_1016})

V_235 = Vertex(name = 'V_235',
               particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_236,(0,11):C.GC_3697,(0,9):C.GC_3694,(0,10):C.GC_3694,(0,6):C.GC_3482,(0,1):C.GC_1770,(0,2):C.GC_1535,(0,3):C.GC_618,(0,7):C.GC_1301,(0,4):C.GC_1298,(0,5):C.GC_1298,(0,0):C.GC_1018})

V_236 = Vertex(name = 'V_236',
               particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_238,(0,11):C.GC_3677,(0,9):C.GC_3674,(0,10):C.GC_3674,(0,6):C.GC_3472,(0,1):C.GC_1779,(0,2):C.GC_1536,(0,3):C.GC_619,(0,7):C.GC_1305,(0,4):C.GC_1302,(0,5):C.GC_1302,(0,0):C.GC_1020})

V_237 = Vertex(name = 'V_237',
               particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_240,(0,11):C.GC_3689,(0,9):C.GC_3686,(0,10):C.GC_3686,(0,6):C.GC_3478,(0,1):C.GC_1788,(0,2):C.GC_1537,(0,3):C.GC_620,(0,7):C.GC_1309,(0,4):C.GC_1306,(0,5):C.GC_1306,(0,0):C.GC_1022})

V_238 = Vertex(name = 'V_238',
               particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_242,(0,11):C.GC_3701,(0,9):C.GC_3698,(0,10):C.GC_3698,(0,6):C.GC_3484,(0,1):C.GC_1797,(0,2):C.GC_1538,(0,3):C.GC_621,(0,7):C.GC_1313,(0,4):C.GC_1310,(0,5):C.GC_1310,(0,0):C.GC_1024})

V_239 = Vertex(name = 'V_239',
               particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_244,(0,11):C.GC_3777,(0,9):C.GC_3774,(0,10):C.GC_3774,(0,6):C.GC_3522,(0,1):C.GC_1726,(0,2):C.GC_1539,(0,3):C.GC_622,(0,7):C.GC_1317,(0,4):C.GC_1314,(0,5):C.GC_1314,(0,0):C.GC_1026})

V_240 = Vertex(name = 'V_240',
               particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_246,(0,11):C.GC_3789,(0,9):C.GC_3786,(0,10):C.GC_3786,(0,6):C.GC_3528,(0,1):C.GC_1735,(0,2):C.GC_1540,(0,3):C.GC_623,(0,7):C.GC_1321,(0,4):C.GC_1318,(0,5):C.GC_1318,(0,0):C.GC_1028})

V_241 = Vertex(name = 'V_241',
               particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_248,(0,11):C.GC_3801,(0,9):C.GC_3798,(0,10):C.GC_3798,(0,6):C.GC_3534,(0,1):C.GC_1744,(0,2):C.GC_1541,(0,3):C.GC_624,(0,7):C.GC_1325,(0,4):C.GC_1322,(0,5):C.GC_1322,(0,0):C.GC_1030})

V_242 = Vertex(name = 'V_242',
               particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_250,(0,11):C.GC_3781,(0,9):C.GC_3778,(0,10):C.GC_3778,(0,6):C.GC_3524,(0,1):C.GC_1753,(0,2):C.GC_1542,(0,3):C.GC_625,(0,7):C.GC_1329,(0,4):C.GC_1326,(0,5):C.GC_1326,(0,0):C.GC_1032})

V_243 = Vertex(name = 'V_243',
               particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_252,(0,11):C.GC_3793,(0,9):C.GC_3790,(0,10):C.GC_3790,(0,6):C.GC_3530,(0,1):C.GC_1762,(0,2):C.GC_1543,(0,3):C.GC_626,(0,7):C.GC_1333,(0,4):C.GC_1330,(0,5):C.GC_1330,(0,0):C.GC_1034})

V_244 = Vertex(name = 'V_244',
               particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_254,(0,11):C.GC_3805,(0,9):C.GC_3802,(0,10):C.GC_3802,(0,6):C.GC_3536,(0,1):C.GC_1771,(0,2):C.GC_1544,(0,3):C.GC_627,(0,7):C.GC_1337,(0,4):C.GC_1334,(0,5):C.GC_1334,(0,0):C.GC_1036})

V_245 = Vertex(name = 'V_245',
               particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_256,(0,11):C.GC_3785,(0,9):C.GC_3782,(0,10):C.GC_3782,(0,6):C.GC_3526,(0,1):C.GC_1780,(0,2):C.GC_1545,(0,3):C.GC_628,(0,7):C.GC_1341,(0,4):C.GC_1338,(0,5):C.GC_1338,(0,0):C.GC_1038})

V_246 = Vertex(name = 'V_246',
               particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_258,(0,11):C.GC_3797,(0,9):C.GC_3794,(0,10):C.GC_3794,(0,6):C.GC_3532,(0,1):C.GC_1789,(0,2):C.GC_1546,(0,3):C.GC_629,(0,7):C.GC_1345,(0,4):C.GC_1342,(0,5):C.GC_1342,(0,0):C.GC_1040})

V_247 = Vertex(name = 'V_247',
               particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_260,(0,11):C.GC_3809,(0,9):C.GC_3806,(0,10):C.GC_3806,(0,6):C.GC_3538,(0,1):C.GC_1798,(0,2):C.GC_1547,(0,3):C.GC_630,(0,7):C.GC_1349,(0,4):C.GC_1346,(0,5):C.GC_1346,(0,0):C.GC_1042})

V_248 = Vertex(name = 'V_248',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_262,(0,11):C.GC_3885,(0,9):C.GC_3882,(0,10):C.GC_3882,(0,6):C.GC_3576,(0,1):C.GC_1727,(0,2):C.GC_1548,(0,3):C.GC_631,(0,7):C.GC_1353,(0,4):C.GC_1350,(0,5):C.GC_1350,(0,0):C.GC_1044})

V_249 = Vertex(name = 'V_249',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_264,(0,11):C.GC_3897,(0,9):C.GC_3894,(0,10):C.GC_3894,(0,6):C.GC_3582,(0,1):C.GC_1736,(0,2):C.GC_1549,(0,3):C.GC_632,(0,7):C.GC_1357,(0,4):C.GC_1354,(0,5):C.GC_1354,(0,0):C.GC_1046})

V_250 = Vertex(name = 'V_250',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_266,(0,11):C.GC_3909,(0,9):C.GC_3906,(0,10):C.GC_3906,(0,6):C.GC_3588,(0,1):C.GC_1745,(0,2):C.GC_1550,(0,3):C.GC_633,(0,7):C.GC_1361,(0,4):C.GC_1358,(0,5):C.GC_1358,(0,0):C.GC_1048})

V_251 = Vertex(name = 'V_251',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_268,(0,11):C.GC_3889,(0,9):C.GC_3886,(0,10):C.GC_3886,(0,6):C.GC_3578,(0,1):C.GC_1754,(0,2):C.GC_1551,(0,3):C.GC_634,(0,7):C.GC_1365,(0,4):C.GC_1362,(0,5):C.GC_1362,(0,0):C.GC_1050})

V_252 = Vertex(name = 'V_252',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_270,(0,11):C.GC_3901,(0,9):C.GC_3898,(0,10):C.GC_3898,(0,6):C.GC_3584,(0,1):C.GC_1763,(0,2):C.GC_1552,(0,3):C.GC_635,(0,7):C.GC_1369,(0,4):C.GC_1366,(0,5):C.GC_1366,(0,0):C.GC_1052})

V_253 = Vertex(name = 'V_253',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_272,(0,11):C.GC_3913,(0,9):C.GC_3910,(0,10):C.GC_3910,(0,6):C.GC_3590,(0,1):C.GC_1772,(0,2):C.GC_1553,(0,3):C.GC_636,(0,7):C.GC_1373,(0,4):C.GC_1370,(0,5):C.GC_1370,(0,0):C.GC_1054})

V_254 = Vertex(name = 'V_254',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_274,(0,11):C.GC_3893,(0,9):C.GC_3890,(0,10):C.GC_3890,(0,6):C.GC_3580,(0,1):C.GC_1781,(0,2):C.GC_1554,(0,3):C.GC_637,(0,7):C.GC_1377,(0,4):C.GC_1374,(0,5):C.GC_1374,(0,0):C.GC_1056})

V_255 = Vertex(name = 'V_255',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_276,(0,11):C.GC_3905,(0,9):C.GC_3902,(0,10):C.GC_3902,(0,6):C.GC_3586,(0,1):C.GC_1790,(0,2):C.GC_1555,(0,3):C.GC_638,(0,7):C.GC_1381,(0,4):C.GC_1378,(0,5):C.GC_1378,(0,0):C.GC_1058})

V_256 = Vertex(name = 'V_256',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,8):C.GC_278,(0,11):C.GC_3917,(0,9):C.GC_3914,(0,10):C.GC_3914,(0,6):C.GC_3592,(0,1):C.GC_1799,(0,2):C.GC_1556,(0,3):C.GC_639,(0,7):C.GC_1385,(0,4):C.GC_1382,(0,5):C.GC_1382,(0,0):C.GC_1060})

V_257 = Vertex(name = 'V_257',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1395,(0,5):C.GC_3596,(0,3):C.GC_3595,(0,4):C.GC_3595,(0,1):C.GC_3433,(0,0):C.GC_3351})

V_258 = Vertex(name = 'V_258',
               particles = [ P.vm__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1404,(0,5):C.GC_3704,(0,3):C.GC_3703,(0,4):C.GC_3703,(0,1):C.GC_3487,(0,0):C.GC_3378})

V_259 = Vertex(name = 'V_259',
               particles = [ P.vt__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1413,(0,5):C.GC_3812,(0,3):C.GC_3811,(0,4):C.GC_3811,(0,1):C.GC_3541,(0,0):C.GC_3405})

V_260 = Vertex(name = 'V_260',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1398,(0,5):C.GC_3600,(0,3):C.GC_3599,(0,4):C.GC_3599,(0,1):C.GC_3435,(0,0):C.GC_3352})

V_261 = Vertex(name = 'V_261',
               particles = [ P.vm__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1407,(0,5):C.GC_3708,(0,3):C.GC_3707,(0,4):C.GC_3707,(0,1):C.GC_3489,(0,0):C.GC_3379})

V_262 = Vertex(name = 'V_262',
               particles = [ P.vt__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1416,(0,5):C.GC_3816,(0,3):C.GC_3815,(0,4):C.GC_3815,(0,1):C.GC_3543,(0,0):C.GC_3406})

V_263 = Vertex(name = 'V_263',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1401,(0,5):C.GC_3604,(0,3):C.GC_3603,(0,4):C.GC_3603,(0,1):C.GC_3437,(0,0):C.GC_3353})

V_264 = Vertex(name = 'V_264',
               particles = [ P.vm__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1410,(0,5):C.GC_3712,(0,3):C.GC_3711,(0,4):C.GC_3711,(0,1):C.GC_3491,(0,0):C.GC_3380})

V_265 = Vertex(name = 'V_265',
               particles = [ P.vt__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1419,(0,5):C.GC_3820,(0,3):C.GC_3819,(0,4):C.GC_3819,(0,1):C.GC_3545,(0,0):C.GC_3407})

V_266 = Vertex(name = 'V_266',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1396,(0,5):C.GC_3608,(0,3):C.GC_3607,(0,4):C.GC_3607,(0,1):C.GC_3439,(0,0):C.GC_3354})

V_267 = Vertex(name = 'V_267',
               particles = [ P.vm__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1405,(0,5):C.GC_3716,(0,3):C.GC_3715,(0,4):C.GC_3715,(0,1):C.GC_3493,(0,0):C.GC_3381})

V_268 = Vertex(name = 'V_268',
               particles = [ P.vt__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1414,(0,5):C.GC_3824,(0,3):C.GC_3823,(0,4):C.GC_3823,(0,1):C.GC_3547,(0,0):C.GC_3408})

V_269 = Vertex(name = 'V_269',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1399,(0,5):C.GC_3612,(0,3):C.GC_3611,(0,4):C.GC_3611,(0,1):C.GC_3441,(0,0):C.GC_3355})

V_270 = Vertex(name = 'V_270',
               particles = [ P.vm__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1408,(0,5):C.GC_3720,(0,3):C.GC_3719,(0,4):C.GC_3719,(0,1):C.GC_3495,(0,0):C.GC_3382})

V_271 = Vertex(name = 'V_271',
               particles = [ P.vt__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1417,(0,5):C.GC_3828,(0,3):C.GC_3827,(0,4):C.GC_3827,(0,1):C.GC_3549,(0,0):C.GC_3409})

V_272 = Vertex(name = 'V_272',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1402,(0,5):C.GC_3616,(0,3):C.GC_3615,(0,4):C.GC_3615,(0,1):C.GC_3443,(0,0):C.GC_3356})

V_273 = Vertex(name = 'V_273',
               particles = [ P.vm__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1411,(0,5):C.GC_3724,(0,3):C.GC_3723,(0,4):C.GC_3723,(0,1):C.GC_3497,(0,0):C.GC_3383})

V_274 = Vertex(name = 'V_274',
               particles = [ P.vt__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1420,(0,5):C.GC_3832,(0,3):C.GC_3831,(0,4):C.GC_3831,(0,1):C.GC_3551,(0,0):C.GC_3410})

V_275 = Vertex(name = 'V_275',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1397,(0,5):C.GC_3620,(0,3):C.GC_3619,(0,4):C.GC_3619,(0,1):C.GC_3445,(0,0):C.GC_3357})

V_276 = Vertex(name = 'V_276',
               particles = [ P.vm__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1406,(0,5):C.GC_3728,(0,3):C.GC_3727,(0,4):C.GC_3727,(0,1):C.GC_3499,(0,0):C.GC_3384})

V_277 = Vertex(name = 'V_277',
               particles = [ P.vt__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1415,(0,5):C.GC_3836,(0,3):C.GC_3835,(0,4):C.GC_3835,(0,1):C.GC_3553,(0,0):C.GC_3411})

V_278 = Vertex(name = 'V_278',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1400,(0,5):C.GC_3624,(0,3):C.GC_3623,(0,4):C.GC_3623,(0,1):C.GC_3447,(0,0):C.GC_3358})

V_279 = Vertex(name = 'V_279',
               particles = [ P.vm__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1409,(0,5):C.GC_3732,(0,3):C.GC_3731,(0,4):C.GC_3731,(0,1):C.GC_3501,(0,0):C.GC_3385})

V_280 = Vertex(name = 'V_280',
               particles = [ P.vt__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1418,(0,5):C.GC_3840,(0,3):C.GC_3839,(0,4):C.GC_3839,(0,1):C.GC_3555,(0,0):C.GC_3412})

V_281 = Vertex(name = 'V_281',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1403,(0,5):C.GC_3628,(0,3):C.GC_3627,(0,4):C.GC_3627,(0,1):C.GC_3449,(0,0):C.GC_3359})

V_282 = Vertex(name = 'V_282',
               particles = [ P.vm__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1412,(0,5):C.GC_3736,(0,3):C.GC_3735,(0,4):C.GC_3735,(0,1):C.GC_3503,(0,0):C.GC_3386})

V_283 = Vertex(name = 'V_283',
               particles = [ P.vt__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1421,(0,5):C.GC_3844,(0,3):C.GC_3843,(0,4):C.GC_3843,(0,1):C.GC_3557,(0,0):C.GC_3413})

V_284 = Vertex(name = 'V_284',
               particles = [ P.ve__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1422,(0,5):C.GC_3632,(0,3):C.GC_3631,(0,4):C.GC_3631,(0,1):C.GC_3451,(0,0):C.GC_3360})

V_285 = Vertex(name = 'V_285',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1431,(0,5):C.GC_3740,(0,3):C.GC_3739,(0,4):C.GC_3739,(0,1):C.GC_3505,(0,0):C.GC_3387})

V_286 = Vertex(name = 'V_286',
               particles = [ P.vt__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1440,(0,5):C.GC_3848,(0,3):C.GC_3847,(0,4):C.GC_3847,(0,1):C.GC_3559,(0,0):C.GC_3414})

V_287 = Vertex(name = 'V_287',
               particles = [ P.ve__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1425,(0,5):C.GC_3636,(0,3):C.GC_3635,(0,4):C.GC_3635,(0,1):C.GC_3453,(0,0):C.GC_3361})

V_288 = Vertex(name = 'V_288',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1434,(0,5):C.GC_3744,(0,3):C.GC_3743,(0,4):C.GC_3743,(0,1):C.GC_3507,(0,0):C.GC_3388})

V_289 = Vertex(name = 'V_289',
               particles = [ P.vt__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1443,(0,5):C.GC_3852,(0,3):C.GC_3851,(0,4):C.GC_3851,(0,1):C.GC_3561,(0,0):C.GC_3415})

V_290 = Vertex(name = 'V_290',
               particles = [ P.ve__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1428,(0,5):C.GC_3640,(0,3):C.GC_3639,(0,4):C.GC_3639,(0,1):C.GC_3455,(0,0):C.GC_3362})

V_291 = Vertex(name = 'V_291',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1437,(0,5):C.GC_3748,(0,3):C.GC_3747,(0,4):C.GC_3747,(0,1):C.GC_3509,(0,0):C.GC_3389})

V_292 = Vertex(name = 'V_292',
               particles = [ P.vt__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1446,(0,5):C.GC_3856,(0,3):C.GC_3855,(0,4):C.GC_3855,(0,1):C.GC_3563,(0,0):C.GC_3416})

V_293 = Vertex(name = 'V_293',
               particles = [ P.ve__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1423,(0,5):C.GC_3644,(0,3):C.GC_3643,(0,4):C.GC_3643,(0,1):C.GC_3457,(0,0):C.GC_3363})

V_294 = Vertex(name = 'V_294',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1432,(0,5):C.GC_3752,(0,3):C.GC_3751,(0,4):C.GC_3751,(0,1):C.GC_3511,(0,0):C.GC_3390})

V_295 = Vertex(name = 'V_295',
               particles = [ P.vt__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1441,(0,5):C.GC_3860,(0,3):C.GC_3859,(0,4):C.GC_3859,(0,1):C.GC_3565,(0,0):C.GC_3417})

V_296 = Vertex(name = 'V_296',
               particles = [ P.ve__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1426,(0,5):C.GC_3648,(0,3):C.GC_3647,(0,4):C.GC_3647,(0,1):C.GC_3459,(0,0):C.GC_3364})

V_297 = Vertex(name = 'V_297',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1435,(0,5):C.GC_3756,(0,3):C.GC_3755,(0,4):C.GC_3755,(0,1):C.GC_3513,(0,0):C.GC_3391})

V_298 = Vertex(name = 'V_298',
               particles = [ P.vt__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1444,(0,5):C.GC_3864,(0,3):C.GC_3863,(0,4):C.GC_3863,(0,1):C.GC_3567,(0,0):C.GC_3418})

V_299 = Vertex(name = 'V_299',
               particles = [ P.ve__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1429,(0,5):C.GC_3652,(0,3):C.GC_3651,(0,4):C.GC_3651,(0,1):C.GC_3461,(0,0):C.GC_3365})

V_300 = Vertex(name = 'V_300',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1438,(0,5):C.GC_3760,(0,3):C.GC_3759,(0,4):C.GC_3759,(0,1):C.GC_3515,(0,0):C.GC_3392})

V_301 = Vertex(name = 'V_301',
               particles = [ P.vt__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1447,(0,5):C.GC_3868,(0,3):C.GC_3867,(0,4):C.GC_3867,(0,1):C.GC_3569,(0,0):C.GC_3419})

V_302 = Vertex(name = 'V_302',
               particles = [ P.ve__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1424,(0,5):C.GC_3656,(0,3):C.GC_3655,(0,4):C.GC_3655,(0,1):C.GC_3463,(0,0):C.GC_3366})

V_303 = Vertex(name = 'V_303',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1433,(0,5):C.GC_3764,(0,3):C.GC_3763,(0,4):C.GC_3763,(0,1):C.GC_3517,(0,0):C.GC_3393})

V_304 = Vertex(name = 'V_304',
               particles = [ P.vt__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1442,(0,5):C.GC_3872,(0,3):C.GC_3871,(0,4):C.GC_3871,(0,1):C.GC_3571,(0,0):C.GC_3420})

V_305 = Vertex(name = 'V_305',
               particles = [ P.ve__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1427,(0,5):C.GC_3660,(0,3):C.GC_3659,(0,4):C.GC_3659,(0,1):C.GC_3465,(0,0):C.GC_3367})

V_306 = Vertex(name = 'V_306',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1436,(0,5):C.GC_3768,(0,3):C.GC_3767,(0,4):C.GC_3767,(0,1):C.GC_3519,(0,0):C.GC_3394})

V_307 = Vertex(name = 'V_307',
               particles = [ P.vt__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1445,(0,5):C.GC_3876,(0,3):C.GC_3875,(0,4):C.GC_3875,(0,1):C.GC_3573,(0,0):C.GC_3421})

V_308 = Vertex(name = 'V_308',
               particles = [ P.ve__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1430,(0,5):C.GC_3664,(0,3):C.GC_3663,(0,4):C.GC_3663,(0,1):C.GC_3467,(0,0):C.GC_3368})

V_309 = Vertex(name = 'V_309',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1439,(0,5):C.GC_3772,(0,3):C.GC_3771,(0,4):C.GC_3771,(0,1):C.GC_3521,(0,0):C.GC_3395})

V_310 = Vertex(name = 'V_310',
               particles = [ P.vt__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1448,(0,5):C.GC_3880,(0,3):C.GC_3879,(0,4):C.GC_3879,(0,1):C.GC_3575,(0,0):C.GC_3422})

V_311 = Vertex(name = 'V_311',
               particles = [ P.ve__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1449,(0,5):C.GC_3668,(0,3):C.GC_3667,(0,4):C.GC_3667,(0,1):C.GC_3469,(0,0):C.GC_3369})

V_312 = Vertex(name = 'V_312',
               particles = [ P.vm__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1458,(0,5):C.GC_3776,(0,3):C.GC_3775,(0,4):C.GC_3775,(0,1):C.GC_3523,(0,0):C.GC_3396})

V_313 = Vertex(name = 'V_313',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1467,(0,5):C.GC_3884,(0,3):C.GC_3883,(0,4):C.GC_3883,(0,1):C.GC_3577,(0,0):C.GC_3423})

V_314 = Vertex(name = 'V_314',
               particles = [ P.ve__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1452,(0,5):C.GC_3672,(0,3):C.GC_3671,(0,4):C.GC_3671,(0,1):C.GC_3471,(0,0):C.GC_3370})

V_315 = Vertex(name = 'V_315',
               particles = [ P.vm__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1461,(0,5):C.GC_3780,(0,3):C.GC_3779,(0,4):C.GC_3779,(0,1):C.GC_3525,(0,0):C.GC_3397})

V_316 = Vertex(name = 'V_316',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1470,(0,5):C.GC_3888,(0,3):C.GC_3887,(0,4):C.GC_3887,(0,1):C.GC_3579,(0,0):C.GC_3424})

V_317 = Vertex(name = 'V_317',
               particles = [ P.ve__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1455,(0,5):C.GC_3676,(0,3):C.GC_3675,(0,4):C.GC_3675,(0,1):C.GC_3473,(0,0):C.GC_3371})

V_318 = Vertex(name = 'V_318',
               particles = [ P.vm__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1464,(0,5):C.GC_3784,(0,3):C.GC_3783,(0,4):C.GC_3783,(0,1):C.GC_3527,(0,0):C.GC_3398})

V_319 = Vertex(name = 'V_319',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1473,(0,5):C.GC_3892,(0,3):C.GC_3891,(0,4):C.GC_3891,(0,1):C.GC_3581,(0,0):C.GC_3425})

V_320 = Vertex(name = 'V_320',
               particles = [ P.ve__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1450,(0,5):C.GC_3680,(0,3):C.GC_3679,(0,4):C.GC_3679,(0,1):C.GC_3475,(0,0):C.GC_3372})

V_321 = Vertex(name = 'V_321',
               particles = [ P.vm__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1459,(0,5):C.GC_3788,(0,3):C.GC_3787,(0,4):C.GC_3787,(0,1):C.GC_3529,(0,0):C.GC_3399})

V_322 = Vertex(name = 'V_322',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1468,(0,5):C.GC_3896,(0,3):C.GC_3895,(0,4):C.GC_3895,(0,1):C.GC_3583,(0,0):C.GC_3426})

V_323 = Vertex(name = 'V_323',
               particles = [ P.ve__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1453,(0,5):C.GC_3684,(0,3):C.GC_3683,(0,4):C.GC_3683,(0,1):C.GC_3477,(0,0):C.GC_3373})

V_324 = Vertex(name = 'V_324',
               particles = [ P.vm__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1462,(0,5):C.GC_3792,(0,3):C.GC_3791,(0,4):C.GC_3791,(0,1):C.GC_3531,(0,0):C.GC_3400})

V_325 = Vertex(name = 'V_325',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1471,(0,5):C.GC_3900,(0,3):C.GC_3899,(0,4):C.GC_3899,(0,1):C.GC_3585,(0,0):C.GC_3427})

V_326 = Vertex(name = 'V_326',
               particles = [ P.ve__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1456,(0,5):C.GC_3688,(0,3):C.GC_3687,(0,4):C.GC_3687,(0,1):C.GC_3479,(0,0):C.GC_3374})

V_327 = Vertex(name = 'V_327',
               particles = [ P.vm__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1465,(0,5):C.GC_3796,(0,3):C.GC_3795,(0,4):C.GC_3795,(0,1):C.GC_3533,(0,0):C.GC_3401})

V_328 = Vertex(name = 'V_328',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1474,(0,5):C.GC_3904,(0,3):C.GC_3903,(0,4):C.GC_3903,(0,1):C.GC_3587,(0,0):C.GC_3428})

V_329 = Vertex(name = 'V_329',
               particles = [ P.ve__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1451,(0,5):C.GC_3692,(0,3):C.GC_3691,(0,4):C.GC_3691,(0,1):C.GC_3481,(0,0):C.GC_3375})

V_330 = Vertex(name = 'V_330',
               particles = [ P.vm__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1460,(0,5):C.GC_3800,(0,3):C.GC_3799,(0,4):C.GC_3799,(0,1):C.GC_3535,(0,0):C.GC_3402})

V_331 = Vertex(name = 'V_331',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1469,(0,5):C.GC_3908,(0,3):C.GC_3907,(0,4):C.GC_3907,(0,1):C.GC_3589,(0,0):C.GC_3429})

V_332 = Vertex(name = 'V_332',
               particles = [ P.ve__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1454,(0,5):C.GC_3696,(0,3):C.GC_3695,(0,4):C.GC_3695,(0,1):C.GC_3483,(0,0):C.GC_3376})

V_333 = Vertex(name = 'V_333',
               particles = [ P.vm__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1463,(0,5):C.GC_3804,(0,3):C.GC_3803,(0,4):C.GC_3803,(0,1):C.GC_3537,(0,0):C.GC_3403})

V_334 = Vertex(name = 'V_334',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1472,(0,5):C.GC_3912,(0,3):C.GC_3911,(0,4):C.GC_3911,(0,1):C.GC_3591,(0,0):C.GC_3430})

V_335 = Vertex(name = 'V_335',
               particles = [ P.ve__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1457,(0,5):C.GC_3700,(0,3):C.GC_3699,(0,4):C.GC_3699,(0,1):C.GC_3485,(0,0):C.GC_3377})

V_336 = Vertex(name = 'V_336',
               particles = [ P.vm__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1466,(0,5):C.GC_3808,(0,3):C.GC_3807,(0,4):C.GC_3807,(0,1):C.GC_3539,(0,0):C.GC_3404})

V_337 = Vertex(name = 'V_337',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,2):C.GC_1475,(0,5):C.GC_3916,(0,3):C.GC_3915,(0,4):C.GC_3915,(0,1):C.GC_3593,(0,0):C.GC_3431})

V_338 = Vertex(name = 'V_338',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_119,(0,1):C.GC_1719,(0,2):C.GC_657,(0,3):C.GC_469,(0,5):C.GC_819,(0,0):C.GC_3351})

V_339 = Vertex(name = 'V_339',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_137,(0,1):C.GC_1720,(0,2):C.GC_666,(0,3):C.GC_478,(0,5):C.GC_828,(0,0):C.GC_3378})

V_340 = Vertex(name = 'V_340',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_155,(0,1):C.GC_1721,(0,2):C.GC_675,(0,3):C.GC_487,(0,5):C.GC_837,(0,0):C.GC_3405})

V_341 = Vertex(name = 'V_341',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_173,(0,1):C.GC_1722,(0,2):C.GC_684,(0,3):C.GC_496,(0,5):C.GC_846,(0,0):C.GC_3360})

V_342 = Vertex(name = 'V_342',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_191,(0,1):C.GC_1723,(0,2):C.GC_693,(0,3):C.GC_505,(0,5):C.GC_855,(0,0):C.GC_3387})

V_343 = Vertex(name = 'V_343',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_209,(0,1):C.GC_1724,(0,2):C.GC_702,(0,3):C.GC_514,(0,5):C.GC_864,(0,0):C.GC_3414})

V_344 = Vertex(name = 'V_344',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_227,(0,1):C.GC_1725,(0,2):C.GC_711,(0,3):C.GC_523,(0,5):C.GC_873,(0,0):C.GC_3369})

V_345 = Vertex(name = 'V_345',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_245,(0,1):C.GC_1726,(0,2):C.GC_720,(0,3):C.GC_532,(0,5):C.GC_882,(0,0):C.GC_3396})

V_346 = Vertex(name = 'V_346',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_263,(0,1):C.GC_1727,(0,2):C.GC_729,(0,3):C.GC_541,(0,5):C.GC_891,(0,0):C.GC_3423})

V_347 = Vertex(name = 'V_347',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_121,(0,1):C.GC_1728,(0,2):C.GC_658,(0,3):C.GC_470,(0,5):C.GC_820,(0,0):C.GC_3354})

V_348 = Vertex(name = 'V_348',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_139,(0,1):C.GC_1729,(0,2):C.GC_667,(0,3):C.GC_479,(0,5):C.GC_829,(0,0):C.GC_3381})

V_349 = Vertex(name = 'V_349',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_157,(0,1):C.GC_1730,(0,2):C.GC_676,(0,3):C.GC_488,(0,5):C.GC_838,(0,0):C.GC_3408})

V_350 = Vertex(name = 'V_350',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_175,(0,1):C.GC_1731,(0,2):C.GC_685,(0,3):C.GC_497,(0,5):C.GC_847,(0,0):C.GC_3363})

V_351 = Vertex(name = 'V_351',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_193,(0,1):C.GC_1732,(0,2):C.GC_694,(0,3):C.GC_506,(0,5):C.GC_856,(0,0):C.GC_3390})

V_352 = Vertex(name = 'V_352',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_211,(0,1):C.GC_1733,(0,2):C.GC_703,(0,3):C.GC_515,(0,5):C.GC_865,(0,0):C.GC_3417})

V_353 = Vertex(name = 'V_353',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_229,(0,1):C.GC_1734,(0,2):C.GC_712,(0,3):C.GC_524,(0,5):C.GC_874,(0,0):C.GC_3372})

V_354 = Vertex(name = 'V_354',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_247,(0,1):C.GC_1735,(0,2):C.GC_721,(0,3):C.GC_533,(0,5):C.GC_883,(0,0):C.GC_3399})

V_355 = Vertex(name = 'V_355',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_265,(0,1):C.GC_1736,(0,2):C.GC_730,(0,3):C.GC_542,(0,5):C.GC_892,(0,0):C.GC_3426})

V_356 = Vertex(name = 'V_356',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_123,(0,1):C.GC_1737,(0,2):C.GC_659,(0,3):C.GC_471,(0,5):C.GC_821,(0,0):C.GC_3357})

V_357 = Vertex(name = 'V_357',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_141,(0,1):C.GC_1738,(0,2):C.GC_668,(0,3):C.GC_480,(0,5):C.GC_830,(0,0):C.GC_3384})

V_358 = Vertex(name = 'V_358',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_159,(0,1):C.GC_1739,(0,2):C.GC_677,(0,3):C.GC_489,(0,5):C.GC_839,(0,0):C.GC_3411})

V_359 = Vertex(name = 'V_359',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_177,(0,1):C.GC_1740,(0,2):C.GC_686,(0,3):C.GC_498,(0,5):C.GC_848,(0,0):C.GC_3366})

V_360 = Vertex(name = 'V_360',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_195,(0,1):C.GC_1741,(0,2):C.GC_695,(0,3):C.GC_507,(0,5):C.GC_857,(0,0):C.GC_3393})

V_361 = Vertex(name = 'V_361',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_213,(0,1):C.GC_1742,(0,2):C.GC_704,(0,3):C.GC_516,(0,5):C.GC_866,(0,0):C.GC_3420})

V_362 = Vertex(name = 'V_362',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_231,(0,1):C.GC_1743,(0,2):C.GC_713,(0,3):C.GC_525,(0,5):C.GC_875,(0,0):C.GC_3375})

V_363 = Vertex(name = 'V_363',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_249,(0,1):C.GC_1744,(0,2):C.GC_722,(0,3):C.GC_534,(0,5):C.GC_884,(0,0):C.GC_3402})

V_364 = Vertex(name = 'V_364',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_267,(0,1):C.GC_1745,(0,2):C.GC_731,(0,3):C.GC_543,(0,5):C.GC_893,(0,0):C.GC_3429})

V_365 = Vertex(name = 'V_365',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_125,(0,1):C.GC_1746,(0,2):C.GC_660,(0,3):C.GC_472,(0,5):C.GC_822,(0,0):C.GC_3352})

V_366 = Vertex(name = 'V_366',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_143,(0,1):C.GC_1747,(0,2):C.GC_669,(0,3):C.GC_481,(0,5):C.GC_831,(0,0):C.GC_3379})

V_367 = Vertex(name = 'V_367',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_161,(0,1):C.GC_1748,(0,2):C.GC_678,(0,3):C.GC_490,(0,5):C.GC_840,(0,0):C.GC_3406})

V_368 = Vertex(name = 'V_368',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_179,(0,1):C.GC_1749,(0,2):C.GC_687,(0,3):C.GC_499,(0,5):C.GC_849,(0,0):C.GC_3361})

V_369 = Vertex(name = 'V_369',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_197,(0,1):C.GC_1750,(0,2):C.GC_696,(0,3):C.GC_508,(0,5):C.GC_858,(0,0):C.GC_3388})

V_370 = Vertex(name = 'V_370',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_215,(0,1):C.GC_1751,(0,2):C.GC_705,(0,3):C.GC_517,(0,5):C.GC_867,(0,0):C.GC_3415})

V_371 = Vertex(name = 'V_371',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_233,(0,1):C.GC_1752,(0,2):C.GC_714,(0,3):C.GC_526,(0,5):C.GC_876,(0,0):C.GC_3370})

V_372 = Vertex(name = 'V_372',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_251,(0,1):C.GC_1753,(0,2):C.GC_723,(0,3):C.GC_535,(0,5):C.GC_885,(0,0):C.GC_3397})

V_373 = Vertex(name = 'V_373',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_269,(0,1):C.GC_1754,(0,2):C.GC_732,(0,3):C.GC_544,(0,5):C.GC_894,(0,0):C.GC_3424})

V_374 = Vertex(name = 'V_374',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_127,(0,1):C.GC_1755,(0,2):C.GC_661,(0,3):C.GC_473,(0,5):C.GC_823,(0,0):C.GC_3355})

V_375 = Vertex(name = 'V_375',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_145,(0,1):C.GC_1756,(0,2):C.GC_670,(0,3):C.GC_482,(0,5):C.GC_832,(0,0):C.GC_3382})

V_376 = Vertex(name = 'V_376',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_163,(0,1):C.GC_1757,(0,2):C.GC_679,(0,3):C.GC_491,(0,5):C.GC_841,(0,0):C.GC_3409})

V_377 = Vertex(name = 'V_377',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_181,(0,1):C.GC_1758,(0,2):C.GC_688,(0,3):C.GC_500,(0,5):C.GC_850,(0,0):C.GC_3364})

V_378 = Vertex(name = 'V_378',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_199,(0,1):C.GC_1759,(0,2):C.GC_697,(0,3):C.GC_509,(0,5):C.GC_859,(0,0):C.GC_3391})

V_379 = Vertex(name = 'V_379',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_217,(0,1):C.GC_1760,(0,2):C.GC_706,(0,3):C.GC_518,(0,5):C.GC_868,(0,0):C.GC_3418})

V_380 = Vertex(name = 'V_380',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_235,(0,1):C.GC_1761,(0,2):C.GC_715,(0,3):C.GC_527,(0,5):C.GC_877,(0,0):C.GC_3373})

V_381 = Vertex(name = 'V_381',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_253,(0,1):C.GC_1762,(0,2):C.GC_724,(0,3):C.GC_536,(0,5):C.GC_886,(0,0):C.GC_3400})

V_382 = Vertex(name = 'V_382',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_271,(0,1):C.GC_1763,(0,2):C.GC_733,(0,3):C.GC_545,(0,5):C.GC_895,(0,0):C.GC_3427})

V_383 = Vertex(name = 'V_383',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_129,(0,1):C.GC_1764,(0,2):C.GC_662,(0,3):C.GC_474,(0,5):C.GC_824,(0,0):C.GC_3358})

V_384 = Vertex(name = 'V_384',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_147,(0,1):C.GC_1765,(0,2):C.GC_671,(0,3):C.GC_483,(0,5):C.GC_833,(0,0):C.GC_3385})

V_385 = Vertex(name = 'V_385',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_165,(0,1):C.GC_1766,(0,2):C.GC_680,(0,3):C.GC_492,(0,5):C.GC_842,(0,0):C.GC_3412})

V_386 = Vertex(name = 'V_386',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_183,(0,1):C.GC_1767,(0,2):C.GC_689,(0,3):C.GC_501,(0,5):C.GC_851,(0,0):C.GC_3367})

V_387 = Vertex(name = 'V_387',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_201,(0,1):C.GC_1768,(0,2):C.GC_698,(0,3):C.GC_510,(0,5):C.GC_860,(0,0):C.GC_3394})

V_388 = Vertex(name = 'V_388',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_219,(0,1):C.GC_1769,(0,2):C.GC_707,(0,3):C.GC_519,(0,5):C.GC_869,(0,0):C.GC_3421})

V_389 = Vertex(name = 'V_389',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_237,(0,1):C.GC_1770,(0,2):C.GC_716,(0,3):C.GC_528,(0,5):C.GC_878,(0,0):C.GC_3376})

V_390 = Vertex(name = 'V_390',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_255,(0,1):C.GC_1771,(0,2):C.GC_725,(0,3):C.GC_537,(0,5):C.GC_887,(0,0):C.GC_3403})

V_391 = Vertex(name = 'V_391',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_273,(0,1):C.GC_1772,(0,2):C.GC_734,(0,3):C.GC_546,(0,5):C.GC_896,(0,0):C.GC_3430})

V_392 = Vertex(name = 'V_392',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_131,(0,1):C.GC_1773,(0,2):C.GC_663,(0,3):C.GC_475,(0,5):C.GC_825,(0,0):C.GC_3353})

V_393 = Vertex(name = 'V_393',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_149,(0,1):C.GC_1774,(0,2):C.GC_672,(0,3):C.GC_484,(0,5):C.GC_834,(0,0):C.GC_3380})

V_394 = Vertex(name = 'V_394',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_167,(0,1):C.GC_1775,(0,2):C.GC_681,(0,3):C.GC_493,(0,5):C.GC_843,(0,0):C.GC_3407})

V_395 = Vertex(name = 'V_395',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_185,(0,1):C.GC_1776,(0,2):C.GC_690,(0,3):C.GC_502,(0,5):C.GC_852,(0,0):C.GC_3362})

V_396 = Vertex(name = 'V_396',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_203,(0,1):C.GC_1777,(0,2):C.GC_699,(0,3):C.GC_511,(0,5):C.GC_861,(0,0):C.GC_3389})

V_397 = Vertex(name = 'V_397',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_221,(0,1):C.GC_1778,(0,2):C.GC_708,(0,3):C.GC_520,(0,5):C.GC_870,(0,0):C.GC_3416})

V_398 = Vertex(name = 'V_398',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_239,(0,1):C.GC_1779,(0,2):C.GC_717,(0,3):C.GC_529,(0,5):C.GC_879,(0,0):C.GC_3371})

V_399 = Vertex(name = 'V_399',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_257,(0,1):C.GC_1780,(0,2):C.GC_726,(0,3):C.GC_538,(0,5):C.GC_888,(0,0):C.GC_3398})

V_400 = Vertex(name = 'V_400',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_275,(0,1):C.GC_1781,(0,2):C.GC_735,(0,3):C.GC_547,(0,5):C.GC_897,(0,0):C.GC_3425})

V_401 = Vertex(name = 'V_401',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_133,(0,1):C.GC_1782,(0,2):C.GC_664,(0,3):C.GC_476,(0,5):C.GC_826,(0,0):C.GC_3356})

V_402 = Vertex(name = 'V_402',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_151,(0,1):C.GC_1783,(0,2):C.GC_673,(0,3):C.GC_485,(0,5):C.GC_835,(0,0):C.GC_3383})

V_403 = Vertex(name = 'V_403',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_169,(0,1):C.GC_1784,(0,2):C.GC_682,(0,3):C.GC_494,(0,5):C.GC_844,(0,0):C.GC_3410})

V_404 = Vertex(name = 'V_404',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_187,(0,1):C.GC_1785,(0,2):C.GC_691,(0,3):C.GC_503,(0,5):C.GC_853,(0,0):C.GC_3365})

V_405 = Vertex(name = 'V_405',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_205,(0,1):C.GC_1786,(0,2):C.GC_700,(0,3):C.GC_512,(0,5):C.GC_862,(0,0):C.GC_3392})

V_406 = Vertex(name = 'V_406',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_223,(0,1):C.GC_1787,(0,2):C.GC_709,(0,3):C.GC_521,(0,5):C.GC_871,(0,0):C.GC_3419})

V_407 = Vertex(name = 'V_407',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_241,(0,1):C.GC_1788,(0,2):C.GC_718,(0,3):C.GC_530,(0,5):C.GC_880,(0,0):C.GC_3374})

V_408 = Vertex(name = 'V_408',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_259,(0,1):C.GC_1789,(0,2):C.GC_727,(0,3):C.GC_539,(0,5):C.GC_889,(0,0):C.GC_3401})

V_409 = Vertex(name = 'V_409',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_277,(0,1):C.GC_1790,(0,2):C.GC_736,(0,3):C.GC_548,(0,5):C.GC_898,(0,0):C.GC_3428})

V_410 = Vertex(name = 'V_410',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_135,(0,1):C.GC_1791,(0,2):C.GC_665,(0,3):C.GC_477,(0,5):C.GC_827,(0,0):C.GC_3359})

V_411 = Vertex(name = 'V_411',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_153,(0,1):C.GC_1792,(0,2):C.GC_674,(0,3):C.GC_486,(0,5):C.GC_836,(0,0):C.GC_3386})

V_412 = Vertex(name = 'V_412',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_171,(0,1):C.GC_1793,(0,2):C.GC_683,(0,3):C.GC_495,(0,5):C.GC_845,(0,0):C.GC_3413})

V_413 = Vertex(name = 'V_413',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_189,(0,1):C.GC_1794,(0,2):C.GC_692,(0,3):C.GC_504,(0,5):C.GC_854,(0,0):C.GC_3368})

V_414 = Vertex(name = 'V_414',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_207,(0,1):C.GC_1795,(0,2):C.GC_701,(0,3):C.GC_513,(0,5):C.GC_863,(0,0):C.GC_3395})

V_415 = Vertex(name = 'V_415',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_225,(0,1):C.GC_1796,(0,2):C.GC_710,(0,3):C.GC_522,(0,5):C.GC_872,(0,0):C.GC_3422})

V_416 = Vertex(name = 'V_416',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_243,(0,1):C.GC_1797,(0,2):C.GC_719,(0,3):C.GC_531,(0,5):C.GC_881,(0,0):C.GC_3377})

V_417 = Vertex(name = 'V_417',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_261,(0,1):C.GC_1798,(0,2):C.GC_728,(0,3):C.GC_540,(0,5):C.GC_890,(0,0):C.GC_3404})

V_418 = Vertex(name = 'V_418',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_279,(0,1):C.GC_1799,(0,2):C.GC_737,(0,3):C.GC_549,(0,5):C.GC_899,(0,0):C.GC_3431})

V_419 = Vertex(name = 'V_419',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1395,(0,4):C.GC_1064,(0,2):C.GC_1063,(0,3):C.GC_1063,(0,0):C.GC_819,(0,1):C.GC_901})

V_420 = Vertex(name = 'V_420',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1396,(0,4):C.GC_1068,(0,2):C.GC_1067,(0,3):C.GC_1067,(0,0):C.GC_820,(0,1):C.GC_903})

V_421 = Vertex(name = 'V_421',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1397,(0,4):C.GC_1072,(0,2):C.GC_1071,(0,3):C.GC_1071,(0,0):C.GC_821,(0,1):C.GC_905})

V_422 = Vertex(name = 'V_422',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1422,(0,4):C.GC_1172,(0,2):C.GC_1171,(0,3):C.GC_1171,(0,0):C.GC_846,(0,1):C.GC_955})

V_423 = Vertex(name = 'V_423',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1423,(0,4):C.GC_1176,(0,2):C.GC_1175,(0,3):C.GC_1175,(0,0):C.GC_847,(0,1):C.GC_957})

V_424 = Vertex(name = 'V_424',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1424,(0,4):C.GC_1180,(0,2):C.GC_1179,(0,3):C.GC_1179,(0,0):C.GC_848,(0,1):C.GC_959})

V_425 = Vertex(name = 'V_425',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1449,(0,4):C.GC_1280,(0,2):C.GC_1279,(0,3):C.GC_1279,(0,0):C.GC_873,(0,1):C.GC_1009})

V_426 = Vertex(name = 'V_426',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1450,(0,4):C.GC_1284,(0,2):C.GC_1283,(0,3):C.GC_1283,(0,0):C.GC_874,(0,1):C.GC_1011})

V_427 = Vertex(name = 'V_427',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1451,(0,4):C.GC_1288,(0,2):C.GC_1287,(0,3):C.GC_1287,(0,0):C.GC_875,(0,1):C.GC_1013})

V_428 = Vertex(name = 'V_428',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1404,(0,4):C.GC_1100,(0,2):C.GC_1099,(0,3):C.GC_1099,(0,0):C.GC_828,(0,1):C.GC_919})

V_429 = Vertex(name = 'V_429',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1405,(0,4):C.GC_1104,(0,2):C.GC_1103,(0,3):C.GC_1103,(0,0):C.GC_829,(0,1):C.GC_921})

V_430 = Vertex(name = 'V_430',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1406,(0,4):C.GC_1108,(0,2):C.GC_1107,(0,3):C.GC_1107,(0,0):C.GC_830,(0,1):C.GC_923})

V_431 = Vertex(name = 'V_431',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1431,(0,4):C.GC_1208,(0,2):C.GC_1207,(0,3):C.GC_1207,(0,0):C.GC_855,(0,1):C.GC_973})

V_432 = Vertex(name = 'V_432',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1432,(0,4):C.GC_1212,(0,2):C.GC_1211,(0,3):C.GC_1211,(0,0):C.GC_856,(0,1):C.GC_975})

V_433 = Vertex(name = 'V_433',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1433,(0,4):C.GC_1216,(0,2):C.GC_1215,(0,3):C.GC_1215,(0,0):C.GC_857,(0,1):C.GC_977})

V_434 = Vertex(name = 'V_434',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1458,(0,4):C.GC_1316,(0,2):C.GC_1315,(0,3):C.GC_1315,(0,0):C.GC_882,(0,1):C.GC_1027})

V_435 = Vertex(name = 'V_435',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1459,(0,4):C.GC_1320,(0,2):C.GC_1319,(0,3):C.GC_1319,(0,0):C.GC_883,(0,1):C.GC_1029})

V_436 = Vertex(name = 'V_436',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1460,(0,4):C.GC_1324,(0,2):C.GC_1323,(0,3):C.GC_1323,(0,0):C.GC_884,(0,1):C.GC_1031})

V_437 = Vertex(name = 'V_437',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1413,(0,4):C.GC_1136,(0,2):C.GC_1135,(0,3):C.GC_1135,(0,0):C.GC_837,(0,1):C.GC_937})

V_438 = Vertex(name = 'V_438',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1414,(0,4):C.GC_1140,(0,2):C.GC_1139,(0,3):C.GC_1139,(0,0):C.GC_838,(0,1):C.GC_939})

V_439 = Vertex(name = 'V_439',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1415,(0,4):C.GC_1144,(0,2):C.GC_1143,(0,3):C.GC_1143,(0,0):C.GC_839,(0,1):C.GC_941})

V_440 = Vertex(name = 'V_440',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1440,(0,4):C.GC_1244,(0,2):C.GC_1243,(0,3):C.GC_1243,(0,0):C.GC_864,(0,1):C.GC_991})

V_441 = Vertex(name = 'V_441',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1441,(0,4):C.GC_1248,(0,2):C.GC_1247,(0,3):C.GC_1247,(0,0):C.GC_865,(0,1):C.GC_993})

V_442 = Vertex(name = 'V_442',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1442,(0,4):C.GC_1252,(0,2):C.GC_1251,(0,3):C.GC_1251,(0,0):C.GC_866,(0,1):C.GC_995})

V_443 = Vertex(name = 'V_443',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1467,(0,4):C.GC_1352,(0,2):C.GC_1351,(0,3):C.GC_1351,(0,0):C.GC_891,(0,1):C.GC_1045})

V_444 = Vertex(name = 'V_444',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1468,(0,4):C.GC_1356,(0,2):C.GC_1355,(0,3):C.GC_1355,(0,0):C.GC_892,(0,1):C.GC_1047})

V_445 = Vertex(name = 'V_445',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1469,(0,4):C.GC_1360,(0,2):C.GC_1359,(0,3):C.GC_1359,(0,0):C.GC_893,(0,1):C.GC_1049})

V_446 = Vertex(name = 'V_446',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1398,(0,4):C.GC_1076,(0,2):C.GC_1075,(0,3):C.GC_1075,(0,0):C.GC_822,(0,1):C.GC_907})

V_447 = Vertex(name = 'V_447',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1399,(0,4):C.GC_1080,(0,2):C.GC_1079,(0,3):C.GC_1079,(0,0):C.GC_823,(0,1):C.GC_909})

V_448 = Vertex(name = 'V_448',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1400,(0,4):C.GC_1084,(0,2):C.GC_1083,(0,3):C.GC_1083,(0,0):C.GC_824,(0,1):C.GC_911})

V_449 = Vertex(name = 'V_449',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1425,(0,4):C.GC_1184,(0,2):C.GC_1183,(0,3):C.GC_1183,(0,0):C.GC_849,(0,1):C.GC_961})

V_450 = Vertex(name = 'V_450',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1426,(0,4):C.GC_1188,(0,2):C.GC_1187,(0,3):C.GC_1187,(0,0):C.GC_850,(0,1):C.GC_963})

V_451 = Vertex(name = 'V_451',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1427,(0,4):C.GC_1192,(0,2):C.GC_1191,(0,3):C.GC_1191,(0,0):C.GC_851,(0,1):C.GC_965})

V_452 = Vertex(name = 'V_452',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1452,(0,4):C.GC_1292,(0,2):C.GC_1291,(0,3):C.GC_1291,(0,0):C.GC_876,(0,1):C.GC_1015})

V_453 = Vertex(name = 'V_453',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1453,(0,4):C.GC_1296,(0,2):C.GC_1295,(0,3):C.GC_1295,(0,0):C.GC_877,(0,1):C.GC_1017})

V_454 = Vertex(name = 'V_454',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1454,(0,4):C.GC_1300,(0,2):C.GC_1299,(0,3):C.GC_1299,(0,0):C.GC_878,(0,1):C.GC_1019})

V_455 = Vertex(name = 'V_455',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1407,(0,4):C.GC_1112,(0,2):C.GC_1111,(0,3):C.GC_1111,(0,0):C.GC_831,(0,1):C.GC_925})

V_456 = Vertex(name = 'V_456',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1408,(0,4):C.GC_1116,(0,2):C.GC_1115,(0,3):C.GC_1115,(0,0):C.GC_832,(0,1):C.GC_927})

V_457 = Vertex(name = 'V_457',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1409,(0,4):C.GC_1120,(0,2):C.GC_1119,(0,3):C.GC_1119,(0,0):C.GC_833,(0,1):C.GC_929})

V_458 = Vertex(name = 'V_458',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1434,(0,4):C.GC_1220,(0,2):C.GC_1219,(0,3):C.GC_1219,(0,0):C.GC_858,(0,1):C.GC_979})

V_459 = Vertex(name = 'V_459',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1435,(0,4):C.GC_1224,(0,2):C.GC_1223,(0,3):C.GC_1223,(0,0):C.GC_859,(0,1):C.GC_981})

V_460 = Vertex(name = 'V_460',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1436,(0,4):C.GC_1228,(0,2):C.GC_1227,(0,3):C.GC_1227,(0,0):C.GC_860,(0,1):C.GC_983})

V_461 = Vertex(name = 'V_461',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1461,(0,4):C.GC_1328,(0,2):C.GC_1327,(0,3):C.GC_1327,(0,0):C.GC_885,(0,1):C.GC_1033})

V_462 = Vertex(name = 'V_462',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1462,(0,4):C.GC_1332,(0,2):C.GC_1331,(0,3):C.GC_1331,(0,0):C.GC_886,(0,1):C.GC_1035})

V_463 = Vertex(name = 'V_463',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1463,(0,4):C.GC_1336,(0,2):C.GC_1335,(0,3):C.GC_1335,(0,0):C.GC_887,(0,1):C.GC_1037})

V_464 = Vertex(name = 'V_464',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1416,(0,4):C.GC_1148,(0,2):C.GC_1147,(0,3):C.GC_1147,(0,0):C.GC_840,(0,1):C.GC_943})

V_465 = Vertex(name = 'V_465',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1417,(0,4):C.GC_1152,(0,2):C.GC_1151,(0,3):C.GC_1151,(0,0):C.GC_841,(0,1):C.GC_945})

V_466 = Vertex(name = 'V_466',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1418,(0,4):C.GC_1156,(0,2):C.GC_1155,(0,3):C.GC_1155,(0,0):C.GC_842,(0,1):C.GC_947})

V_467 = Vertex(name = 'V_467',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1443,(0,4):C.GC_1256,(0,2):C.GC_1255,(0,3):C.GC_1255,(0,0):C.GC_867,(0,1):C.GC_997})

V_468 = Vertex(name = 'V_468',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1444,(0,4):C.GC_1260,(0,2):C.GC_1259,(0,3):C.GC_1259,(0,0):C.GC_868,(0,1):C.GC_999})

V_469 = Vertex(name = 'V_469',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1445,(0,4):C.GC_1264,(0,2):C.GC_1263,(0,3):C.GC_1263,(0,0):C.GC_869,(0,1):C.GC_1001})

V_470 = Vertex(name = 'V_470',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1470,(0,4):C.GC_1364,(0,2):C.GC_1363,(0,3):C.GC_1363,(0,0):C.GC_894,(0,1):C.GC_1051})

V_471 = Vertex(name = 'V_471',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1471,(0,4):C.GC_1368,(0,2):C.GC_1367,(0,3):C.GC_1367,(0,0):C.GC_895,(0,1):C.GC_1053})

V_472 = Vertex(name = 'V_472',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1472,(0,4):C.GC_1372,(0,2):C.GC_1371,(0,3):C.GC_1371,(0,0):C.GC_896,(0,1):C.GC_1055})

V_473 = Vertex(name = 'V_473',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1401,(0,4):C.GC_1088,(0,2):C.GC_1087,(0,3):C.GC_1087,(0,0):C.GC_825,(0,1):C.GC_913})

V_474 = Vertex(name = 'V_474',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1402,(0,4):C.GC_1092,(0,2):C.GC_1091,(0,3):C.GC_1091,(0,0):C.GC_826,(0,1):C.GC_915})

V_475 = Vertex(name = 'V_475',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1403,(0,4):C.GC_1096,(0,2):C.GC_1095,(0,3):C.GC_1095,(0,0):C.GC_827,(0,1):C.GC_917})

V_476 = Vertex(name = 'V_476',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1428,(0,4):C.GC_1196,(0,2):C.GC_1195,(0,3):C.GC_1195,(0,0):C.GC_852,(0,1):C.GC_967})

V_477 = Vertex(name = 'V_477',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1429,(0,4):C.GC_1200,(0,2):C.GC_1199,(0,3):C.GC_1199,(0,0):C.GC_853,(0,1):C.GC_969})

V_478 = Vertex(name = 'V_478',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1430,(0,4):C.GC_1204,(0,2):C.GC_1203,(0,3):C.GC_1203,(0,0):C.GC_854,(0,1):C.GC_971})

V_479 = Vertex(name = 'V_479',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1455,(0,4):C.GC_1304,(0,2):C.GC_1303,(0,3):C.GC_1303,(0,0):C.GC_879,(0,1):C.GC_1021})

V_480 = Vertex(name = 'V_480',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1456,(0,4):C.GC_1308,(0,2):C.GC_1307,(0,3):C.GC_1307,(0,0):C.GC_880,(0,1):C.GC_1023})

V_481 = Vertex(name = 'V_481',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1457,(0,4):C.GC_1312,(0,2):C.GC_1311,(0,3):C.GC_1311,(0,0):C.GC_881,(0,1):C.GC_1025})

V_482 = Vertex(name = 'V_482',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1410,(0,4):C.GC_1124,(0,2):C.GC_1123,(0,3):C.GC_1123,(0,0):C.GC_834,(0,1):C.GC_931})

V_483 = Vertex(name = 'V_483',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1411,(0,4):C.GC_1128,(0,2):C.GC_1127,(0,3):C.GC_1127,(0,0):C.GC_835,(0,1):C.GC_933})

V_484 = Vertex(name = 'V_484',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1412,(0,4):C.GC_1132,(0,2):C.GC_1131,(0,3):C.GC_1131,(0,0):C.GC_836,(0,1):C.GC_935})

V_485 = Vertex(name = 'V_485',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1437,(0,4):C.GC_1232,(0,2):C.GC_1231,(0,3):C.GC_1231,(0,0):C.GC_861,(0,1):C.GC_985})

V_486 = Vertex(name = 'V_486',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1438,(0,4):C.GC_1236,(0,2):C.GC_1235,(0,3):C.GC_1235,(0,0):C.GC_862,(0,1):C.GC_987})

V_487 = Vertex(name = 'V_487',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1439,(0,4):C.GC_1240,(0,2):C.GC_1239,(0,3):C.GC_1239,(0,0):C.GC_863,(0,1):C.GC_989})

V_488 = Vertex(name = 'V_488',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1464,(0,4):C.GC_1340,(0,2):C.GC_1339,(0,3):C.GC_1339,(0,0):C.GC_888,(0,1):C.GC_1039})

V_489 = Vertex(name = 'V_489',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1465,(0,4):C.GC_1344,(0,2):C.GC_1343,(0,3):C.GC_1343,(0,0):C.GC_889,(0,1):C.GC_1041})

V_490 = Vertex(name = 'V_490',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1466,(0,4):C.GC_1348,(0,2):C.GC_1347,(0,3):C.GC_1347,(0,0):C.GC_890,(0,1):C.GC_1043})

V_491 = Vertex(name = 'V_491',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1419,(0,4):C.GC_1160,(0,2):C.GC_1159,(0,3):C.GC_1159,(0,0):C.GC_843,(0,1):C.GC_949})

V_492 = Vertex(name = 'V_492',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1420,(0,4):C.GC_1164,(0,2):C.GC_1163,(0,3):C.GC_1163,(0,0):C.GC_844,(0,1):C.GC_951})

V_493 = Vertex(name = 'V_493',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1421,(0,4):C.GC_1168,(0,2):C.GC_1167,(0,3):C.GC_1167,(0,0):C.GC_845,(0,1):C.GC_953})

V_494 = Vertex(name = 'V_494',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1446,(0,4):C.GC_1268,(0,2):C.GC_1267,(0,3):C.GC_1267,(0,0):C.GC_870,(0,1):C.GC_1003})

V_495 = Vertex(name = 'V_495',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1447,(0,4):C.GC_1272,(0,2):C.GC_1271,(0,3):C.GC_1271,(0,0):C.GC_871,(0,1):C.GC_1005})

V_496 = Vertex(name = 'V_496',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1448,(0,4):C.GC_1276,(0,2):C.GC_1275,(0,3):C.GC_1275,(0,0):C.GC_872,(0,1):C.GC_1007})

V_497 = Vertex(name = 'V_497',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1473,(0,4):C.GC_1376,(0,2):C.GC_1375,(0,3):C.GC_1375,(0,0):C.GC_897,(0,1):C.GC_1057})

V_498 = Vertex(name = 'V_498',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1474,(0,4):C.GC_1380,(0,2):C.GC_1379,(0,3):C.GC_1379,(0,0):C.GC_898,(0,1):C.GC_1059})

V_499 = Vertex(name = 'V_499',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
               couplings = {(0,5):C.GC_1475,(0,4):C.GC_1384,(0,2):C.GC_1383,(0,3):C.GC_1383,(0,0):C.GC_899,(0,1):C.GC_1061})

V_500 = Vertex(name = 'V_500',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS3, L.VVVS4, L.VVVS6 ],
               couplings = {(0,1):C.GC_2683,(0,0):C.GC_2773,(0,3):C.GC_2680,(0,2):C.GC_2772})

V_501 = Vertex(name = 'V_501',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
               couplings = {(0,1):C.GC_2517,(0,0):C.GC_2516,(0,2):C.GC_5})

V_502 = Vertex(name = 'V_502',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_3002})

V_503 = Vertex(name = 'V_503',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11, L.VVVV14, L.VVVV7 ],
               couplings = {(0,2):C.GC_2487,(0,1):C.GC_2486,(0,0):C.GC_3003})

V_504 = Vertex(name = 'V_504',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_2507})

V_505 = Vertex(name = 'V_505',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS2, L.VVVS3, L.VVVS5, L.VVVS6 ],
               couplings = {(0,1):C.GC_2774,(0,0):C.GC_2682,(0,3):C.GC_2771,(0,2):C.GC_2681})

V_506 = Vertex(name = 'V_506',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
               couplings = {(0,1):C.GC_2510,(0,0):C.GC_2508,(0,2):C.GC_2491})

V_507 = Vertex(name = 'V_507',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_2493})

V_508 = Vertex(name = 'V_508',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
               couplings = {(0,1):C.GC_2511,(0,0):C.GC_2509,(0,2):C.GC_2492})

V_509 = Vertex(name = 'V_509',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_2988})

V_510 = Vertex(name = 'V_510',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,3):C.GC_1,(0,2):C.GC_3009,(0,0):C.GC_2990,(0,1):C.GC_3089,(0,4):C.GC_2850})

V_511 = Vertex(name = 'V_511',
               particles = [ P.s__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3116,(0,1):C.GC_2851})

V_512 = Vertex(name = 'V_512',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3143,(0,1):C.GC_2852})

V_513 = Vertex(name = 'V_513',
               particles = [ P.d__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3098,(0,1):C.GC_2853})

V_514 = Vertex(name = 'V_514',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,3):C.GC_1,(0,2):C.GC_3009,(0,0):C.GC_2990,(0,1):C.GC_3125,(0,4):C.GC_2854})

V_515 = Vertex(name = 'V_515',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3152,(0,1):C.GC_2855})

V_516 = Vertex(name = 'V_516',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3107,(0,1):C.GC_2856})

V_517 = Vertex(name = 'V_517',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3134,(0,1):C.GC_2857})

V_518 = Vertex(name = 'V_518',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,3):C.GC_1,(0,2):C.GC_3009,(0,0):C.GC_2990,(0,1):C.GC_3161,(0,4):C.GC_2858})

V_519 = Vertex(name = 'V_519',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,2):C.GC_4,(0,3):C.GC_3010,(0,0):C.GC_2990,(0,1):C.GC_3188,(0,4):C.GC_2868})

V_520 = Vertex(name = 'V_520',
               particles = [ P.mu__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3215,(0,1):C.GC_2869})

V_521 = Vertex(name = 'V_521',
               particles = [ P.ta__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3242,(0,1):C.GC_2870})

V_522 = Vertex(name = 'V_522',
               particles = [ P.e__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3197,(0,1):C.GC_2871})

V_523 = Vertex(name = 'V_523',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,2):C.GC_4,(0,3):C.GC_3010,(0,0):C.GC_2990,(0,1):C.GC_3224,(0,4):C.GC_2872})

V_524 = Vertex(name = 'V_524',
               particles = [ P.ta__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3251,(0,1):C.GC_2873})

V_525 = Vertex(name = 'V_525',
               particles = [ P.e__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3206,(0,1):C.GC_2874})

V_526 = Vertex(name = 'V_526',
               particles = [ P.mu__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3233,(0,1):C.GC_2875})

V_527 = Vertex(name = 'V_527',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,2):C.GC_4,(0,3):C.GC_3010,(0,0):C.GC_2990,(0,1):C.GC_3260,(0,4):C.GC_2876})

V_528 = Vertex(name = 'V_528',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_2,(0,3):C.GC_3009,(0,0):C.GC_2989,(0,1):C.GC_4295,(0,4):C.GC_2886})

V_529 = Vertex(name = 'V_529',
               particles = [ P.c__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4322,(0,1):C.GC_2887})

V_530 = Vertex(name = 'V_530',
               particles = [ P.t__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4349,(0,1):C.GC_2888})

V_531 = Vertex(name = 'V_531',
               particles = [ P.u__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4304,(0,1):C.GC_2889})

V_532 = Vertex(name = 'V_532',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_2,(0,3):C.GC_3009,(0,0):C.GC_2989,(0,1):C.GC_4331,(0,4):C.GC_2890})

V_533 = Vertex(name = 'V_533',
               particles = [ P.t__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4358,(0,1):C.GC_2891})

V_534 = Vertex(name = 'V_534',
               particles = [ P.u__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4313,(0,1):C.GC_2892})

V_535 = Vertex(name = 'V_535',
               particles = [ P.c__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4340,(0,1):C.GC_2893})

V_536 = Vertex(name = 'V_536',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_2,(0,3):C.GC_3009,(0,0):C.GC_2989,(0,1):C.GC_4367,(0,4):C.GC_2894})

V_537 = Vertex(name = 'V_537',
               particles = [ P.ve__tilde__, P.ve, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3011})

V_538 = Vertex(name = 'V_538',
               particles = [ P.vm__tilde__, P.vm, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3011})

V_539 = Vertex(name = 'V_539',
               particles = [ P.vt__tilde__, P.vt, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3011})

V_540 = Vertex(name = 'V_540',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_3037,(0,2):C.GC_2584})

V_541 = Vertex(name = 'V_541',
               particles = [ P.s__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3046,(0,1):C.GC_2585})

V_542 = Vertex(name = 'V_542',
               particles = [ P.b__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3055,(0,1):C.GC_2586})

V_543 = Vertex(name = 'V_543',
               particles = [ P.d__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3040,(0,1):C.GC_2587})

V_544 = Vertex(name = 'V_544',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_3049,(0,2):C.GC_2588})

V_545 = Vertex(name = 'V_545',
               particles = [ P.b__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3058,(0,1):C.GC_2589})

V_546 = Vertex(name = 'V_546',
               particles = [ P.d__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3043,(0,1):C.GC_2590})

V_547 = Vertex(name = 'V_547',
               particles = [ P.s__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_3052,(0,1):C.GC_2591})

V_548 = Vertex(name = 'V_548',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_3061,(0,2):C.GC_2592})

V_549 = Vertex(name = 'V_549',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_4243,(0,2):C.GC_2635})

V_550 = Vertex(name = 'V_550',
               particles = [ P.c__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4252,(0,1):C.GC_2636})

V_551 = Vertex(name = 'V_551',
               particles = [ P.t__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4261,(0,1):C.GC_2637})

V_552 = Vertex(name = 'V_552',
               particles = [ P.u__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4246,(0,1):C.GC_2638})

V_553 = Vertex(name = 'V_553',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_4255,(0,2):C.GC_2639})

V_554 = Vertex(name = 'V_554',
               particles = [ P.t__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4264,(0,1):C.GC_2640})

V_555 = Vertex(name = 'V_555',
               particles = [ P.u__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4249,(0,1):C.GC_2641})

V_556 = Vertex(name = 'V_556',
               particles = [ P.c__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_4258,(0,1):C.GC_2642})

V_557 = Vertex(name = 'V_557',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_4267,(0,2):C.GC_2643})

V_558 = Vertex(name = 'V_558',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_4287,(0,3):C.GC_460,(0,2):C.GC_2744,(0,0):C.GC_2738})

V_559 = Vertex(name = 'V_559',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_4314,(0,3):C.GC_461,(0,2):C.GC_2745,(0,0):C.GC_2739})

V_560 = Vertex(name = 'V_560',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_4341,(0,3):C.GC_462,(0,2):C.GC_2746,(0,0):C.GC_2740})

V_561 = Vertex(name = 'V_561',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_4296,(0,3):C.GC_463,(0,2):C.GC_2747,(0,0):C.GC_3291})

V_562 = Vertex(name = 'V_562',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_4323,(0,3):C.GC_464,(0,2):C.GC_2748,(0,0):C.GC_2741})

V_563 = Vertex(name = 'V_563',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_4350,(0,3):C.GC_465,(0,2):C.GC_2749,(0,0):C.GC_2742})

V_564 = Vertex(name = 'V_564',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_4305,(0,3):C.GC_466,(0,2):C.GC_2750,(0,0):C.GC_3297})

V_565 = Vertex(name = 'V_565',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_4332,(0,3):C.GC_467,(0,2):C.GC_2751,(0,0):C.GC_3303})

V_566 = Vertex(name = 'V_566',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_4359,(0,3):C.GC_468,(0,2):C.GC_2752,(0,0):C.GC_2743})

V_567 = Vertex(name = 'V_567',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_4288,(0,3):C.GC_2602,(0,0):C.GC_2495,(0,2):C.GC_2828})

V_568 = Vertex(name = 'V_568',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2952})

V_569 = Vertex(name = 'V_569',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_4315,(0,3):C.GC_2603,(0,0):C.GC_2496,(0,2):C.GC_2829})

V_570 = Vertex(name = 'V_570',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2953})

V_571 = Vertex(name = 'V_571',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_4342,(0,3):C.GC_2604,(0,0):C.GC_2497,(0,2):C.GC_2830})

V_572 = Vertex(name = 'V_572',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2954})

V_573 = Vertex(name = 'V_573',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_4297,(0,3):C.GC_2605,(0,0):C.GC_2498,(0,2):C.GC_2831})

V_574 = Vertex(name = 'V_574',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3294})

V_575 = Vertex(name = 'V_575',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_4324,(0,3):C.GC_2606,(0,0):C.GC_2499,(0,2):C.GC_2832})

V_576 = Vertex(name = 'V_576',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2955})

V_577 = Vertex(name = 'V_577',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_4351,(0,3):C.GC_2607,(0,0):C.GC_2500,(0,2):C.GC_2833})

V_578 = Vertex(name = 'V_578',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2956})

V_579 = Vertex(name = 'V_579',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_4306,(0,3):C.GC_2608,(0,0):C.GC_2501,(0,2):C.GC_2834})

V_580 = Vertex(name = 'V_580',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3300})

V_581 = Vertex(name = 'V_581',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_4333,(0,3):C.GC_2609,(0,0):C.GC_2502,(0,2):C.GC_2835})

V_582 = Vertex(name = 'V_582',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3306})

V_583 = Vertex(name = 'V_583',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_4360,(0,3):C.GC_2610,(0,0):C.GC_2503,(0,2):C.GC_2836})

V_584 = Vertex(name = 'V_584',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2957})

V_585 = Vertex(name = 'V_585',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_2620,(0,0):C.GC_2494})

V_586 = Vertex(name = 'V_586',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2949})

V_587 = Vertex(name = 'V_587',
               particles = [ P.mu__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_2621,(0,0):C.GC_2825})

V_588 = Vertex(name = 'V_588',
               particles = [ P.ta__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_2622,(0,0):C.GC_2826})

V_589 = Vertex(name = 'V_589',
               particles = [ P.e__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_2623,(0,0):C.GC_3274})

V_590 = Vertex(name = 'V_590',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_2624,(0,0):C.GC_2494})

V_591 = Vertex(name = 'V_591',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2950})

V_592 = Vertex(name = 'V_592',
               particles = [ P.ta__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_2625,(0,0):C.GC_2827})

V_593 = Vertex(name = 'V_593',
               particles = [ P.e__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_2626,(0,0):C.GC_3280})

V_594 = Vertex(name = 'V_594',
               particles = [ P.mu__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_2627,(0,0):C.GC_3286})

V_595 = Vertex(name = 'V_595',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_2628,(0,0):C.GC_2494})

V_596 = Vertex(name = 'V_596',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2951})

V_597 = Vertex(name = 'V_597',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_640,(0,0):C.GC_2732})

V_598 = Vertex(name = 'V_598',
               particles = [ P.mu__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_641,(0,0):C.GC_2733})

V_599 = Vertex(name = 'V_599',
               particles = [ P.ta__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_642,(0,0):C.GC_2734})

V_600 = Vertex(name = 'V_600',
               particles = [ P.e__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_643,(0,0):C.GC_3273})

V_601 = Vertex(name = 'V_601',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_644,(0,0):C.GC_2735})

V_602 = Vertex(name = 'V_602',
               particles = [ P.ta__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_645,(0,0):C.GC_2736})

V_603 = Vertex(name = 'V_603',
               particles = [ P.e__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_646,(0,0):C.GC_3279})

V_604 = Vertex(name = 'V_604',
               particles = [ P.mu__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_647,(0,0):C.GC_3285})

V_605 = Vertex(name = 'V_605',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_648,(0,0):C.GC_2737})

V_606 = Vertex(name = 'V_606',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_3081,(0,3):C.GC_2475,(0,2):C.GC_3315,(0,0):C.GC_2738})

V_607 = Vertex(name = 'V_607',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_3108,(0,3):C.GC_2476,(0,2):C.GC_3321,(0,0):C.GC_2739})

V_608 = Vertex(name = 'V_608',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_3135,(0,3):C.GC_2477,(0,2):C.GC_3327,(0,0):C.GC_2740})

V_609 = Vertex(name = 'V_609',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_3090,(0,3):C.GC_2478,(0,2):C.GC_3317,(0,0):C.GC_3291})

V_610 = Vertex(name = 'V_610',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_3117,(0,3):C.GC_2479,(0,2):C.GC_3323,(0,0):C.GC_2741})

V_611 = Vertex(name = 'V_611',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_3144,(0,3):C.GC_2480,(0,2):C.GC_3329,(0,0):C.GC_2742})

V_612 = Vertex(name = 'V_612',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_3099,(0,3):C.GC_2481,(0,2):C.GC_3319,(0,0):C.GC_3297})

V_613 = Vertex(name = 'V_613',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_3126,(0,3):C.GC_2482,(0,2):C.GC_3325,(0,0):C.GC_3303})

V_614 = Vertex(name = 'V_614',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_3153,(0,3):C.GC_2483,(0,2):C.GC_3331,(0,0):C.GC_2743})

V_615 = Vertex(name = 'V_615',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_3082,(0,3):C.GC_2653,(0,0):C.GC_3334,(0,2):C.GC_3316})

V_616 = Vertex(name = 'V_616',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3333})

V_617 = Vertex(name = 'V_617',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_3109,(0,3):C.GC_2654,(0,0):C.GC_3340,(0,2):C.GC_3322})

V_618 = Vertex(name = 'V_618',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3339})

V_619 = Vertex(name = 'V_619',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_3136,(0,3):C.GC_2655,(0,0):C.GC_3346,(0,2):C.GC_3328})

V_620 = Vertex(name = 'V_620',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3345})

V_621 = Vertex(name = 'V_621',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_3091,(0,3):C.GC_2656,(0,0):C.GC_3336,(0,2):C.GC_3318})

V_622 = Vertex(name = 'V_622',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3335})

V_623 = Vertex(name = 'V_623',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_3118,(0,3):C.GC_2657,(0,0):C.GC_3342,(0,2):C.GC_3324})

V_624 = Vertex(name = 'V_624',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3341})

V_625 = Vertex(name = 'V_625',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_3145,(0,3):C.GC_2658,(0,0):C.GC_3348,(0,2):C.GC_3330})

V_626 = Vertex(name = 'V_626',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3347})

V_627 = Vertex(name = 'V_627',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_3100,(0,3):C.GC_2659,(0,0):C.GC_3338,(0,2):C.GC_3320})

V_628 = Vertex(name = 'V_628',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3337})

V_629 = Vertex(name = 'V_629',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_3127,(0,3):C.GC_2660,(0,0):C.GC_3344,(0,2):C.GC_3326})

V_630 = Vertex(name = 'V_630',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3343})

V_631 = Vertex(name = 'V_631',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_3154,(0,3):C.GC_2661,(0,0):C.GC_3350,(0,2):C.GC_3332})

V_632 = Vertex(name = 'V_632',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3349})

V_633 = Vertex(name = 'V_633',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_3181,(0,0):C.GC_2494})

V_634 = Vertex(name = 'V_634',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2949})

V_635 = Vertex(name = 'V_635',
               particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_3208,(0,0):C.GC_2825})

V_636 = Vertex(name = 'V_636',
               particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_3235,(0,0):C.GC_2826})

V_637 = Vertex(name = 'V_637',
               particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_3190,(0,0):C.GC_3274})

V_638 = Vertex(name = 'V_638',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_3217,(0,0):C.GC_2494})

V_639 = Vertex(name = 'V_639',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2950})

V_640 = Vertex(name = 'V_640',
               particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_3244,(0,0):C.GC_2827})

V_641 = Vertex(name = 'V_641',
               particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_3199,(0,0):C.GC_3280})

V_642 = Vertex(name = 'V_642',
               particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_3226,(0,0):C.GC_3286})

V_643 = Vertex(name = 'V_643',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_3253,(0,0):C.GC_2494})

V_644 = Vertex(name = 'V_644',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2951})

V_645 = Vertex(name = 'V_645',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_3180,(0,0):C.GC_2732})

V_646 = Vertex(name = 'V_646',
               particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_3207,(0,0):C.GC_2733})

V_647 = Vertex(name = 'V_647',
               particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_3234,(0,0):C.GC_2734})

V_648 = Vertex(name = 'V_648',
               particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_3189,(0,0):C.GC_3273})

V_649 = Vertex(name = 'V_649',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_3216,(0,0):C.GC_2735})

V_650 = Vertex(name = 'V_650',
               particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_3243,(0,0):C.GC_2736})

V_651 = Vertex(name = 'V_651',
               particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_3198,(0,0):C.GC_3279})

V_652 = Vertex(name = 'V_652',
               particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_3225,(0,0):C.GC_3285})

V_653 = Vertex(name = 'V_653',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_3252,(0,0):C.GC_2737})

V_654 = Vertex(name = 'V_654',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_2505,(0,4):C.GC_2944,(0,3):C.GC_2512,(0,2):C.GC_2958,(0,1):C.GC_3088,(0,5):C.GC_2841})

V_655 = Vertex(name = 'V_655',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_2998,(0,1):C.GC_3004})

V_656 = Vertex(name = 'V_656',
               particles = [ P.s__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_2977,(0,2):C.GC_2959,(0,1):C.GC_3115,(0,3):C.GC_2842})

V_657 = Vertex(name = 'V_657',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_2979,(0,2):C.GC_2960,(0,1):C.GC_3142,(0,3):C.GC_2843})

V_658 = Vertex(name = 'V_658',
               particles = [ P.d__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_3296,(0,2):C.GC_3262,(0,1):C.GC_3097,(0,3):C.GC_2844})

V_659 = Vertex(name = 'V_659',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_2505,(0,4):C.GC_2944,(0,3):C.GC_2512,(0,2):C.GC_2961,(0,1):C.GC_3124,(0,5):C.GC_2845})

V_660 = Vertex(name = 'V_660',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_2999,(0,1):C.GC_3004})

V_661 = Vertex(name = 'V_661',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_2981,(0,2):C.GC_2962,(0,1):C.GC_3151,(0,3):C.GC_2846})

V_662 = Vertex(name = 'V_662',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_3302,(0,2):C.GC_3264,(0,1):C.GC_3106,(0,3):C.GC_2847})

V_663 = Vertex(name = 'V_663',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_3308,(0,2):C.GC_3266,(0,1):C.GC_3133,(0,3):C.GC_2848})

V_664 = Vertex(name = 'V_664',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_2505,(0,4):C.GC_2944,(0,3):C.GC_2512,(0,2):C.GC_2963,(0,1):C.GC_3160,(0,5):C.GC_2849})

V_665 = Vertex(name = 'V_665',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_3000,(0,1):C.GC_3004})

V_666 = Vertex(name = 'V_666',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2920,(0,2):C.GC_2895,(0,1):C.GC_3086,(0,3):C.GC_2519})

V_667 = Vertex(name = 'V_667',
               particles = [ P.s__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2922,(0,2):C.GC_2896,(0,1):C.GC_3113,(0,3):C.GC_2520})

V_668 = Vertex(name = 'V_668',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2924,(0,2):C.GC_2897,(0,1):C.GC_3140,(0,3):C.GC_2521})

V_669 = Vertex(name = 'V_669',
               particles = [ P.d__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_3293,(0,2):C.GC_3261,(0,1):C.GC_3095,(0,3):C.GC_2522})

V_670 = Vertex(name = 'V_670',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2926,(0,2):C.GC_2898,(0,1):C.GC_3122,(0,3):C.GC_2523})

V_671 = Vertex(name = 'V_671',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2928,(0,2):C.GC_2899,(0,1):C.GC_3149,(0,3):C.GC_2524})

V_672 = Vertex(name = 'V_672',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_3299,(0,2):C.GC_3263,(0,1):C.GC_3104,(0,3):C.GC_2525})

V_673 = Vertex(name = 'V_673',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_3305,(0,2):C.GC_3265,(0,1):C.GC_3131,(0,3):C.GC_2526})

V_674 = Vertex(name = 'V_674',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2930,(0,2):C.GC_2900,(0,1):C.GC_3158,(0,3):C.GC_2527})

V_675 = Vertex(name = 'V_675',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_2505,(0,3):C.GC_2946,(0,4):C.GC_2513,(0,2):C.GC_2964,(0,1):C.GC_3187,(0,5):C.GC_2859})

V_676 = Vertex(name = 'V_676',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_2995,(0,1):C.GC_3005})

V_677 = Vertex(name = 'V_677',
               particles = [ P.mu__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_2971,(0,2):C.GC_2965,(0,1):C.GC_3214,(0,3):C.GC_2860})

V_678 = Vertex(name = 'V_678',
               particles = [ P.ta__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_2973,(0,2):C.GC_2966,(0,1):C.GC_3241,(0,3):C.GC_2861})

V_679 = Vertex(name = 'V_679',
               particles = [ P.e__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_3278,(0,2):C.GC_3268,(0,1):C.GC_3196,(0,3):C.GC_2862})

V_680 = Vertex(name = 'V_680',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_2505,(0,3):C.GC_2946,(0,4):C.GC_2513,(0,2):C.GC_2967,(0,1):C.GC_3223,(0,5):C.GC_2863})

V_681 = Vertex(name = 'V_681',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_2996,(0,1):C.GC_3005})

V_682 = Vertex(name = 'V_682',
               particles = [ P.ta__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_2975,(0,2):C.GC_2968,(0,1):C.GC_3250,(0,3):C.GC_2864})

V_683 = Vertex(name = 'V_683',
               particles = [ P.e__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_3284,(0,2):C.GC_3270,(0,1):C.GC_3205,(0,3):C.GC_2865})

V_684 = Vertex(name = 'V_684',
               particles = [ P.mu__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_3290,(0,2):C.GC_3272,(0,1):C.GC_3232,(0,3):C.GC_2866})

V_685 = Vertex(name = 'V_685',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_2505,(0,3):C.GC_2946,(0,4):C.GC_2513,(0,2):C.GC_2969,(0,1):C.GC_3259,(0,5):C.GC_2867})

V_686 = Vertex(name = 'V_686',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_2997,(0,1):C.GC_3005})

V_687 = Vertex(name = 'V_687',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2908,(0,2):C.GC_2901,(0,1):C.GC_3185,(0,3):C.GC_2537})

V_688 = Vertex(name = 'V_688',
               particles = [ P.mu__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2910,(0,2):C.GC_2902,(0,1):C.GC_3212,(0,3):C.GC_2538})

V_689 = Vertex(name = 'V_689',
               particles = [ P.ta__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2912,(0,2):C.GC_2903,(0,1):C.GC_3239,(0,3):C.GC_2539})

V_690 = Vertex(name = 'V_690',
               particles = [ P.e__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_3276,(0,2):C.GC_3267,(0,1):C.GC_3194,(0,3):C.GC_2540})

V_691 = Vertex(name = 'V_691',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2914,(0,2):C.GC_2904,(0,1):C.GC_3221,(0,3):C.GC_2541})

V_692 = Vertex(name = 'V_692',
               particles = [ P.ta__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2916,(0,2):C.GC_2905,(0,1):C.GC_3248,(0,3):C.GC_2542})

V_693 = Vertex(name = 'V_693',
               particles = [ P.e__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_3282,(0,2):C.GC_3269,(0,1):C.GC_3203,(0,3):C.GC_2543})

V_694 = Vertex(name = 'V_694',
               particles = [ P.mu__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_3288,(0,2):C.GC_3271,(0,1):C.GC_3230,(0,3):C.GC_2544})

V_695 = Vertex(name = 'V_695',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2918,(0,2):C.GC_2906,(0,1):C.GC_3257,(0,3):C.GC_2545})

V_696 = Vertex(name = 'V_696',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_2504,(0,3):C.GC_2945,(0,4):C.GC_2512,(0,2):C.GC_2982,(0,1):C.GC_4294,(0,5):C.GC_2877})

V_697 = Vertex(name = 'V_697',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV7 ],
               couplings = {(0,0):C.GC_2992,(0,1):C.GC_3004})

V_698 = Vertex(name = 'V_698',
               particles = [ P.c__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_2976,(0,2):C.GC_2983,(0,1):C.GC_4321,(0,3):C.GC_2878})

V_699 = Vertex(name = 'V_699',
               particles = [ P.t__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_2978,(0,2):C.GC_2984,(0,1):C.GC_4348,(0,3):C.GC_2879})

V_700 = Vertex(name = 'V_700',
               particles = [ P.u__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_3295,(0,2):C.GC_3310,(0,1):C.GC_4303,(0,3):C.GC_2880})

V_701 = Vertex(name = 'V_701',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_2504,(0,3):C.GC_2945,(0,4):C.GC_2512,(0,2):C.GC_2985,(0,1):C.GC_4330,(0,5):C.GC_2881})

V_702 = Vertex(name = 'V_702',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV7 ],
               couplings = {(0,0):C.GC_2993,(0,1):C.GC_3004})

V_703 = Vertex(name = 'V_703',
               particles = [ P.t__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_2980,(0,2):C.GC_2986,(0,1):C.GC_4357,(0,3):C.GC_2882})

V_704 = Vertex(name = 'V_704',
               particles = [ P.u__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_3301,(0,2):C.GC_3312,(0,1):C.GC_4312,(0,3):C.GC_2883})

V_705 = Vertex(name = 'V_705',
               particles = [ P.c__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_3307,(0,2):C.GC_3314,(0,1):C.GC_4339,(0,3):C.GC_2884})

V_706 = Vertex(name = 'V_706',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_2504,(0,3):C.GC_2945,(0,4):C.GC_2512,(0,2):C.GC_2987,(0,1):C.GC_4366,(0,5):C.GC_2885})

V_707 = Vertex(name = 'V_707',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV7 ],
               couplings = {(0,0):C.GC_2994,(0,1):C.GC_3004})

V_708 = Vertex(name = 'V_708',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2919,(0,2):C.GC_2931,(0,1):C.GC_4292,(0,3):C.GC_2555})

V_709 = Vertex(name = 'V_709',
               particles = [ P.c__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2921,(0,2):C.GC_2932,(0,1):C.GC_4319,(0,3):C.GC_2556})

V_710 = Vertex(name = 'V_710',
               particles = [ P.t__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2923,(0,2):C.GC_2933,(0,1):C.GC_4346,(0,3):C.GC_2557})

V_711 = Vertex(name = 'V_711',
               particles = [ P.u__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_3292,(0,2):C.GC_3309,(0,1):C.GC_4301,(0,3):C.GC_2558})

V_712 = Vertex(name = 'V_712',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2925,(0,2):C.GC_2934,(0,1):C.GC_4328,(0,3):C.GC_2559})

V_713 = Vertex(name = 'V_713',
               particles = [ P.t__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2927,(0,2):C.GC_2935,(0,1):C.GC_4355,(0,3):C.GC_2560})

V_714 = Vertex(name = 'V_714',
               particles = [ P.u__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_3298,(0,2):C.GC_3311,(0,1):C.GC_4310,(0,3):C.GC_2561})

V_715 = Vertex(name = 'V_715',
               particles = [ P.c__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_3304,(0,2):C.GC_3313,(0,1):C.GC_4337,(0,3):C.GC_2562})

V_716 = Vertex(name = 'V_716',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_2929,(0,2):C.GC_2936,(0,1):C.GC_4364,(0,3):C.GC_2563})

V_717 = Vertex(name = 'V_717',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2518})

V_718 = Vertex(name = 'V_718',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3006})

V_719 = Vertex(name = 'V_719',
               particles = [ P.vm__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2970})

V_720 = Vertex(name = 'V_720',
               particles = [ P.vt__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2972})

V_721 = Vertex(name = 'V_721',
               particles = [ P.ve__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3277})

V_722 = Vertex(name = 'V_722',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2518})

V_723 = Vertex(name = 'V_723',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3007})

V_724 = Vertex(name = 'V_724',
               particles = [ P.vt__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2974})

V_725 = Vertex(name = 'V_725',
               particles = [ P.ve__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3283})

V_726 = Vertex(name = 'V_726',
               particles = [ P.vm__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3289})

V_727 = Vertex(name = 'V_727',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2518})

V_728 = Vertex(name = 'V_728',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3008})

V_729 = Vertex(name = 'V_729',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_2907})

V_730 = Vertex(name = 'V_730',
               particles = [ P.vm__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_2909})

V_731 = Vertex(name = 'V_731',
               particles = [ P.vt__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_2911})

V_732 = Vertex(name = 'V_732',
               particles = [ P.ve__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_3275})

V_733 = Vertex(name = 'V_733',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_2913})

V_734 = Vertex(name = 'V_734',
               particles = [ P.vt__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_2915})

V_735 = Vertex(name = 'V_735',
               particles = [ P.ve__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_3281})

V_736 = Vertex(name = 'V_736',
               particles = [ P.vm__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_3287})

V_737 = Vertex(name = 'V_737',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_2917})

V_738 = Vertex(name = 'V_738',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_281,(0,7):C.GC_281,(0,0):C.GC_1557,(2,0):C.GC_1638,(1,3):C.GC_1557,(3,3):C.GC_1638,(1,1):C.GC_1557,(3,1):C.GC_1638,(1,2):C.GC_442,(0,4):C.GC_1557,(2,4):C.GC_1638,(0,5):C.GC_442})

V_739 = Vertex(name = 'V_739',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_283,(0,7):C.GC_283,(0,0):C.GC_1558,(2,0):C.GC_1639,(1,3):C.GC_1566,(3,3):C.GC_1647,(1,1):C.GC_1558,(3,1):C.GC_1639,(1,2):C.GC_10,(0,4):C.GC_1566,(2,4):C.GC_1647,(0,5):C.GC_10})

V_740 = Vertex(name = 'V_740',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_288,(0,7):C.GC_288,(0,0):C.GC_1559,(2,0):C.GC_1640,(1,3):C.GC_1575,(3,3):C.GC_1656,(1,1):C.GC_1559,(3,1):C.GC_1640,(1,2):C.GC_11,(0,4):C.GC_1575,(2,4):C.GC_1656,(0,5):C.GC_11})

V_741 = Vertex(name = 'V_741',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_296,(0,7):C.GC_296,(0,0):C.GC_1584,(2,0):C.GC_1665,(1,3):C.GC_1584,(3,3):C.GC_1665,(1,1):C.GC_1560,(3,1):C.GC_1641,(1,2):C.GC_13,(0,4):C.GC_1560,(2,4):C.GC_1641,(0,5):C.GC_13})

V_742 = Vertex(name = 'V_742',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_307,(0,7):C.GC_299,(0,0):C.GC_1585,(2,0):C.GC_1666,(1,3):C.GC_1593,(3,3):C.GC_1674,(1,1):C.GC_1561,(3,1):C.GC_1642,(1,2):C.GC_16,(0,4):C.GC_1569,(2,4):C.GC_1650,(0,5):C.GC_14})

V_743 = Vertex(name = 'V_743',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_321,(0,7):C.GC_302,(0,0):C.GC_1586,(2,0):C.GC_1667,(1,3):C.GC_1602,(3,3):C.GC_1683,(1,1):C.GC_1562,(3,1):C.GC_1643,(1,2):C.GC_20,(0,4):C.GC_1578,(2,4):C.GC_1659,(0,5):C.GC_15})

V_744 = Vertex(name = 'V_744',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_338,(0,7):C.GC_338,(0,0):C.GC_1611,(2,0):C.GC_1692,(1,3):C.GC_1611,(3,3):C.GC_1692,(1,1):C.GC_1563,(3,1):C.GC_1644,(1,2):C.GC_25,(0,4):C.GC_1563,(2,4):C.GC_1644,(0,5):C.GC_25})

V_745 = Vertex(name = 'V_745',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_358,(0,7):C.GC_341,(0,0):C.GC_1612,(2,0):C.GC_1693,(1,3):C.GC_1620,(3,3):C.GC_1701,(1,1):C.GC_1564,(3,1):C.GC_1645,(1,2):C.GC_31,(0,4):C.GC_1572,(2,4):C.GC_1653,(0,5):C.GC_26})

V_746 = Vertex(name = 'V_746',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_381,(0,7):C.GC_344,(0,0):C.GC_1613,(2,0):C.GC_1694,(1,3):C.GC_1629,(3,3):C.GC_1710,(1,1):C.GC_1565,(3,1):C.GC_1646,(1,2):C.GC_38,(0,4):C.GC_1581,(2,4):C.GC_1662,(0,5):C.GC_27})

V_747 = Vertex(name = 'V_747',
               particles = [ P.s__tilde__, P.d, P.s__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_286,(0,7):C.GC_286,(0,0):C.GC_1567,(2,0):C.GC_1648,(1,3):C.GC_1567,(3,3):C.GC_1648,(1,1):C.GC_1567,(3,1):C.GC_1648,(1,2):C.GC_443,(0,4):C.GC_1567,(2,4):C.GC_1648,(0,5):C.GC_443})

V_748 = Vertex(name = 'V_748',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_291,(0,7):C.GC_291,(0,0):C.GC_1568,(2,0):C.GC_1649,(1,3):C.GC_1576,(3,3):C.GC_1657,(1,1):C.GC_1568,(3,1):C.GC_1649,(1,2):C.GC_12,(0,4):C.GC_1576,(2,4):C.GC_1657,(0,5):C.GC_12})

V_749 = Vertex(name = 'V_749',
               particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_310,(0,7):C.GC_310,(0,0):C.GC_1594,(2,0):C.GC_1675,(1,3):C.GC_1594,(3,3):C.GC_1675,(1,1):C.GC_1570,(3,1):C.GC_1651,(1,2):C.GC_17,(0,4):C.GC_1570,(2,4):C.GC_1651,(0,5):C.GC_17})

V_750 = Vertex(name = 'V_750',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_324,(0,7):C.GC_313,(0,0):C.GC_1595,(2,0):C.GC_1676,(1,3):C.GC_1603,(3,3):C.GC_1684,(1,1):C.GC_1571,(3,1):C.GC_1652,(1,2):C.GC_21,(0,4):C.GC_1579,(2,4):C.GC_1660,(0,5):C.GC_18})

V_751 = Vertex(name = 'V_751',
               particles = [ P.s__tilde__, P.d, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_361,(0,7):C.GC_361,(0,0):C.GC_1621,(2,0):C.GC_1702,(1,3):C.GC_1621,(3,3):C.GC_1702,(1,1):C.GC_1573,(3,1):C.GC_1654,(1,2):C.GC_32,(0,4):C.GC_1573,(2,4):C.GC_1654,(0,5):C.GC_32})

V_752 = Vertex(name = 'V_752',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_384,(0,7):C.GC_364,(0,0):C.GC_1622,(2,0):C.GC_1703,(1,3):C.GC_1630,(3,3):C.GC_1711,(1,1):C.GC_1574,(3,1):C.GC_1655,(1,2):C.GC_39,(0,4):C.GC_1582,(2,4):C.GC_1663,(0,5):C.GC_33})

V_753 = Vertex(name = 'V_753',
               particles = [ P.b__tilde__, P.d, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_294,(0,7):C.GC_294,(0,0):C.GC_1577,(2,0):C.GC_1658,(1,3):C.GC_1577,(3,3):C.GC_1658,(1,1):C.GC_1577,(3,1):C.GC_1658,(1,2):C.GC_444,(0,4):C.GC_1577,(2,4):C.GC_1658,(0,5):C.GC_444})

V_754 = Vertex(name = 'V_754',
               particles = [ P.b__tilde__, P.d, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_327,(0,7):C.GC_327,(0,0):C.GC_1604,(2,0):C.GC_1685,(1,3):C.GC_1604,(3,3):C.GC_1685,(1,1):C.GC_1580,(3,1):C.GC_1661,(1,2):C.GC_22,(0,4):C.GC_1580,(2,4):C.GC_1661,(0,5):C.GC_22})

V_755 = Vertex(name = 'V_755',
               particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_387,(0,7):C.GC_387,(0,0):C.GC_1631,(2,0):C.GC_1712,(1,3):C.GC_1631,(3,3):C.GC_1712,(1,1):C.GC_1583,(3,1):C.GC_1664,(1,2):C.GC_40,(0,4):C.GC_1583,(2,4):C.GC_1664,(0,5):C.GC_40})

V_756 = Vertex(name = 'V_756',
               particles = [ P.d__tilde__, P.s, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_305,(0,7):C.GC_305,(0,0):C.GC_1587,(2,0):C.GC_1668,(1,3):C.GC_1587,(3,3):C.GC_1668,(1,1):C.GC_1587,(3,1):C.GC_1668,(1,2):C.GC_445,(0,4):C.GC_1587,(2,4):C.GC_1668,(0,5):C.GC_445})

V_757 = Vertex(name = 'V_757',
               particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_316,(0,7):C.GC_316,(0,0):C.GC_1588,(2,0):C.GC_1669,(1,3):C.GC_1596,(3,3):C.GC_1677,(1,1):C.GC_1588,(3,1):C.GC_1669,(1,2):C.GC_19,(0,4):C.GC_1596,(2,4):C.GC_1677,(0,5):C.GC_19})

V_758 = Vertex(name = 'V_758',
               particles = [ P.b__tilde__, P.s, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_330,(0,7):C.GC_330,(0,0):C.GC_1589,(2,0):C.GC_1670,(1,3):C.GC_1605,(3,3):C.GC_1686,(1,1):C.GC_1589,(3,1):C.GC_1670,(1,2):C.GC_23,(0,4):C.GC_1605,(2,4):C.GC_1686,(0,5):C.GC_23})

V_759 = Vertex(name = 'V_759',
               particles = [ P.d__tilde__, P.s, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_347,(0,7):C.GC_347,(0,0):C.GC_1614,(2,0):C.GC_1695,(1,3):C.GC_1614,(3,3):C.GC_1695,(1,1):C.GC_1590,(3,1):C.GC_1671,(1,2):C.GC_28,(0,4):C.GC_1590,(2,4):C.GC_1671,(0,5):C.GC_28})

V_760 = Vertex(name = 'V_760',
               particles = [ P.s__tilde__, P.s, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_367,(0,7):C.GC_350,(0,0):C.GC_1615,(2,0):C.GC_1696,(1,3):C.GC_1623,(3,3):C.GC_1704,(1,1):C.GC_1591,(3,1):C.GC_1672,(1,2):C.GC_34,(0,4):C.GC_1599,(2,4):C.GC_1680,(0,5):C.GC_29})

V_761 = Vertex(name = 'V_761',
               particles = [ P.b__tilde__, P.s, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_390,(0,7):C.GC_353,(0,0):C.GC_1616,(2,0):C.GC_1697,(1,3):C.GC_1632,(3,3):C.GC_1713,(1,1):C.GC_1592,(3,1):C.GC_1673,(1,2):C.GC_41,(0,4):C.GC_1608,(2,4):C.GC_1689,(0,5):C.GC_30})

V_762 = Vertex(name = 'V_762',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_319,(0,7):C.GC_319,(0,0):C.GC_1597,(2,0):C.GC_1678,(1,3):C.GC_1597,(3,3):C.GC_1678,(1,1):C.GC_1597,(3,1):C.GC_1678,(1,2):C.GC_446,(0,4):C.GC_1597,(2,4):C.GC_1678,(0,5):C.GC_446})

V_763 = Vertex(name = 'V_763',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_333,(0,7):C.GC_333,(0,0):C.GC_1598,(2,0):C.GC_1679,(1,3):C.GC_1606,(3,3):C.GC_1687,(1,1):C.GC_1598,(3,1):C.GC_1679,(1,2):C.GC_24,(0,4):C.GC_1606,(2,4):C.GC_1687,(0,5):C.GC_24})

V_764 = Vertex(name = 'V_764',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_370,(0,7):C.GC_370,(0,0):C.GC_1624,(2,0):C.GC_1705,(1,3):C.GC_1624,(3,3):C.GC_1705,(1,1):C.GC_1600,(3,1):C.GC_1681,(1,2):C.GC_35,(0,4):C.GC_1600,(2,4):C.GC_1681,(0,5):C.GC_35})

V_765 = Vertex(name = 'V_765',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_393,(0,7):C.GC_373,(0,0):C.GC_1625,(2,0):C.GC_1706,(1,3):C.GC_1633,(3,3):C.GC_1714,(1,1):C.GC_1601,(3,1):C.GC_1682,(1,2):C.GC_42,(0,4):C.GC_1609,(2,4):C.GC_1690,(0,5):C.GC_36})

V_766 = Vertex(name = 'V_766',
               particles = [ P.b__tilde__, P.s, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_336,(0,7):C.GC_336,(0,0):C.GC_1607,(2,0):C.GC_1688,(1,3):C.GC_1607,(3,3):C.GC_1688,(1,1):C.GC_1607,(3,1):C.GC_1688,(1,2):C.GC_447,(0,4):C.GC_1607,(2,4):C.GC_1688,(0,5):C.GC_447})

V_767 = Vertex(name = 'V_767',
               particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_396,(0,7):C.GC_396,(0,0):C.GC_1634,(2,0):C.GC_1715,(1,3):C.GC_1634,(3,3):C.GC_1715,(1,1):C.GC_1610,(3,1):C.GC_1691,(1,2):C.GC_43,(0,4):C.GC_1610,(2,4):C.GC_1691,(0,5):C.GC_43})

V_768 = Vertex(name = 'V_768',
               particles = [ P.d__tilde__, P.b, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_356,(0,7):C.GC_356,(0,0):C.GC_1617,(2,0):C.GC_1698,(1,3):C.GC_1617,(3,3):C.GC_1698,(1,1):C.GC_1617,(3,1):C.GC_1698,(1,2):C.GC_448,(0,4):C.GC_1617,(2,4):C.GC_1698,(0,5):C.GC_448})

V_769 = Vertex(name = 'V_769',
               particles = [ P.s__tilde__, P.b, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_376,(0,7):C.GC_376,(0,0):C.GC_1618,(2,0):C.GC_1699,(1,3):C.GC_1626,(3,3):C.GC_1707,(1,1):C.GC_1618,(3,1):C.GC_1699,(1,2):C.GC_37,(0,4):C.GC_1626,(2,4):C.GC_1707,(0,5):C.GC_37})

V_770 = Vertex(name = 'V_770',
               particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_399,(0,7):C.GC_399,(0,0):C.GC_1619,(2,0):C.GC_1700,(1,3):C.GC_1635,(3,3):C.GC_1716,(1,1):C.GC_1619,(3,1):C.GC_1700,(1,2):C.GC_44,(0,4):C.GC_1635,(2,4):C.GC_1716,(0,5):C.GC_44})

V_771 = Vertex(name = 'V_771',
               particles = [ P.s__tilde__, P.b, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_379,(0,7):C.GC_379,(0,0):C.GC_1627,(2,0):C.GC_1708,(1,3):C.GC_1627,(3,3):C.GC_1708,(1,1):C.GC_1627,(3,1):C.GC_1708,(1,2):C.GC_449,(0,4):C.GC_1627,(2,4):C.GC_1708,(0,5):C.GC_449})

V_772 = Vertex(name = 'V_772',
               particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_402,(0,7):C.GC_402,(0,0):C.GC_1628,(2,0):C.GC_1709,(1,3):C.GC_1636,(3,3):C.GC_1717,(1,1):C.GC_1628,(3,1):C.GC_1709,(1,2):C.GC_45,(0,4):C.GC_1636,(2,4):C.GC_1717,(0,5):C.GC_45})

V_773 = Vertex(name = 'V_773',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_405,(0,7):C.GC_405,(0,0):C.GC_1637,(2,0):C.GC_1718,(1,3):C.GC_1637,(3,3):C.GC_1718,(1,1):C.GC_1637,(3,1):C.GC_1718,(1,2):C.GC_450,(0,4):C.GC_1637,(2,4):C.GC_1718,(0,5):C.GC_450})

V_774 = Vertex(name = 'V_774',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_1386,(0,7):C.GC_1386,(0,0):C.GC_738,(0,3):C.GC_738,(0,1):C.GC_738,(0,2):C.GC_550,(0,4):C.GC_738,(0,5):C.GC_550})

V_775 = Vertex(name = 'V_775',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_82,(0,7):C.GC_82,(0,0):C.GC_739,(0,3):C.GC_747,(0,1):C.GC_739,(0,2):C.GC_46,(0,4):C.GC_747,(0,5):C.GC_46})

V_776 = Vertex(name = 'V_776',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_83,(0,7):C.GC_83,(0,0):C.GC_740,(0,3):C.GC_756,(0,1):C.GC_740,(0,2):C.GC_47,(0,4):C.GC_756,(0,5):C.GC_47})

V_777 = Vertex(name = 'V_777',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_85,(0,7):C.GC_85,(0,0):C.GC_765,(0,3):C.GC_765,(0,1):C.GC_741,(0,2):C.GC_49,(0,4):C.GC_741,(0,5):C.GC_49})

V_778 = Vertex(name = 'V_778',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_88,(0,7):C.GC_86,(0,0):C.GC_766,(0,3):C.GC_774,(0,1):C.GC_742,(0,2):C.GC_52,(0,4):C.GC_750,(0,5):C.GC_50})

V_779 = Vertex(name = 'V_779',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_92,(0,7):C.GC_87,(0,0):C.GC_767,(0,3):C.GC_783,(0,1):C.GC_743,(0,2):C.GC_56,(0,4):C.GC_759,(0,5):C.GC_51})

V_780 = Vertex(name = 'V_780',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_97,(0,7):C.GC_97,(0,0):C.GC_792,(0,3):C.GC_792,(0,1):C.GC_744,(0,2):C.GC_61,(0,4):C.GC_744,(0,5):C.GC_61})

V_781 = Vertex(name = 'V_781',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_103,(0,7):C.GC_98,(0,0):C.GC_793,(0,3):C.GC_801,(0,1):C.GC_745,(0,2):C.GC_67,(0,4):C.GC_753,(0,5):C.GC_62})

V_782 = Vertex(name = 'V_782',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_110,(0,7):C.GC_99,(0,0):C.GC_794,(0,3):C.GC_810,(0,1):C.GC_746,(0,2):C.GC_74,(0,4):C.GC_762,(0,5):C.GC_63})

V_783 = Vertex(name = 'V_783',
               particles = [ P.mu__plus__, P.e__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_1387,(0,7):C.GC_1387,(0,0):C.GC_748,(0,3):C.GC_748,(0,1):C.GC_748,(0,2):C.GC_551,(0,4):C.GC_748,(0,5):C.GC_551})

V_784 = Vertex(name = 'V_784',
               particles = [ P.ta__plus__, P.e__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_84,(0,7):C.GC_84,(0,0):C.GC_749,(0,3):C.GC_757,(0,1):C.GC_749,(0,2):C.GC_48,(0,4):C.GC_757,(0,5):C.GC_48})

V_785 = Vertex(name = 'V_785',
               particles = [ P.mu__plus__, P.e__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_89,(0,7):C.GC_89,(0,0):C.GC_775,(0,3):C.GC_775,(0,1):C.GC_751,(0,2):C.GC_53,(0,4):C.GC_751,(0,5):C.GC_53})

V_786 = Vertex(name = 'V_786',
               particles = [ P.ta__plus__, P.e__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_93,(0,7):C.GC_90,(0,0):C.GC_776,(0,3):C.GC_784,(0,1):C.GC_752,(0,2):C.GC_57,(0,4):C.GC_760,(0,5):C.GC_54})

V_787 = Vertex(name = 'V_787',
               particles = [ P.mu__plus__, P.e__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_104,(0,7):C.GC_104,(0,0):C.GC_802,(0,3):C.GC_802,(0,1):C.GC_754,(0,2):C.GC_68,(0,4):C.GC_754,(0,5):C.GC_68})

V_788 = Vertex(name = 'V_788',
               particles = [ P.ta__plus__, P.e__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_111,(0,7):C.GC_105,(0,0):C.GC_803,(0,3):C.GC_811,(0,1):C.GC_755,(0,2):C.GC_75,(0,4):C.GC_763,(0,5):C.GC_69})

V_789 = Vertex(name = 'V_789',
               particles = [ P.ta__plus__, P.e__minus__, P.ta__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_1388,(0,7):C.GC_1388,(0,0):C.GC_758,(0,3):C.GC_758,(0,1):C.GC_758,(0,2):C.GC_552,(0,4):C.GC_758,(0,5):C.GC_552})

V_790 = Vertex(name = 'V_790',
               particles = [ P.ta__plus__, P.e__minus__, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_94,(0,7):C.GC_94,(0,0):C.GC_785,(0,3):C.GC_785,(0,1):C.GC_761,(0,2):C.GC_58,(0,4):C.GC_761,(0,5):C.GC_58})

V_791 = Vertex(name = 'V_791',
               particles = [ P.ta__plus__, P.e__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_112,(0,7):C.GC_112,(0,0):C.GC_812,(0,3):C.GC_812,(0,1):C.GC_764,(0,2):C.GC_76,(0,4):C.GC_764,(0,5):C.GC_76})

V_792 = Vertex(name = 'V_792',
               particles = [ P.e__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_1389,(0,7):C.GC_1389,(0,0):C.GC_768,(0,3):C.GC_768,(0,1):C.GC_768,(0,2):C.GC_553,(0,4):C.GC_768,(0,5):C.GC_553})

V_793 = Vertex(name = 'V_793',
               particles = [ P.mu__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_91,(0,7):C.GC_91,(0,0):C.GC_769,(0,3):C.GC_777,(0,1):C.GC_769,(0,2):C.GC_55,(0,4):C.GC_777,(0,5):C.GC_55})

V_794 = Vertex(name = 'V_794',
               particles = [ P.ta__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_95,(0,7):C.GC_95,(0,0):C.GC_770,(0,3):C.GC_786,(0,1):C.GC_770,(0,2):C.GC_59,(0,4):C.GC_786,(0,5):C.GC_59})

V_795 = Vertex(name = 'V_795',
               particles = [ P.e__plus__, P.mu__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_100,(0,7):C.GC_100,(0,0):C.GC_795,(0,3):C.GC_795,(0,1):C.GC_771,(0,2):C.GC_64,(0,4):C.GC_771,(0,5):C.GC_64})

V_796 = Vertex(name = 'V_796',
               particles = [ P.mu__plus__, P.mu__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_106,(0,7):C.GC_101,(0,0):C.GC_796,(0,3):C.GC_804,(0,1):C.GC_772,(0,2):C.GC_70,(0,4):C.GC_780,(0,5):C.GC_65})

V_797 = Vertex(name = 'V_797',
               particles = [ P.ta__plus__, P.mu__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_113,(0,7):C.GC_102,(0,0):C.GC_797,(0,3):C.GC_813,(0,1):C.GC_773,(0,2):C.GC_77,(0,4):C.GC_789,(0,5):C.GC_66})

V_798 = Vertex(name = 'V_798',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_1390,(0,7):C.GC_1390,(0,0):C.GC_778,(0,3):C.GC_778,(0,1):C.GC_778,(0,2):C.GC_554,(0,4):C.GC_778,(0,5):C.GC_554})

V_799 = Vertex(name = 'V_799',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_96,(0,7):C.GC_96,(0,0):C.GC_779,(0,3):C.GC_787,(0,1):C.GC_779,(0,2):C.GC_60,(0,4):C.GC_787,(0,5):C.GC_60})

V_800 = Vertex(name = 'V_800',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_107,(0,7):C.GC_107,(0,0):C.GC_805,(0,3):C.GC_805,(0,1):C.GC_781,(0,2):C.GC_71,(0,4):C.GC_781,(0,5):C.GC_71})

V_801 = Vertex(name = 'V_801',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_114,(0,7):C.GC_108,(0,0):C.GC_806,(0,3):C.GC_814,(0,1):C.GC_782,(0,2):C.GC_78,(0,4):C.GC_790,(0,5):C.GC_72})

V_802 = Vertex(name = 'V_802',
               particles = [ P.ta__plus__, P.mu__minus__, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_1391,(0,7):C.GC_1391,(0,0):C.GC_788,(0,3):C.GC_788,(0,1):C.GC_788,(0,2):C.GC_555,(0,4):C.GC_788,(0,5):C.GC_555})

V_803 = Vertex(name = 'V_803',
               particles = [ P.ta__plus__, P.mu__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_115,(0,7):C.GC_115,(0,0):C.GC_815,(0,3):C.GC_815,(0,1):C.GC_791,(0,2):C.GC_79,(0,4):C.GC_791,(0,5):C.GC_79})

V_804 = Vertex(name = 'V_804',
               particles = [ P.e__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_1392,(0,7):C.GC_1392,(0,0):C.GC_798,(0,3):C.GC_798,(0,1):C.GC_798,(0,2):C.GC_556,(0,4):C.GC_798,(0,5):C.GC_556})

V_805 = Vertex(name = 'V_805',
               particles = [ P.mu__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_109,(0,7):C.GC_109,(0,0):C.GC_799,(0,3):C.GC_807,(0,1):C.GC_799,(0,2):C.GC_73,(0,4):C.GC_807,(0,5):C.GC_73})

V_806 = Vertex(name = 'V_806',
               particles = [ P.ta__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_116,(0,7):C.GC_116,(0,0):C.GC_800,(0,3):C.GC_816,(0,1):C.GC_800,(0,2):C.GC_80,(0,4):C.GC_816,(0,5):C.GC_80})

V_807 = Vertex(name = 'V_807',
               particles = [ P.mu__plus__, P.ta__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_1393,(0,7):C.GC_1393,(0,0):C.GC_808,(0,3):C.GC_808,(0,1):C.GC_808,(0,2):C.GC_557,(0,4):C.GC_808,(0,5):C.GC_557})

V_808 = Vertex(name = 'V_808',
               particles = [ P.ta__plus__, P.ta__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_117,(0,7):C.GC_117,(0,0):C.GC_809,(0,3):C.GC_817,(0,1):C.GC_809,(0,2):C.GC_81,(0,4):C.GC_817,(0,5):C.GC_81})

V_809 = Vertex(name = 'V_809',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_1394,(0,7):C.GC_1394,(0,0):C.GC_818,(0,3):C.GC_818,(0,1):C.GC_818,(0,2):C.GC_558,(0,4):C.GC_818,(0,5):C.GC_558})

V_810 = Vertex(name = 'V_810',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_281,(0,7):C.GC_281,(0,0):C.GC_1809,(2,0):C.GC_1890,(1,3):C.GC_1809,(3,3):C.GC_1890,(1,1):C.GC_1809,(3,1):C.GC_1890,(1,2):C.GC_2466,(0,4):C.GC_1809,(2,4):C.GC_1890,(0,5):C.GC_2466})

V_811 = Vertex(name = 'V_811',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_283,(0,7):C.GC_283,(0,0):C.GC_1810,(2,0):C.GC_1891,(1,3):C.GC_1818,(3,3):C.GC_1899,(1,1):C.GC_1810,(3,1):C.GC_1891,(1,2):C.GC_406,(0,4):C.GC_1818,(2,4):C.GC_1899,(0,5):C.GC_406})

V_812 = Vertex(name = 'V_812',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_288,(0,7):C.GC_288,(0,0):C.GC_1811,(2,0):C.GC_1892,(1,3):C.GC_1827,(3,3):C.GC_1908,(1,1):C.GC_1811,(3,1):C.GC_1892,(1,2):C.GC_407,(0,4):C.GC_1827,(2,4):C.GC_1908,(0,5):C.GC_407})

V_813 = Vertex(name = 'V_813',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_296,(0,7):C.GC_296,(0,0):C.GC_1836,(2,0):C.GC_1917,(1,3):C.GC_1836,(3,3):C.GC_1917,(1,1):C.GC_1812,(3,1):C.GC_1893,(1,2):C.GC_409,(0,4):C.GC_1812,(2,4):C.GC_1893,(0,5):C.GC_409})

V_814 = Vertex(name = 'V_814',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_307,(0,7):C.GC_299,(0,0):C.GC_1837,(2,0):C.GC_1918,(1,3):C.GC_1845,(3,3):C.GC_1926,(1,1):C.GC_1813,(3,1):C.GC_1894,(1,2):C.GC_412,(0,4):C.GC_1821,(2,4):C.GC_1902,(0,5):C.GC_410})

V_815 = Vertex(name = 'V_815',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_321,(0,7):C.GC_302,(0,0):C.GC_1838,(2,0):C.GC_1919,(1,3):C.GC_1854,(3,3):C.GC_1935,(1,1):C.GC_1814,(3,1):C.GC_1895,(1,2):C.GC_416,(0,4):C.GC_1830,(2,4):C.GC_1911,(0,5):C.GC_411})

V_816 = Vertex(name = 'V_816',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_338,(0,7):C.GC_338,(0,0):C.GC_1863,(2,0):C.GC_1944,(1,3):C.GC_1863,(3,3):C.GC_1944,(1,1):C.GC_1815,(3,1):C.GC_1896,(1,2):C.GC_421,(0,4):C.GC_1815,(2,4):C.GC_1896,(0,5):C.GC_421})

V_817 = Vertex(name = 'V_817',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_358,(0,7):C.GC_341,(0,0):C.GC_1864,(2,0):C.GC_1945,(1,3):C.GC_1872,(3,3):C.GC_1953,(1,1):C.GC_1816,(3,1):C.GC_1897,(1,2):C.GC_427,(0,4):C.GC_1824,(2,4):C.GC_1905,(0,5):C.GC_422})

V_818 = Vertex(name = 'V_818',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_381,(0,7):C.GC_344,(0,0):C.GC_1865,(2,0):C.GC_1946,(1,3):C.GC_1881,(3,3):C.GC_1962,(1,1):C.GC_1817,(3,1):C.GC_1898,(1,2):C.GC_434,(0,4):C.GC_1833,(2,4):C.GC_1914,(0,5):C.GC_423})

V_819 = Vertex(name = 'V_819',
               particles = [ P.c__tilde__, P.u, P.c__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_286,(0,7):C.GC_286,(0,0):C.GC_1819,(2,0):C.GC_1900,(1,3):C.GC_1819,(3,3):C.GC_1900,(1,1):C.GC_1819,(3,1):C.GC_1900,(1,2):C.GC_2467,(0,4):C.GC_1819,(2,4):C.GC_1900,(0,5):C.GC_2467})

V_820 = Vertex(name = 'V_820',
               particles = [ P.t__tilde__, P.u, P.c__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_291,(0,7):C.GC_291,(0,0):C.GC_1820,(2,0):C.GC_1901,(1,3):C.GC_1828,(3,3):C.GC_1909,(1,1):C.GC_1820,(3,1):C.GC_1901,(1,2):C.GC_408,(0,4):C.GC_1828,(2,4):C.GC_1909,(0,5):C.GC_408})

V_821 = Vertex(name = 'V_821',
               particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_310,(0,7):C.GC_310,(0,0):C.GC_1846,(2,0):C.GC_1927,(1,3):C.GC_1846,(3,3):C.GC_1927,(1,1):C.GC_1822,(3,1):C.GC_1903,(1,2):C.GC_413,(0,4):C.GC_1822,(2,4):C.GC_1903,(0,5):C.GC_413})

V_822 = Vertex(name = 'V_822',
               particles = [ P.t__tilde__, P.u, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_324,(0,7):C.GC_313,(0,0):C.GC_1847,(2,0):C.GC_1928,(1,3):C.GC_1855,(3,3):C.GC_1936,(1,1):C.GC_1823,(3,1):C.GC_1904,(1,2):C.GC_417,(0,4):C.GC_1831,(2,4):C.GC_1912,(0,5):C.GC_414})

V_823 = Vertex(name = 'V_823',
               particles = [ P.c__tilde__, P.u, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_361,(0,7):C.GC_361,(0,0):C.GC_1873,(2,0):C.GC_1954,(1,3):C.GC_1873,(3,3):C.GC_1954,(1,1):C.GC_1825,(3,1):C.GC_1906,(1,2):C.GC_428,(0,4):C.GC_1825,(2,4):C.GC_1906,(0,5):C.GC_428})

V_824 = Vertex(name = 'V_824',
               particles = [ P.t__tilde__, P.u, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_384,(0,7):C.GC_364,(0,0):C.GC_1874,(2,0):C.GC_1955,(1,3):C.GC_1882,(3,3):C.GC_1963,(1,1):C.GC_1826,(3,1):C.GC_1907,(1,2):C.GC_435,(0,4):C.GC_1834,(2,4):C.GC_1915,(0,5):C.GC_429})

V_825 = Vertex(name = 'V_825',
               particles = [ P.t__tilde__, P.u, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_294,(0,7):C.GC_294,(0,0):C.GC_1829,(2,0):C.GC_1910,(1,3):C.GC_1829,(3,3):C.GC_1910,(1,1):C.GC_1829,(3,1):C.GC_1910,(1,2):C.GC_2468,(0,4):C.GC_1829,(2,4):C.GC_1910,(0,5):C.GC_2468})

V_826 = Vertex(name = 'V_826',
               particles = [ P.t__tilde__, P.u, P.t__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_327,(0,7):C.GC_327,(0,0):C.GC_1856,(2,0):C.GC_1937,(1,3):C.GC_1856,(3,3):C.GC_1937,(1,1):C.GC_1832,(3,1):C.GC_1913,(1,2):C.GC_418,(0,4):C.GC_1832,(2,4):C.GC_1913,(0,5):C.GC_418})

V_827 = Vertex(name = 'V_827',
               particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_387,(0,7):C.GC_387,(0,0):C.GC_1883,(2,0):C.GC_1964,(1,3):C.GC_1883,(3,3):C.GC_1964,(1,1):C.GC_1835,(3,1):C.GC_1916,(1,2):C.GC_436,(0,4):C.GC_1835,(2,4):C.GC_1916,(0,5):C.GC_436})

V_828 = Vertex(name = 'V_828',
               particles = [ P.u__tilde__, P.c, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_305,(0,7):C.GC_305,(0,0):C.GC_1839,(2,0):C.GC_1920,(1,3):C.GC_1839,(3,3):C.GC_1920,(1,1):C.GC_1839,(3,1):C.GC_1920,(1,2):C.GC_2469,(0,4):C.GC_1839,(2,4):C.GC_1920,(0,5):C.GC_2469})

V_829 = Vertex(name = 'V_829',
               particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_316,(0,7):C.GC_316,(0,0):C.GC_1840,(2,0):C.GC_1921,(1,3):C.GC_1848,(3,3):C.GC_1929,(1,1):C.GC_1840,(3,1):C.GC_1921,(1,2):C.GC_415,(0,4):C.GC_1848,(2,4):C.GC_1929,(0,5):C.GC_415})

V_830 = Vertex(name = 'V_830',
               particles = [ P.t__tilde__, P.c, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_330,(0,7):C.GC_330,(0,0):C.GC_1841,(2,0):C.GC_1922,(1,3):C.GC_1857,(3,3):C.GC_1938,(1,1):C.GC_1841,(3,1):C.GC_1922,(1,2):C.GC_419,(0,4):C.GC_1857,(2,4):C.GC_1938,(0,5):C.GC_419})

V_831 = Vertex(name = 'V_831',
               particles = [ P.u__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_347,(0,7):C.GC_347,(0,0):C.GC_1866,(2,0):C.GC_1947,(1,3):C.GC_1866,(3,3):C.GC_1947,(1,1):C.GC_1842,(3,1):C.GC_1923,(1,2):C.GC_424,(0,4):C.GC_1842,(2,4):C.GC_1923,(0,5):C.GC_424})

V_832 = Vertex(name = 'V_832',
               particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_367,(0,7):C.GC_350,(0,0):C.GC_1867,(2,0):C.GC_1948,(1,3):C.GC_1875,(3,3):C.GC_1956,(1,1):C.GC_1843,(3,1):C.GC_1924,(1,2):C.GC_430,(0,4):C.GC_1851,(2,4):C.GC_1932,(0,5):C.GC_425})

V_833 = Vertex(name = 'V_833',
               particles = [ P.t__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_390,(0,7):C.GC_353,(0,0):C.GC_1868,(2,0):C.GC_1949,(1,3):C.GC_1884,(3,3):C.GC_1965,(1,1):C.GC_1844,(3,1):C.GC_1925,(1,2):C.GC_437,(0,4):C.GC_1860,(2,4):C.GC_1941,(0,5):C.GC_426})

V_834 = Vertex(name = 'V_834',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_319,(0,7):C.GC_319,(0,0):C.GC_1849,(2,0):C.GC_1930,(1,3):C.GC_1849,(3,3):C.GC_1930,(1,1):C.GC_1849,(3,1):C.GC_1930,(1,2):C.GC_2470,(0,4):C.GC_1849,(2,4):C.GC_1930,(0,5):C.GC_2470})

V_835 = Vertex(name = 'V_835',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_333,(0,7):C.GC_333,(0,0):C.GC_1850,(2,0):C.GC_1931,(1,3):C.GC_1858,(3,3):C.GC_1939,(1,1):C.GC_1850,(3,1):C.GC_1931,(1,2):C.GC_420,(0,4):C.GC_1858,(2,4):C.GC_1939,(0,5):C.GC_420})

V_836 = Vertex(name = 'V_836',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_370,(0,7):C.GC_370,(0,0):C.GC_1876,(2,0):C.GC_1957,(1,3):C.GC_1876,(3,3):C.GC_1957,(1,1):C.GC_1852,(3,1):C.GC_1933,(1,2):C.GC_431,(0,4):C.GC_1852,(2,4):C.GC_1933,(0,5):C.GC_431})

V_837 = Vertex(name = 'V_837',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_393,(0,7):C.GC_373,(0,0):C.GC_1877,(2,0):C.GC_1958,(1,3):C.GC_1885,(3,3):C.GC_1966,(1,1):C.GC_1853,(3,1):C.GC_1934,(1,2):C.GC_438,(0,4):C.GC_1861,(2,4):C.GC_1942,(0,5):C.GC_432})

V_838 = Vertex(name = 'V_838',
               particles = [ P.t__tilde__, P.c, P.t__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_336,(0,7):C.GC_336,(0,0):C.GC_1859,(2,0):C.GC_1940,(1,3):C.GC_1859,(3,3):C.GC_1940,(1,1):C.GC_1859,(3,1):C.GC_1940,(1,2):C.GC_2471,(0,4):C.GC_1859,(2,4):C.GC_1940,(0,5):C.GC_2471})

V_839 = Vertex(name = 'V_839',
               particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_396,(0,7):C.GC_396,(0,0):C.GC_1886,(2,0):C.GC_1967,(1,3):C.GC_1886,(3,3):C.GC_1967,(1,1):C.GC_1862,(3,1):C.GC_1943,(1,2):C.GC_439,(0,4):C.GC_1862,(2,4):C.GC_1943,(0,5):C.GC_439})

V_840 = Vertex(name = 'V_840',
               particles = [ P.u__tilde__, P.t, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_356,(0,7):C.GC_356,(0,0):C.GC_1869,(2,0):C.GC_1950,(1,3):C.GC_1869,(3,3):C.GC_1950,(1,1):C.GC_1869,(3,1):C.GC_1950,(1,2):C.GC_2472,(0,4):C.GC_1869,(2,4):C.GC_1950,(0,5):C.GC_2472})

V_841 = Vertex(name = 'V_841',
               particles = [ P.c__tilde__, P.t, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_376,(0,7):C.GC_376,(0,0):C.GC_1870,(2,0):C.GC_1951,(1,3):C.GC_1878,(3,3):C.GC_1959,(1,1):C.GC_1870,(3,1):C.GC_1951,(1,2):C.GC_433,(0,4):C.GC_1878,(2,4):C.GC_1959,(0,5):C.GC_433})

V_842 = Vertex(name = 'V_842',
               particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_399,(0,7):C.GC_399,(0,0):C.GC_1871,(2,0):C.GC_1952,(1,3):C.GC_1887,(3,3):C.GC_1968,(1,1):C.GC_1871,(3,1):C.GC_1952,(1,2):C.GC_440,(0,4):C.GC_1887,(2,4):C.GC_1968,(0,5):C.GC_440})

V_843 = Vertex(name = 'V_843',
               particles = [ P.c__tilde__, P.t, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_379,(0,7):C.GC_379,(0,0):C.GC_1879,(2,0):C.GC_1960,(1,3):C.GC_1879,(3,3):C.GC_1960,(1,1):C.GC_1879,(3,1):C.GC_1960,(1,2):C.GC_2473,(0,4):C.GC_1879,(2,4):C.GC_1960,(0,5):C.GC_2473})

V_844 = Vertex(name = 'V_844',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_402,(0,7):C.GC_402,(0,0):C.GC_1880,(2,0):C.GC_1961,(1,3):C.GC_1888,(3,3):C.GC_1969,(1,1):C.GC_1880,(3,1):C.GC_1961,(1,2):C.GC_441,(0,4):C.GC_1888,(2,4):C.GC_1969,(0,5):C.GC_441})

V_845 = Vertex(name = 'V_845',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_405,(0,7):C.GC_405,(0,0):C.GC_1889,(2,0):C.GC_1970,(1,3):C.GC_1889,(3,3):C.GC_1970,(1,1):C.GC_1889,(3,1):C.GC_1970,(1,2):C.GC_2474,(0,4):C.GC_1889,(2,4):C.GC_1970,(0,5):C.GC_2474})

V_846 = Vertex(name = 'V_846',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_118,(0,0):C.GC_657})

V_847 = Vertex(name = 'V_847',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_136,(0,0):C.GC_666})

V_848 = Vertex(name = 'V_848',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_154,(0,0):C.GC_675})

V_849 = Vertex(name = 'V_849',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_172,(0,0):C.GC_684})

V_850 = Vertex(name = 'V_850',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_190,(0,0):C.GC_693})

V_851 = Vertex(name = 'V_851',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_208,(0,0):C.GC_702})

V_852 = Vertex(name = 'V_852',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_226,(0,0):C.GC_711})

V_853 = Vertex(name = 'V_853',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_244,(0,0):C.GC_720})

V_854 = Vertex(name = 'V_854',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_262,(0,0):C.GC_729})

V_855 = Vertex(name = 'V_855',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_120,(0,0):C.GC_658})

V_856 = Vertex(name = 'V_856',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_138,(0,0):C.GC_667})

V_857 = Vertex(name = 'V_857',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_156,(0,0):C.GC_676})

V_858 = Vertex(name = 'V_858',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_174,(0,0):C.GC_685})

V_859 = Vertex(name = 'V_859',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_192,(0,0):C.GC_694})

V_860 = Vertex(name = 'V_860',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_210,(0,0):C.GC_703})

V_861 = Vertex(name = 'V_861',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_228,(0,0):C.GC_712})

V_862 = Vertex(name = 'V_862',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_246,(0,0):C.GC_721})

V_863 = Vertex(name = 'V_863',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_264,(0,0):C.GC_730})

V_864 = Vertex(name = 'V_864',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_122,(0,0):C.GC_659})

V_865 = Vertex(name = 'V_865',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_140,(0,0):C.GC_668})

V_866 = Vertex(name = 'V_866',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_158,(0,0):C.GC_677})

V_867 = Vertex(name = 'V_867',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_176,(0,0):C.GC_686})

V_868 = Vertex(name = 'V_868',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_194,(0,0):C.GC_695})

V_869 = Vertex(name = 'V_869',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_212,(0,0):C.GC_704})

V_870 = Vertex(name = 'V_870',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_230,(0,0):C.GC_713})

V_871 = Vertex(name = 'V_871',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_248,(0,0):C.GC_722})

V_872 = Vertex(name = 'V_872',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_266,(0,0):C.GC_731})

V_873 = Vertex(name = 'V_873',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_124,(0,0):C.GC_660})

V_874 = Vertex(name = 'V_874',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_142,(0,0):C.GC_669})

V_875 = Vertex(name = 'V_875',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_160,(0,0):C.GC_678})

V_876 = Vertex(name = 'V_876',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_178,(0,0):C.GC_687})

V_877 = Vertex(name = 'V_877',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_196,(0,0):C.GC_696})

V_878 = Vertex(name = 'V_878',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_214,(0,0):C.GC_705})

V_879 = Vertex(name = 'V_879',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_232,(0,0):C.GC_714})

V_880 = Vertex(name = 'V_880',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_250,(0,0):C.GC_723})

V_881 = Vertex(name = 'V_881',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_268,(0,0):C.GC_732})

V_882 = Vertex(name = 'V_882',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_126,(0,0):C.GC_661})

V_883 = Vertex(name = 'V_883',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_144,(0,0):C.GC_670})

V_884 = Vertex(name = 'V_884',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_162,(0,0):C.GC_679})

V_885 = Vertex(name = 'V_885',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_180,(0,0):C.GC_688})

V_886 = Vertex(name = 'V_886',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_198,(0,0):C.GC_697})

V_887 = Vertex(name = 'V_887',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_216,(0,0):C.GC_706})

V_888 = Vertex(name = 'V_888',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_234,(0,0):C.GC_715})

V_889 = Vertex(name = 'V_889',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_252,(0,0):C.GC_724})

V_890 = Vertex(name = 'V_890',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_270,(0,0):C.GC_733})

V_891 = Vertex(name = 'V_891',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_128,(0,0):C.GC_662})

V_892 = Vertex(name = 'V_892',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_146,(0,0):C.GC_671})

V_893 = Vertex(name = 'V_893',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_164,(0,0):C.GC_680})

V_894 = Vertex(name = 'V_894',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_182,(0,0):C.GC_689})

V_895 = Vertex(name = 'V_895',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_200,(0,0):C.GC_698})

V_896 = Vertex(name = 'V_896',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_218,(0,0):C.GC_707})

V_897 = Vertex(name = 'V_897',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_236,(0,0):C.GC_716})

V_898 = Vertex(name = 'V_898',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_254,(0,0):C.GC_725})

V_899 = Vertex(name = 'V_899',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_272,(0,0):C.GC_734})

V_900 = Vertex(name = 'V_900',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_130,(0,0):C.GC_663})

V_901 = Vertex(name = 'V_901',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_148,(0,0):C.GC_672})

V_902 = Vertex(name = 'V_902',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_166,(0,0):C.GC_681})

V_903 = Vertex(name = 'V_903',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_184,(0,0):C.GC_690})

V_904 = Vertex(name = 'V_904',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_202,(0,0):C.GC_699})

V_905 = Vertex(name = 'V_905',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_220,(0,0):C.GC_708})

V_906 = Vertex(name = 'V_906',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_238,(0,0):C.GC_717})

V_907 = Vertex(name = 'V_907',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_256,(0,0):C.GC_726})

V_908 = Vertex(name = 'V_908',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_274,(0,0):C.GC_735})

V_909 = Vertex(name = 'V_909',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_132,(0,0):C.GC_664})

V_910 = Vertex(name = 'V_910',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_150,(0,0):C.GC_673})

V_911 = Vertex(name = 'V_911',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_168,(0,0):C.GC_682})

V_912 = Vertex(name = 'V_912',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_186,(0,0):C.GC_691})

V_913 = Vertex(name = 'V_913',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_204,(0,0):C.GC_700})

V_914 = Vertex(name = 'V_914',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_222,(0,0):C.GC_709})

V_915 = Vertex(name = 'V_915',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_240,(0,0):C.GC_718})

V_916 = Vertex(name = 'V_916',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_258,(0,0):C.GC_727})

V_917 = Vertex(name = 'V_917',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_276,(0,0):C.GC_736})

V_918 = Vertex(name = 'V_918',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_134,(0,0):C.GC_665})

V_919 = Vertex(name = 'V_919',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_152,(0,0):C.GC_674})

V_920 = Vertex(name = 'V_920',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_170,(0,0):C.GC_683})

V_921 = Vertex(name = 'V_921',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_188,(0,0):C.GC_692})

V_922 = Vertex(name = 'V_922',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_206,(0,0):C.GC_701})

V_923 = Vertex(name = 'V_923',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_224,(0,0):C.GC_710})

V_924 = Vertex(name = 'V_924',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_242,(0,0):C.GC_719})

V_925 = Vertex(name = 'V_925',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_260,(0,0):C.GC_728})

V_926 = Vertex(name = 'V_926',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_278,(0,0):C.GC_737})

V_927 = Vertex(name = 'V_927',
               particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_1386,(0,0):C.GC_738})

V_928 = Vertex(name = 'V_928',
               particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_82,(0,0):C.GC_747})

V_929 = Vertex(name = 'V_929',
               particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_83,(0,0):C.GC_756})

V_930 = Vertex(name = 'V_930',
               particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_85,(0,0):C.GC_765})

V_931 = Vertex(name = 'V_931',
               particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_88,(0,0):C.GC_774})

V_932 = Vertex(name = 'V_932',
               particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_92,(0,0):C.GC_783})

V_933 = Vertex(name = 'V_933',
               particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_97,(0,0):C.GC_792})

V_934 = Vertex(name = 'V_934',
               particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_103,(0,0):C.GC_801})

V_935 = Vertex(name = 'V_935',
               particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_110,(0,0):C.GC_810})

V_936 = Vertex(name = 'V_936',
               particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_82,(0,0):C.GC_739})

V_937 = Vertex(name = 'V_937',
               particles = [ P.mu__plus__, P.e__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_1387,(0,0):C.GC_748})

V_938 = Vertex(name = 'V_938',
               particles = [ P.mu__plus__, P.e__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_84,(0,0):C.GC_757})

V_939 = Vertex(name = 'V_939',
               particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_86,(0,0):C.GC_766})

V_940 = Vertex(name = 'V_940',
               particles = [ P.mu__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_89,(0,0):C.GC_775})

V_941 = Vertex(name = 'V_941',
               particles = [ P.mu__plus__, P.e__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_93,(0,0):C.GC_784})

V_942 = Vertex(name = 'V_942',
               particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_98,(0,0):C.GC_793})

V_943 = Vertex(name = 'V_943',
               particles = [ P.mu__plus__, P.e__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_104,(0,0):C.GC_802})

V_944 = Vertex(name = 'V_944',
               particles = [ P.mu__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_111,(0,0):C.GC_811})

V_945 = Vertex(name = 'V_945',
               particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_83,(0,0):C.GC_740})

V_946 = Vertex(name = 'V_946',
               particles = [ P.ta__plus__, P.e__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_84,(0,0):C.GC_749})

V_947 = Vertex(name = 'V_947',
               particles = [ P.ta__plus__, P.e__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_1388,(0,0):C.GC_758})

V_948 = Vertex(name = 'V_948',
               particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_87,(0,0):C.GC_767})

V_949 = Vertex(name = 'V_949',
               particles = [ P.ta__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_90,(0,0):C.GC_776})

V_950 = Vertex(name = 'V_950',
               particles = [ P.ta__plus__, P.e__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_94,(0,0):C.GC_785})

V_951 = Vertex(name = 'V_951',
               particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_99,(0,0):C.GC_794})

V_952 = Vertex(name = 'V_952',
               particles = [ P.ta__plus__, P.e__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_105,(0,0):C.GC_803})

V_953 = Vertex(name = 'V_953',
               particles = [ P.ta__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_112,(0,0):C.GC_812})

V_954 = Vertex(name = 'V_954',
               particles = [ P.e__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_85,(0,0):C.GC_741})

V_955 = Vertex(name = 'V_955',
               particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_86,(0,0):C.GC_750})

V_956 = Vertex(name = 'V_956',
               particles = [ P.e__plus__, P.mu__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_87,(0,0):C.GC_759})

V_957 = Vertex(name = 'V_957',
               particles = [ P.e__plus__, P.mu__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_1389,(0,0):C.GC_768})

V_958 = Vertex(name = 'V_958',
               particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_91,(0,0):C.GC_777})

V_959 = Vertex(name = 'V_959',
               particles = [ P.e__plus__, P.mu__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_95,(0,0):C.GC_786})

V_960 = Vertex(name = 'V_960',
               particles = [ P.e__plus__, P.mu__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_100,(0,0):C.GC_795})

V_961 = Vertex(name = 'V_961',
               particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_106,(0,0):C.GC_804})

V_962 = Vertex(name = 'V_962',
               particles = [ P.e__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_113,(0,0):C.GC_813})

V_963 = Vertex(name = 'V_963',
               particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_88,(0,0):C.GC_742})

V_964 = Vertex(name = 'V_964',
               particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_89,(0,0):C.GC_751})

V_965 = Vertex(name = 'V_965',
               particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_90,(0,0):C.GC_760})

V_966 = Vertex(name = 'V_966',
               particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_91,(0,0):C.GC_769})

V_967 = Vertex(name = 'V_967',
               particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_1390,(0,0):C.GC_778})

V_968 = Vertex(name = 'V_968',
               particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_96,(0,0):C.GC_787})

V_969 = Vertex(name = 'V_969',
               particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_101,(0,0):C.GC_796})

V_970 = Vertex(name = 'V_970',
               particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_107,(0,0):C.GC_805})

V_971 = Vertex(name = 'V_971',
               particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_114,(0,0):C.GC_814})

V_972 = Vertex(name = 'V_972',
               particles = [ P.ta__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_92,(0,0):C.GC_743})

V_973 = Vertex(name = 'V_973',
               particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_93,(0,0):C.GC_752})

V_974 = Vertex(name = 'V_974',
               particles = [ P.ta__plus__, P.mu__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_94,(0,0):C.GC_761})

V_975 = Vertex(name = 'V_975',
               particles = [ P.ta__plus__, P.mu__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_95,(0,0):C.GC_770})

V_976 = Vertex(name = 'V_976',
               particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_96,(0,0):C.GC_779})

V_977 = Vertex(name = 'V_977',
               particles = [ P.ta__plus__, P.mu__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_1391,(0,0):C.GC_788})

V_978 = Vertex(name = 'V_978',
               particles = [ P.ta__plus__, P.mu__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_102,(0,0):C.GC_797})

V_979 = Vertex(name = 'V_979',
               particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_108,(0,0):C.GC_806})

V_980 = Vertex(name = 'V_980',
               particles = [ P.ta__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_115,(0,0):C.GC_815})

V_981 = Vertex(name = 'V_981',
               particles = [ P.e__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_97,(0,0):C.GC_744})

V_982 = Vertex(name = 'V_982',
               particles = [ P.e__plus__, P.ta__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_98,(0,0):C.GC_753})

V_983 = Vertex(name = 'V_983',
               particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_99,(0,0):C.GC_762})

V_984 = Vertex(name = 'V_984',
               particles = [ P.e__plus__, P.ta__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_100,(0,0):C.GC_771})

V_985 = Vertex(name = 'V_985',
               particles = [ P.e__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_101,(0,0):C.GC_780})

V_986 = Vertex(name = 'V_986',
               particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_102,(0,0):C.GC_789})

V_987 = Vertex(name = 'V_987',
               particles = [ P.e__plus__, P.ta__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_1392,(0,0):C.GC_798})

V_988 = Vertex(name = 'V_988',
               particles = [ P.e__plus__, P.ta__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_109,(0,0):C.GC_807})

V_989 = Vertex(name = 'V_989',
               particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_116,(0,0):C.GC_816})

V_990 = Vertex(name = 'V_990',
               particles = [ P.mu__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_103,(0,0):C.GC_745})

V_991 = Vertex(name = 'V_991',
               particles = [ P.mu__plus__, P.ta__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_104,(0,0):C.GC_754})

V_992 = Vertex(name = 'V_992',
               particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_105,(0,0):C.GC_763})

V_993 = Vertex(name = 'V_993',
               particles = [ P.mu__plus__, P.ta__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_106,(0,0):C.GC_772})

V_994 = Vertex(name = 'V_994',
               particles = [ P.mu__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_107,(0,0):C.GC_781})

V_995 = Vertex(name = 'V_995',
               particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_108,(0,0):C.GC_790})

V_996 = Vertex(name = 'V_996',
               particles = [ P.mu__plus__, P.ta__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_109,(0,0):C.GC_799})

V_997 = Vertex(name = 'V_997',
               particles = [ P.mu__plus__, P.ta__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_1393,(0,0):C.GC_808})

V_998 = Vertex(name = 'V_998',
               particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_117,(0,0):C.GC_817})

V_999 = Vertex(name = 'V_999',
               particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF12, L.FFFF4 ],
               couplings = {(0,1):C.GC_110,(0,0):C.GC_746})

V_1000 = Vertex(name = 'V_1000',
                particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_111,(0,0):C.GC_755})

V_1001 = Vertex(name = 'V_1001',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_112,(0,0):C.GC_764})

V_1002 = Vertex(name = 'V_1002',
                particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_113,(0,0):C.GC_773})

V_1003 = Vertex(name = 'V_1003',
                particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_114,(0,0):C.GC_782})

V_1004 = Vertex(name = 'V_1004',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_115,(0,0):C.GC_791})

V_1005 = Vertex(name = 'V_1005',
                particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_116,(0,0):C.GC_800})

V_1006 = Vertex(name = 'V_1006',
                particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_117,(0,0):C.GC_809})

V_1007 = Vertex(name = 'V_1007',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_1394,(0,0):C.GC_818})

V_1008 = Vertex(name = 'V_1008',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_119,(0,0):C.GC_1476})

V_1009 = Vertex(name = 'V_1009',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_137,(0,0):C.GC_1485})

V_1010 = Vertex(name = 'V_1010',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_155,(0,0):C.GC_1494})

V_1011 = Vertex(name = 'V_1011',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_173,(0,0):C.GC_1503})

V_1012 = Vertex(name = 'V_1012',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_191,(0,0):C.GC_1512})

V_1013 = Vertex(name = 'V_1013',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_209,(0,0):C.GC_1521})

V_1014 = Vertex(name = 'V_1014',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_227,(0,0):C.GC_1530})

V_1015 = Vertex(name = 'V_1015',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_245,(0,0):C.GC_1539})

V_1016 = Vertex(name = 'V_1016',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_263,(0,0):C.GC_1548})

V_1017 = Vertex(name = 'V_1017',
                particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_121,(0,0):C.GC_1477})

V_1018 = Vertex(name = 'V_1018',
                particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_139,(0,0):C.GC_1486})

V_1019 = Vertex(name = 'V_1019',
                particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_157,(0,0):C.GC_1495})

V_1020 = Vertex(name = 'V_1020',
                particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_175,(0,0):C.GC_1504})

V_1021 = Vertex(name = 'V_1021',
                particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_193,(0,0):C.GC_1513})

V_1022 = Vertex(name = 'V_1022',
                particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_211,(0,0):C.GC_1522})

V_1023 = Vertex(name = 'V_1023',
                particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_229,(0,0):C.GC_1531})

V_1024 = Vertex(name = 'V_1024',
                particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_247,(0,0):C.GC_1540})

V_1025 = Vertex(name = 'V_1025',
                particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_265,(0,0):C.GC_1549})

V_1026 = Vertex(name = 'V_1026',
                particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_123,(0,0):C.GC_1478})

V_1027 = Vertex(name = 'V_1027',
                particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_141,(0,0):C.GC_1487})

V_1028 = Vertex(name = 'V_1028',
                particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_159,(0,0):C.GC_1496})

V_1029 = Vertex(name = 'V_1029',
                particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_177,(0,0):C.GC_1505})

V_1030 = Vertex(name = 'V_1030',
                particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_195,(0,0):C.GC_1514})

V_1031 = Vertex(name = 'V_1031',
                particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_213,(0,0):C.GC_1523})

V_1032 = Vertex(name = 'V_1032',
                particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_231,(0,0):C.GC_1532})

V_1033 = Vertex(name = 'V_1033',
                particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_249,(0,0):C.GC_1541})

V_1034 = Vertex(name = 'V_1034',
                particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_267,(0,0):C.GC_1550})

V_1035 = Vertex(name = 'V_1035',
                particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_125,(0,0):C.GC_1479})

V_1036 = Vertex(name = 'V_1036',
                particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_143,(0,0):C.GC_1488})

V_1037 = Vertex(name = 'V_1037',
                particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_161,(0,0):C.GC_1497})

V_1038 = Vertex(name = 'V_1038',
                particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_179,(0,0):C.GC_1506})

V_1039 = Vertex(name = 'V_1039',
                particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_197,(0,0):C.GC_1515})

V_1040 = Vertex(name = 'V_1040',
                particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_215,(0,0):C.GC_1524})

V_1041 = Vertex(name = 'V_1041',
                particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_233,(0,0):C.GC_1533})

V_1042 = Vertex(name = 'V_1042',
                particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_251,(0,0):C.GC_1542})

V_1043 = Vertex(name = 'V_1043',
                particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_269,(0,0):C.GC_1551})

V_1044 = Vertex(name = 'V_1044',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_127,(0,0):C.GC_1480})

V_1045 = Vertex(name = 'V_1045',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_145,(0,0):C.GC_1489})

V_1046 = Vertex(name = 'V_1046',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_163,(0,0):C.GC_1498})

V_1047 = Vertex(name = 'V_1047',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_181,(0,0):C.GC_1507})

V_1048 = Vertex(name = 'V_1048',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_199,(0,0):C.GC_1516})

V_1049 = Vertex(name = 'V_1049',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_217,(0,0):C.GC_1525})

V_1050 = Vertex(name = 'V_1050',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_235,(0,0):C.GC_1534})

V_1051 = Vertex(name = 'V_1051',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_253,(0,0):C.GC_1543})

V_1052 = Vertex(name = 'V_1052',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_271,(0,0):C.GC_1552})

V_1053 = Vertex(name = 'V_1053',
                particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_129,(0,0):C.GC_1481})

V_1054 = Vertex(name = 'V_1054',
                particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_147,(0,0):C.GC_1490})

V_1055 = Vertex(name = 'V_1055',
                particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_165,(0,0):C.GC_1499})

V_1056 = Vertex(name = 'V_1056',
                particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_183,(0,0):C.GC_1508})

V_1057 = Vertex(name = 'V_1057',
                particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_201,(0,0):C.GC_1517})

V_1058 = Vertex(name = 'V_1058',
                particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_219,(0,0):C.GC_1526})

V_1059 = Vertex(name = 'V_1059',
                particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_237,(0,0):C.GC_1535})

V_1060 = Vertex(name = 'V_1060',
                particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_255,(0,0):C.GC_1544})

V_1061 = Vertex(name = 'V_1061',
                particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_273,(0,0):C.GC_1553})

V_1062 = Vertex(name = 'V_1062',
                particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_131,(0,0):C.GC_1482})

V_1063 = Vertex(name = 'V_1063',
                particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_149,(0,0):C.GC_1491})

V_1064 = Vertex(name = 'V_1064',
                particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_167,(0,0):C.GC_1500})

V_1065 = Vertex(name = 'V_1065',
                particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_185,(0,0):C.GC_1509})

V_1066 = Vertex(name = 'V_1066',
                particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_203,(0,0):C.GC_1518})

V_1067 = Vertex(name = 'V_1067',
                particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_221,(0,0):C.GC_1527})

V_1068 = Vertex(name = 'V_1068',
                particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_239,(0,0):C.GC_1536})

V_1069 = Vertex(name = 'V_1069',
                particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_257,(0,0):C.GC_1545})

V_1070 = Vertex(name = 'V_1070',
                particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_275,(0,0):C.GC_1554})

V_1071 = Vertex(name = 'V_1071',
                particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_133,(0,0):C.GC_1483})

V_1072 = Vertex(name = 'V_1072',
                particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_151,(0,0):C.GC_1492})

V_1073 = Vertex(name = 'V_1073',
                particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_169,(0,0):C.GC_1501})

V_1074 = Vertex(name = 'V_1074',
                particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_187,(0,0):C.GC_1510})

V_1075 = Vertex(name = 'V_1075',
                particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_205,(0,0):C.GC_1519})

V_1076 = Vertex(name = 'V_1076',
                particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_223,(0,0):C.GC_1528})

V_1077 = Vertex(name = 'V_1077',
                particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_241,(0,0):C.GC_1537})

V_1078 = Vertex(name = 'V_1078',
                particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_259,(0,0):C.GC_1546})

V_1079 = Vertex(name = 'V_1079',
                particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_277,(0,0):C.GC_1555})

V_1080 = Vertex(name = 'V_1080',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_135,(0,0):C.GC_1484})

V_1081 = Vertex(name = 'V_1081',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_153,(0,0):C.GC_1493})

V_1082 = Vertex(name = 'V_1082',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_171,(0,0):C.GC_1502})

V_1083 = Vertex(name = 'V_1083',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_189,(0,0):C.GC_1511})

V_1084 = Vertex(name = 'V_1084',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_207,(0,0):C.GC_1520})

V_1085 = Vertex(name = 'V_1085',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_225,(0,0):C.GC_1529})

V_1086 = Vertex(name = 'V_1086',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_243,(0,0):C.GC_1538})

V_1087 = Vertex(name = 'V_1087',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_261,(0,0):C.GC_1547})

V_1088 = Vertex(name = 'V_1088',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_279,(0,0):C.GC_1556})

V_1089 = Vertex(name = 'V_1089',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_1386,(0,1):C.GC_1386})

V_1090 = Vertex(name = 'V_1090',
                particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_82,(0,1):C.GC_82})

V_1091 = Vertex(name = 'V_1091',
                particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_83,(0,1):C.GC_83})

V_1092 = Vertex(name = 'V_1092',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_85,(0,1):C.GC_85})

V_1093 = Vertex(name = 'V_1093',
                particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_88,(0,1):C.GC_86})

V_1094 = Vertex(name = 'V_1094',
                particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_92,(0,1):C.GC_87})

V_1095 = Vertex(name = 'V_1095',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_97,(0,1):C.GC_97})

V_1096 = Vertex(name = 'V_1096',
                particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_103,(0,1):C.GC_98})

V_1097 = Vertex(name = 'V_1097',
                particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_110,(0,1):C.GC_99})

V_1098 = Vertex(name = 'V_1098',
                particles = [ P.vm__tilde__, P.ve, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_1387,(0,1):C.GC_1387})

V_1099 = Vertex(name = 'V_1099',
                particles = [ P.vt__tilde__, P.ve, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_84,(0,1):C.GC_84})

V_1100 = Vertex(name = 'V_1100',
                particles = [ P.vm__tilde__, P.ve, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_89,(0,1):C.GC_89})

V_1101 = Vertex(name = 'V_1101',
                particles = [ P.vt__tilde__, P.ve, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_93,(0,1):C.GC_90})

V_1102 = Vertex(name = 'V_1102',
                particles = [ P.vm__tilde__, P.ve, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_104,(0,1):C.GC_104})

V_1103 = Vertex(name = 'V_1103',
                particles = [ P.vt__tilde__, P.ve, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_111,(0,1):C.GC_105})

V_1104 = Vertex(name = 'V_1104',
                particles = [ P.vt__tilde__, P.ve, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_1388,(0,1):C.GC_1388})

V_1105 = Vertex(name = 'V_1105',
                particles = [ P.vt__tilde__, P.ve, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_94,(0,1):C.GC_94})

V_1106 = Vertex(name = 'V_1106',
                particles = [ P.vt__tilde__, P.ve, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_112,(0,1):C.GC_112})

V_1107 = Vertex(name = 'V_1107',
                particles = [ P.ve__tilde__, P.vm, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_1389,(0,1):C.GC_1389})

V_1108 = Vertex(name = 'V_1108',
                particles = [ P.vm__tilde__, P.vm, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_91,(0,1):C.GC_91})

V_1109 = Vertex(name = 'V_1109',
                particles = [ P.vt__tilde__, P.vm, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_95,(0,1):C.GC_95})

V_1110 = Vertex(name = 'V_1110',
                particles = [ P.ve__tilde__, P.vm, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_100,(0,1):C.GC_100})

V_1111 = Vertex(name = 'V_1111',
                particles = [ P.vm__tilde__, P.vm, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_106,(0,1):C.GC_101})

V_1112 = Vertex(name = 'V_1112',
                particles = [ P.vt__tilde__, P.vm, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_113,(0,1):C.GC_102})

V_1113 = Vertex(name = 'V_1113',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_1390,(0,1):C.GC_1390})

V_1114 = Vertex(name = 'V_1114',
                particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_96,(0,1):C.GC_96})

V_1115 = Vertex(name = 'V_1115',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_107,(0,1):C.GC_107})

V_1116 = Vertex(name = 'V_1116',
                particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_114,(0,1):C.GC_108})

V_1117 = Vertex(name = 'V_1117',
                particles = [ P.vt__tilde__, P.vm, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_1391,(0,1):C.GC_1391})

V_1118 = Vertex(name = 'V_1118',
                particles = [ P.vt__tilde__, P.vm, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_115,(0,1):C.GC_115})

V_1119 = Vertex(name = 'V_1119',
                particles = [ P.ve__tilde__, P.vt, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_1392,(0,1):C.GC_1392})

V_1120 = Vertex(name = 'V_1120',
                particles = [ P.vm__tilde__, P.vt, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_109,(0,1):C.GC_109})

V_1121 = Vertex(name = 'V_1121',
                particles = [ P.vt__tilde__, P.vt, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_116,(0,1):C.GC_116})

V_1122 = Vertex(name = 'V_1122',
                particles = [ P.vm__tilde__, P.vt, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_1393,(0,1):C.GC_1393})

V_1123 = Vertex(name = 'V_1123',
                particles = [ P.vt__tilde__, P.vt, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_117,(0,1):C.GC_117})

V_1124 = Vertex(name = 'V_1124',
                particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_1394,(0,1):C.GC_1394})

V_1125 = Vertex(name = 'V_1125',
                particles = [ P.d__tilde__, P.d, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3087,(0,1):C.GC_2528})

V_1126 = Vertex(name = 'V_1126',
                particles = [ P.s__tilde__, P.d, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3114,(0,1):C.GC_2529})

V_1127 = Vertex(name = 'V_1127',
                particles = [ P.b__tilde__, P.d, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3141,(0,1):C.GC_2530})

V_1128 = Vertex(name = 'V_1128',
                particles = [ P.d__tilde__, P.s, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3096,(0,1):C.GC_2531})

V_1129 = Vertex(name = 'V_1129',
                particles = [ P.s__tilde__, P.s, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3123,(0,1):C.GC_2532})

V_1130 = Vertex(name = 'V_1130',
                particles = [ P.b__tilde__, P.s, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3150,(0,1):C.GC_2533})

V_1131 = Vertex(name = 'V_1131',
                particles = [ P.d__tilde__, P.b, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3105,(0,1):C.GC_2534})

V_1132 = Vertex(name = 'V_1132',
                particles = [ P.s__tilde__, P.b, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3132,(0,1):C.GC_2535})

V_1133 = Vertex(name = 'V_1133',
                particles = [ P.b__tilde__, P.b, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3159,(0,1):C.GC_2536})

V_1134 = Vertex(name = 'V_1134',
                particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3186,(0,1):C.GC_2546})

V_1135 = Vertex(name = 'V_1135',
                particles = [ P.mu__plus__, P.e__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3213,(0,1):C.GC_2547})

V_1136 = Vertex(name = 'V_1136',
                particles = [ P.ta__plus__, P.e__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3240,(0,1):C.GC_2548})

V_1137 = Vertex(name = 'V_1137',
                particles = [ P.e__plus__, P.mu__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3195,(0,1):C.GC_2549})

V_1138 = Vertex(name = 'V_1138',
                particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3222,(0,1):C.GC_2550})

V_1139 = Vertex(name = 'V_1139',
                particles = [ P.ta__plus__, P.mu__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3249,(0,1):C.GC_2551})

V_1140 = Vertex(name = 'V_1140',
                particles = [ P.e__plus__, P.ta__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3204,(0,1):C.GC_2552})

V_1141 = Vertex(name = 'V_1141',
                particles = [ P.mu__plus__, P.ta__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3231,(0,1):C.GC_2553})

V_1142 = Vertex(name = 'V_1142',
                particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3258,(0,1):C.GC_2554})

V_1143 = Vertex(name = 'V_1143',
                particles = [ P.u__tilde__, P.u, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4293,(0,1):C.GC_2564})

V_1144 = Vertex(name = 'V_1144',
                particles = [ P.c__tilde__, P.u, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4320,(0,1):C.GC_2565})

V_1145 = Vertex(name = 'V_1145',
                particles = [ P.t__tilde__, P.u, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4347,(0,1):C.GC_2566})

V_1146 = Vertex(name = 'V_1146',
                particles = [ P.u__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4302,(0,1):C.GC_2567})

V_1147 = Vertex(name = 'V_1147',
                particles = [ P.c__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4329,(0,1):C.GC_2568})

V_1148 = Vertex(name = 'V_1148',
                particles = [ P.t__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4356,(0,1):C.GC_2569})

V_1149 = Vertex(name = 'V_1149',
                particles = [ P.u__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4311,(0,1):C.GC_2570})

V_1150 = Vertex(name = 'V_1150',
                particles = [ P.c__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4338,(0,1):C.GC_2571})

V_1151 = Vertex(name = 'V_1151',
                particles = [ P.t__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4365,(0,1):C.GC_2572})

V_1152 = Vertex(name = 'V_1152',
                particles = [ P.d__tilde__, P.d, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3036,(0,1):C.GC_451})

V_1153 = Vertex(name = 'V_1153',
                particles = [ P.s__tilde__, P.d, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3045,(0,1):C.GC_452})

V_1154 = Vertex(name = 'V_1154',
                particles = [ P.b__tilde__, P.d, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3054,(0,1):C.GC_453})

V_1155 = Vertex(name = 'V_1155',
                particles = [ P.d__tilde__, P.s, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3039,(0,1):C.GC_454})

V_1156 = Vertex(name = 'V_1156',
                particles = [ P.s__tilde__, P.s, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3048,(0,1):C.GC_455})

V_1157 = Vertex(name = 'V_1157',
                particles = [ P.b__tilde__, P.s, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3057,(0,1):C.GC_456})

V_1158 = Vertex(name = 'V_1158',
                particles = [ P.d__tilde__, P.b, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3042,(0,1):C.GC_457})

V_1159 = Vertex(name = 'V_1159',
                particles = [ P.s__tilde__, P.b, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3051,(0,1):C.GC_458})

V_1160 = Vertex(name = 'V_1160',
                particles = [ P.b__tilde__, P.b, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_3060,(0,1):C.GC_459})

V_1161 = Vertex(name = 'V_1161',
                particles = [ P.u__tilde__, P.u, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4242,(0,1):C.GC_2457})

V_1162 = Vertex(name = 'V_1162',
                particles = [ P.c__tilde__, P.u, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4251,(0,1):C.GC_2458})

V_1163 = Vertex(name = 'V_1163',
                particles = [ P.t__tilde__, P.u, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4260,(0,1):C.GC_2459})

V_1164 = Vertex(name = 'V_1164',
                particles = [ P.u__tilde__, P.c, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4245,(0,1):C.GC_2460})

V_1165 = Vertex(name = 'V_1165',
                particles = [ P.c__tilde__, P.c, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4254,(0,1):C.GC_2461})

V_1166 = Vertex(name = 'V_1166',
                particles = [ P.t__tilde__, P.c, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4263,(0,1):C.GC_2462})

V_1167 = Vertex(name = 'V_1167',
                particles = [ P.u__tilde__, P.t, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4248,(0,1):C.GC_2463})

V_1168 = Vertex(name = 'V_1168',
                particles = [ P.c__tilde__, P.t, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4257,(0,1):C.GC_2464})

V_1169 = Vertex(name = 'V_1169',
                particles = [ P.t__tilde__, P.t, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS4 ],
                couplings = {(0,0):C.GC_4266,(0,1):C.GC_2465})

V_1170 = Vertex(name = 'V_1170',
                particles = [ P.d__tilde__, P.d, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3038,(0,1):C.GC_2693})

V_1171 = Vertex(name = 'V_1171',
                particles = [ P.s__tilde__, P.d, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3047,(0,1):C.GC_2694})

V_1172 = Vertex(name = 'V_1172',
                particles = [ P.b__tilde__, P.d, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3056,(0,1):C.GC_2695})

V_1173 = Vertex(name = 'V_1173',
                particles = [ P.d__tilde__, P.s, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3041,(0,1):C.GC_2696})

V_1174 = Vertex(name = 'V_1174',
                particles = [ P.s__tilde__, P.s, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3050,(0,1):C.GC_2697})

V_1175 = Vertex(name = 'V_1175',
                particles = [ P.b__tilde__, P.s, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3059,(0,1):C.GC_2698})

V_1176 = Vertex(name = 'V_1176',
                particles = [ P.d__tilde__, P.b, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3044,(0,1):C.GC_2699})

V_1177 = Vertex(name = 'V_1177',
                particles = [ P.s__tilde__, P.b, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3053,(0,1):C.GC_2700})

V_1178 = Vertex(name = 'V_1178',
                particles = [ P.b__tilde__, P.b, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3062,(0,1):C.GC_2701})

V_1179 = Vertex(name = 'V_1179',
                particles = [ P.u__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4244,(0,1):C.GC_2704})

V_1180 = Vertex(name = 'V_1180',
                particles = [ P.c__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4253,(0,1):C.GC_2705})

V_1181 = Vertex(name = 'V_1181',
                particles = [ P.t__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4262,(0,1):C.GC_2706})

V_1182 = Vertex(name = 'V_1182',
                particles = [ P.u__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4247,(0,1):C.GC_2707})

V_1183 = Vertex(name = 'V_1183',
                particles = [ P.c__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4256,(0,1):C.GC_2708})

V_1184 = Vertex(name = 'V_1184',
                particles = [ P.t__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4265,(0,1):C.GC_2709})

V_1185 = Vertex(name = 'V_1185',
                particles = [ P.u__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4250,(0,1):C.GC_2710})

V_1186 = Vertex(name = 'V_1186',
                particles = [ P.c__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4259,(0,1):C.GC_2711})

V_1187 = Vertex(name = 'V_1187',
                particles = [ P.t__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4268,(0,1):C.GC_2712})

V_1188 = Vertex(name = 'V_1188',
                particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3083,(0,1):C.GC_2684})

V_1189 = Vertex(name = 'V_1189',
                particles = [ P.c__tilde__, P.d, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3110,(0,1):C.GC_2685})

V_1190 = Vertex(name = 'V_1190',
                particles = [ P.t__tilde__, P.d, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3137,(0,1):C.GC_2686})

V_1191 = Vertex(name = 'V_1191',
                particles = [ P.u__tilde__, P.s, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3092,(0,1):C.GC_2687})

V_1192 = Vertex(name = 'V_1192',
                particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3119,(0,1):C.GC_2688})

V_1193 = Vertex(name = 'V_1193',
                particles = [ P.t__tilde__, P.s, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3146,(0,1):C.GC_2689})

V_1194 = Vertex(name = 'V_1194',
                particles = [ P.u__tilde__, P.b, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3101,(0,1):C.GC_2690})

V_1195 = Vertex(name = 'V_1195',
                particles = [ P.c__tilde__, P.b, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3128,(0,1):C.GC_2691})

V_1196 = Vertex(name = 'V_1196',
                particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3155,(0,1):C.GC_2692})

V_1197 = Vertex(name = 'V_1197',
                particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3182})

V_1198 = Vertex(name = 'V_1198',
                particles = [ P.vm__tilde__, P.e__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3209})

V_1199 = Vertex(name = 'V_1199',
                particles = [ P.vt__tilde__, P.e__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3236})

V_1200 = Vertex(name = 'V_1200',
                particles = [ P.ve__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3191})

V_1201 = Vertex(name = 'V_1201',
                particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3218})

V_1202 = Vertex(name = 'V_1202',
                particles = [ P.vt__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3245})

V_1203 = Vertex(name = 'V_1203',
                particles = [ P.ve__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3200})

V_1204 = Vertex(name = 'V_1204',
                particles = [ P.vm__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3227})

V_1205 = Vertex(name = 'V_1205',
                particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3254})

V_1206 = Vertex(name = 'V_1206',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4289,(0,1):C.GC_2662})

V_1207 = Vertex(name = 'V_1207',
                particles = [ P.s__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4316,(0,1):C.GC_2663})

V_1208 = Vertex(name = 'V_1208',
                particles = [ P.b__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4343,(0,1):C.GC_2664})

V_1209 = Vertex(name = 'V_1209',
                particles = [ P.d__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4298,(0,1):C.GC_2665})

V_1210 = Vertex(name = 'V_1210',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4325,(0,1):C.GC_2666})

V_1211 = Vertex(name = 'V_1211',
                particles = [ P.b__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4352,(0,1):C.GC_2667})

V_1212 = Vertex(name = 'V_1212',
                particles = [ P.d__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4307,(0,1):C.GC_2668})

V_1213 = Vertex(name = 'V_1213',
                particles = [ P.s__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4334,(0,1):C.GC_2669})

V_1214 = Vertex(name = 'V_1214',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4361,(0,1):C.GC_2670})

V_1215 = Vertex(name = 'V_1215',
                particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3084,(0,1):C.GC_2714})

V_1216 = Vertex(name = 'V_1216',
                particles = [ P.s__tilde__, P.d, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3111,(0,1):C.GC_2715})

V_1217 = Vertex(name = 'V_1217',
                particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3138,(0,1):C.GC_2716})

V_1218 = Vertex(name = 'V_1218',
                particles = [ P.d__tilde__, P.s, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3093,(0,1):C.GC_2717})

V_1219 = Vertex(name = 'V_1219',
                particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3120,(0,1):C.GC_2718})

V_1220 = Vertex(name = 'V_1220',
                particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3147,(0,1):C.GC_2719})

V_1221 = Vertex(name = 'V_1221',
                particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3102,(0,1):C.GC_2720})

V_1222 = Vertex(name = 'V_1222',
                particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3129,(0,1):C.GC_2721})

V_1223 = Vertex(name = 'V_1223',
                particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3156,(0,1):C.GC_2722})

V_1224 = Vertex(name = 'V_1224',
                particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3183,(0,1):C.GC_2723})

V_1225 = Vertex(name = 'V_1225',
                particles = [ P.mu__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3210,(0,1):C.GC_2724})

V_1226 = Vertex(name = 'V_1226',
                particles = [ P.ta__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3237,(0,1):C.GC_2725})

V_1227 = Vertex(name = 'V_1227',
                particles = [ P.e__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3192,(0,1):C.GC_2726})

V_1228 = Vertex(name = 'V_1228',
                particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3219,(0,1):C.GC_2727})

V_1229 = Vertex(name = 'V_1229',
                particles = [ P.ta__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3246,(0,1):C.GC_2728})

V_1230 = Vertex(name = 'V_1230',
                particles = [ P.e__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3201,(0,1):C.GC_2729})

V_1231 = Vertex(name = 'V_1231',
                particles = [ P.mu__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3228,(0,1):C.GC_2730})

V_1232 = Vertex(name = 'V_1232',
                particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3255,(0,1):C.GC_2731})

V_1233 = Vertex(name = 'V_1233',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4290,(0,1):C.GC_2775})

V_1234 = Vertex(name = 'V_1234',
                particles = [ P.c__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4317,(0,1):C.GC_2777})

V_1235 = Vertex(name = 'V_1235',
                particles = [ P.t__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4344,(0,1):C.GC_2779})

V_1236 = Vertex(name = 'V_1236',
                particles = [ P.u__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4299,(0,1):C.GC_2781})

V_1237 = Vertex(name = 'V_1237',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4326,(0,1):C.GC_2783})

V_1238 = Vertex(name = 'V_1238',
                particles = [ P.t__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4353,(0,1):C.GC_2785})

V_1239 = Vertex(name = 'V_1239',
                particles = [ P.u__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4308,(0,1):C.GC_2787})

V_1240 = Vertex(name = 'V_1240',
                particles = [ P.c__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4335,(0,1):C.GC_2789})

V_1241 = Vertex(name = 'V_1241',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4362,(0,1):C.GC_2791})

V_1242 = Vertex(name = 'V_1242',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3085,(0,1):C.GC_2776})

V_1243 = Vertex(name = 'V_1243',
                particles = [ P.c__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3112,(0,1):C.GC_2778})

V_1244 = Vertex(name = 'V_1244',
                particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3139,(0,1):C.GC_2780})

V_1245 = Vertex(name = 'V_1245',
                particles = [ P.u__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3094,(0,1):C.GC_2782})

V_1246 = Vertex(name = 'V_1246',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3121,(0,1):C.GC_2784})

V_1247 = Vertex(name = 'V_1247',
                particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3148,(0,1):C.GC_2786})

V_1248 = Vertex(name = 'V_1248',
                particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3103,(0,1):C.GC_2788})

V_1249 = Vertex(name = 'V_1249',
                particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3130,(0,1):C.GC_2790})

V_1250 = Vertex(name = 'V_1250',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_3157,(0,1):C.GC_2792})

V_1251 = Vertex(name = 'V_1251',
                particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3184})

V_1252 = Vertex(name = 'V_1252',
                particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3211})

V_1253 = Vertex(name = 'V_1253',
                particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3238})

V_1254 = Vertex(name = 'V_1254',
                particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3193})

V_1255 = Vertex(name = 'V_1255',
                particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3220})

V_1256 = Vertex(name = 'V_1256',
                particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3247})

V_1257 = Vertex(name = 'V_1257',
                particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3202})

V_1258 = Vertex(name = 'V_1258',
                particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3229})

V_1259 = Vertex(name = 'V_1259',
                particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_3256})

V_1260 = Vertex(name = 'V_1260',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4291,(0,1):C.GC_2753})

V_1261 = Vertex(name = 'V_1261',
                particles = [ P.s__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4318,(0,1):C.GC_2754})

V_1262 = Vertex(name = 'V_1262',
                particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4345,(0,1):C.GC_2755})

V_1263 = Vertex(name = 'V_1263',
                particles = [ P.d__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4300,(0,1):C.GC_2756})

V_1264 = Vertex(name = 'V_1264',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4327,(0,1):C.GC_2757})

V_1265 = Vertex(name = 'V_1265',
                particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4354,(0,1):C.GC_2758})

V_1266 = Vertex(name = 'V_1266',
                particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4309,(0,1):C.GC_2759})

V_1267 = Vertex(name = 'V_1267',
                particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4336,(0,1):C.GC_2760})

V_1268 = Vertex(name = 'V_1268',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4363,(0,1):C.GC_2761})

V_1269 = Vertex(name = 'V_1269',
                particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2671})

V_1270 = Vertex(name = 'V_1270',
                particles = [ P.mu__plus__, P.ve, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2672})

V_1271 = Vertex(name = 'V_1271',
                particles = [ P.ta__plus__, P.ve, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2673})

V_1272 = Vertex(name = 'V_1272',
                particles = [ P.e__plus__, P.vm, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2674})

V_1273 = Vertex(name = 'V_1273',
                particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2675})

V_1274 = Vertex(name = 'V_1274',
                particles = [ P.ta__plus__, P.vm, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2676})

V_1275 = Vertex(name = 'V_1275',
                particles = [ P.e__plus__, P.vt, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2677})

V_1276 = Vertex(name = 'V_1276',
                particles = [ P.mu__plus__, P.vt, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2678})

V_1277 = Vertex(name = 'V_1277',
                particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2679})

V_1278 = Vertex(name = 'V_1278',
                particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2762})

V_1279 = Vertex(name = 'V_1279',
                particles = [ P.mu__plus__, P.ve, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2763})

V_1280 = Vertex(name = 'V_1280',
                particles = [ P.ta__plus__, P.ve, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2764})

V_1281 = Vertex(name = 'V_1281',
                particles = [ P.e__plus__, P.vm, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2765})

V_1282 = Vertex(name = 'V_1282',
                particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2766})

V_1283 = Vertex(name = 'V_1283',
                particles = [ P.ta__plus__, P.vm, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2767})

V_1284 = Vertex(name = 'V_1284',
                particles = [ P.e__plus__, P.vt, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2768})

V_1285 = Vertex(name = 'V_1285',
                particles = [ P.mu__plus__, P.vt, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2769})

V_1286 = Vertex(name = 'V_1286',
                particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2770})

