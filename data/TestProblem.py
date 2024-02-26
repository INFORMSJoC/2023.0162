from __future__ import division
'''
This file contains the definitions of several benchmark problems from the
COCONUT Benchmark Library. The Problems are implemented as objects of the
OptimizationProblem class, defined in OptimizationProblem.py.

Problem names are as defined in the COCONUT benchmark.
'''
################################################################################
# Necessary imports are specified here
################################################################################

from OptimizationProblem import OptimizationProblem
from Ineqtransformation import *
import numpy as np
import sympy as sym

################################################################################
# Initialize the symbols that are used in the functions definitions
################################################################################

x1 = sym.Symbol('x1')
x2 = sym.Symbol('x2')
x3 = sym.Symbol('x3')
x4 = sym.Symbol('x4')
x5 = sym.Symbol('x5')
x6 = sym.Symbol('x6')
x7 = sym.Symbol('x7')
x8 = sym.Symbol('x8')
x9 = sym.Symbol('x9')
x10 = sym.Symbol('x10')

x11 = sym.Symbol('x11')
x12 = sym.Symbol('x12')
x13 = sym.Symbol('x13')
x14 = sym.Symbol('x14')
x15 = sym.Symbol('x15')
x16 = sym.Symbol('x16')
x17 = sym.Symbol('x17')
x18 = sym.Symbol('x18')
x19 = sym.Symbol('x19')
x20 = sym.Symbol('x20')

x21 = sym.Symbol('x21')
x22 = sym.Symbol('x22')
x23 = sym.Symbol('x23')
x24 = sym.Symbol('x24')
x25 = sym.Symbol('x25')
x26 = sym.Symbol('x26')
x27 = sym.Symbol('x27')
x28 = sym.Symbol('x28')
x29 = sym.Symbol('x29')
x30 = sym.Symbol('x30')

x31 = sym.Symbol('x31')
x32 = sym.Symbol('x32')
x33 = sym.Symbol('x33')
x34 = sym.Symbol('x34')
x35 = sym.Symbol('x35')
x36 = sym.Symbol('x36')
x37 = sym.Symbol('x37')
x38 = sym.Symbol('x38')
x39 = sym.Symbol('x39')
x40 = sym.Symbol('x40')

x41 = sym.Symbol('x41')
x42 = sym.Symbol('x42')
x43 = sym.Symbol('x43')
x44 = sym.Symbol('x44')
x45 = sym.Symbol('x45')
x46 = sym.Symbol('x46')
x47 = sym.Symbol('x47')
x48 = sym.Symbol('x48')
x49 = sym.Symbol('x49')
x50 = sym.Symbol('x50')

x51 = sym.Symbol('x51')
x52 = sym.Symbol('x52')
x53 = sym.Symbol('x53')
x54 = sym.Symbol('x54')
x55 = sym.Symbol('x55')
x56 = sym.Symbol('x56')
x57 = sym.Symbol('x57')
x58 = sym.Symbol('x58')
x59 = sym.Symbol('x59')
x60 = sym.Symbol('x60')

x61 = sym.Symbol('x61')
x62 = sym.Symbol('x62')
x63 = sym.Symbol('x63')
x64 = sym.Symbol('x64')
x65 = sym.Symbol('x65')
x66 = sym.Symbol('x66')
x67 = sym.Symbol('x67')
x68 = sym.Symbol('x68')
x69 = sym.Symbol('x69')
x70 = sym.Symbol('x70')

x71 = sym.Symbol('x71')
x72 = sym.Symbol('x72')
x73 = sym.Symbol('x73')
x74 = sym.Symbol('x74')
x75 = sym.Symbol('x75')
x76 = sym.Symbol('x76')
x77 = sym.Symbol('x77')
x78 = sym.Symbol('x78')
x79 = sym.Symbol('x79')
x80 = sym.Symbol('x80')

################################################################################
# Problems
################################################################################
symobj_extrasim = x1 + 1
sol_extrasim = np.array([0., 1.])
eq1_extrasim = x1 + 2 * x2 - 2
cons_extrasim = [{'func':eq1_extrasim, 'type':'eq', 'prop':'convex'}]
vars_extrasim = [x1, x2]
bnds_extrasim = [np.array([0, 10000]), np.array([-10000, 10000])]
extrasim = OptimizationProblem('extrasim', sol_extrasim, symobj_extrasim, cons_extrasim, vars_extrasim, bnds_extrasim)

symobj_hs006 = (1-x1)**2
sol_hs006 = np.array([1., 1.])
eq1_hs006 = 10*(x2 - x1**2)
cons_hs006 = [{'func':eq1_hs006, 'type':'eq', 'prop':'non-convex'}]
vars_hs006 = [x1, x2]
bnds_hs006 = [np.array([-10000, 10000]), np.array([-10000, 10000])]
hs006 = OptimizationProblem('hs006', sol_hs006, symobj_hs006, cons_hs006, vars_hs006, bnds_hs006)

symobj_maratos = -x1 + 9.9999999999999995e-07 * x1**2 + 9.9999999999999995e-07 * x2**2 - 9.9999999999999995e-07
sol_maratos = np.array([1., -1.72277e-06])
eq1_maratos = x1**2 + x2**2 - 1
cons_maratos = [{'func':eq1_maratos, 'type':'eq', 'prop':'non-convex'}]
vars_maratos = [x1, x2]
bnds_maratos = [np.array([-10000, 10000]), np.array([-10000, 10000])]
maratos = OptimizationProblem('maratos', sol_maratos, symobj_maratos, cons_maratos, vars_maratos, bnds_maratos)

symobj_tame = (x1 - x2)**2
sol_tame = np.array([0.5, 0.5])
eq1_tame = x1 + x2 - 1
cons_tame = [{'func':eq1_tame, 'type':'eq', 'prop':'convex'}]
vars_tame = [x1, x2]
bnds_tame = [np.array([0, 10000]), np.array([0, 10000])]
tame = OptimizationProblem('tame', sol_tame, symobj_tame, cons_tame, vars_tame, bnds_tame)

symobj_b1 = 0
sol_b1 = np.array([0.5, 1.65139, -1, -0.151388])
eq1_b1 = x1 + x2 + x3 + x4 - 1
eq2_b1 = 2*x3 + 2
eq3_b1 = 2*x1 - 1
eq4_b1 = x1**2 + x2**2 + x3**2 + x4**2 - 4
cons_b1 = [{'func':eq1_b1, 'type':'eq', 'prop':'convex'}, {'func':eq2_b1, 'type':'eq', 'prop':'convex'}, {'func':eq3_b1, 'type':'eq', 'prop':'convex'}, {'func':eq4_b1, 'type':'eq', 'prop':'unknown'}]
vars_b1 = [x1, x2, x3, x4]
bnds_b1 = [np.array([-10, 10]), np.array([-10, 10]), np.array([-10, 10]), np.array([-10, 10])]
b1 = OptimizationProblem('b1', sol_b1, symobj_b1, cons_b1, vars_b1, bnds_b1)

symobj_gottfr = 0
sol_gottfr = np.array([1.15592e-07, 2.56387e-07])
eq1_gottfr = x1 - ((- x1) + 1) * (0.11360000000000001 * x1 + 0.34079999999999999 * x2)
eq2_gottfr = x2 + ((- x2) + 1) * (15 * x1 - 7.5 * x1)
cons_gottfr = [{'func':eq1_gottfr, 'type':'eq', 'prop':'unknown'}, {'func':eq2_gottfr, 'type':'eq', 'prop':'unknown'}]
vars_gottfr = [x1, x2]
bnds_gottfr = [np.array([-10001, 10000]), np.array([-10001, 10000])]
gottfr = OptimizationProblem('gottfr', sol_gottfr, symobj_gottfr, cons_gottfr, vars_gottfr, bnds_gottfr)

symobj_himmelbc = 0
sol_himmelbc = np.array([3, 2])
eq1_himmelbc = x2 + x1**2 - 11
eq2_himmelbc = x1 + x2**2 - 7
cons_himmelbc = [{'func':eq1_himmelbc, 'type':'eq', 'prop':'unknown'}, {'func':eq2_himmelbc, 'type':'eq', 'prop':'unknown'}]
vars_himmelbc = [x1, x2]
bnds_himmelbc = [np.array([-10001, 10000]), np.array([-10001, 10000])]
himmelbc = OptimizationProblem('himmelbc', sol_himmelbc, symobj_himmelbc, cons_himmelbc, vars_himmelbc, bnds_himmelbc)

symobj_hypcir = 0
sol_hypcir = np.array([1.93185, 0.517638])
eq1_hypcir = x1 * x2 - 1
eq2_hypcir = x1**2 + x2**2 - 4
cons_hypcir = [{'func':eq1_hypcir, 'type':'eq', 'prop':'unknown'}, {'func':eq2_hypcir, 'type':'eq', 'prop':'unknown'}]
vars_hypcir = [x1, x2]
bnds_hypcir = [np.array([-10001, 10000]), np.array([-10001, 10000])]
hypcir = OptimizationProblem('hypcir', sol_hypcir, symobj_hypcir, cons_hypcir, vars_hypcir, bnds_hypcir)

symobj_hs8 = 0
sol_hs8 = np.array([4.60159,1.95584])
eq1_hs8 = (x1**2) + (x2**2) - 25
eq2_hs8 = x1 * x2 - 9
cons_hs8 = [{'func':eq1_hs8,'type': 'eq', 'prop':'unknown'},{'func':eq2_hs8,'type': 'eq', 'prop':'unknown'}]
bnds_hs8 = [np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_hs8 = [x1, x2]
hs8 = OptimizationProblem("hs8", sol_hs8, symobj_hs8, cons_hs8, vars_hs8, bnds_hs8)

symobj_hs008 = 0
sol_hs008 = np.array([4.6015949177, 1.9558436066])
eq1_hs008 = x1**2 + x2**2 - 25
eq2_hs008 = x1 * x2 - 9
cons_hs008 = [{'func':eq1_hs008, 'type':'eq', 'prop':'unknown'}, {'func':eq2_hs008, 'type':'eq', 'prop':'unknown'}]
vars_hs008 = [x1, x2]
bnds_hs008 = [np.array([-10001, 10000]), np.array([-10001, 10000])]
hs008 = OptimizationProblem('hs008', sol_hs008, symobj_hs008, cons_hs008, vars_hs008, bnds_hs008)

symobj_mickey = 0
sol_mickey = np.array([1.23607, 0.786151])
eq1_mickey = x1**2 + 4 * x2**2 - 4
eq2_mickey = -x1 + 2 * x2**2
cons_mickey = [{'func':eq1_mickey, 'type':'eq', 'prop':'unknown'}, {'func':eq2_mickey, 'type':'eq', 'prop':'unknown'}]
vars_mickey = [x1, x2]
bnds_mickey = [np.array([-10000, 10000]), np.array([-10000, 10000])]
mickey = OptimizationProblem('mickey', sol_mickey, symobj_mickey, cons_mickey, vars_mickey, bnds_mickey)

symobj_parabola = x1
sol_parabola = np.array([1., 1.])
eq1_parabola = x1**2 - x2
eq2_parabola = x2**2 + x1**2 - 2
cons_parabola = [{'func':eq1_parabola, 'type':'eq', 'prop':'unknown'}, {'func':eq2_parabola, 'type':'eq', 'prop':'unknown'}]
vars_parabola = [x1, x2]
bnds_parabola = [np.array([0, 10]), np.array([0, 2])]
parabola = OptimizationProblem('parabola', sol_parabola, symobj_parabola, cons_parabola, vars_parabola, bnds_parabola)

symobj_precondk = 0
sol_precondk = np.array([1, 0])
eq1_precondk = (x1**2) - (x2**2) - 1
eq2_precondk = x1 * x2 - 0
cons_precondk = [{'func':eq1_precondk,'type': 'eq', 'prop':'unknown'},{'func':eq2_precondk,'type': 'eq', 'prop':'unknown'}]
bnds_precondk = [np.array([0.90000000000000002, 1.2]), np.array([-0.10000000000000001, 0.10000000000000001])]
vars_precondk = [x1, x2]
precondk = OptimizationProblem("precondk", sol_precondk, symobj_precondk, cons_precondk, vars_precondk, bnds_precondk)

symobj_supersim = 0
sol_supersim = np.array([0.666667, 0.666667])
eq1_supersim = 2 * x1 + x2 - 2
eq2_supersim = x1 + 2 * x2 - 2
cons_supersim = [{'func':eq1_supersim, 'type':'eq', 'prop':'convex'}, {'func':eq2_supersim, 'type':'eq', 'prop':'convex'}]
vars_supersim = [x1, x2]
bnds_supersim = [np.array([0, 10000]), np.array([-10000, 10000])]
supersim = OptimizationProblem('supersim', sol_supersim, symobj_supersim, cons_supersim, vars_supersim, bnds_supersim)

symobj_booth = 0
sol_booth = np.array([1., 3.])
ineq1_booth = (x1 + 2 * x2 - 7)**2 + (2 * x1 + x2 - 5)**2 - 1
cons_booth = [{'func':ineq1_booth, 'type':'ineq', 'prop':'unknown'}]
vars_booth = [x1, x2]
bnds_booth = [np.array([-10000, 10000]), np.array([-10000, 10000])]
booth = OptimizationProblem('booth', sol_booth, symobj_booth, cons_booth, vars_booth, bnds_booth)

symobj_hs011 = (x2**2) + ((x1) - 5)**2 - 25
sol_hs011 = np.array([1.2347728250,1.5246639295])
ineq1_hs011 = -x2 + (x1**2) - 0
cons_hs011 = [{'func':ineq1_hs011,'type': 'ineq', 'prop':'unknown'}]
bnds_hs011 = [np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_hs011 = [x1, x2]
hs011 = OptimizationProblem("hs011", sol_hs011, symobj_hs011, cons_hs011, vars_hs011, bnds_hs011)

symobj_hs012 = (-7) * x1 - 7 * x2 + (x2**2) + 0.5 * (x1**2) - x1 * x2
sol_hs012 = np.array([2, 3])
ineq1_hs012 = (x2**2) + 4 * (x1**2) - 25
cons_hs012 = [{'func':ineq1_hs012,'type': 'ineq'}]
bnds_hs012 = [np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_hs012 = [x1, x2]
hs012 = OptimizationProblem("hs012", sol_hs012, symobj_hs012, cons_hs012, vars_hs012, bnds_hs012)

symobj_hs6 = 0
sol_hs6 = np.array([0.781875, 0.611328])
eq1_hs6 = 10 * x2 - 10 * x1**2
ineq1_hs6 = (-x1 + 1)**2 - 1
cons_hs6 = [{'func':eq1_hs6, 'type':'eq', 'prop':'unknown'}, {'func':ineq1_hs6, 'type':'ineq', 'prop':'unknown'}]
vars_hs6 = [x1, x2]
bnds_hs6 = [np.array([-10000, 10000]), np.array([-10000, 10000])]
hs6 = OptimizationProblem('hs6', sol_hs6, symobj_hs6, cons_hs6, vars_hs6, bnds_hs6)

symobj_tryb = (x1 - 1)**2
sol_tryb = np.array([1, 9])
eq1_tryb = (x1 - 1)**2 + (x2 - 10)**2 - 1
ineq1_tryb = (x1 - 1)**2 - 2
cons_tryb = [{'func':eq1_tryb, 'type':'eq', 'prop':'unknown'}, {'func':ineq1_tryb, 'type':'ineq', 'prop':'unknown'}]
vars_tryb = [x1, x2]
bnds_tryb = [np.array([0, 10000]), np.array([0, 10000])]
tryb = OptimizationProblem('tryb', sol_tryb, symobj_tryb, cons_tryb, vars_tryb, bnds_tryb)

symobj_hs022 = ((x1) - 2)**2 + ((x2) - 1)**2
sol_hs022 = np.array([1, 1])
ineq1_hs022 = x1 + x2 - 2
ineq2_hs022 = -(x2 - (x1**2))
cons_hs022 = [{'func':ineq1_hs022,'type': 'ineq', 'prop':'unknown'},{'func':ineq2_hs022,'type': 'ineq', 'prop':'unknown'}]
bnds_hs022 = [np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_hs022 = [x1, x2]
hs022 = OptimizationProblem("hs022", sol_hs022, symobj_hs022, cons_hs022, vars_hs022, bnds_hs022)

symobj_simpllpa = 2 * x1 + x2
sol_simpllpa = np.array([0, 1])
ineq1_simpllpa = -(x1 + 2 * x2) + 1.5
ineq2_simpllpa = -(x1 + x2) + 1
cons_simpllpa = [{'func':ineq1_simpllpa,'type': 'ineq', 'prop':'convex'},{'func':ineq2_simpllpa,'type': 'ineq', 'prop':'convex'}]
bnds_simpllpa = [np.array([0, 10000]), np.array([0, 10000])]
vars_simpllpa = [x1, x2]
simpllpa = OptimizationProblem("simpllpa", sol_simpllpa, symobj_simpllpa, cons_simpllpa, vars_simpllpa, bnds_simpllpa)

symobj_zecevic3 = (-84) * x1 - 24 * x2 + 7 * (x1**2) + 3 * (x2**2) + 300
sol_zecevic3 = np.array([2.7955451851,1.0885437701])
ineq1_zecevic3 = (x1**2) + (x2**2) - 9
ineq2_zecevic3 = - x1 * x2 + 1
cons_zecevic3 = [{'func':ineq1_zecevic3,'type': 'ineq', 'prop':'convex'},{'func':ineq2_zecevic3,'type': 'ineq', 'prop':'convex'}]
bnds_zecevic3 = [np.array([0, 10]), np.array([0, 10])]
vars_zecevic3 = [x1, x2]
zecevic3 = OptimizationProblem("zecevic3", sol_zecevic3, symobj_zecevic3, cons_zecevic3, vars_zecevic3, bnds_zecevic3)

symobj_zecevic4 = (-60) * x1 - 8 * x2 + (x2**2) + 6 * (x1**2) + 166
sol_zecevic4 = np.array([4.9709528802,1.2518287248])
ineq1_zecevic4 = -x1 - x2 - -3
ineq2_zecevic4 = -x1 - x2 + x1 * x2 - 0
cons_zecevic4 = [{'func':ineq1_zecevic4,'type': 'ineq', 'prop':'convex'},{'func':ineq2_zecevic4,'type': 'ineq', 'prop':'unknown'}]
bnds_zecevic4 = [np.array([0, 10]), np.array([0, 10])]
vars_zecevic4 = [x1, x2]
zecevic4 = OptimizationProblem("zecevic4", sol_zecevic4, symobj_zecevic4, cons_zecevic4, vars_zecevic4, bnds_zecevic4)

symobj_simpllpb = 1.5 * x1 + x2
sol_simpllpb = np.array([0.2, 0.8, 1.1])
ineq1_simpllpb = -x1 - x2 + 1
ineq2_simpllpb = -x1 - 2 * x2 + 1.2
ineq3_simpllpb = -2*x1 - x2 + 1.2
cons_simpllpb = [{'func':ineq1_simpllpb,'type': 'ineq', 'prop':'convex'},{'func':ineq2_simpllpb,'type': 'ineq', 'prop':'convex'},{'func':ineq3_simpllpb,'type': 'ineq', 'prop':'convex'}]
bnds_simpllpb = [np.array([0, 10000]), np.array([0, 10000])]
vars_simpllpb = [x1, x2]
simpllpb = OptimizationProblem("simpllpb", sol_simpllpb, symobj_simpllpb, cons_simpllpb, vars_simpllpb, bnds_simpllpb)

symobj_zecevic2 = 0
sol_zecevic2 = np.array([0.736017,1.05593])
ineq1_zecevic2 = 4 * x1 + x2 - 4
ineq2_zecevic2 = x1 + x2 - 2
ineq3_zecevic2 = (-3) * x1 - 2 * x2 + 2 * (x1**2) + 3.125
cons_zecevic2 = [{'func':ineq1_zecevic2,'type': 'ineq', 'prop':'convex'},{'func':ineq2_zecevic2,'type': 'ineq', 'prop':'convex'},{'func':ineq3_zecevic2,'type': 'ineq', 'prop':'unknown'}]
bnds_zecevic2 = [np.array([0, 10]), np.array([0, 10])]
vars_zecevic2 = [x1, x2]
zecevic2 = OptimizationProblem("zecevic2", sol_zecevic2, symobj_zecevic2, cons_zecevic2, vars_zecevic2, bnds_zecevic2)

symobj_aljazzaf = 50.005000000000003 * ((x1) + 1)**2 + 0.010000000000005116 * ((x2) - 1)**2 + 100 * (x3 - 0.5)**2
sol_aljazzaf = np.array([0., 0.9999999940, 0.9999990004])
eq1_aljazzaf = -x3 + 10000 * (x2 - 1)**2 + 5000.5 * (x1)**2 + 1
cons_aljazzaf = [{'func':eq1_aljazzaf, 'type':'eq', 'prop':'unknown'}]
vars_aljazzaf = [x1, x2, x3]
bnds_aljazzaf = [np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000])]
aljazzaf = OptimizationProblem('aljazzaf', sol_aljazzaf, symobj_aljazzaf, cons_aljazzaf, vars_aljazzaf, bnds_aljazzaf)

symobj_hs028 = (x1 + x2)**2 + (x2 + x3)**2
sol_hs028 = np.array([0.5, -0.5, 0.5])
eq1_hs028 = x1 + 2 * x2 + 3 * x3 - 1
cons_hs028 = [{'func':eq1_hs028, 'type':'eq', 'prop':'unknown'}]
vars_hs028 = [x1, x2, x3]
bnds_hs028 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
hs028 = OptimizationProblem('hs028', sol_hs028, symobj_hs028, cons_hs028, vars_hs028, bnds_hs028)

symobj_hs042 = ((x1) - 3)**2 + ((x2) - 4)**2 + ((2) - 1)**2 + ((x3) - 2)**2
sol_hs042 = np.array([0.84853,1.13137,2.00001])
eq1_hs042 = (x1**2) + (x2**2) - 2
cons_hs042 = [{'func':eq1_hs042,'type': 'eq', 'prop':'unknown'}]
bnds_hs042 = [np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000])]
vars_hs042 = [x1, x2, x3]
hs042 = OptimizationProblem("hs042", sol_hs042, symobj_hs042, cons_hs042, vars_hs042, bnds_hs042)

symobj_hs061 = 16 * x1 - 24 * x2 - 33 * x3 + 2 * (x1)**2 + 2 * (x2)**2 + 4 * (x3)**2
sol_hs061 = np.array([-2.1190398764, 3.2105368221, 5.3268866265])
eq1_hs061 = 4 * x3 - x2**2 - 11
eq2_hs061 = 3 * x3 - 2 * x1**2 - 7
cons_hs061 = [{'func':eq1_hs061, 'type':'eq', 'prop':'unknown'}, {'func':eq2_hs061, 'type':'eq', 'prop':'unknown'}]
vars_hs061 = [x1, x2, x3]
bnds_hs061 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
hs061 = OptimizationProblem('hs061', sol_hs061, symobj_hs061, cons_hs061, vars_hs061, bnds_hs061)

symobj_bronstein = 0
sol_bronstein = np.array([-1.7566229888, 4.8388299903, 3.0822070015])
eq1_bronstein = x1 + x2 - x3
eq2_bronstein = x1**2 + x2**2 + x3**2 - 36
eq3_bronstein = x3**2 + x1 * x2 - 1
cons_bronstein = [{'func':eq1_bronstein, 'type':'eq', 'prop':'convex'}, {'func':eq2_bronstein, 'type':'eq', 'prop':'unknown'}, {'func':eq3_bronstein, 'type':'eq', 'prop':'unknown'}]
vars_bronstein = [x1, x2, x3]
bnds_bronstein = [np.array([-11000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
bronstein = OptimizationProblem('bronstein', sol_bronstein, symobj_bronstein, cons_bronstein, vars_bronstein, bnds_bronstein)

symobj_clo1 = 0
sol_clo1 = np.array([0.999822, 0.000177558, 0.000177558])
eq1_clo1 = x1 + x2 + x3**2 - 1
eq2_clo1 = x2 + x3 + x1**2 - 1
eq3_clo1 = x1 + x3 + x2**2 - 1
cons_clo1 = [{'func':eq1_clo1, 'type':'eq', 'prop':'unknown'}, {'func':eq2_clo1, 'type':'eq', 'prop':'unknown'}, {'func':eq3_clo1, 'type':'eq', 'prop':'unknown'}]
vars_clo1 = [x1, x2, x3]
bnds_clo1 = [np.array([-10, 10]), np.array([-10, 10]), np.array([-10, 10])]
clo1 = OptimizationProblem('clo1', sol_clo1, symobj_clo1, cons_clo1, vars_clo1, bnds_clo1)

symobj_czaporgeddes = 0
sol_czaporgeddes = np.array([-0.6988995833, 0.2326846489, 0.1654295542])
eq1_czaporgeddes = 3 * x1 + 10 * x2 -8 * x3 +8 * x1**2 +3 * x2**2 +10 * x3**2 - 2 * x1 * x2 -6 * x1 * x3 -7 * x2 * x3 - 4
eq2_czaporgeddes = 8 * x1 + 2 * x2 - 7 * x3 + 5 * x1**2 + 9 * x2**2 - x3**2 + 12 * x1 * x3 - 6 * x2 * x3 + 5
eq3_czaporgeddes = (-6) * x1 - 4 * x2 + 5 * x3 + 10 * x1**2 + 9 * x2**2 - 2 * x3**2 - 2 * x1 * x2 + 6 * x1 * x3 - x2 * x3 - 9
cons_czaporgeddes = [{'func':eq1_czaporgeddes, 'type':'eq', 'prop':'unknown'}, {'func':eq2_czaporgeddes, 'type':'eq', 'prop':'unknown'}, {'func':eq3_czaporgeddes, 'type':'eq', 'prop':'unknown'}]
vars_czaporgeddes = [x1, x2, x3]
bnds_czaporgeddes = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
czaporgeddes = OptimizationProblem('czaporgeddes', sol_czaporgeddes, symobj_czaporgeddes, cons_czaporgeddes, vars_czaporgeddes, bnds_czaporgeddes)

symobj_eqlin = 0
sol_eqlin = np.array([3.33067e-16, 1, 2])
eq1_eqlin = 3 * x1 + 5 * x2 - 3 * x3 + 1
eq2_eqlin = 2 * x1 + 4 * x2 + 7 * x3 - 18
eq3_eqlin = x1 - 2 * x2 + x3
cons_eqlin = [{'func':eq1_eqlin, 'type':'eq', 'prop':'convex'}, {'func':eq2_eqlin, 'type':'eq', 'prop':'convex'}, {'func':eq3_eqlin, 'type':'eq', 'prop':'convex'}]
vars_eqlin = [x1, x2, x3]
bnds_eqlin = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
eqlin = OptimizationProblem('eqlin', sol_eqlin, symobj_eqlin, cons_eqlin, vars_eqlin, bnds_eqlin)

symobj_hong2 = 0
sol_hong2 = np.array([0.555893, 0.618034, 0.555893])
eq1_hong2 = x1 - x3
eq2_hong2 = x1**2 + x2**2 + x3**2 - 1
eq3_hong2 = -x2 + x1**2 + x3**2
cons_hong2 = [{'func':eq1_hong2, 'type':'eq', 'prop':'unknown'}, {'func':eq2_hong2, 'type':'eq', 'prop':'unknown'}, {'func':eq3_hong2, 'type':'eq', 'prop':'unknown'}]
vars_hong2 = [x1, x2, x3]
bnds_hong2 = [np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000])]
hong2 = OptimizationProblem('hong2', sol_hong2, symobj_hong2, cons_hong2, vars_hong2, bnds_hong2)

symobj_mathews = 0
sol_mathews = np.array([1.18046, 2.18046, -0.18046])
eq1_mathews = -x1 + x1**2 + x2**2 + x3**2 - 5
eq2_mathews = x3 + x1**2 + x2**2 + x3**2 - 6
eq3_mathews = -x2 + x1**2 + x2**2 + x3**2 - 4
cons_mathews = [{'func':eq1_mathews, 'type':'eq', 'prop':'unknown'}, {'func':eq2_mathews, 'type':'eq', 'prop':'unknown'}, {'func':eq3_mathews, 'type':'eq', 'prop':'unknown'}]
vars_mathews = [x1, x2, x3]
bnds_mathews = [np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000])]
mathews = OptimizationProblem('mathews', sol_mathews, symobj_mathews, cons_mathews, vars_mathews, bnds_mathews)

symobj_rediff3 = 0
sol_rediff3 = np.array([0.252318, 0.34699, 0.252318])
eq1_rediff3 = (-2) * x1 + x2 + 0.83563453399999998 * ((- x1) + 1) * x1
eq2_rediff3 = x2 - 2 * x3 + 0.83563453399999998 * ((- x3) + 1) * x3
eq3_rediff3 = x1 - 2 * x2 + x3 + 0.83563453399999998 * ((- x2) + 1) * x2
cons_rediff3 = [{'func':eq1_rediff3, 'type':'eq', 'prop':'unknown'}, {'func':eq2_rediff3, 'type':'eq', 'prop':'unknown'}, {'func':eq3_rediff3, 'type':'eq', 'prop':'unknown'}]
vars_rediff3 = [x1, x2, x3]
bnds_rediff3 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
rediff3 = OptimizationProblem('rediff3', sol_rediff3, symobj_rediff3, cons_rediff3, vars_rediff3, bnds_rediff3)

symobj_zangwil3 = 0
#sol_zangwil3 = np.array([4.44089e-16, 0, 5.55112e-17])
sol_zangwil3 = np.array([0, 0, 0])
eq1_zangwil3 = x1 - x2 + x3
eq2_zangwil3 = -x1 + x2 + x3
eq3_zangwil3 = x1 + x2 - x3
cons_zangwil3 = [{'func':eq1_zangwil3, 'type':'eq', 'prop':'convex'}, {'func':eq2_zangwil3, 'type':'eq', 'prop':'convex'}, {'func':eq3_zangwil3, 'type':'eq', 'prop':'convex'}]
vars_zangwil3 = [x1, x2, x3]
bnds_zangwil3 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
zangwil3 = OptimizationProblem('zangwil3', sol_zangwil3, symobj_zangwil3, cons_zangwil3, vars_zangwil3, bnds_zangwil3)

symobj_hs030 = x1**2 + x2**2 + x3**2
sol_hs030 = np.array([1, 1.32507e-09, -5.74407e-05])
ineq1_hs030 = x1**2 + x2**2 - 1
cons_hs030 = [{'func':ineq1_hs030, 'type':'ineq', 'prop':'unknown'}]
vars_hs030 = [x1, x2, x3]
bnds_hs030 = [np.array([1, 10]), np.array([-10, 10]), np.array([-10, 10])]
hs030 = OptimizationProblem('hs030', sol_hs030, symobj_hs030, cons_hs030, vars_hs030, bnds_hs030)

symobj_hs035 = (-8) * x1 - 6 * x2 - 4 * x3 + x3**2 + 2 * x1**2 + 2 * x2**2 + 2 * x1 * x2 + 2 * x1 * x3 + 9
sol_hs035 = np.array([1.3333333333, 0.7777777778, 0.4444444444])
ineq1_hs035 = x1 + x2 + 2 * x3 - 3
cons_hs035 = [{'func':ineq1_hs035, 'type':'ineq', 'prop':'convex'}]
vars_hs035 = [x1, x2, x3]
bnds_hs035 = [np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000])]
hs035 = OptimizationProblem('hs035', sol_hs035, symobj_hs035, cons_hs035, vars_hs035, bnds_hs035)

symobj_hs065 = (x3 - 5)**2 + (x1 - x2)**2 + 0.1111111111111111 * (x1 + x2 - 10)**2
sol_hs065 = np.array([3.65046, 3.65046, 4.62042])
ineq1_hs065 = x1**2 + x2**2 + x3**2 - 48
cons_hs065 = [{'func':ineq1_hs065, 'type':'ineq', 'prop':'unknown'}]
vars_hs065 = [x1, x2, x3]
bnds_hs065 = [np.array([-4.5, 4.5]), np.array([-4.5, 4.5]), np.array([-5, 5])]
hs065 = OptimizationProblem('hs065', sol_hs065, symobj_hs065, cons_hs065, vars_hs065, bnds_hs065)

symobj_hs35mod = (-8) * x1 - 6 * x2 - 4 * x3 + (x3**2) + 2 * (x1**2) + 2 * (x2**2) + 2 * x1 * x2 + 2 * x1 * x3 + 9
sol_hs35mod = np.array([1.5000000000,0.5000000000,0.5000000000])
ineq1_hs35mod = -(-x1 - x2 - 2 * x3) - 3
cons_hs35mod = [{'func':ineq1_hs35mod,'type': 'ineq', 'prop':'convex'}]
bnds_hs35mod = [np.array([0, 10000]), np.array([0.5, 0.5]), np.array([0, 10000])]
vars_hs35mod = [x1, x2, x3]
hs35mod = OptimizationProblem("hs35mod", sol_hs35mod, symobj_hs35mod, cons_hs35mod, vars_hs35mod, bnds_hs35mod)

symobj_congigmz = x3
sol_congigmz = np.array([-4.0000000001, -5.9999999999, 27.9999999969])
ineq1_congigmz = x1 + x2 + 10
ineq2_congigmz = 5 * x1 + x2 - x3
ineq3_congigmz = -5 * x1 + x2 - x3
ineq4_congigmz = 4 * x2 - x3 + x1**2 + x2**2
ineq5_congigmz = 2 * x1**2 - x2**2 + 4
cons_congigmz = [{'func':ineq1_congigmz, 'type':'ineq', 'prop':'unknown'}, {'func':ineq2_congigmz, 'type':'ineq', 'prop':'unknown'}, {'func':ineq3_congigmz, 'type':'ineq', 'prop':'unknown'}, {'func':ineq4_congigmz, 'type':'ineq', 'prop':'unknown'}, {'func':ineq5_congigmz, 'type':'ineq', 'prop':'unknown'}]
vars_congigmz = [x1, x2, x3]
bnds_congigmz = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
congigmz = OptimizationProblem('congigmz', sol_congigmz, symobj_congigmz, cons_congigmz, vars_congigmz, bnds_congigmz)

symobj_b = 0
sol_b = np.array([0.5,1.65139,-1,-0.151388])
eq1_b = x1 + x2 - x3 + x4 - 3
eq2_b = x1 + x2 + x3 + x4 - 1
eq3_b = (x1**2) + (x2**2) + (x3**2) + (x4**2) - 4
eq4_b = (-2) * x1 + (x1**2) + (x2**2) + (x3**2) + (x4**2) - 3
cons_b = [{'func':eq1_b,'type': 'eq', 'prop':'convex'},{'func':eq2_b,'type': 'eq', 'prop':'convex'},{'func':eq3_b,'type': 'eq', 'prop':'unknown'},{'func':eq4_b,'type': 'eq', 'prop':'unknown'}]
bnds_b = [np.array([-10, 10]), np.array([-10, 10]), np.array([-10, 10]), np.array([-10, 10])]
vars_b = [x1, x2, x3, x4]
b = OptimizationProblem("b", sol_b, symobj_b, cons_b, vars_b, bnds_b)

symobj_eiger = 0
sol_eiger = np.array([0.1, 0.1, 0.1, 0.1])
eq1_eiger = (-0.20000000000000001) * x1 + x2 + x1**2 - 0.089999999999999997
eq2_eiger = x1 - 0.20000000000000001 * x4 + x4**2 - 0.089999999999999997
eq3_eiger = (-0.20000000000000001) * x2 + x3 + x2**2 - 0.089999999999999997
eq4_eiger = (-0.20000000000000001) * x3 + x4 + x3**2 - 0.089999999999999997
cons_eiger = [{'func':eq1_eiger, 'type':'eq', 'prop':'unknown'}, {'func':eq2_eiger, 'type':'eq', 'prop':'unknown'}, {'func':eq3_eiger, 'type':'eq', 'prop':'unknown'}, {'func':eq4_eiger, 'type':'eq', 'prop':'unknown'}]
vars_eiger = [x1, x2, x3, x4]
bnds_eiger = [np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100])]
eiger = OptimizationProblem('eiger', sol_eiger, symobj_eiger, cons_eiger, vars_eiger, bnds_eiger)

symobj_hong1 = 0
sol_hong1 = np.array([0.5, 1.65139, -1, -0.151388])
eq1_hong1 = x1 + x2 - x3 + x4 - 3
eq2_hong1 = x1 + x2 + x3 + x4 - 1
eq3_hong1 = x1**2 + x2**2 + x3**2 + x4**2 - 4
eq4_hong1 = (-2) * x1 + x1**2 + x2**2 + x3**2 + x4**2 - 3
cons_hong1 = [{'func':eq1_hong1, 'type':'eq', 'prop':'convex'}, {'func':eq2_hong1, 'type':'eq', 'prop':'convex'}, {'func':eq3_hong1, 'type':'eq', 'prop':'unknown'}, {'func':eq4_hong1, 'type':'eq', 'prop':'unknown'}]
vars_hong1 = [x1, x2, x3, x4]
bnds_hong1 = [np.array([-10, 10]), np.array([-10, 10]), np.array([-10, 10]), np.array([-10, 10])]
hong1 = OptimizationProblem('hong1', sol_hong1, symobj_hong1, cons_hong1, vars_hong1, bnds_hong1)

symobj_kear3 = 0
sol_kear3 = np.array([2.77556e-17, -3.46945e-18, -1.73472e-18, -1.73472e-18])
eq1_kear3 = x3 - x4
eq2_kear3 = x1 + 10 * x2
eq3_kear3 = (x2 - 2 * x3)**2
eq4_kear3 = (x1 - x4)**2
cons_kear3 = [{'func':eq1_kear3, 'type':'eq', 'prop':'convex'}, {'func':eq2_kear3, 'type':'eq', 'prop':'convex'}, {'func':eq3_kear3, 'type':'eq', 'prop':'unknown'}, {'func':eq4_kear3, 'type':'eq', 'prop':'unknown'}]
vars_kear3 = [x1, x2, x3, x4]
bnds_kear3 = [np.array([-2, 3]), np.array([-2, 3]), np.array([-2, 3]), np.array([-2, 3])]
kear3 = OptimizationProblem('kear3', sol_kear3, symobj_kear3, cons_kear3, vars_kear3, bnds_kear3)

symobj_kincox = 0
sol_kincox = np.array([0.907472,0.12883,0.420113,-0.991667])
eq1_kincox = (-10) * x3 + 6 * x1 * x2 - 6 * x3 * x4 - -1
eq2_kincox = (x2**2) + (x4**2) - 1
eq3_kincox = (x1**2) + (x3**2) - 1
eq4_kincox = (-10) * x1 - 6 * x1 * x4 - 6 * x2 * x3 - -4
cons_kincox = [{'func':eq1_kincox,'type': 'eq', 'prop':'unknown'},{'func':eq2_kincox,'type': 'eq', 'prop':'unknown'},{'func':eq3_kincox,'type': 'eq', 'prop':'unknown'},{'func':eq4_kincox,'type': 'eq', 'prop':'unknown'}]
bnds_kincox = [np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1])]
vars_kincox = [x1, x2, x3, x4]
kincox = OptimizationProblem("kincox", sol_kincox, symobj_kincox, cons_kincox, vars_kincox, bnds_kincox)

symobj_lorentz = 0
sol_lorentz = np.array([1, -3.2916e-13, 1, 2.24014e-13])
eq1_lorentz = -x4 + x1 * x2 - x1 * x3 + 1
eq2_lorentz = -x3 - x2 * x4 + x1 * x4 + 1
eq3_lorentz = -x1 + x2 * x3 - x2 * x4 + 1
eq4_lorentz = -x2 - x1 * x3 + x3 * x4 + 1
cons_lorentz = [{'func':eq1_lorentz, 'type':'eq', 'prop':'unknown'}, {'func':eq2_lorentz, 'type':'eq', 'prop':'unknown'}, {'func':eq3_lorentz, 'type':'eq', 'prop':'unknown'}, {'func':eq4_lorentz, 'type':'eq', 'prop':'unknown'}]
vars_lorentz = [x1, x2, x3, x4]
bnds_lorentz = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
lorentz = OptimizationProblem('lorentz', sol_lorentz, symobj_lorentz, cons_lorentz, vars_lorentz, bnds_lorentz)

symobj_monfroy1 = 0
sol_monfroy1 = np.array([15.8113883008,15.8113883008,3.2235246281,50.9683995923])
eq1_monfroy1 = -x1 + x2 - 0
eq2_monfroy1 = (x1**2) + (x2**2) - 500
eq3_monfroy1 = x4 - x1 * x3 - 0
eq4_monfroy1 = 4.9050000000000002 * (x3**2) - x2 * x3 - 0
cons_monfroy1 = [{'func':eq1_monfroy1,'type': 'eq', 'prop':'unknown'},{'func':eq2_monfroy1,'type': 'eq', 'prop':'unknown'},{'func':eq3_monfroy1,'type': 'eq', 'prop':'unknown'},{'func':eq4_monfroy1,'type': 'eq', 'prop':'unknown'}]
bnds_monfroy1 = [np.array([0, 100000]), np.array([0, 100000]), np.array([0, 100000]), np.array([0.10000000000000001, 100000])]
vars_monfroy1 = [x1, x2, x3, x4]
monfroy1 = OptimizationProblem("monfroy1", sol_monfroy1, symobj_monfroy1, cons_monfroy1, vars_monfroy1, bnds_monfroy1)

symobj_powell = 0
sol_powell = np.array([2.77556e-17, -3.46945e-18, -1.73472e-18, -1.73472e-18])
eq1_powell = x3 - x4
eq2_powell = x1 + 10 * x2
eq3_powell = x2**2 + 4 * x3**2 - 4 * x2 * x3
eq4_powell = x1**2 + x4**2 - 2 * x1 * x4
cons_powell = [{'func':eq1_powell, 'type':'eq', 'prop':'convex'}, {'func':eq2_powell, 'type':'eq', 'prop':'convex'}, {'func':eq3_powell, 'type':'eq', 'prop':'unknown'}, {'func':eq4_powell, 'type':'eq', 'prop':'unknown'}]
vars_powell = [x1, x2, x3, x4]
bnds_powell = [np.array([-2, 2]), np.array([-2, 2]), np.array([-2, 2]), np.array([-2, 2])]
powell = OptimizationProblem('powell', sol_powell, symobj_powell, cons_powell, vars_powell, bnds_powell)

symobj_dispatch = 11.669 * x1 + 10.333 * x2 + 10.833 * x3 + 0.0053299999999999997 * x1**2 + 0.0088900000000000003 * x2**2 + 0.0074099999999999999 * x3**2 + 653.10000000000002
sol_dispatch = np.array([50.0, 75.4858804799, 93.2622541695, 8.7481346494])
eq1_dispatch = 0.00076599999999999997 * x1 + 3.4199999999999998e-05 * x2 - 0.00018900000000000001 * x3 + x4 - 0.00067599999999999995 * x1**2 - 0.00052099999999999998 * x2**2 - 0.00029399999999999999 * x3**2 - 0.0001906 * x1 * x2 + 5.0699999999999999e-05 * x1 * x3 + 5.0699999999999999e-05 * x1 * x3 - 0.00018020000000000002 * x2 * x3 - 0.040356999999999997
ineq1_dispatch = -x1 - x2 - x3 + x4 + 210
cons_dispatch = [{'func':eq1_dispatch, 'type':'eq', 'prop':'unknown'}, {'func':ineq1_dispatch, 'type':'ineq', 'prop':'convex'}]
vars_dispatch = [x1, x2, x3, x4]
bnds_dispatch = [np.array([50, 200]), np.array([37.5, 150]), np.array([45, 180]), np.array([-10, 10])]
dispatch = OptimizationProblem('dispatch', sol_dispatch, symobj_dispatch, cons_dispatch, vars_dispatch, bnds_dispatch)

symobj_hs043 = (-5) * x1 - 5 * x2 - 21 * x3 + 7 * x4 + x1**2 + x2**2 + x4**2 + 2 * x3**2
sol_hs043 = np.array([8.36698e-07, 0.999999, 2, -1])
ineq1_hs043 = 2 * x1 - x2 - x4 + 2 * x1**2 + x2**2 + x3**2 - 5
ineq2_hs043 = -x1 - x4 + x1**2 + 2 * x2**2 + 2 * x4**2 + x3**2 - 10
ineq3_hs043 = x1 - x2 + x3 - x4 + x1**2 + x2**2 + x4**2 + x3**2 - 8
cons_hs043 = [{'func':ineq1_hs043, 'type':'ineq', 'prop':'unknown'}, {'func':ineq2_hs043, 'type':'ineq', 'prop':'unknown'}, {'func':ineq3_hs043, 'type':'ineq', 'prop':'unknown'}]
vars_hs043 = [x1, x2, x3, x4]
bnds_hs043 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
hs043 = OptimizationProblem('hs043', sol_hs043, symobj_hs043, cons_hs043, vars_hs043, bnds_hs043)

symobj_hs076 = -x1 - 3 * x2 + x3 - x4 + x1**2 + x3**2 + 0.5 * x2**2 + 0.5 * x4**2 - x1 * x3 + x3 * x4
sol_hs076 = np.array([0.2727272727, 2.0909090909, 0, 0.5454545455])
ineq1_hs076 = -x2 - 4 * x3 + 1.5
ineq2_hs076 = 3 * x1 + x2 + 2 * x3 - x4 - 4
ineq3_hs076 = x1 + 2 * x2 + x3 + x4 - 5
cons_hs076 = [{'func':ineq1_hs076, 'type':'ineq', 'prop':'convex'}, {'func':ineq2_hs076, 'type':'ineq', 'prop':'convex'}, {'func':ineq3_hs076, 'type':'ineq', 'prop':'convex'}]
vars_hs076 = [x1, x2, x3, x4]
bnds_hs076 = [np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000])]
hs076 = OptimizationProblem('hs076', sol_hs076, symobj_hs076, cons_hs076, vars_hs076, bnds_hs076)

symobj_hs044 = x1 - x2 - x3 - x1 * x3 + x1 * x4 + x2 * x3 - x2 * x4
sol_hs044 = np.array([6.81905e-18,3,4.66772e-18,4])
ineq1_hs044 = x3 + x4 - 5
ineq2_hs044 = x3 + 2 * x4 - 8
ineq3_hs044 = 2 * x3 + x4 - 8
ineq4_hs044 = 3 * x1 + 4 * x2 - 12
ineq5_hs044 = 4 * x1 + x2 - 12
ineq6_hs044 = x1 + 2 * x2 - 8
cons_hs044 = [{'func':ineq1_hs044,'type': 'ineq', 'prop':'convex'},{'func':ineq2_hs044,'type': 'ineq', 'prop':'convex'},{'func':ineq3_hs044,'type': 'ineq', 'prop':'convex'},{'func':ineq4_hs044,'type': 'ineq', 'prop':'convex'},{'func':ineq5_hs044,'type': 'ineq', 'prop':'convex'},{'func':ineq6_hs044,'type': 'ineq', 'prop':'convex'}]
bnds_hs044 = [np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000])]
vars_hs044 = [x1, x2, x3, x4]
hs044 = OptimizationProblem("hs044", sol_hs044, symobj_hs044, cons_hs044, vars_hs044, bnds_hs044)

symobj_hs44new = x1 - x2 - x3 - x1 * x3 + x1 * x4 + x2 * x3 - x2 * x4
sol_hs44new = np.array([6.81905e-18, 3, 4.66772e-18, 4])
ineq1_hs44new = x3 + x4 - 5
ineq2_hs44new = x3 + 2 * x4 - 8
ineq3_hs44new = (2) * x3 + x4 - 8
ineq4_hs44new = (3) * x1 + 4 * x2 - 12
ineq5_hs44new = (4) * x1 + x2 - 12
ineq6_hs44new = x1 + x2 - 8
cons_hs44new = [{'func':ineq1_hs44new, 'type':'ineq', 'prop':'convex'}, {'func':ineq2_hs44new, 'type':'ineq', 'prop':'convex'}, {'func':ineq3_hs44new, 'type':'ineq', 'prop':'convex'}, {'func':ineq4_hs44new, 'type':'ineq', 'prop':'convex'}, {'func':ineq5_hs44new, 'type':'ineq', 'prop':'convex'}, {'func':ineq6_hs44new, 'type':'ineq', 'prop':'convex'}]
vars_hs44new = [x1, x2, x3, x4]
bnds_hs44new = [np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000])]
hs44new = OptimizationProblem('hs44new', sol_hs44new, symobj_hs44new, cons_hs44new, vars_hs44new, bnds_hs44new)

symobj_bt13 = x5
sol_bt13 = np.array([0.000171212, -8.15277e-05, -0.000100024, 5.63993e-05, 0])
eq1_bt13 = x1**2 - x5**2 + (x1 - 2 * x2)**2 + (x2 - 3 * x3)**2 + (x3 - 4 * x4)**2
cons_bt13 = [{'func':eq1_bt13, 'type':'eq', 'prop':'unknown'}]
vars_bt13 = [x1, x2, x3, x4, x5]
bnds_bt13 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([0, 10000])]
bt13 = OptimizationProblem('bt13', sol_bt13, symobj_bt13, cons_bt13, vars_bt13, bnds_bt13)

symobj_bt8 = x1**2 + x2**2 + x5**2
sol_bt8 = np.array([0.888031, 0.459783, 0.315328, 8.78968e-07, -3.76183e-06])
eq1_bt8 = x1 + x2**2 - x3**2 - 1
eq2_bt8 = x1**2 + x2**2 - x4**2 - 1
cons_bt8 = [{'func':eq1_bt8, 'type':'eq', 'prop':'unknown'}, {'func':eq2_bt8, 'type':'eq', 'prop':'unknown'}]
vars_bt8 = [x1, x2, x3, x4, x5]
bnds_bt8 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
bt8 = OptimizationProblem('bt8', sol_bt8, symobj_bt8, cons_bt8, vars_bt8, bnds_bt8)

symobj_hs048 = (x1 - 1)**2 + (x2 - x3)**2 + (x4 - x5)**2
sol_hs048 = np.array([1, 0.999999, 1, 1, 0.999999])
eq1_hs048 = x3 - 2 * x4 - 2 * x5 + 3
eq2_hs048 = x1 + x2 + x3 + x4 + x5 - 5
cons_hs048 = [{'func':eq1_hs048, 'type':'eq', 'prop':'unknown'}, {'func':eq2_hs048, 'type':'eq', 'prop':'unknown'}]
vars_hs048 = [x1, x2, x3, x4, x5]
bnds_hs048 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
hs048 = OptimizationProblem('hs048', sol_hs048, symobj_hs048, cons_hs048, vars_hs048, bnds_hs048)

symobj_bt3 = (x4 - 1)**2 + (x5 - 1)**2 + (x1 - x2)**2 + (x2 + x3 - 2)**2
sol_bt3 = np.array([-0.7674418605, 0.2558139535, 0.6279069767, -0.1162790698, 0.2558139535])
eq1_bt3 = x2 - x5
eq2_bt3 = x3 + x4 - 2 * x5
eq3_bt3 = x1 + 3 * x2
cons_bt3 = [{'func':eq1_bt3, 'type':'eq', 'prop':'unknown'}, {'func':eq2_bt3, 'type':'eq', 'prop':'unknown'}, {'func':eq3_bt3, 'type':'eq', 'prop':'unknown'}]
vars_bt3 = [x1, x2, x3, x4, x5]
bnds_bt3 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
bt3 = OptimizationProblem('bt3', sol_bt3, symobj_bt3, cons_bt3, vars_bt3, bnds_bt3)

symobj_bt12 = x2**2 + 0.01 * x1**2
#sol_bt12 = np.array([24.7525, 0.247525, 2.63158e-08, -24.2435, 4.76996])
sol_bt12 = np.array([24.75247525, 0.24752475, 0.0, -24.24347952, 4.76995548])
eq1_bt12 = x1 + x2 - x3**2 - 25
eq2_bt12 = x1 - x5**2 - 2
eq3_bt12 = x2**2 + x1**2 - x4**2 - 25
cons_bt12 = [{'func':eq1_bt12, 'type':'eq', 'prop':'unknown'}, {'func':eq2_bt12, 'type':'eq', 'prop':'unknown'}, {'func':eq3_bt12, 'type':'eq', 'prop':'unknown'}]
vars_bt12 = [x1, x2, x3, x4, x5]
bnds_bt12 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
bt12 = OptimizationProblem('bt12', sol_bt12, symobj_bt12, cons_bt12, vars_bt12, bnds_bt12)

symobj_hs051 = (x4 - 1)**2 + (x5 - 1)**2 + (x1 - x2)**2 + (x2 + x3 - 2)**2
sol_hs051 = np.array([1, 1, 1, 1, 1])
eq1_hs051 = x2 - x5
eq2_hs051 = x3 + x4 - 2 * x5
eq3_hs051 = x1 + 3 * x2 - 4
cons_hs051 = [{'func':eq1_hs051, 'type':'eq', 'prop':'unknown'}, {'func':eq2_hs051, 'type':'eq', 'prop':'unknown'}, {'func':eq3_hs051, 'type':'eq', 'prop':'unknown'}]
vars_hs051 = [x1, x2, x3, x4, x5]
bnds_hs051 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
hs051 = OptimizationProblem('hs051', sol_hs051, symobj_hs051, cons_hs051, vars_hs051, bnds_hs051)

symobj_hs052 = (x4 - 1)**2 + (x5 - 1)**2 + (4 * x1 - x2)**2 + (x2 + x3 - 2)**2
sol_hs052 = np.array([-0.0945558739, 0.0315186246, 0.5157593123, -0.452722063, 0.0315186246])
eq1_hs052 = x2 - x5
eq2_hs052 = x3 + x4 - 2 * x5
eq3_hs052 = x1 + 3 * x2
cons_hs052 = [{'func':eq1_hs052, 'type':'eq', 'prop':'unknown'}, {'func':eq2_hs052, 'type':'eq', 'prop':'unknown'}, {'func':eq3_hs052, 'type':'eq', 'prop':'unknown'}]
vars_hs052 = [x1, x2, x3, x4, x5]
bnds_hs052 = [np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1])]
#bnds_hs052 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
hs052 = OptimizationProblem('hs052', sol_hs052, symobj_hs052, cons_hs052, vars_hs052, bnds_hs052)

symobj_aircrfta = 0
sol_aircrfta = np.array([-2.8819233426, -2.8411289852, -0.2022780355, 0.0003759005, 1.0265036693])
eq1_aircrfta = (-3.9329999999999998) * x1 + 0.107 * x2 + 0.126 * x3 - 9.9900000000000002 * x5 - 0.72699999999999998 * x2 * x3 + 63.5 * x2 * x4 + 8.3900000000000006 * x3 * x4 - 684.39999999999998 * x4 * x5
eq2_aircrfta = -x3 - 0.19600000000000001 * x5 + x1 * x4
eq3_aircrfta = x2 - x4 - x1 * x5 - 0.1168
eq4_aircrfta = 0.002 * x1 - 0.23499999999999999 * x3 + 5.6699999999999999 * x5 - 0.71599999999999997 * x1 * x2 - 1.5780000000000001 * x1 * x4 + 1.1319999999999999 * x2 * x4
eq5_aircrfta = (-0.98699999999999999) * x2 - 22.949999999999999 * x4 + 0.94899999999999995 * x1 * x3 + 0.17299999999999999 * x1 * x5 - 2.8370000000000002
cons_aircrfta = [{'func':eq1_aircrfta, 'type':'eq', 'prop':'unknown'}, {'func':eq2_aircrfta, 'type':'eq', 'prop':'unknown'}, {'func':eq3_aircrfta, 'type':'eq', 'prop':'unknown'}, {'func':eq4_aircrfta, 'type':'eq', 'prop':'unknown'}, {'func':eq5_aircrfta, 'type':'eq', 'prop':'unknown'}]
vars_aircrfta = [x1, x2, x3, x4, x5]
bnds_aircrfta = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
aircrfta = OptimizationProblem('aircrfta', sol_aircrfta, symobj_aircrfta, cons_aircrfta, vars_aircrfta, bnds_aircrfta)

symobj_redeco5 = 0
sol_redeco5 = np.array([0.7948,-1.14417,0.030515,-0.681144,-0.170286])
eq1_redeco5 = x1 + x2 + x3 + x4 - -1
eq2_redeco5 = x4 - 4 * x5 - 0
eq3_redeco5 = x1 - x5 + x1 * x2 + x2 * x3 + x3 * x4 - 0
eq4_redeco5 = x3 - 3 * x5 + x1 * x4 - 0
eq5_redeco5 = x2 - 2 * x5 + x1 * x3 + x2 * x4 - 0
cons_redeco5 = [{'func':eq1_redeco5,'type': 'eq', 'prop': 'convex'},{'func':eq2_redeco5,'type': 'eq', 'prop': 'convex'},{'func':eq3_redeco5,'type': 'eq', 'prop': 'unknown'},{'func':eq4_redeco5,'type': 'eq', 'prop': 'unknown'},{'func':eq5_redeco5,'type': 'eq', 'prop': 'unknown'}]
bnds_redeco5 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_redeco5 = [x1, x2, x3, x4, x5]
redeco5 = OptimizationProblem("redeco5", sol_redeco5, symobj_redeco5, cons_redeco5, vars_redeco5, bnds_redeco5)

symobj_wright = 0
sol_wright = np.array([2,2,2,2,2])
eq1_wright = -x1 + x2 + x3 + x4 + x5 + (x1**2) - 10
eq2_wright = x1 - x2 + x3 + x4 + x5 + (x2**2) - 10
eq3_wright = x1 + x2 + x3 + x4 - x5 + (x5**2) - 10
eq4_wright = x1 + x2 + x3 - x4 + x5 + (x4**2) - 10
eq5_wright = x1 + x2 - x3 + x4 + x5 + (x3**2) - 10
cons_wright = [{'func':eq1_wright,'type': 'eq', 'prop':'unknown'},{'func':eq2_wright,'type': 'eq', 'prop':'unknown'},{'func':eq3_wright,'type': 'eq', 'prop':'unknown'},{'func':eq4_wright,'type': 'eq', 'prop':'unknown'},{'func':eq5_wright,'type': 'eq', 'prop':'unknown'}]
bnds_wright = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_wright = [x1, x2, x3, x4, x5]
wright = OptimizationProblem("wright", sol_wright, symobj_wright, cons_wright, vars_wright, bnds_wright)

symobj_hs268 = 18340 * x1 - 34198 * x2 + 4542 * x3 + 8672 * x4 + 86 * x5 + 20909 * (x2**2) + 1755 * (x3**2) + 1515 * (x4**2) + 27 * (x5**2) + 10197 * (x1**2) - 24908 * x1 * x2 - 2026 * x1 * x3 + 3896 * x1 * x4 + 658 * x1 * x5 - 3466 * x2 * x3 - 9828 * x2 * x4 - 372 * x2 * x5 + 2178 * x3 * x4 - 348 * x3 * x5 - 44 * x4 * x5 + 14463
sol_hs268 = np.array([0.9999999949, 1.9999999953, -1.0000000077, 2.9999999964, -4.0000000233])
ineq1_hs268 = (4) * x1 + 2 * x2 - 3 * x3 + 5 * x4 - x5 - 30
ineq2_hs268 = -8 * x1 + x2 - 2 * x3 - 5 * x4 + 3 * x5 + 11
ineq3_hs268 = (8) * x1 - x2 + 2 * x3 + 5 * x4 - 3 * x5 - 40
ineq4_hs268 = -10 * x1 - 10 * x2 + 3 * x3 - 5 * x4 - 4 * x5 + 20
ineq5_hs268 = x1 + x2 + x3 + x4 + x5 - 5
cons_hs268 = [{'func':ineq1_hs268, 'type':'ineq', 'prop':'unknown'}, {'func':ineq2_hs268, 'type':'ineq', 'prop':'unknown'}, {'func':ineq3_hs268, 'type':'ineq', 'prop':'unknown'}, {'func':ineq4_hs268, 'type':'ineq', 'prop':'unknown'}, {'func':ineq5_hs268, 'type':'ineq', 'prop':'unknown'}]
vars_hs268 = [x1, x2, x3, x4, x5]
bnds_hs268 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
hs268 = OptimizationProblem('hs268', sol_hs268, symobj_hs268, cons_hs268, vars_hs268, bnds_hs268)

symobj_ex3_1_2 = 37.293239 * x1 + 5.3578546999999999 * (x2**2) + 0.83568909999999996 * x1 * x3 - 40792.141000000003
sol_ex3_1_2 = np.array([78.00000,29.99526,36.77581,33.00000,45.00000])
ineq1_ex3_1_2 = (-0.0012547000000000001) * x1 * x2 - 0.0047026000000000004 * x2 * x3 - 0.0019085 * x2 * x5 + 10.699039000000001
ineq2_ex3_1_2 = 0.0012547000000000001 * x1 * x2 + 0.0047026000000000004 * x2 * x3 + 0.0019085 * x2 * x5 - 15.599038999999999
ineq3_ex3_1_2 = (-0.0021813000000000002) * (x2**2) - 0.0071317000000000004 * x3 * x4 - 0.0029954999999999999 * x1 * x4 + 9.4875100000000003
ineq4_ex3_1_2 = 0.0021813000000000002 * (x2**2) + 0.0071317000000000004 * x3 * x4 + 0.0029954999999999999 * x1 * x4 - 29.48751
ineq5_ex3_1_2 = 0.00062620000000000004 * x1 * x5 - 0.0022052999999999999 * x2 * x3 + 0.0056858000000000004 * x3 * x4 - 6.6655930000000003
ineq6_ex3_1_2 = (-0.00062620000000000004) * x1 * x5 + 0.0022052999999999999 * x2 * x3 - 0.0056858000000000004 * x3 * x4 - 85.334406999999999
cons_ex3_1_2 = [{'func':ineq1_ex3_1_2,'type': 'ineq', 'prop': 'unknown'},{'func':ineq2_ex3_1_2,'type': 'ineq', 'prop': 'unknown'},{'func':ineq3_ex3_1_2,'type': 'ineq', 'prop': 'unknown'},{'func':ineq4_ex3_1_2,'type': 'ineq', 'prop': 'unknown'},{'func':ineq5_ex3_1_2,'type': 'ineq', 'prop': 'unknown'},{'func':ineq6_ex3_1_2,'type': 'ineq', 'prop': 'unknown'}]
bnds_ex3_1_2 = [np.array([78, 102]), np.array([27, 45]), np.array([27, 45]), np.array([33, 45]), np.array([27, 45])]
vars_ex3_1_2 = [x1, x2, x3, x4, x5]
ex3_1_2 = OptimizationProblem("ex3_1_2", sol_ex3_1_2, symobj_ex3_1_2, cons_ex3_1_2, vars_ex3_1_2, bnds_ex3_1_2)

symobj_hs083 = 37.293239 * x1 + 5.3578546999999999 * x2**2 + 0.83568909999999996 * x1 * x3 - 40792.141000000003
sol_hs083 = np.array([78.0, 29.99526, 36.77581, 33.0, 45.0])
ineq1_hs083 = -0.0012547000000000001 * x1 * x2 - 0.0047026000000000004 * x2 * x3 - 0.0019085 * x2 * x5 + 10.699039000000001
ineq2_hs083 = 0.0012547000000000001 * x1 * x2 + 0.0047026000000000004 * x2 * x3 + 0.0019085 * x2 * x5 - 15.699039000000001
ineq3_hs083 = -0.0021813000000000002 * x2**2 - 0.0071317000000000004 * x3 * x4 - 0.0029954999999999999 * x1 * x4 + 9.4875100000000003
ineq4_hs083 = 0.0021813000000000002 * x2**2 + 0.0071317000000000004 * x3 * x4 + 0.0029954999999999999 * x1 * x4 - 29.48751
ineq5_hs083 = -0.00062620000000000004 * x1 * x5 + 0.0022052999999999999 * x2 * x3 - 0.0056858000000000004 * x3 * x4 - 85.334406999999999
ineq6_hs083 = 0.00062620000000000004 * x1 * x5 - 0.0022052999999999999 * x2 * x3 + 0.0056858000000000004 * x3 * x4 - 6.6655930000000012
cons_hs083 = [{'func':ineq1_hs083, 'type':'ineq', 'prop':'unknown'}, {'func':ineq2_hs083, 'type':'ineq', 'prop':'unknown'}, {'func':ineq3_hs083, 'type':'ineq', 'prop':'unknown'}, {'func':ineq4_hs083, 'type':'ineq', 'prop':'unknown'}, {'func':ineq5_hs083, 'type':'ineq', 'prop':'unknown'}, {'func':ineq6_hs083, 'type':'ineq', 'prop':'unknown'}]
vars_hs083 = [x1, x2, x3, x4, x5]
bnds_hs083 = [np.array([78, 102]), np.array([27, 45]), np.array([27, 45]), np.array([33, 45]), np.array([27, 45])]
hs083 = OptimizationProblem('hs083', sol_hs083, symobj_hs083, cons_hs083, vars_hs083, bnds_hs083)

symobj_hs054 = (x3**2) + (x4**2) + (x5**2) + (x6**2) + 1.0416666666666667 * (x1**2) + 1.0416666666666667 * (x2**2) + 0.41666666666666674 * x1 * x2
sol_hs054 = np.array([0.385716,0.128568,6.12846e-06,0,2.76242e-06,2.30202e-06])
eq1_hs054 = x1 + 0.5 * x2 - 0.45000000000000001
cons_hs054 = [{'func':eq1_hs054,'type': 'eq', 'prop':'convex'}]
bnds_hs054 = [np.array([-1.25, 1.25]), np.array([-11, 9]), np.array([-0.2857142857142857, 1.1428571428571428]), np.array([-0.20000000000000001, 0.20000000000000001]), np.array([-20.019999999999996, 19.98]), np.array([-0.20000000000000001, 0.20000000000000001])]
vars_hs054 = [x1, x2, x3, x4, x5, x6]
hs054 = OptimizationProblem("hs054", sol_hs054, symobj_hs054, cons_hs054, vars_hs054, bnds_hs054)

symobj_ex9_2_8 = 2 * x5 + 3 * x6 - 4 * x5 * x6 + 1
sol_ex9_2_8 = np.array([0.0000000000,1.0000000000,0.0000000000,0.0000000000,0.2500000000,0.0000000000])
eq1_ex9_2_8 = -x3 + x4 + 4 * x5 - 1
eq2_ex9_2_8 = x2 + x6 - 1
eq3_ex9_2_8 = x1 - x6 - 0
eq4_ex9_2_8 = x2 * x4 - 0
eq5_ex9_2_8 = x1 * x3 - 0
cons_ex9_2_8 = [{'func':eq1_ex9_2_8,'type': 'eq', 'prop':'convex'},{'func':eq2_ex9_2_8,'type': 'eq', 'prop':'convex'},{'func':eq3_ex9_2_8,'type': 'eq', 'prop':'convex'},{'func':eq4_ex9_2_8,'type': 'eq', 'prop':'unknown'},{'func':eq5_ex9_2_8,'type': 'eq', 'prop':'unknown'}]
bnds_ex9_2_8 = [np.array([0, 20]), np.array([0, 20]), np.array([0, 0]), np.array([0, 0]), np.array([0, 1]), np.array([0, 10000])]
vars_ex9_2_8 = [x1, x2, x3, x4, x5, x6]
ex9_2_8 = OptimizationProblem("ex9_2_8", sol_ex9_2_8, symobj_ex9_2_8, cons_ex9_2_8, vars_ex9_2_8, bnds_ex9_2_8)

symobj_katsura5 = 0
sol_katsura5 = np.array([0.162143,0.22587,0.27721,-0.12399,0.0115328,0.085839])
eq1_katsura5 = 2 * x1 + 2 * x2 + x3 + 2 * x4 + 2 * x5 + 2 * x6 - 1
eq2_katsura5 = -x3 + (x3**2) + 2 * (x1**2) + 2 * (x2**2) + 2 * (x4**2) + 2 * (x5**2) + 2 * (x6**2) - 0
eq3_katsura5 = -x5 + (x1**2) + 2 * x3 * x4 + 2 * x3 * x5 + 2 * x3 * x6 - 0
eq4_katsura5 = -x6 + 2 * x1 * x2 + 2 * x1 * x4 + 2 * x2 * x5 + 2 * x3 * x6 - 0
eq5_katsura5 = -x2 + 2 * x1 * x2 + 2 * x1 * x6 + 2 * x2 * x3 + x4 * x5 + x5 * x6 - 0
eq6_katsura5 = -x1 + (x2**2) + 2 * x1 * x3 + 2 * x1 * x5 + 2 * x2 * x6 + 2 * x4 * x6 - 0
cons_katsura5 = [{'func':eq1_katsura5,'type': 'eq', 'prop':'convex'},{'func':eq2_katsura5,'type': 'eq', 'prop':'unknown'},{'func':eq3_katsura5,'type': 'eq', 'prop':'unknown'},{'func':eq4_katsura5,'type': 'eq', 'prop':'unknown'},{'func':eq5_katsura5,'type': 'eq', 'prop':'unknown'},{'func':eq6_katsura5,'type': 'eq', 'prop':'unknown'}]
bnds_katsura5 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_katsura5 = [x1, x2, x3, x4, x5, x6]
katsura5 = OptimizationProblem("katsura5", sol_katsura5, symobj_katsura5, cons_katsura5, vars_katsura5, bnds_katsura5)

symobj_redeco6 = 0
sol_redeco6 = np.array([-0.2000000000,-0.2000000000,-0.2000000000,-0.2000000000,-0.2000000000,-0.0400000000])
eq1_redeco6 = x1 + x2 + x3 + x4 + x5 - -1
eq2_redeco6 = x5 - 5 * x6 - 0
eq3_redeco6 = x1 - x6 + x1 * x2 + x2 * x3 + x3 * x4 + x4 * x5 - 0
eq4_redeco6 = x4 - 4 * x6 + x1 * x5 - 0
eq5_redeco6 = x2 - 2 * x6 + x1 * x3 + x2 * x4 + x3 * x5 - 0
eq6_redeco6 = x3 - 3 * x6 + x1 * x4 + x2 * x5 - 0
cons_redeco6 = [{'func':eq1_redeco6,'type': 'eq', 'prop':'convex'},{'func':eq2_redeco6,'type': 'eq', 'prop':'convex'},{'func':eq3_redeco6,'type': 'eq', 'prop':'unknown'},{'func':eq4_redeco6,'type': 'eq', 'prop':'unknown'},{'func':eq5_redeco6,'type': 'eq', 'prop':'unknown'},{'func':eq6_redeco6,'type': 'eq', 'prop':'unknown'}]
bnds_redeco6 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_redeco6 = [x1, x2, x3, x4, x5, x6]
redeco6 = OptimizationProblem("redeco6", sol_redeco6, symobj_redeco6, cons_redeco6, vars_redeco6, bnds_redeco6)

symobj_ex2_1_2 =  (-10.5) * x1 - 7.5 * x2 - 3.5 * x3 - 2.5 * x4 - 1.5 * x5 - 10 * x6 - 0.5 * (x1**2) - 0.5 * (x2**2) - 0.5 * (x3**2) - 0.5 * (x4**2) - 0.5 * (x5**2)
sol_ex2_1_2 = np.array([0.0000000000,1.0000000000,0.0000000000,1.0000000000,1.0000000000,20.0000000000])
ineq1_ex2_1_2 = 10 * x1 + 10 * x3 + x6 - 20
ineq2_ex2_1_2 = 6 * x1 + 3 * x2 + 3 * x3 + 2 * x4 + x5 - 6.5
cons_ex2_1_2 = [{'func':ineq1_ex2_1_2,'type': 'ineq', 'prop': 'convex'},{'func':ineq2_ex2_1_2,'type': 'ineq', 'prop': 'convex'}]
bnds_ex2_1_2 = [np.array([0, 1]), np.array([0, 1]), np.array([0, 1]), np.array([0, 1]), np.array([0, 1]), np.array([0, 1000])]
vars_ex2_1_2 = [x1, x2, x3, x4, x5, x6]
ex2_1_2 = OptimizationProblem("ex2_1_2", sol_ex2_1_2, symobj_ex2_1_2, cons_ex2_1_2, vars_ex2_1_2, bnds_ex2_1_2)

symobj_hs098 = 4.2999999999999998 * x1 + 63.299999999999997 * x2 + 15.800000000000001 * x3 + 68.5 * x4 + 4.7000000000000002 * x5 + 31.800000000000001 * x6
sol_hs098 = np.array([0.268565, 5.23749e-21, 8.47671e-21, 0.028, 0.0134, 0])
ineq1_hs098 = -159.90000000000001 * x1 - 587 * x3 - 391 * x4 - 2198 * x5 + 311 * x6 + 14000 * x1 * x5 - 173.02000000000001
ineq2_hs098 = (70) * x3 + 819 * x4 + 273 * x6 - 26000 * x3 * x4 - 124.08
ineq3_hs098 = -17.100000000000001 * x1 - 204.19999999999999 * x2 - 212.30000000000001 * x3 - 623.39999999999998 * x4 - 1495.5 * x5 - 38.200000000000003 * x6 + 169 * x1 * x2 + 3580 * x2 * x4 + 3810 * x3 * x4 + 18500 * x3 * x5 + 24300 * x4 * x5 + 32.969999999999999
ineq4_hs098 = -17.899999999999999 * x1 - 113.90000000000001 * x2 - 169.69999999999999 * x3 - 337.80000000000001 * x4 - 1385.2 * x5 - 36.799999999999997 * x6 + 139 * x1 * x2 + 2450 * x3 * x4 + 16600 * x3 * x5 + 17200 * x4 * x5 + 25.120000000000001
cons_hs098 = [{'func':ineq1_hs098, 'type':'ineq', 'prop':'unknown'}, {'func':ineq2_hs098, 'type':'ineq', 'prop':'unknown'}, {'func':ineq3_hs098, 'type':'ineq', 'prop':'unknown'}, {'func':ineq4_hs098, 'type':'ineq', 'prop':'unknown'}]
vars_hs098 = [x1, x2, x3, x4, x5, x6]
bnds_hs098 = [np.array([0, 0.31]), np.array([0, 0.068000000000000005]), np.array([0, 0.042000000000000003]), np.array([0, 0.028000000000000001]), np.array([0, 0.0134]), np.array([0, 0.045999999999999999])]
hs098 = OptimizationProblem('hs098', sol_hs098, symobj_hs098, cons_hs098, vars_hs098, bnds_hs098)

symobj_redeco7 = 0
sol_redeco7 = np.array([0.654799,-0.854233,0.15732,-0.520756,-0.0662201,-0.37091,-0.0618184])
eq1_redeco7 = x1 + x2 + x3 + x4 + x5 + x6 - -1
eq2_redeco7 = x6 - 6 * x7 - 0
eq3_redeco7 = x1 - x7 + x1 * x2 + x2 * x3 + x3 * x4 + x4 * x5 + x5 * x6 - 0
eq4_redeco7 = x5 - 5 * x7 + x1 * x6 - 0
eq5_redeco7 = x2 - 2 * x7 + x1 * x3 + x2 * x4 + x3 * x5 + x4 * x6 - 0
eq6_redeco7 = x4 - 4 * x7 + x1 * x5 + x2 * x6 - 0
eq7_redeco7 = x3 - 3 * x7 + x1 * x4 + x2 * x5 + x3 * x6 - 0
cons_redeco7 = [{'func':eq1_redeco7,'type': 'eq', 'prop': 'convex'},{'func':eq2_redeco7,'type': 'eq', 'prop': 'convex'},{'func':eq3_redeco7,'type': 'eq', 'prop': 'unknown'},{'func':eq4_redeco7,'type': 'eq', 'prop': 'unknown'},{'func':eq5_redeco7,'type': 'eq', 'prop': 'unknown'},{'func':eq6_redeco7,'type': 'eq', 'prop': 'unknown'},{'func':eq7_redeco7,'type': 'eq', 'prop': 'unknown'}]
bnds_redeco7 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_redeco7 = [x1, x2, x3, x4, x5, x6, x7]
redeco7 = OptimizationProblem("redeco7", sol_redeco7, symobj_redeco7, cons_redeco7, vars_redeco7, bnds_redeco7)

symobj_ladders = 0
sol_ladders = np.array([-18.7316354819, -2.9910178412, -33.4334340541, 7.9935511772, -26.7251866592, 42.8022209143, -8.534813887])
eq1_ladders = x1 - x4 - x5
eq2_ladders = (x2**2) + (x4**2) - (x7**2)
eq3_ladders = (x3**2) + (x5**2) - (x6**2)
eq4_ladders = 10 * x6 + (x6 - 30) * x3
eq5_ladders = 60 * x6 + (x4**2) - (x6**2) - 800
eq6_ladders = 10 * x7 + (x7 - 20) * x2
eq7_ladders = (-30) * x3 + (x3 + 10) * x6
eq8_ladders = 40 * x7 - (x7**2) + (x5**2) - 300
eq9_ladders = (-20) * x2 + (x2 + 10) * x7
eq10_ladders = 20 * x4 - x1 * x7
eq11_ladders = 30 * x5 - x1 * x6
eq12_ladders = (x1**2) + (x2 + 20) * x2 - 300
eq13_ladders = (x1**2) + (x3 + 20) * x3 - 800
cons_ladders = [{'func':eq1_ladders, 'type':'eq', 'prop':'convex'}, {'func':eq2_ladders, 'type':'eq', 'prop':'unknown'}, {'func':eq3_ladders, 'type':'eq', 'prop':'unknown'}, {'func':eq4_ladders, 'type':'eq', 'prop':'unknown'}, {'func':eq5_ladders, 'type':'eq', 'prop':'unknown'}, {'func':eq6_ladders, 'type':'eq', 'prop':'unknown'}, {'func':eq7_ladders, 'type':'eq', 'prop':'unknown'}, {'func':eq8_ladders, 'type':'eq', 'prop':'unknown'}, {'func':eq9_ladders, 'type':'eq', 'prop':'unknown'}, {'func':eq10_ladders, 'type':'eq', 'prop':'unknown'}, {'func':eq11_ladders, 'type':'eq', 'prop':'unknown'}, {'func':eq12_ladders, 'type':'eq', 'prop':'unknown'}, {'func':eq13_ladders, 'type':'eq', 'prop':'unknown'}]
vars_ladders = [x1, x2, x3, x4, x5, x6, x7]
bnds_ladders = [np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000])]
ladders = OptimizationProblem('ladders', sol_ladders, symobj_ladders, cons_ladders, vars_ladders, bnds_ladders)

symobj_meanvar = 21.09 * (x1**2) + 35.445 * (x2**2) + 12.755000000000001 * (x3**2) + 11.164999999999999 * (x4**2) + 15.005000000000001 * (x5**2) + 21.114999999999998 * (x6**2) + 8.2100000000000009 * (x7**2) + x4 * x7 + 20.18 * x1 * x2 + 5.4400000000000004 * x1 * x3 + 2.6499999999999999 * x1 * x4 + 6.1600000000000001 * x1 * x5 + 11.92 * x1 * x6 + 8.7050000000000001 * x1 * x7 + 10.789999999999999 * x2 * x3 + 7.7050000000000001 * x2 * x4 + 11.619999999999999 * x2 * x5 + 11.9 * x2 * x6 + 6.3099999999999996 * x2 * x7 + 5.4400000000000004 * x1 * x3 + 10.789999999999999 * x2 * x3 + 4.7999999999999998 * x3 * x4 + 11.315 * x3 * x5 + 6.6100000000000003 * x3 * x6 + 2.3500000000000001 * x3 * x7 + 2.6499999999999999 * x1 * x4 + 7.7050000000000001 * x2 * x4 + 4.7999999999999998 * x3 * x4 + 5.1600000000000001 * x4 * x5 + 5.2300000000000004 * x4 * x6 + 6.1600000000000001 * x1 * x5 + 11.619999999999999 * x2 * x5 + 11.315 * x3 * x5 + 5.1600000000000001 * x4 * x5 + 8.1799999999999997 * x5 * x6 + 3.6000000000000001 * x5 * x7 + 11.92 * x1 * x6 + 11.9 * x2 * x6 + 6.6100000000000003 * x3 * x6 + 5.2300000000000004 * x4 * x6 + 8.1799999999999997 * x5 * x6 + 9.9000000000000004 * x6 * x7 + 8.7050000000000001 * x1 * x7 + 6.3099999999999996 * x2 * x7 + 2.3500000000000001 * x3 * x7 + 3.6000000000000001 * x5 * x7
sol_meanvar = np.array([0,0,0.0144299,0.464722,2.09909e-20,0.0904447,0.430404,0.115])
eq1_meanvar = x1 + x2 + x3 + x4 + x5 + x6 + x7 - 1
eq2_meanvar = (-0.12870000000000001) * x1 - 0.1096 * x2 - 0.050099999999999999 * x3 - 0.15240000000000001 * x4 - 0.076300000000000007 * x5 - 0.18540000000000001 * x6 - 0.062 * x7 + x8 - 0
cons_meanvar = [{'func':eq1_meanvar,'type': 'eq', 'prop': 'convex'},{'func':eq2_meanvar,'type': 'eq', 'prop': 'convex'}]
bnds_meanvar = [np.array([0, 1]), np.array([0, 1]), np.array([0, 1]), np.array([0, 1]), np.array([0, 1]), np.array([0, 1]), np.array([0, 1]), np.array([0.115, 0.115])]
vars_meanvar = [x1, x2, x3, x4, x5, x6, x7, x8]
meanvar = OptimizationProblem("meanvar", sol_meanvar, symobj_meanvar, cons_meanvar, vars_meanvar, bnds_meanvar)

symobj_discret3 = 0
sol_discret3 = np.array([2.60554,2.78811,2.41699,1.80763,2.01919,2.22184,1.34424,1.58457])
eq1_discret3 = 4.1261870974784403 * x7 - 0.13753956991594801 * (x7**2) - 0.034384892478987003 * x1 * x7 - 0.039297019975985198 * x3 * x7 - 0.068769784957974006 * x4 * x7 - 0.055015827966379202 * x5 * x7 - 0.045846523305316002 * x6 * x7 - 0.091693046610632004 * x7 * x8 - 4.4012662373103399
eq2_discret3 = 3.7706363994307801 * x2 - 0.134067071979761 * x1 * x2 - 0.143643291406887 * x2 * x3 - 0.18281873451785599 * x2 * x4 - 0.167583839974702 * x2 * x5 - 0.154692775361263 * x2 * x6 - 0.22344511996626901 * x2 * x7 - 0.20110060796964199 * x2 * x8 - 4.0220121593928404
eq3_discret3 = 3.7909702490275499 * x1 - 0.126365674967585 * (x1**2) - 0.13608611150355299 * x1 * x3 - 0.17691194495461901 * x1 * x4 - 0.160829040867835 * x1 * x5 - 0.14742662079551599 * x1 * x6 - 0.22113993119327399 * x1 * x7 - 0.19656882772735401 * x1 * x8 - 4.0437015989627199
eq4_discret3 = 4.0109410738286702 * x8 - 0.13369803579428899 * (x8**2) - 0.17826404772571899 * x7 * x8 - 0.059421349241906202 * x1 * x8 - 0.066849017897144494 * x3 * x8 - 0.10695842863543099 * x4 * x8 - 0.089132023862859303 * x5 * x8 - 0.076398877596736497 * x6 * x8 - 4.2783371454172503
eq5_discret3 = 3.8156285426954102 * x3 - 0.12718761808984699 * (x3**2) - 0.11740395515985901 * x1 * x3 - 0.16958349078646301 * x3 * x4 - 0.15262514170781599 * x3 * x5 - 0.138750128825288 * x3 * x6 - 0.218035916725452 * x3 * x7 - 0.19078142713477 * x3 * x8 - 4.0700037788751002
eq6_discret3 = 3.8462210482499199 * x6 - 0.12820736827499701 * (x6**2) - 0.106839473562498 * x1 * x6 - 0.11655215297726999 * x3 * x6 - 0.16025921034374699 * x4 * x6 - 0.14245263141666401 * x5 * x6 - 0.21367894712499599 * x6 * x7 - 0.183153383249996 * x6 * x8 - 4.1026357847999098
eq7_discret3 = 3.88531963403948 * x5 - 0.12951065446798299 * (x5**2) - 0.094189566885805501 * x1 * x5 - 0.10360852357438601 * x3 * x5 - 0.148012176534837 * x4 * x5 - 0.115120581749318 * x5 * x6 - 0.20721704714877201 * x5 * x7 - 0.17268087262397699 * x5 * x8 - 4.1443409429754396
eq8_discret3 = 3.93736328599701 * x4 - 0.131245442866567 * (x4**2) - 0.078747265719940299 * x1 * x4 - 0.087496961911044793 * x3 * x4 - 0.11249609388562901 * x4 * x5 - 0.0984340821499253 * x4 * x6 - 0.19686816429985099 * x4 * x7 - 0.15749453143988101 * x4 * x8 - 4.1998541717301503
cons_discret3 = [{'func':eq1_discret3,'type': 'eq', 'prop': 'unknown'},{'func':eq2_discret3,'type': 'eq', 'prop': 'unknown'},{'func':eq3_discret3,'type': 'eq', 'prop': 'unknown'},{'func':eq4_discret3,'type': 'eq', 'prop': 'unknown'},{'func':eq5_discret3,'type': 'eq', 'prop': 'unknown'},{'func':eq6_discret3,'type': 'eq', 'prop': 'unknown'},{'func':eq7_discret3,'type': 'eq', 'prop': 'unknown'},{'func':eq8_discret3,'type': 'eq', 'prop': 'unknown'}]
bnds_discret3 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_discret3 = [x1, x2, x3, x4, x5, x6, x7, x8]
discret3 = OptimizationProblem("discret3", sol_discret3, symobj_discret3, cons_discret3, vars_discret3, bnds_discret3)

symobj_eco9 = 0
sol_eco9 = np.array([1.53785,0.224122,-1.17811,-0.258552,0.386083,-1.40486,0.602632,-0.909159])
eq1_eco9 = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + 1
eq2_eco9 = x1 - ((- x7) + 0.125) * x8 + x2 * (x1 + x3) + x4 * (x3 + x5) + x6 * (x5 + x7) - 0
eq3_eco9 = x7 - ((- x1) + 0.875) * x8 - 0
eq4_eco9 = x6 + x1 * x7 - ((- x2) + 0.75) * x8 - 0
eq5_eco9 = x5 + x1 * x6 + x2 * x7 - ((- x3) + 0.625) * x8 - 0
eq6_eco9 = x2 + x5 * x7 - ((- x6) + 0.25) * x8 + x3 * (x1 + x5) + x4 * (x2 + x6) - 0
eq7_eco9 = x4 + x1 * x5 + x2 * x6 + x3 * x7 - ((- x4) + 0.5) * x8 - 0
eq8_eco9 = x2 * x5 + (x6 + 1) * x3 - ((- x5) + 0.375) * x8 + x4 * (x1 + x7) - 0
cons_eco9 = [{'func':eq1_eco9,'type': 'eq', 'prop': 'convex'},{'func':eq2_eco9,'type': 'eq', 'prop': 'unknown'},{'func':eq3_eco9,'type': 'eq', 'prop': 'unknown'},{'func':eq4_eco9,'type': 'eq', 'prop': 'unknown'},{'func':eq5_eco9,'type': 'eq', 'prop': 'unknown'},{'func':eq6_eco9,'type': 'eq', 'prop': 'unknown'},{'func':eq7_eco9,'type': 'eq', 'prop': 'unknown'},{'func':eq8_eco9,'type': 'eq', 'prop': 'unknown'}]
bnds_eco9 = [np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100])]
vars_eco9 = [x1, x2, x3, x4, x5, x6, x7, x8]
eco9 = OptimizationProblem("eco9", sol_eco9, symobj_eco9, cons_eco9, vars_eco9, bnds_eco9)

symobj_ipp = 0
sol_ipp = np.array([-0.5636326343,0.8260255768,0.3590420181,0.9333213965,-0.8618968518,-0.5070836389,0.9115095274,0.4112789581])
eq1_ipp = (x1**2) + (x2**2) - 1
eq2_ipp = (x3**2) + (x4**2) - 1
eq3_ipp = (x5**2) + (x6**2) - 1
eq4_ipp = (x7**2) + (x8**2) - 1
eq5_ipp = 0.074052387999999997 * x1 - 0.083050030999999996 * x2 - 0.38615960999999999 * x3 - 0.75526603000000003 * x4 + 0.50420167999999999 * x5 - 1.0916287 * x6 + 0.40026383999999998 * x8 - 0.24915068000000001 * x1 * x3 + 1.6091354 * x1 * x4 + 0.27942342999999997 * x2 * x3 + 1.4348015999999999 * x2 * x4 + 0.40026383999999998 * x5 * x8 - 0.80052767999999996 * x6 * x7 + 0.049207290000000001
eq6_ipp = (-0.20816984999999999) * x1 + 2.6868319999999999 * x2 - 0.69910317 * x3 + 0.35744413000000003 * x4 + 1.2499117 * x5 + 1.4677359999999999 * x6 + 1.1651720000000001 * x7 + 1.10763397 * x8 + 1.4894772999999999 * x1 * x3 + 0.23062341 * x1 * x4 + 1.3281073000000001 * x2 * x3 - 0.25864503 * x2 * x4 + 1.1651720000000001 * x5 * x7 - 0.26908493999999999 * x5 * x8 + 0.53816987000000005 * x6 * x7 + 0.58258597999999995 * x6 * x8 - 0.69686809000000005
eq7_ipp = 0.19594661999999999 * x1 - 1.2280342 * x2 - 0.079034221000000002 * x4 + 0.026387877000000001 * x5 - 0.057131429999999997 * x6 - 1.1628080999999999 * x7 + 1.2587767000000001 * x8 + 0.29070203 * x5 * x7 - 0.63555006999999997 * x1 * x3 - 0.11571992 * x1 * x4 - 0.66640447999999997 * x2 * x3 + 0.11036211 * x2 * x4 + 1.2587767000000001 * x5 * x8 - 0.62938835999999998 * x6 * x7 + 0.58140406 * x6 * x8 + 2.1625749999999999
eq8_ipp = (-0.037157269999999999) * x1 + 0.035436896000000002 * x2 + 0.085383481999999997 * x3 - 0.039251966999999999 * x5 - 0.43241927000000002 * x7 + 0.12501635 * x1 * x3 - 0.68660736 * x1 * x4 - 0.11922812000000001 * x2 * x3 - 0.71994047000000005 * x2 * x4 - 0.43241927000000002 * x5 * x7 - 0.86483854999999998 * x6 * x8 - -0.01387301
cons_ipp = [{'func':eq1_ipp,'type': 'eq', 'prop': 'unknown'},{'func':eq2_ipp,'type': 'eq', 'prop': 'unknown'},{'func':eq3_ipp,'type': 'eq', 'prop': 'unknown'},{'func':eq4_ipp,'type': 'eq', 'prop': 'unknown'},{'func':eq5_ipp,'type': 'eq', 'prop': 'unknown'},{'func':eq6_ipp,'type': 'eq', 'prop': 'unknown'},{'func':eq7_ipp,'type': 'eq', 'prop': 'unknown'},{'func':eq8_ipp,'type': 'eq', 'prop': 'unknown'}]
bnds_ipp = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_ipp = [x1, x2, x3, x4, x5, x6, x7, x8]
ipp = OptimizationProblem("ipp", sol_ipp, symobj_ipp, cons_ipp, vars_ipp, bnds_ipp)

symobj_kear11 = 0
sol_kear11 = np.array([0.671554,0.740955,0.95473,0.297474,0.128778,-0.991673,0.969312,0.245835])
eq1_kear11 = (-0.76229999999999998) * x1 + 0.2238 * x2 - -0.34610000000000002
eq2_kear11 = (x1**2) + (x2**2) - 1
eq3_kear11 = (x3**2) + (x4**2) - 1
eq4_kear11 = 0.35780000000000001 * x1 + 0.004731 * x2 + x6 * x8 - 0
eq5_kear11 = 0.26379999999999998 * x1 - 0.077450000000000005 * x2 - 0.6734 * x4 + 0.2238 * x1 * x3 + 0.76229999999999998 * x2 * x3 - 0.60219999999999996
eq6_kear11 = (x5**2) + (x6**2) - 1
eq7_kear11 = (x7**2) + (x8**2) - 1
eq8_kear11 = (-0.12379999999999999) * x1 - 0.001637 * x2 - 0.93379999999999996 * x4 + x7 + 0.004731 * x1 * x3 - 0.35780000000000001 * x2 * x3 - 0.35709999999999997
cons_kear11 = [{'func':eq1_kear11,'type': 'eq', 'prop': 'unknown'},{'func':eq2_kear11,'type': 'eq', 'prop': 'unknown'},{'func':eq3_kear11,'type': 'eq', 'prop': 'unknown'},{'func':eq4_kear11,'type': 'eq', 'prop': 'unknown'},{'func':eq5_kear11,'type': 'eq', 'prop': 'unknown'},{'func':eq6_kear11,'type': 'eq', 'prop': 'unknown'},{'func':eq7_kear11,'type': 'eq', 'prop': 'unknown'},{'func':eq8_kear11,'type': 'eq', 'prop': 'unknown'}]
bnds_kear11 = [np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1])]
vars_kear11 = [x1, x2, x3, x4, x5, x6, x7, x8]
kear11 = OptimizationProblem("kear11", sol_kear11, symobj_kear11, cons_kear11, vars_kear11, bnds_kear11)

symobj_kin2 = 0
sol_kin2 = np.array([0.977922,0.208971,0.0261133,0.999659,-0.0978686,0.995199,0.0770736,-0.997025])
eq1_kin2 = (x1**2) + (x2**2) - 1
eq2_kin2 = (x3**2) + (x4**2) - 1
eq3_kin2 = (x5**2) + (x6**2) - 1
eq4_kin2 = (x7**2) + (x8**2) - 1
eq5_kin2 = 0.074052387999999997 * x1 - 0.083050030999999996 * x2 + 0.50420167999999999 * x5 + (0.40026383999999998 * x5 + 0.049207290000000001) * x8 + ((-0.80052767999999996) * x7 - 1.0916287) * x6 + x3 * ((-0.24915068000000001) * x1 + 0.27942342999999997 * x2 - 0.38615960999999999) + x4 * (1.6091354 * x1 + 1.4348015999999999 * x2 - 0.75526603000000003) - -0.049207290000000001
eq6_kin2 = (-0.20816984999999999) * x1 + 2.6868319999999999 * x2 + 1.2499117 * x5 + 1.4677359999999999 * x6 + x3 * (1.4894772999999999 * x1 + 1.3281073000000001 * x2 - 0.69910317) + x4 * (0.23062341 * x1 - 0.25864503 * x2 + 0.35744413000000003) + x7 * (1.1651720000000001 * x5 + 0.53816987000000005 * x6 + 1.1651720000000001) + x8 * ((-0.26908493999999999) * x5 + 0.58258597999999995 * x6 + 1.0763396999999999) - 0.69686809000000005
eq7_kin2 = 0.19594661999999999 * x1 - 1.2280342 * x2 + 0.026387877000000001 * x5 - 0.057131429999999997 * x6 + x3 * ((-0.63555006999999997) * x1 - 0.66640447999999997 * x2) + x4 * ((-0.11571992) * x1 + 0.11036211 * x2 - 0.079034221000000002) + x7 * (0.29070203 * x5 - 0.62938835999999998 * x6 - 1.1628080999999999) + x8 * (1.2587767000000001 * x5 + 0.58140406 * x6 + 1.2587767000000001) - -2.1625749999999999
eq8_kin2 = (-0.037157269999999999) * x1 + 0.035436896000000002 * x2 - 0.039251966999999999 * x5 - 0.86483854999999998 * x6 * x8 + ((-0.43241927000000002) * x5 - 0.43241927000000002) * x7 + x3 * (0.12501635 * x1 - 0.11922812000000001 * x2 + 0.085383481999999997) + x4 * ((-0.68660736) * x1 - 0.71994047000000005 * x2) - -0.01387301
cons_kin2 = [{'func':eq1_kin2,'type': 'eq', 'prop': 'unknown'},{'func':eq2_kin2,'type': 'eq', 'prop': 'unknown'},{'func':eq3_kin2,'type': 'eq', 'prop': 'unknown'},{'func':eq4_kin2,'type': 'eq', 'prop': 'unknown'},{'func':eq5_kin2,'type': 'eq', 'prop': 'unknown'},{'func':eq6_kin2,'type': 'eq', 'prop': 'unknown'},{'func':eq7_kin2,'type': 'eq', 'prop': 'unknown'},{'func':eq8_kin2,'type': 'eq', 'prop': 'unknown'}]
bnds_kin2 = [np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]),np.array([-1, 1]),np.array([-1, 1])]
vars_kin2 = [x1, x2, x3, x4, x5, x6, x7, x8]
kin2 = OptimizationProblem("kin2", sol_kin2, symobj_kin2, cons_kin2, vars_kin2, bnds_kin2)

symobj_kink = 0
sol_kink = np.array([0.671554,0.740955,0.95473,0.297474,0.128778,-0.991673,0.969312,0.245835])
eq1_kink = (-0.76229999999999998) * x1 + 0.2238 * x2 - -0.34610000000000002
eq2_kink = (x1**2) + (x2**2) - 1
eq3_kink = (x3**2) + (x4**2) - 1
eq4_kink = 0.35780000000000001 * x1 + 0.004731 * x2 + x6 * x8 - 0
eq5_kink = 0.26379999999999998 * x1 - 0.077450000000000005 * x2 - 0.6734 * x4 + 0.2238 * x1 * x3 + 0.76229999999999998 * x2 * x3 - 0.60219999999999996
eq6_kink = (x5**2) + (x6**2) - 1
eq7_kink = (x7**2) + (x8**2) - 1
eq8_kink = (-0.12379999999999999) * x1 - 0.001637 * x2 - 0.93379999999999996 * x4 + x7 + 0.004731 * x1 * x3 - 0.35780000000000001 * x2 * x3 - 0.35709999999999997
cons_kink = [{'func':eq1_kink,'type': 'eq', 'prop': 'unknown'},{'func':eq2_kink,'type': 'eq', 'prop': 'unknown'},{'func':eq3_kink,'type': 'eq', 'prop': 'unknown'},{'func':eq4_kink,'type': 'eq', 'prop': 'unknown'},{'func':eq5_kink,'type': 'eq', 'prop': 'unknown'},{'func':eq6_kink,'type': 'eq', 'prop': 'unknown'},{'func':eq7_kink,'type': 'eq', 'prop': 'unknown'},{'func':eq8_kink,'type': 'eq', 'prop': 'unknown'}]
bnds_kink = [np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1]), np.array([-1, 1])]
vars_kink = [x1, x2, x3, x4, x5, x6, x7, x8]
kink = OptimizationProblem("kink", sol_kink, symobj_kink, cons_kink, vars_kink, bnds_kink)

symobj_nauheim = 0
sol_nauheim = np.array([-0.9984478660,-0.1806010465,0.2196069929,0.7151726480,0.1057627501,0.0643026161,-0.1408615420,-0.4941157341])
eq1_nauheim = 9 * x1 - 7 * x7 - -8
eq2_nauheim = 9 * x2 + 6 * x7 - 5 * x8 - 0
eq3_nauheim = 7 * x1 + 8 * x4 - 9 * x7 - 0
eq4_nauheim = 9 * x3 + 4 * x8 - 0
eq5_nauheim = 2 * x2 * x6 + x3 * x5 - 0
eq6_nauheim = 4 * x1 * x6 + 3 * x2 * x5 + 2 * x3 * x4 - 0
eq7_nauheim = 5 * x2 + 7 * x5 - 9 * x8 + 6 * x1 * x4 - 0
eq8_nauheim = 3 * x3 + 6 * x6 + 5 * x1 * x5 + 4 * x2 * x4 - 0
cons_nauheim = [{'func':eq1_nauheim,'type': 'eq', 'prop': 'convex'},{'func':eq2_nauheim,'type': 'eq', 'prop': 'convex'},{'func':eq3_nauheim,'type': 'eq', 'prop': 'convex'},{'func':eq4_nauheim,'type': 'eq', 'prop': 'convex'},{'func':eq5_nauheim,'type': 'eq', 'prop': 'unknown'},{'func':eq6_nauheim,'type': 'eq', 'prop': 'unknown'},{'func':eq7_nauheim,'type': 'eq', 'prop': 'unknown'},{'func':eq8_nauheim,'type': 'eq', 'prop': 'unknown'}]
bnds_nauheim = [np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000])]
vars_nauheim = [x1, x2, x3, x4, x5, x6, x7, x8]
nauheim = OptimizationProblem("nauheim", sol_nauheim, symobj_nauheim, cons_nauheim, vars_nauheim, bnds_nauheim)

symobj_puma = 0
sol_puma = np.array([0.671554,0.740955,0.95473,0.297474,0.128778,-0.991673,0.969312,0.245835])
eq1_puma = (-0.76229999999999998) * x1 + 0.2238 * x2 - -0.34610000000000002
eq2_puma = (x1**2) + (x2**2) - 1
eq3_puma = (x3**2) + (x4**2) - 1
eq4_puma = (x5**2) + (x6**2) - 1
eq5_puma = (x7**2) + (x8**2) - 1
eq6_puma = (-0.12379999999999999) * x1 - 0.001637 * x2 - 0.93379999999999996 * x4 + x7 + 0.004731 * x1 * x3 - 0.35780000000000001 * x2 * x3 - 0.35709999999999997
eq7_puma = 0.35780000000000001 * x1 + 0.004731 * x2 + x6 * x8 - 0
eq8_puma = 0.26379999999999998 * x1 - 0.077450000000000005 * x2 - 0.6734 * x4 + 0.2238 * x1 * x3 + 0.76229999999999998 * x2 * x3 - 0.60219999999999996
cons_puma = [{'func':eq1_puma,'type': 'eq', 'prop': 'unknown'},{'func':eq2_puma,'type': 'eq', 'prop': 'unknown'},{'func':eq3_puma,'type': 'eq', 'prop': 'unknown'},{'func':eq4_puma,'type': 'eq', 'prop': 'unknown'},{'func':eq5_puma,'type': 'eq', 'prop': 'unknown'},{'func':eq6_puma,'type': 'eq', 'prop': 'unknown'},{'func':eq7_puma,'type': 'eq', 'prop': 'unknown'},{'func':eq8_puma,'type': 'eq', 'prop': 'unknown'}]
bnds_puma = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_puma = [x1, x2, x3, x4, x5, x6, x7, x8]
puma = OptimizationProblem("puma", sol_puma, symobj_puma, cons_puma, vars_puma, bnds_puma)

symobj_redeco8 = 0
sol_redeco8 = np.array([-0.1428571429,-0.1428571429,-0.1428571429,-0.1428571429,-0.1428571429,-0.1428571429,-0.1428571429,-0.0204081633])
eq1_redeco8 = x1 + x2 + x3 + x4 + x5 + x6 + x7 - -1
eq2_redeco8 = x7 - 7 * x8 - 0
eq3_redeco8 = x1 - x8 + x1 * x2 + x2 * x3 + x3 * x4 + x4 * x5 + x5 * x6 + x6 * x7 - 0
eq4_redeco8 = x6 - 6 * x8 + x1 * x7 - 0
eq5_redeco8 = x5 - 5 * x8 + x1 * x6 + x2 * x7 - 0
eq6_redeco8 = x2 - 2 * x8 + x1 * x3 + x2 * x4 + x3 * x5 + x4 * x6 + x5 * x7 - 0
eq7_redeco8 = x4 - 4 * x8 + x1 * x5 + x2 * x6 + x3 * x7 - 0
eq8_redeco8 = x3 - 3 * x8 + x1 * x4 + x2 * x5 + x3 * x6 + x4 * x7 - 0
cons_redeco8 = [{'func':eq1_redeco8,'type': 'eq', 'prop': 'convex'},{'func':eq2_redeco8,'type': 'eq', 'prop': 'convex'},{'func':eq3_redeco8,'type': 'eq', 'prop': 'unknown'},{'func':eq4_redeco8,'type': 'eq', 'prop': 'unknown'},{'func':eq5_redeco8,'type': 'eq', 'prop': 'unknown'},{'func':eq6_redeco8,'type': 'eq', 'prop': 'unknown'},{'func':eq7_redeco8,'type': 'eq', 'prop': 'unknown'},{'func':eq8_redeco8,'type': 'eq', 'prop': 'unknown'}]
bnds_redeco8 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_redeco8 = [x1, x2, x3, x4, x5, x6, x7, x8]
redeco8 = OptimizationProblem("redeco8", sol_redeco8, symobj_redeco8, cons_redeco8, vars_redeco8, bnds_redeco8)

symobj_s9_1 = 0
sol_s9_1 = np.array([-0.9984478660,-0.1806010465,0.2196069929,0.7151726480,0.1057627501,0.0643026161,-0.1408615420,-0.4941157341])
eq1_s9_1 = 9 * x1 - 7 * x7 - -8
eq2_s9_1 = 9 * x2 + 6 * x7 - 5 * x8 - 0
eq3_s9_1 = (-7) * x1 - 8 * x4 + 9 * x7 - 0
eq4_s9_1 = 9 * x3 + 4 * x8 - 0
eq5_s9_1 = (-2) * x2 * x6 - x3 * x5 - 0
eq6_s9_1 = (-4) * x1 * x6 - 3 * x2 * x5 - 2 * x3 * x4 - 0
eq7_s9_1 = (-5) * x2 - 7 * x5 + 9 * x8 - 6 * x1 * x4 - 0
eq8_s9_1 = (-3) * x3 - 6 * x6 - 5 * x1 * x5 - 4 * x2 * x4 - 0
cons_s9_1 = [{'func':eq1_s9_1,'type': 'eq', 'prop': 'convex'},{'func':eq2_s9_1,'type': 'eq', 'prop': 'convex'},{'func':eq3_s9_1,'type': 'eq', 'prop': 'convex'},{'func':eq4_s9_1,'type': 'eq', 'prop': 'convex'},{'func':eq5_s9_1,'type': 'eq', 'prop': 'unknown'},{'func':eq6_s9_1,'type': 'eq', 'prop': 'unknown'},{'func':eq7_s9_1,'type': 'eq', 'prop': 'unknown'},{'func':eq8_s9_1,'type': 'eq', 'prop': 'unknown'}]
bnds_s9_1 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_s9_1 = [x1, x2, x3, x4, x5, x6, x7, x8]
s9_1 = OptimizationProblem("s9_1", sol_s9_1, symobj_s9_1, cons_s9_1, vars_s9_1, bnds_s9_1)

symobj_bellido = 0
sol_bellido = np.array([9.3916661681, 9.2476345419, 2.6415631705, 7.9626675077, 5.1949976754, 6.3204349074, 5.0133097151, 6.5045382606, 10.9665507117])
eq1_bellido = x1 + x3 - 2 * x4 + x5 - x6 + 2 * x7 - 2 * x8 + 8
eq2_bellido = x1 + x2 + 2 * x3 + 2 * x4 + 2 * x6 - 2 * x7 + x8 - x9 - 38
eq3_bellido = 2 * x2 + 2 * x3 - x4 - x5 - 2 * x6 - x7 - x9 + 18
eq4_bellido = (-12) * x1 + x1**2 + x2**2 + x3**2 - 68
eq5_bellido = (-12) * x5 + x4**2 + x5**2 + x6**2 - 68
eq6_bellido = (-6) * x5 - 12 * x8 - 6 * x9 + x4 * x7 + x5 * x8 + x6 * x9 + 32
eq7_bellido = (-24) * x8 - 12 * x9 + x7**2 + x8**2 + x9**2 + 100
eq8_bellido = (-6) * x1 - 12 * x8 - 6 * x9 + x1 * x7 + x2 * x8 + x3 * x9 + 64
eq9_bellido = (-6) * x1 - 6 * x5 + x1 * x4 + x2 * x5 + x3 * x6 - 52
cons_bellido = [{'func':eq1_bellido, 'type':'eq', 'prop':'unknown'}, {'func':eq2_bellido, 'type':'eq', 'prop':'unknown'}, {'func':eq3_bellido, 'type':'eq', 'prop':'unknown'}, {'func':eq4_bellido, 'type':'eq', 'prop':'unknown'}, {'func':eq5_bellido, 'type':'eq', 'prop':'unknown'}, {'func':eq6_bellido, 'type':'eq', 'prop':'unknown'}, {'func':eq7_bellido, 'type':'eq', 'prop':'unknown'}, {'func':eq8_bellido, 'type':'eq', 'prop':'unknown'}, {'func':eq9_bellido, 'type':'eq', 'prop':'unknown'}]
vars_bellido = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
bnds_bellido = [np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000])]
bellido = OptimizationProblem('bellido', sol_bellido, symobj_bellido, cons_bellido, vars_bellido, bnds_bellido)

symobj_kapur = 0
sol_kapur = np.array([1.3552017928,3.2156376596,2.5470511926,0.1404910598,2.6875422524,4.5708394524,0.3578379213,4.3578379213,2.9661096069])
eq1_kapur = -x1 - x2 + x6 - 0
eq2_kapur = -x3 - x4 + x5 - 0
eq3_kapur = x7 + x2 * x5 - 9
eq4_kapur = x7 + x1 * x5 - 4
eq5_kapur = x8 - x1 * x2 - 0
eq6_kapur = x7 - x3 * x4 - 0
eq7_kapur = x8 + x4 * x6 - 5
eq8_kapur = (-9) * x9 + 2 * x5 * x8 + 2 * x6 * x7 - 0
eq9_kapur = x8 + x3 * x6 - 16
cons_kapur = [{'func':eq1_kapur,'type': 'eq', 'prop': 'convex'},{'func':eq2_kapur,'type': 'eq', 'prop': 'convex'},{'func':eq3_kapur,'type': 'eq'},{'func':eq4_kapur,'type': 'eq'},{'func':eq5_kapur,'type': 'eq'},{'func':eq6_kapur,'type': 'eq'},{'func':eq7_kapur,'type': 'eq'},{'func':eq8_kapur,'type': 'eq'},{'func':eq9_kapur,'type': 'eq'}]
bnds_kapur = [np.array([0, 1000]), np.array([0, 1000]), np.array([0, 1000]), np.array([0, 1000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([0, 1000])]
vars_kapur = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
kapur = OptimizationProblem("kapur", sol_kapur, symobj_kapur, cons_kapur, vars_kapur, bnds_kapur)

symobj_kinema = 0
sol_kinema = np.array([5.1422604971,8.3190211463,5.8359378092,1.0548391333,10.4491459122,9.1155041032,1.8911493054,10.9922302297,14.6837753538])
eq1_kinema = x1 + x3 - 2 * x4 + x5 - x6 + 2 * x7 - 2 * x8 + 8
eq2_kinema = x1 + x2 + 2 * x3 + 2 * x4 + 2 * x6 - 2 * x7 + x8 - x9 - 38
eq3_kinema = 2 * x2 + 2 * x3 - x4 - x5 - 2 * x6 - x7 - x9 + 18
eq4_kinema = (-12) * x1 + (x1**2) + (x2**2) + (x3**2) - 68
eq5_kinema = (-12) * x5 + (x4**2) + (x5**2) + (x6**2) - 68
eq6_kinema = (-24) * x8 - 12 * x9 + (x7**2) + (x8**2) + (x9**2) + 100
eq7_kinema = (-6) * x5 - 12 * x8 - 6 * x9 + x4 * x7 + x5 * x8 + x6 * x9 + 32
eq8_kinema = (-6) * x1 - 6 * x5 + x1 * x4 + x2 * x5 + x3 * x6 - 52
eq9_kinema = (-6) * x1 - 12 * x8 - 6 * x9 + x1 * x7 + x2 * x8 + x3 * x9 + 64
cons_kinema = [{'func':eq1_kinema,'type': 'eq', 'prop': 'convex'},{'func':eq2_kinema,'type': 'eq', 'prop': 'convex'},{'func':eq3_kinema,'type': 'eq', 'prop': 'convex'},{'func':eq4_kinema,'type': 'eq'},{'func':eq5_kinema,'type': 'eq'},{'func':eq6_kinema,'type': 'eq'},{'func':eq7_kinema,'type': 'eq'},{'func':eq8_kinema,'type': 'eq'},{'func':eq9_kinema,'type': 'eq'}]
bnds_kinema = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_kinema = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
kinema = OptimizationProblem("kinema", sol_kinema, symobj_kinema, cons_kinema, vars_kinema, bnds_kinema)

symobj_vrahatis = 0
#sol_vrahatis = np.array([0, 0, 0, 0, -8.47033e-22, -6.52318e-12, 1.79451e-16, -6.20445e-20, 0])
sol_vrahatis = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
eq1_vrahatis = -x2 + x1**2
eq2_vrahatis = -x1 + x9**2
eq3_vrahatis = -x3 + x2**2
eq4_vrahatis = -x9 + x8**2
eq5_vrahatis = -x4 + x3**2
eq6_vrahatis = -x8 + x7**2
eq7_vrahatis = -x5 + x4**2
eq8_vrahatis = -x7 + x6**2
eq9_vrahatis = -x6 + x5**2
cons_vrahatis = [{'func':eq1_vrahatis, 'type':'eq', 'prop':'unknown'}, {'func':eq2_vrahatis, 'type':'eq', 'prop':'unknown'}, {'func':eq3_vrahatis, 'type':'eq', 'prop':'unknown'}, {'func':eq4_vrahatis, 'type':'eq', 'prop':'unknown'}, {'func':eq5_vrahatis, 'type':'eq', 'prop':'unknown'}, {'func':eq6_vrahatis, 'type':'eq', 'prop':'unknown'}, {'func':eq7_vrahatis, 'type':'eq', 'prop':'unknown'}, {'func':eq8_vrahatis, 'type':'eq', 'prop':'unknown'}, {'func':eq9_vrahatis, 'type':'eq', 'prop':'unknown'}]
vars_vrahatis = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
bnds_vrahatis = [np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000]), np.array([-1000, 1000])]
vrahatis = OptimizationProblem('vrahatis', sol_vrahatis, symobj_vrahatis, cons_vrahatis, vars_vrahatis, bnds_vrahatis)

symobj_chemkin = 0
sol_chemkin = np.array([-0.9942302805,-0.4193892828,0.4430190520,0.0917581828,-0.9077859376,-0.5158801861,0.7397012830,0.0555570451,-0.0061090885,-0.7891492397])
eq1_chemkin = x7 + x8 + x9 + x10 - 0
eq2_chemkin = x3 + x4 + x5 + x6 - -0.88888888888888895
eq3_chemkin = x1 + x2 - 2.8284271247461898 * x3 - -2.6666666666666665
eq4_chemkin = (-5.6568542494923806) * x3 + x7 + 9 * (x3**2) - 0
eq5_chemkin = (x1**2) + (x4**2) + (x8**2) - 1
eq6_chemkin = 0.33333333333333331 * x2 + x5 * x6 + x9 * x10 - 0.33333333333333331
eq7_chemkin = (x2**2) + (x5**2) + (x9**2) - 1
eq8_chemkin = x1 * x2 + x4 * x5 + x8 * x9 - 0.33333333333333331
eq9_chemkin = (x6**2) + (x10**2) - 0.88888888888888895
eq10_chemkin = x3 * x4 + x7 * x8 + ((-2.8284271247461898) * x3 + 1) * x1 - 0.33333333333333331
cons_chemkin = [{'func':eq1_chemkin,'type': 'eq', 'prop': 'convex'},{'func':eq2_chemkin,'type': 'eq', 'prop': 'convex'},{'func':eq3_chemkin,'type': 'eq', 'prop': 'convex'},{'func':eq4_chemkin,'type': 'eq'},{'func':eq5_chemkin,'type': 'eq'},{'func':eq6_chemkin,'type': 'eq'},{'func':eq7_chemkin,'type': 'eq'},{'func':eq8_chemkin,'type': 'eq'},{'func':eq9_chemkin,'type': 'eq'},{'func':eq10_chemkin,'type': 'eq'}]
bnds_chemkin = [np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]),np.array([-100000000, 100000000]),np.array([-100000000, 100000000]),np.array([-100000000, 100000000]),np.array([-100000000, 100000000])]
vars_chemkin = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
chemkin = OptimizationProblem("chemkin", sol_chemkin, symobj_chemkin, cons_chemkin, vars_chemkin, bnds_chemkin)

symobj_dccircuit = 0
sol_dccircuit = np.array([10.8283, 10, 0.56909, -0.31183, 0.53206, 0.25726, 0.296239, 0.828299, 0.259209, 0.0389788])
eq1_dccircuit = x1 - x2 - x3 - x9
eq2_dccircuit = -x2 + 4 * x5 + 7 * x8 + 8 * x9
eq3_dccircuit = (-4) * x5 + 6 * x7 + 9 * x10
eq4_dccircuit = 3 * x4 + 5 * x6 - 9 * x10
eq5_dccircuit = 2 * x3 - 3 * x4 - 8 * x9
eq6_dccircuit = -x1 + x2 + x8
eq7_dccircuit = x6 - x7 + x10
eq8_dccircuit = x5 + x7 - x8
eq9_dccircuit = -x4 - x5 + x9 - x10
eq10_dccircuit = x3 + x4 - x6
cons_dccircuit = [{'func':eq1_dccircuit, 'type':'eq', 'prop':'convex'}, {'func':eq2_dccircuit, 'type':'eq', 'prop':'convex'}, {'func':eq3_dccircuit, 'type':'eq', 'prop':'convex'}, {'func':eq4_dccircuit, 'type':'eq', 'prop':'convex'}, {'func':eq5_dccircuit, 'type':'eq', 'prop':'convex'}, {'func':eq6_dccircuit, 'type':'eq', 'prop':'convex'}, {'func':eq7_dccircuit, 'type':'eq', 'prop':'convex'}, {'func':eq8_dccircuit, 'type':'eq', 'prop':'convex'}, {'func':eq9_dccircuit, 'type':'eq', 'prop':'convex'}, {'func':eq10_dccircuit, 'type':'eq', 'prop':'convex'}]
vars_dccircuit = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
bnds_dccircuit = [np.array([-100, 100]), np.array([10, 10]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100]), np.array([-100, 100])]
dccircuit = OptimizationProblem('dccircuit', sol_dccircuit, symobj_dccircuit, cons_dccircuit, vars_dccircuit, bnds_dccircuit)

symobj_ex912 = -x9 - 3 * x10
eq1_ex912 = x5 + 2 * x6 - x7 - x8 + 1
eq2_ex912 = x4 - x10
eq3_ex912 = x3 + 4 * x9 - x10 - 12
eq4_ex912 = x2 + x9 + 2 * x10 - 12
eq5_ex912 = x1 - x9 + x10 - 3
eq6_ex912 = x1 * x5
eq7_ex912 = x2 * x6
eq8_ex912 = x4 * x8
eq9_ex912 = x3 * x7
cons_ex912 = [{'func':eq1_ex912, 'type':'eq', 'prop':'unknown'}, {'func':eq2_ex912, 'type':'eq', 'prop':'unknown'}, {'func':eq3_ex912, 'type':'eq', 'prop':'unknown'}, {'func':eq4_ex912, 'type':'eq', 'prop':'unknown'}, {'func':eq5_ex912, 'type':'eq', 'prop':'unknown'}, {'func':eq6_ex912, 'type':'eq', 'prop':'unknown'}, {'func':eq7_ex912, 'type':'eq', 'prop':'unknown'}, {'func':eq8_ex912, 'type':'eq', 'prop':'unknown'}, {'func':eq9_ex912, 'type':'eq', 'prop':'unknown'}]
vars_ex912 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
bnds_ex912 = [np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000])]
ex9_1_2 = OptimizationProblem('ex912', None, symobj_ex912, cons_ex912, vars_ex912, bnds_ex912)

symobj_ex9_1_4 = x9 - 4 * x10
sol_ex9_1_4 = np.array([24.0000000000,0.0000000000,0.0000000000,14.0000000000,0.0000000000,0.0000000000,0.3333333333,0.0000000000,19.0000000000,14.0000000000])
eq1_ex9_1_4 = x5 + 5 * x6 - 3 * x7 - x8 + 1
eq2_ex9_1_4 = x4 - x10 - 0
eq3_ex9_1_4 = x3 + 2 * x9 - 3 * x10 + 4
eq4_ex9_1_4 = x2 + 2 * x9 + 5 * x10 - 108
eq5_ex9_1_4 = x1 - 2 * x9 + x10 - 0
eq6_ex9_1_4 = x1 * x5 - 0
eq7_ex9_1_4 = x2 * x6 - 0
eq8_ex9_1_4 = x4 * x8 - 0
eq9_ex9_1_4 = x3 * x7 - 0
cons_ex9_1_4 = [{'func':eq1_ex9_1_4,'type': 'eq', 'prop': 'convex'},{'func':eq2_ex9_1_4,'type': 'eq', 'prop': 'convex'},{'func':eq3_ex9_1_4,'type': 'eq', 'prop': 'convex'},{'func':eq4_ex9_1_4,'type': 'eq', 'prop': 'convex'},{'func':eq5_ex9_1_4,'type': 'eq', 'prop': 'convex'},{'func':eq6_ex9_1_4,'type': 'eq'},{'func':eq7_ex9_1_4,'type': 'eq'},{'func':eq8_ex9_1_4,'type': 'eq'},{'func':eq9_ex9_1_4,'type': 'eq'}]
bnds_ex9_1_4 = [np.array([0, 200]), np.array([0, 200]), np.array([0, 200]), np.array([0, 200]), np.array([0, 200]), np.array([0, 200]), np.array([0, 200]), np.array([0, 200]), np.array([0, 10000]), np.array([0, 10000])]
vars_ex9_1_4 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
ex9_1_4 = OptimizationProblem("ex9_1_4", sol_ex9_1_4, symobj_ex9_1_4, cons_ex9_1_4, vars_ex9_1_4, bnds_ex9_1_4)

symobj_ex9_2_1 = (x9 - 5) * (x9 - 5) + (2 * x10 + 1) * (2 * x10 + 1)
sol_ex9_2_1 = np.array([0,3,6,2.66454e-15,3.5,4.05304e-16,0,4.838e-17,1,0])
eq1_ex9_2_1 = x5 - 0.5 * x6 + x7 - x8 - 1.5 * x9 + 2 * x10 - 2
eq2_ex9_2_1 = x4 - x10 - 0
eq3_ex9_2_1 = x3 + x9 + x10 - 7
eq4_ex9_2_1 = x2 + x9 - 0.5 * x10 - 4
eq5_ex9_2_1 = x1 - 3 * x9 + x10 - -3
eq6_ex9_2_1 = x4 * x8 - 0
eq7_ex9_2_1 = x3 * x7 - 0
eq8_ex9_2_1 = x2 * x6 - 0
eq9_ex9_2_1 = x1 * x5 - 0
cons_ex9_2_1 = [{'func':eq1_ex9_2_1,'type': 'eq', 'prop': 'convex'},{'func':eq2_ex9_2_1,'type': 'eq', 'prop': 'convex'},{'func':eq3_ex9_2_1,'type': 'eq', 'prop': 'convex'},{'func':eq4_ex9_2_1,'type': 'eq', 'prop': 'convex'},{'func':eq5_ex9_2_1,'type': 'eq', 'prop': 'convex'},{'func':eq6_ex9_2_1,'type': 'eq'},{'func':eq7_ex9_2_1,'type': 'eq'},{'func':eq8_ex9_2_1,'type': 'eq'},{'func':eq9_ex9_2_1,'type': 'eq'}]
bnds_ex9_2_1 = [np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 10000]), np.array([0, 10000])]
vars_ex9_2_1 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
ex9_2_1 = OptimizationProblem("ex9_2_1", sol_ex9_2_1, symobj_ex9_2_1, cons_ex9_2_1, vars_ex9_2_1, bnds_ex9_2_1)

symobj_ex9_2_7 = (x9 - 5) * (x9 - 5) + (2 * x10 + 1) * (2 * x10 + 1)
sol_ex9_2_7 = np.array([0,3,6,2.66454e-15,3.5,4.05304e-16,0,4.838e-17,1,0])
eq1_ex9_2_7 = x5 - 0.5 * x6 + x7 - x8 - 1.5 * x9 + 2 * x10 - 2
eq2_ex9_2_7 = x4 - x10 - 0
eq3_ex9_2_7 = x3 + x9 + x10 - 7
eq4_ex9_2_7 = x2 + x9 - 0.5 * x10 - 4
eq5_ex9_2_7 = x1 - 3 * x9 + x10 + 3
eq6_ex9_2_7 = x4 * x8 - 0
eq7_ex9_2_7 = x3 * x7 - 0
eq8_ex9_2_7 = x2 * x6 - 0
eq9_ex9_2_7 = x1 * x5 - 0
cons_ex9_2_7 = [{'func':eq1_ex9_2_7,'type': 'eq', 'prop': 'convex'},{'func':eq2_ex9_2_7,'type': 'eq', 'prop': 'convex'},{'func':eq3_ex9_2_7,'type': 'eq', 'prop': 'convex'},{'func':eq4_ex9_2_7,'type': 'eq', 'prop': 'convex'},{'func':eq5_ex9_2_7,'type': 'eq', 'prop': 'convex'},{'func':eq6_ex9_2_7,'type': 'eq'},{'func':eq7_ex9_2_7,'type': 'eq'},{'func':eq8_ex9_2_7,'type': 'eq'},{'func':eq9_ex9_2_7,'type': 'eq'}]
bnds_ex9_2_7 = [np.array([0, 20]), np.array([0, 20]),np.array([0, 20]),np.array([0, 20]),np.array([0, 20]),np.array([0, 20]),np.array([0, 20]),np.array([0, 20]),np.array([0, 10000]),np.array([0, 10000])]
vars_ex9_2_7 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
ex9_2_7 = OptimizationProblem("ex9_2_7", sol_ex9_2_7, symobj_ex9_2_7, cons_ex9_2_7, vars_ex9_2_7, bnds_ex9_2_7)

symobj_genhs28 = (x1 + x2)**2 +(x2 + x3)**2 +(x3 + x4)**2 +(x4 + x5)**2 +(x5 + x6)**2 +(x6 + x7)**2 +(x7 + x8)**2 +(x8 + x9)**2 + (x9 + x10)**2
sol_genhs28 = np.array([0.164213,-0.0520467,0.313294,0.14182,0.134356,0.19649,0.157555,0.1628,0.172282,0.164212])
eq1_genhs28 = x8 + 2 * x9 + 3 * x10 - 1
eq2_genhs28 = x7 + 2 * x8 + 3 * x9 - 1
eq3_genhs28 = x6 + 2 * x7 + 3 * x8 - 1
eq4_genhs28 = x5 + 2 * x6 + 3 * x7 - 1
eq5_genhs28 = x4 + 2 * x5 + 3 * x6 - 1
eq6_genhs28 = x3 + 2 * x4 + 3 * x5 - 1
eq7_genhs28 = x2 + 2 * x3 + 3 * x4 - 1
eq8_genhs28 = x1 + 2 * x2 + 3 * x3 - 1
cons_genhs28 = [{'func':eq1_genhs28,'type': 'eq', 'prop': 'convex'},{'func':eq2_genhs28,'type': 'eq', 'prop': 'convex'},{'func':eq3_genhs28,'type': 'eq', 'prop': 'convex'},{'func':eq4_genhs28,'type': 'eq', 'prop': 'convex'},{'func':eq5_genhs28,'type': 'eq', 'prop': 'convex'},{'func':eq6_genhs28,'type': 'eq', 'prop': 'convex'},{'func':eq7_genhs28,'type': 'eq', 'prop': 'convex'},{'func':eq8_genhs28,'type': 'eq', 'prop': 'convex'}]
bnds_genhs28 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]),np.array([-10000, 10000])]
vars_genhs28 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
genhs28 = OptimizationProblem("genhs28", sol_genhs28, symobj_genhs28, cons_genhs28, vars_genhs28, bnds_genhs28)

symobj_ku = 0
sol_ku = np.array([2.0000000000,-5.0000000000,-1.0000000000,5.0000000000,-4.0000000000,-3.0000000000,3.0000000000,-2.0000000000,4.0000000000,1.0000000000])
eq1_ku = 3 * x2 + 5 * (x2 + 1) * x1 + 55
eq2_ku = x10 + (3 * x10 - 6) * x1 - -5
eq3_ku = 9 * x3 + (7 * x3 + 9) * x2 + 19
eq4_ku = 3 * x10 + (8 * x10 + 4) * x9 - 51
eq5_ku = 6 * x9 + 4 * (x9 + 1) * x8 - -16
eq6_ku = 5 * x4 + (3 * x4 + 6) * x3 - 4
eq7_ku = x8 + (9 * x8 + 7) * x7 + 35
eq8_ku = x7 + (6 * x7 + 7) * x6 + 72
eq9_ku = 7 * x5 + 6 * (x5 + 1) * x4 + 118
eq10_ku = 9 * x6 + (x6 + 3) * x5 + 27
cons_ku = [{'func':eq1_ku,'type': 'eq'},{'func':eq2_ku,'type': 'eq'},{'func':eq3_ku,'type': 'eq'},{'func':eq4_ku,'type': 'eq'},{'func':eq5_ku,'type': 'eq'},{'func':eq6_ku,'type': 'eq'},{'func':eq7_ku,'type': 'eq'},{'func':eq8_ku,'type': 'eq'},{'func':eq9_ku,'type': 'eq'},{'func':eq10_ku,'type': 'eq'}]
bnds_ku = [np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000]), np.array([-100000000, 100000000])]
vars_ku = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
ku = OptimizationProblem("ku", sol_ku, symobj_ku, cons_ku, vars_ku, bnds_ku)

symobj_ku10 = 0
sol_ku10 = np.array([2.0000000000,1.0000000000,-5.0000000000,-1.0000000000,5.0000000000,-4.0000000000,-3.0000000000,3.0000000000,-2.0000000000,4.0000000000])
eq1_ku10 = 5 * x1 + 3 * x3 + 5 * x1 * x3 + 55
eq2_ku10 = (-6) * x1 + x2 + 3 * x1 * x2 + 5
eq3_ku10 = 9 * x3 + 9 * x4 + 7 * x3 * x4 + 19
eq4_ku10 = 3 * x2 + 4 * x10 + 8 * x2 * x10 - 51
eq5_ku10 = 6 * x4 + 5 * x5 + 3 * x4 * x5 - 4
eq6_ku10 = 4 * x9 + 6 * x10 + 4 * x9 * x10 + 16
eq7_ku10 = 7 * x8 + x9 + 9 * x8 * x9 + 35
eq8_ku10 = 6 * x5 + 7 * x6 + 6 * x5 * x6 + 118
eq9_ku10 = 7 * x7 + x8 + 6 * x7 * x8 + 72
eq10_ku10 = 3 * x6 + 9 * x7 + x6 * x7 + 27
cons_ku10 = [{'func':eq1_ku10,'type': 'eq'},{'func':eq2_ku10,'type': 'eq'},{'func':eq3_ku10,'type': 'eq'},{'func':eq4_ku10,'type': 'eq'},{'func':eq5_ku10,'type': 'eq'},{'func':eq6_ku10,'type': 'eq'},{'func':eq7_ku10,'type': 'eq'},{'func':eq8_ku10,'type': 'eq'},{'func':eq9_ku10,'type': 'eq'},{'func':eq10_ku10,'type': 'eq'}]
bnds_ku10 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_ku10 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
ku10 = OptimizationProblem("ku10", sol_ku10, symobj_ku10, cons_ku10, vars_ku10, bnds_ku10)

symobj_ex9_2_2 = (x9**2) + (x10 - 10) * (x10 - 10)
sol_ex9_2_2 = np.array([4.96494e-05,9.99998,10,0.202093,0.000148948,0,2.7117e-23,5.11611e-21,9.99998,9.99998])
eq1_ex9_2_2 = x5 - x6 + x7 + 2 * x9 + 4 * x10 - 60
eq2_ex9_2_2 = x3 + x10 - 20
eq3_ex9_2_2 = x2 - x10 - 0
eq4_ex9_2_2 = x1 + x9 + x10 - 20
eq5_ex9_2_2 = x4 * x8 - 0
eq6_ex9_2_2 = x1 * x5 - 0
eq7_ex9_2_2 = x3 * x7 - 0
eq8_ex9_2_2 = x2 * x6 - 0
ineq1_ex9_2_2 = -x9 + x10 - 0
cons_ex9_2_2 = [{'func':eq1_ex9_2_2,'type': 'eq', 'prop': 'convex'},{'func':eq2_ex9_2_2,'type': 'eq', 'prop': 'convex'},{'func':eq3_ex9_2_2,'type': 'eq', 'prop': 'convex'},{'func':eq4_ex9_2_2,'type': 'eq', 'prop': 'convex'},{'func':eq5_ex9_2_2,'type': 'eq'},{'func':eq6_ex9_2_2,'type': 'eq'},{'func':eq7_ex9_2_2,'type': 'eq'},{'func':eq8_ex9_2_2,'type': 'eq'},{'func':ineq1_ex9_2_2,'type': 'ineq'}]
bnds_ex9_2_2 = [np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 20]), np.array([0, 15]), np.array([0, 10000])]
vars_ex9_2_2 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
ex9_2_2 = OptimizationProblem("ex9_2_2", sol_ex9_2_2, symobj_ex9_2_2, cons_ex9_2_2, vars_ex9_2_2, bnds_ex9_2_2)

symobj_ex2_1_6 = 48 * x1 +42 * x2 +48 * x3 +45 * x4 +44 * x5 +41 * x6 +47 * x7 +42 * x8 +45 * x9 +46 * x10 -50 * x1**2 -50 * x2**2 -50 * x3**2 -50 * x4**2 -50 * x5**2 -50 * x6**2 -50 * x7**2 -50 * x8**2 -50 * x9**2 -50 * x10**2
sol_ex2_1_6 = np.array([1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0])
ineq1_ex2_1_6 = (-8) * x1 +7 * x2 -4 * x3 -5 * x4 -9 * x5 +x6 -7 * x7 -x8 +3 * x9 -2 * x10 - -12
ineq2_ex2_1_6 = 9 * x1 +5 * x2 -9 * x4 +x5 -8 * x6 +3 * x7 -9 * x8 -9 * x9 -3 * x10 - -23
ineq3_ex2_1_6 = (-5) * x1 +6 * x2 +5 * x3 +3 * x4 +8 * x5 -8 * x6 +9 * x7 +2 * x8 -9 * x10 - -6
ineq4_ex2_1_6 = 6 * x1 -5 * x2 +8 * x3 -3 * x4 +x6 +3 * x7 +8 * x8 +9 * x9 -3 * x10 - 22
ineq5_ex2_1_6 = (-2) * x1 -6 * x2 -x3 -3 * x5 -3 * x6 -2 * x7 -6 * x8 -2 * x9 -2 * x10 - -4
cons_ex2_1_6 = [{'func':ineq1_ex2_1_6,'type': 'ineq', 'prop': 'convex'},{'func':ineq2_ex2_1_6,'type': 'ineq', 'prop': 'convex'},{'func':ineq3_ex2_1_6,'type': 'ineq', 'prop': 'convex'},{'func':ineq4_ex2_1_6,'type': 'ineq', 'prop': 'convex'},{'func':ineq5_ex2_1_6,'type': 'ineq', 'prop': 'convex'}]
bnds_ex2_1_6 = [np.array([0, 1]),np.array([0, 1]),np.array([0, 1]),np.array([0, 1]),np.array([0, 1]),np.array([0, 1]),np.array([0, 1]),np.array([0, 1]),np.array([0, 1]),np.array([0, 1])]
vars_ex2_1_6 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
ex2_1_6 = OptimizationProblem("ex2_1_6", sol_ex2_1_6, symobj_ex2_1_6, cons_ex2_1_6, vars_ex2_1_6, bnds_ex2_1_6)

symobj_hs113 = (-14) * x1 - 16 * x2 + (x1**2) + (x2**2) + ((x3) - 10)**2 + ((x4) - 3)**2 + 5 * (x8**2) + ((x10) - 7)**2 + 2 * ((x5) - 10)**2 + 4 * ((x6) - 5)**2 + 2 * ((x7) - 1)**2 + 7 * ((x9) - 11)**2 + x1 * x2 + 45
sol_hs113 = np.array([2.1719963714,2.3636829746,8.7739257399,0.9906547648,8.2800916622,5.0959844875,1.4305739767,1.3216442077,9.8287258072,8.3759266446])
ineq1_hs113 = -(8 * x1 - 2 * x2 - 5 * x5 + 2 * x10) - 12
ineq2_hs113 = -((-10) * x1 + 8 * x2 + 17 * x8 - 2 * x9)
ineq3_hs113 = -((-4) * x1 - 5 * x2 + 3 * x8 - 9 * x9) - 105
ineq4_hs113 = -(3 * x1 - 6 * x2 + 7 * x10 - 12 * ((x5) - 8)**2)
ineq5_hs113 = -((-14) * x4 + 6 * x7 - (x1**2) - 2 * ((x2) - 2)**2 + 2 * x1 * x2)
ineq6_hs113 = -(x7 - 3 * (x4**2) - 0.5 * ((x1) - 8)**2 - 2 * ((x2) - 4)**2) - 30
ineq7_hs113 = -((-8) * x2 + 2 * x6 - 5 * (x1**2) - ((x3) - 6)**2) - 40
ineq8_hs113 = -(7 * x6 - 2 * (x3**2) - 3 * ((x1) - 2)**2 - 4 * ((x2) - 3)**2) - 120
cons_hs113 = [{'func':ineq1_hs113,'type': 'ineq', 'prop': 'convex'},{'func':ineq2_hs113,'type': 'ineq', 'prop': 'convex'},{'func':ineq3_hs113,'type': 'ineq', 'prop': 'convex'},{'func':ineq4_hs113,'type': 'ineq', 'prop': 'convex'},{'func':ineq5_hs113,'type': 'ineq'},{'func':ineq6_hs113,'type': 'ineq'},{'func':ineq7_hs113,'type': 'ineq'},{'func':ineq8_hs113,'type': 'ineq'}]
bnds_hs113 = [np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000]), np.array([-10000, 10000])]
vars_hs113 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
hs113 = OptimizationProblem("hs113", sol_hs113, symobj_hs113, cons_hs113, vars_hs113, bnds_hs113)

symobj_h113 = 0
sol_h113 = np.array([2.0780290882, 2.5816275637, 8.7805332193, 4.9877049754, 1.0098060239, 1.4004460212, 1.1476525511, 9.6914114980, 7.8573384814, 7.9128574143])
ineq1_h113 = -8 * x1 +2 * x2 +5 * x9 -2 * x10 -12
ineq2_h113 = (+10) * x1 -8 * x2 -17 * x7 +2 * x8
ineq3_h113 = (+4) * x1 +5 * x2 -3 * x7 +9 * x8 -105
ineq4_h113 = (-14) * x1 -16 * x2 + x1**2 + x2**2 + (x3-10)**2 + (x5-3)**2 +5 * x7**2 + (x10-7)**2 +4 * (x4-5)**2 +2 * (x6-1)**2 +7 * (x8-11)**2 +2 * (x9-10)**2 +x1 * x2 + 19.693790929999999
ineq5_h113 = -3 * x1 +6 * x2 -7 * x10 +12 * (x9-8)**2
ineq6_h113 = (+14) * x5 -6 * x6 + x1**2 +2 * (x2-2)**2 -2 * x1 * x2
ineq7_h113 = -x6 +3 * x5**2 +0.5 * (x1-8)**2 +2 * (x2-4)**2 -30
ineq8_h113 = (+8) * x2 -2 * x4 +5 * x1**2 + (x3-6)**2 -40
ineq9_h113 = -7 * x4 +2 * x3**2 +3 * (x1-2)**2 +4 * (x2-3)**2 -120
cons_h113 = [{'func':ineq1_h113,'type': 'ineq', 'prop': 'convex'},{'func':ineq2_h113,'type': 'ineq', 'prop': 'convex'},{'func':ineq3_h113,'type': 'ineq', 'prop': 'convex'},{'func':ineq4_h113,'type': 'ineq', 'prop': 'unknown'},{'func':ineq5_h113,'type': 'ineq', 'prop': 'unknown'},{'func':ineq6_h113,'type': 'ineq', 'prop': 'unknown'},{'func':ineq7_h113,'type': 'ineq', 'prop': 'unknown'},{'func':ineq8_h113,'type': 'ineq', 'prop': 'unknown'},{'func':ineq9_h113,'type': 'ineq', 'prop': 'unknown'}]
bnds_h113 = [np.array([0, 10]),np.array([0, 10]),np.array([0, 10]),np.array([0, 10]),np.array([0, 10]),np.array([0, 10]),np.array([0, 10]),np.array([0, 10]),np.array([0, 10]),np.array([0, 10])]
vars_h113 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
h113 = OptimizationProblem("h113", sol_h113, symobj_h113, cons_h113, vars_h113, bnds_h113)

################################################################################
# Alternative Problem Formulations
################################################################################
symobj_hs35mod_v2 = (-8) * x1 - 6 * x2 - 4 * x3 + (x3**2) + 2 * (x1**2) + 2 * (x2**2) + 2 * x1 * x2 + 2 * x1 * x3 + 9
sol_hs35mod_v2 = np.array([1.5000000000,0.5000000000,0.5000000000])
ineq1_hs35mod_v2 = -(-x1 - x2 - 2 * x3) - 3
eq1_hs35mod_v2 = x2 - 0.5
cons_hs35mod_v2 = [{'func':ineq1_hs35mod_v2,'type': 'ineq', 'prop':'convex'}, {'func':eq1_hs35mod_v2,'type': 'eq', 'prop':'convex'}]
bnds_hs35mod_v2 = [np.array([0, 10000]), np.array([0, 10000]), np.array([0, 10000])]
vars_hs35mod_v2 = [x1, x2, x3]
hs35mod_v2 = OptimizationProblem("hs35mod_v2", sol_hs35mod_v2, symobj_hs35mod_v2, cons_hs35mod_v2, vars_hs35mod_v2, bnds_hs35mod_v2)

