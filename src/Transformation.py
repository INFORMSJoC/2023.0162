from __future__ import division

import sys
sys.path.append('../data')

'''
In this file the approximate active index method is implemented, which allows
the Miranda based method to be used on Optimization Problem with eqs and ineqs.
'''

################################################################################
# Necessary Imports
################################################################################
from BoundingProcedures import zentrischeform, interval_arithmetic
from TestProblem import *

################################################################################
# Active Index Set method
################################################################################

def activeIndexSet(prob, bnds, strict_removal):
    '''
    The function does two things:
    1. it checks whether or not the given prob is solvable on bnds:
    - if an eq constraint can never take on the value 0 -> not solvable
    - if an ineq constraint only takes on values > 0 -> not solvable
    - if the number of active constraints > dim -> not solvable
    2. Builds the approximate active index set of prob on bnds

    Parameters
    ----------
    prob : OptimizationProblem
    bnds : list of ndarrays

    Returns
    -------
    activeineqs : list of dictonaries or None
        if the problem is not solvable None is returned - else activeineqs
    '''
    ineq_cons = []
    eq_cons = []
    for i in prob.cons:
        if i['type'] == 'ineq':
            ineq_cons.append(i)
        else:
            eq_cons.append(i)


    for i in eq_cons:
        # OPTIONAL: change this to centered forms
        # bnds_i = zentrischeform(i['func'], bnds, prob.vars)
        bnds_i = interval_arithmetic(i['func'], bnds, prob.vars)
        if bnds_i[0] > 0 or bnds_i[1] < 0:
            if strict_removal:
                return None
            else:
                pass
        else:
            pass
    

    activeineqs = []
    for i in ineq_cons:

        # OPTIONAL: change this to centered forms
        # bnds_i = zentrischeform(i['func'], bnds, prob.vars)
        bnds_i = interval_arithmetic(i['func'], bnds, prob.vars)

        if bnds_i[0] <= 0 and 0 <= bnds_i[1]:
            activeineqs.append(i)
        elif bnds_i[1] < 0:
            pass
        elif bnds_i[0] > 0:
            if strict_removal:
                return None
            else:
                pass

    for i in eq_cons:
        activeineqs.append(i)
    return activeineqs
