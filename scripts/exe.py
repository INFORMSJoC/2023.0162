from __future__ import print_function

import sys
sys.path.append('../src')

from sBaB import *
from OptimizationProblem import SolutionObject
import csv
import random

'''
This file is executed to test the problems contained in the problem_list with the algorithm defined in sBaB.py.
'''


problem_list = [ simpllpb, extrasim, hs006, maratos, tame ]

########################################################################################################################################################################################
# PARAMETERS
########################################################################################################################################################################################

# Termination tolerance \varepsilon
tol_init = 0.1

# Specify if the box constraints should be enlarged and the original box constraints should be transformed to inequality constraints
enlarge_box_constraints_init = True

# Specify if optimality based bounds tightening should be used -> in some cases this leads to errors -> if this is the case set the parameter to False
use_obbt_init = True

# Specify if feasibility based bounds tightening should be used -> the number specifies the number of iterations for FBBT
""" Note that this may not work properly for all problems, so we did not use it in our tests."""
use_fbbt_init = (False, 10)

# Specify if a summary of each branch-and-bound iteration should be printed to the console
debug_init = False

# Specify if the matrix transformation of the Miranda method should be performed
inversion_phase_init = True

# Specify the maximum number of iterations
maxiter_init = 10000

# Specify the maximum time limit
maxtime_init = 900

# Specify if the tunneling approach should be used -> in this case only boxes containing the globally minimal point are considered by the algorithm
tunnel_approach_init = False

# Specify if TODO
strict_removal_init = True

# Specify if the inequality constraints should be transformed to equality constraints by the lifting approach -> set True to test for the original Miranda based Method by Fuellner et al.
var_lifting_init = False

########################################################################################################################################################################################

k = 0
for i in problem_list:
    k = k+1
    with open(''.join(['../run logs/', i.name,'.csv']), mode='w') as solutions_file:
        header_writer = csv.DictWriter(solutions_file, fieldnames=['Status', 'Prob.Name', 'lb.final', 'ub.final', 'box.final', 'iters.first', 'iters.final', 'time.first', 'time.final'])
        header_writer.writeheader()
        solutions_writer = csv.writer(solutions_file, delimiter=',', quotechar='"')

        print('Start Data Generation Process...')
        print('-----------------------------')
        print('Problem', k, 'of', len(problem_list))
        sol = sBaB(i, tol=0.1, maxiter=maxiter_init, maxtime=maxtime_init, enlarge_box_constraints=enlarge_box_constraints_init, use_obbt=use_obbt_init, use_fbbt=use_fbbt_init, debug=debug_init, inversion_phase=inversion_phase_init, tunnel_approach=tunnel_approach_init, var_lifting=var_lifting_init, strict_removal=strict_removal_init)
        solutions_writer.writerow([sol.status, ''.join([sol.name]), sol.lb, sol.ub, sol.box, sol.iters_first, sol.iters_term, sol.time_first, sol.time_term])
    print('Data Generation Process finished...')
