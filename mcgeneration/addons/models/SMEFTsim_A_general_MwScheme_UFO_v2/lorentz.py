# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Mon 5 Feb 2018 13:13:56


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


UUV1 = Lorentz(name = 'UUV1',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2) + P(3,3)')

SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

SSS2 = Lorentz(name = 'SSS2',
               spins = [ 1, 1, 1 ],
               structure = 'P(-1,1)*P(-1,2) + P(-1,1)*P(-1,3) + P(-1,2)*P(-1,3)')

SSS3 = Lorentz(name = 'SSS3',
               spins = [ 1, 1, 1 ],
               structure = 'P(-1,1)**2 + (2*P(-1,1)*P(-1,2))/3. + P(-1,2)**2 + (2*P(-1,1)*P(-1,3))/3. + (2*P(-1,2)*P(-1,3))/3. + P(-1,3)**2')

FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1)')

FFS2 = Lorentz(name = 'FFS2',
               spins = [ 2, 2, 1 ],
               structure = 'ProjP(2,1)')

FFS3 = Lorentz(name = 'FFS3',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) - 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV5 = Lorentz(name = 'FFV5',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + Gamma(3,2,-1)*ProjP(-1,1)')

FFV6 = Lorentz(name = 'FFV6',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV7 = Lorentz(name = 'FFV7',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)')

FFV8 = Lorentz(name = 'FFV8',
               spins = [ 2, 2, 3 ],
               structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)')

VVS2 = Lorentz(name = 'VVS2',
               spins = [ 3, 3, 1 ],
               structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS3 = Lorentz(name = 'VVS3',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVS4 = Lorentz(name = 'VVS4',
               spins = [ 3, 3, 1 ],
               structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = '-(Epsilon(1,2,3,-1)*P(-1,1))')

VVV2 = Lorentz(name = 'VVV2',
               spins = [ 3, 3, 3 ],
               structure = '-(Epsilon(1,2,3,-1)*P(-1,3))')

VVV3 = Lorentz(name = 'VVV3',
               spins = [ 3, 3, 3 ],
               structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) - Epsilon(1,2,3,-1)*P(-1,2) - Epsilon(1,2,3,-1)*P(-1,3)')

VVV4 = Lorentz(name = 'VVV4',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + 3*P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - 3*P(1,3)*Metric(2,3)')

VVV5 = Lorentz(name = 'VVV5',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVV6 = Lorentz(name = 'VVV6',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) + P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) - P(2,3)*Metric(1,3) - P(1,2)*Metric(2,3) + P(1,3)*Metric(2,3)')

VVV7 = Lorentz(name = 'VVV7',
               spins = [ 3, 3, 3 ],
               structure = '-(P(1,2)*P(2,3)*P(3,1)) + P(1,3)*P(2,1)*P(3,2) + P(-1,2)*P(-1,3)*P(3,1)*Metric(1,2) - P(-1,1)*P(-1,3)*P(3,2)*Metric(1,2) - P(-1,2)*P(-1,3)*P(2,1)*Metric(1,3) + P(-1,1)*P(-1,2)*P(2,3)*Metric(1,3) + P(-1,1)*P(-1,3)*P(1,2)*Metric(2,3) - P(-1,1)*P(-1,2)*P(1,3)*Metric(2,3)')

VVV8 = Lorentz(name = 'VVV8',
               spins = [ 3, 3, 3 ],
               structure = '-2*Epsilon(1,2,3,-2)*P(-2,3)*P(-1,1)*P(-1,2) - 2*Epsilon(1,2,3,-2)*P(-2,2)*P(-1,1)*P(-1,3) - 2*Epsilon(1,2,3,-2)*P(-2,1)*P(-1,2)*P(-1,3) + 2*Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,1)*P(1,2) + 2*Epsilon(2,3,-1,-2)*P(-2,2)*P(-1,1)*P(1,3) - 2*Epsilon(1,3,-1,-2)*P(-2,3)*P(-1,2)*P(2,1) - 2*Epsilon(1,3,-1,-2)*P(-2,1)*P(-1,2)*P(2,3) + 2*Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,3)*P(3,1) + 2*Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,3)*P(3,2) + Epsilon(3,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*Metric(1,2) - Epsilon(3,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*Metric(1,2) - Epsilon(2,-1,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*Metric(1,3) + Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*Metric(1,3) + Epsilon(1,-1,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*Metric(2,3) - Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*Metric(2,3)')

VVV9 = Lorentz(name = 'VVV9',
               spins = [ 3, 3, 3 ],
               structure = 'Epsilon(1,2,3,-2)*P(-2,3)*P(-1,1)*P(-1,2) + Epsilon(1,2,3,-2)*P(-2,2)*P(-1,1)*P(-1,3) + Epsilon(1,2,3,-2)*P(-2,1)*P(-1,2)*P(-1,3) - Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,1)*P(1,2) - Epsilon(2,3,-1,-2)*P(-2,2)*P(-1,1)*P(1,3) + Epsilon(1,3,-1,-2)*P(-2,3)*P(-1,2)*P(2,1) - Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*P(2,3) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*P(3,1) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*P(3,2) + Epsilon(3,-1,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*Metric(1,2) + Epsilon(2,-1,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*Metric(1,3) + Epsilon(1,-1,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*Metric(2,3)')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

SSSS2 = Lorentz(name = 'SSSS2',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)*P(-1,2) + P(-1,1)*P(-1,3) + P(-1,2)*P(-1,3) + P(-1,1)*P(-1,4) + P(-1,2)*P(-1,4) + P(-1,3)*P(-1,4)')

SSSS3 = Lorentz(name = 'SSSS3',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)**2 + (2*P(-1,1)*P(-1,2))/3. + P(-1,2)**2 + (2*P(-1,1)*P(-1,3))/3. + (2*P(-1,2)*P(-1,3))/3. + P(-1,3)**2 + (2*P(-1,1)*P(-1,4))/3. + (2*P(-1,2)*P(-1,4))/3. + (2*P(-1,3)*P(-1,4))/3. + P(-1,4)**2')

FFSS1 = Lorentz(name = 'FFSS1',
                spins = [ 2, 2, 1, 1 ],
                structure = 'ProjM(2,1)')

FFSS2 = Lorentz(name = 'FFSS2',
                spins = [ 2, 2, 1, 1 ],
                structure = 'ProjP(2,1)')

FFFF1 = Lorentz(name = 'FFFF1',
                spins = [ 2, 2, 2, 2 ],
                structure = 'ProjM(2,3)*ProjM(4,1)')

FFFF2 = Lorentz(name = 'FFFF2',
                spins = [ 2, 2, 2, 2 ],
                structure = 'ProjM(2,1)*ProjM(4,3)')

FFFF3 = Lorentz(name = 'FFFF3',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjM(-3,1)*ProjM(-2,3)')

FFFF4 = Lorentz(name = 'FFFF4',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjM(-3,3)*ProjM(-2,1)')

FFFF5 = Lorentz(name = 'FFFF5',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-2,-4,-3)*Gamma(-2,2,-6)*Gamma(-1,-6,-5)*Gamma(-1,4,-4)*ProjM(-5,1)*ProjM(-3,3)')

FFFF6 = Lorentz(name = 'FFFF6',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-2,-4,-3)*Gamma(-2,4,-6)*Gamma(-1,-6,-5)*Gamma(-1,2,-4)*ProjM(-5,3)*ProjM(-3,1)')

FFFF7 = Lorentz(name = 'FFFF7',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-2,-6,-5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Gamma(-1,4,-6)*ProjM(-5,3)*ProjM(-3,1)')

FFFF8 = Lorentz(name = 'FFFF8',
                spins = [ 2, 2, 2, 2 ],
                structure = 'ProjM(4,3)*ProjP(2,1)')

FFFF9 = Lorentz(name = 'FFFF9',
                spins = [ 2, 2, 2, 2 ],
                structure = 'ProjP(2,3)*ProjP(4,1)')

FFFF10 = Lorentz(name = 'FFFF10',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'ProjM(2,1)*ProjP(4,3)')

FFFF11 = Lorentz(name = 'FFFF11',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'ProjP(2,1)*ProjP(4,3)')

FFFF12 = Lorentz(name = 'FFFF12',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-1,2,-3)*Gamma(-1,4,-2)*ProjM(-2,3)*ProjP(-3,1)')

FFFF13 = Lorentz(name = 'FFFF13',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjM(-2,3)*ProjP(-3,1)')

FFFF14 = Lorentz(name = 'FFFF14',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjP(-3,1)*ProjP(-2,3)')

FFFF15 = Lorentz(name = 'FFFF15',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-1,2,-3)*Gamma(-1,4,-2)*ProjM(-2,1)*ProjP(-3,3)')

FFFF16 = Lorentz(name = 'FFFF16',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjM(-2,1)*ProjP(-3,3)')

FFFF17 = Lorentz(name = 'FFFF17',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjP(-3,3)*ProjP(-2,1)')

FFFF18 = Lorentz(name = 'FFFF18',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-2,-4,-3)*Gamma(-2,2,-6)*Gamma(-1,-6,-5)*Gamma(-1,4,-4)*ProjP(-5,1)*ProjP(-3,3)')

FFFF19 = Lorentz(name = 'FFFF19',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-2,-4,-3)*Gamma(-2,4,-6)*Gamma(-1,-6,-5)*Gamma(-1,2,-4)*ProjP(-5,3)*ProjP(-3,1)')

FFFF20 = Lorentz(name = 'FFFF20',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-2,-6,-5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Gamma(-1,4,-6)*ProjP(-5,3)*ProjP(-3,1)')

FFVS1 = Lorentz(name = 'FFVS1',
                spins = [ 2, 2, 3, 1 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFVS2 = Lorentz(name = 'FFVS2',
                spins = [ 2, 2, 3, 1 ],
                structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1)')

FFVS3 = Lorentz(name = 'FFVS3',
                spins = [ 2, 2, 3, 1 ],
                structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

FFVS4 = Lorentz(name = 'FFVS4',
                spins = [ 2, 2, 3, 1 ],
                structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVV1 = Lorentz(name = 'FFVV1',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1)')

FFVV2 = Lorentz(name = 'FFVV2',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)')

VVSS2 = Lorentz(name = 'VVSS2',
                spins = [ 3, 3, 1, 1 ],
                structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVSS3 = Lorentz(name = 'VVSS3',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVSS4 = Lorentz(name = 'VVSS4',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVVS1 = Lorentz(name = 'VVVS1',
                spins = [ 3, 3, 3, 1 ],
                structure = '-(Epsilon(1,2,3,-1)*P(-1,1))')

VVVS2 = Lorentz(name = 'VVVS2',
                spins = [ 3, 3, 3, 1 ],
                structure = '-(Epsilon(1,2,3,-1)*P(-1,3))')

VVVS3 = Lorentz(name = 'VVVS3',
                spins = [ 3, 3, 3, 1 ],
                structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) - Epsilon(1,2,3,-1)*P(-1,2) - Epsilon(1,2,3,-1)*P(-1,3)')

VVVS4 = Lorentz(name = 'VVVS4',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,1)*Metric(1,2) - P(2,1)*Metric(1,3)')

VVVS5 = Lorentz(name = 'VVVS5',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(2,3)*Metric(1,3) - P(1,3)*Metric(2,3)')

VVVS6 = Lorentz(name = 'VVVS6',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(3,2)*P(4,1)*Metric(1,2) - P(3,1)*P(4,2)*Metric(1,2) + P(2,1)*P(4,2)*Metric(1,3) + P(2,4)*P(4,3)*Metric(1,3) - P(2,1)*P(3,2)*Metric(1,4) - P(2,3)*P(3,4)*Metric(1,4) - P(1,2)*P(4,1)*Metric(2,3) - P(1,4)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,2)*Metric(1,4)*Metric(2,3) + P(-1,3)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,2)*P(3,1)*Metric(2,4) + P(1,3)*P(3,4)*Metric(2,4) - P(-1,1)*P(-1,2)*Metric(1,3)*Metric(2,4) - P(-1,3)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,4)*P(2,3)*Metric(3,4) - P(1,3)*P(2,4)*Metric(3,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = '2*Epsilon(1,2,3,4)*P(-1,2)*P(-1,3) + 2*Epsilon(1,2,3,4)*P(-1,1)*P(-1,4) - 2*Epsilon(2,3,4,-1)*P(-1,3)*P(1,2) - 2*Epsilon(2,3,4,-1)*P(-1,2)*P(1,3) + 2*Epsilon(2,3,4,-1)*P(-1,1)*P(1,4) + 2*Epsilon(1,3,4,-1)*P(-1,4)*P(2,1) - 2*Epsilon(1,3,4,-1)*P(-1,2)*P(2,3) + 2*Epsilon(1,3,4,-1)*P(-1,1)*P(2,4) - 2*Epsilon(1,2,4,-1)*P(-1,4)*P(3,1) + 2*Epsilon(1,2,4,-1)*P(-1,3)*P(3,2) - 2*Epsilon(1,2,4,-1)*P(-1,1)*P(3,4) - 2*Epsilon(1,2,3,-1)*P(-1,4)*P(4,1) + 2*Epsilon(1,2,3,-1)*P(-1,3)*P(4,2) + 2*Epsilon(1,2,3,-1)*P(-1,2)*P(4,3) - Epsilon(3,4,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(1,2) - Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,2) + Epsilon(2,4,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,3) + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(1,3) - Epsilon(2,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(1,3) - Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,3) + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,4) + Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(2,3) - Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(2,3) + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(2,4) + Epsilon(1,3,-1,-2)*P(-2,3)*P(-1,2)*Metric(2,4) - Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,3)*Metric(2,4) - Epsilon(1,3,-1,-2)*P(-2,1)*P(-1,4)*Metric(2,4) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*Metric(3,4) - Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,3)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,4)*Metric(3,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = '-2*Epsilon(1,2,3,4)*P(-1,1)*P(-1,3) - 2*Epsilon(1,2,3,4)*P(-1,2)*P(-1,4) + 2*Epsilon(2,3,4,-1)*P(-1,4)*P(1,2) - 2*Epsilon(2,3,4,-1)*P(-1,1)*P(1,3) + 2*Epsilon(2,3,4,-1)*P(-1,2)*P(1,4) - 2*Epsilon(1,3,4,-1)*P(-1,3)*P(2,1) - 2*Epsilon(1,3,4,-1)*P(-1,1)*P(2,3) + 2*Epsilon(1,3,4,-1)*P(-1,2)*P(2,4) - 2*Epsilon(1,2,4,-1)*P(-1,3)*P(3,1) + 2*Epsilon(1,2,4,-1)*P(-1,4)*P(3,2) + 2*Epsilon(1,2,4,-1)*P(-1,2)*P(3,4) - 2*Epsilon(1,2,3,-1)*P(-1,3)*P(4,1) + 2*Epsilon(1,2,3,-1)*P(-1,4)*P(4,2) - 2*Epsilon(1,2,3,-1)*P(-1,1)*P(4,3) + Epsilon(3,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,2) - Epsilon(3,4,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,2) - Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,2) + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,3) - Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,3) + Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,4) + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,4) + Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(2,3) + Epsilon(1,4,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,3) - Epsilon(1,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(2,3) - Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,3) + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,4) - Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,4) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,3)*Metric(3,4) - Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,4)*Metric(3,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = '-(Epsilon(1,2,3,4)*P(-1,1)*P(-1,3)) + Epsilon(1,2,3,4)*P(-1,2)*P(-1,3) + Epsilon(1,2,3,4)*P(-1,1)*P(-1,4) - Epsilon(1,2,3,4)*P(-1,2)*P(-1,4) - Epsilon(2,3,4,-1)*P(-1,3)*P(1,2) + Epsilon(2,3,4,-1)*P(-1,4)*P(1,2) - Epsilon(2,3,4,-1)*P(-1,1)*P(1,3) - Epsilon(2,3,4,-1)*P(-1,2)*P(1,3) + Epsilon(2,3,4,-1)*P(-1,1)*P(1,4) + Epsilon(2,3,4,-1)*P(-1,2)*P(1,4) - Epsilon(1,3,4,-1)*P(-1,3)*P(2,1) + Epsilon(1,3,4,-1)*P(-1,4)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,1)*P(2,3) - Epsilon(1,3,4,-1)*P(-1,2)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,1)*P(2,4) + Epsilon(1,3,4,-1)*P(-1,2)*P(2,4) - Epsilon(1,2,4,-1)*P(-1,3)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,4)*P(3,1) + Epsilon(1,2,4,-1)*P(-1,3)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,4)*P(3,2) - Epsilon(1,2,4,-1)*P(-1,1)*P(3,4) + Epsilon(1,2,4,-1)*P(-1,2)*P(3,4) - Epsilon(1,2,3,-1)*P(-1,3)*P(4,1) - Epsilon(1,2,3,-1)*P(-1,4)*P(4,1) + Epsilon(1,2,3,-1)*P(-1,3)*P(4,2) + Epsilon(1,2,3,-1)*P(-1,4)*P(4,2) - Epsilon(1,2,3,-1)*P(-1,1)*P(4,3) + Epsilon(1,2,3,-1)*P(-1,2)*P(4,3) + Epsilon(3,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,2) - Epsilon(3,4,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(1,2) - Epsilon(3,4,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,2) + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,3) + Epsilon(2,4,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,3) + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(1,3) + Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,4) + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,4) + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,4) + Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(2,3) + Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(2,3) + Epsilon(1,4,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,3) + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(2,4) + Epsilon(1,3,-1,-2)*P(-2,3)*P(-1,2)*Metric(2,4) + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,4) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*Metric(3,4) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*Metric(3,4)')

VVVV6 = Lorentz(name = 'VVVV6',
                spins = [ 3, 3, 3, 3 ],
                structure = '2*Epsilon(1,2,3,4)*P(-1,1)*P(-1,2) + 2*Epsilon(1,2,3,4)*P(-1,3)*P(-1,4) + 2*Epsilon(2,3,4,-1)*P(-1,1)*P(1,2) - 2*Epsilon(2,3,4,-1)*P(-1,4)*P(1,3) - 2*Epsilon(2,3,4,-1)*P(-1,3)*P(1,4) - 2*Epsilon(1,3,4,-1)*P(-1,2)*P(2,1) + 2*Epsilon(1,3,4,-1)*P(-1,4)*P(2,3) + 2*Epsilon(1,3,4,-1)*P(-1,3)*P(2,4) - 2*Epsilon(1,2,4,-1)*P(-1,2)*P(3,1) - 2*Epsilon(1,2,4,-1)*P(-1,1)*P(3,2) + 2*Epsilon(1,2,4,-1)*P(-1,3)*P(3,4) + 2*Epsilon(1,2,3,-1)*P(-1,2)*P(4,1) + 2*Epsilon(1,2,3,-1)*P(-1,1)*P(4,2) - 2*Epsilon(1,2,3,-1)*P(-1,4)*P(4,3) + Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,2) - Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,2) + Epsilon(2,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,3) - Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,3) - Epsilon(2,4,-1,-2)*P(-2,4)*P(-1,3)*Metric(1,3) + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,4)*Metric(1,3) - Epsilon(2,3,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,4) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(1,4) + Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,4)*Metric(1,4) + Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,3) - Epsilon(1,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(2,3) + Epsilon(1,4,-1,-2)*P(-2,4)*P(-1,3)*Metric(2,3) - Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,4)*Metric(2,3) - Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,4) + Epsilon(1,3,-1,-2)*P(-2,1)*P(-1,2)*Metric(2,4) + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(2,4) - Epsilon(1,3,-1,-2)*P(-2,3)*P(-1,4)*Metric(2,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,3)*Metric(3,4) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,4)*Metric(3,4)')

VVVV7 = Lorentz(name = 'VVVV7',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Epsilon(1,2,3,4)*P(-1,1)*P(-1,2) - Epsilon(1,2,3,4)*P(-1,1)*P(-1,3) - Epsilon(1,2,3,4)*P(-1,2)*P(-1,4) + Epsilon(1,2,3,4)*P(-1,3)*P(-1,4) + Epsilon(2,3,4,-1)*P(-1,1)*P(1,2) + Epsilon(2,3,4,-1)*P(-1,4)*P(1,2) - Epsilon(2,3,4,-1)*P(-1,1)*P(1,3) - Epsilon(2,3,4,-1)*P(-1,4)*P(1,3) + Epsilon(2,3,4,-1)*P(-1,2)*P(1,4) - Epsilon(2,3,4,-1)*P(-1,3)*P(1,4) - Epsilon(1,3,4,-1)*P(-1,2)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,3)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,1)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,4)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,2)*P(2,4) + Epsilon(1,3,4,-1)*P(-1,3)*P(2,4) - Epsilon(1,2,4,-1)*P(-1,2)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,3)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,1)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,4)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,2)*P(3,4) + Epsilon(1,2,4,-1)*P(-1,3)*P(3,4) + Epsilon(1,2,3,-1)*P(-1,2)*P(4,1) - Epsilon(1,2,3,-1)*P(-1,3)*P(4,1) + Epsilon(1,2,3,-1)*P(-1,1)*P(4,2) + Epsilon(1,2,3,-1)*P(-1,4)*P(4,2) - Epsilon(1,2,3,-1)*P(-1,1)*P(4,3) - Epsilon(1,2,3,-1)*P(-1,4)*P(4,3) + Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,2) - Epsilon(3,4,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,2) + Epsilon(2,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,3) + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,3) - Epsilon(2,4,-1,-2)*P(-2,4)*P(-1,3)*Metric(1,3) - Epsilon(2,3,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,4) + Epsilon(2,3,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,4) + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(1,4) + Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,3) + Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(2,3) + Epsilon(1,4,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,3) + Epsilon(1,4,-1,-2)*P(-2,4)*P(-1,3)*Metric(2,3) - Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,4) + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,4) + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(2,4) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,3)*Metric(3,4)')

VVVV8 = Lorentz(name = 'VVVV8',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV9 = Lorentz(name = 'VVVV9',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV10 = Lorentz(name = 'VVVV10',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV11 = Lorentz(name = 'VVVV11',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVVV12 = Lorentz(name = 'VVVV12',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,4)*P(4,1)*Metric(1,2) + P(3,2)*P(4,3)*Metric(1,2) - P(2,4)*P(4,1)*Metric(1,3) - P(2,3)*P(4,2)*Metric(1,3) + P(2,4)*P(3,1)*Metric(1,4) - P(2,1)*P(3,4)*Metric(1,4) + P(1,3)*P(4,2)*Metric(2,3) - P(1,2)*P(4,3)*Metric(2,3) - P(1,4)*P(3,1)*Metric(2,4) - P(1,3)*P(3,2)*Metric(2,4) + P(-1,2)*P(-1,3)*Metric(1,3)*Metric(2,4) + P(-1,1)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,4)*P(2,1)*Metric(3,4) + P(1,2)*P(2,3)*Metric(3,4) - P(-1,2)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,1)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVV13 = Lorentz(name = 'VVVV13',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(1,3)*P(4,1)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVV14 = Lorentz(name = 'VVVV14',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,2)*P(4,1)*Metric(1,2) - P(3,1)*P(4,2)*Metric(1,2) + P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) + P(2,1)*P(4,2)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) + P(2,4)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) - P(2,1)*P(3,2)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(2,3)*P(3,4)*Metric(1,4) - P(1,2)*P(4,1)*Metric(2,3) - P(1,3)*P(4,1)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) - P(1,4)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,2)*Metric(1,4)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(-1,3)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,2)*P(3,1)*Metric(2,4) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(1,3)*P(3,4)*Metric(2,4) - P(-1,1)*P(-1,2)*Metric(1,3)*Metric(2,4) - P(-1,3)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,4)*P(2,3)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(1,3)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVV15 = Lorentz(name = 'VVVV15',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,4)*P(4,1)*Metric(1,2) + P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(3,2)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) - P(2,4)*P(4,1)*Metric(1,3) - P(2,3)*P(4,2)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) + P(2,4)*P(3,1)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(2,1)*P(3,4)*Metric(1,4) - P(1,3)*P(4,1)*Metric(2,3) + P(1,3)*P(4,2)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) - P(1,2)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) - P(1,4)*P(3,1)*Metric(2,4) - P(1,3)*P(3,2)*Metric(2,4) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(-1,2)*P(-1,3)*Metric(1,3)*Metric(2,4) + P(-1,1)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,4)*P(2,1)*Metric(3,4) + P(1,2)*P(2,3)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,1)*P(-1,4)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

