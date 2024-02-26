import sys
sys.path.append('../data')

from BranchAndBound import *
from TestProblem import *
import sympy as sym
'''
In this file, the lifting approach using slack variables is implemented.
'''

v1 = sym.Symbol('v1')
v2 = sym.Symbol('v2')
v3 = sym.Symbol('v3')
v4 = sym.Symbol('v4')
v5 = sym.Symbol('v5')
v6 = sym.Symbol('v6')
v7 = sym.Symbol('v7')
v8 = sym.Symbol('v8')
v9 = sym.Symbol('v9')
v10 = sym.Symbol('v10')
v11 = sym.Symbol('v11')
v12 = sym.Symbol('v12')
v13 = sym.Symbol('v13')
v14 = sym.Symbol('v14')
v15 = sym.Symbol('v15')
v16 = sym.Symbol('v16')
v17 = sym.Symbol('v17')
v18 = sym.Symbol('v18')
v19 = sym.Symbol('v19')
v20 = sym.Symbol('v20')

slack_list = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20]

def variable_lifting(opt_prob):
    '''
    Transforms inequality constraints to equality constraints by adding slack vars.

    Input:
    opt_prob : OptimizationProblem
        The considered optimization problem

    Return:
    new_optprob : OptimizationProblem
        Modified problem where the inequality constraints are transformed to equality constraints including slack variables
    '''

    pos = 0
    constraints = opt_prob.cons
    variables = opt_prob.vars
    bounds = opt_prob.bnds


    lifted_constraints = []
    new_variables = variables
    new_bnds = bounds
    for i in constraints:
        if i['type'] == 'ineq':
            function = i['func']
            slack_var = slack_list[pos]
            new_function = function + slack_var**2
            pos = pos + 1
            new_variables.append(slack_var)
            # build constraint dict
            lifted_constraints.append({'func':new_function, 'type':'eq', 'prop':'unknown'})
            new_bnds.append(np.array([-10000, 10000]))
        else:
            lifted_constraints.append(i)

    new_optprob = OptimizationProblem(opt_prob.name, None, opt_prob.symobj, lifted_constraints, new_variables, new_bnds)
    return new_optprob
