from __future__ import division
'''
This file contains a method that transforms the box constraints of an object
with the type OptimizationProblem to inequality constraints and introduces larger
box constraints. In that way, the method in Fuellner et. al. is guaranteed to
verify the existence of a feasible point if such a point exists.
'''

################################################################################
# Necessary Imports
################################################################################

from OptimizationProblem import *
import numpy as np


def transform_problem(prob):
    '''
    Transforms an OptimizationProblem object.
    Enlarges the box constraints and models the old ones as inequality constraints.
    The transformed problem is ensured to not have any feasible points on the edges
    of the transformed box.

    Parameters
    ----------
    prob : OptimizationProblem
        The Problem that should be Transformed.

    Returns
    -------
    transformed_prob : OptimizationProblem
        The transformed OptimizationProblem.
    '''
    # Build new inequality constraints from bounds:
    transformed_cons = prob.cons
    for i, j in zip(prob.vars, prob.bnds):
        con_lb = {'func':j[0]-i, 'type':'ineq', 'prop':'unknown'}
        transformed_cons.append(con_lb)
        con_ub = {'func':i-j[1], 'type':'ineq', 'prop':'unknown'}
        transformed_cons.append(con_ub)
    # Build extended bounds to all variables
    transformed_bnds = []
    for i in prob.bnds:
        transformed_bnds.append(np.array([i[0]-1, i[1]+1]))
    # Build the new OptimizationProblem objective
    transformed_prob = OptimizationProblem(prob.name, prob.sol, prob.symobj, transformed_cons, prob.vars, transformed_bnds)
    return transformed_prob
