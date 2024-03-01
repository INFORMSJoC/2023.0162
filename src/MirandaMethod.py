from __future__ import division
import random
import itertools
from numpy import inf
import math

import sys
sys.path.append('../data')

'''
This file contains the implementation of the Miranda-based Method from
Fuellner et. al. In the first part, some helper functions are defined. After that,
the different operations of the Miranda based Method are implemented. At the end,
the function miranda_method is defined which specifies the whole procedure used
in Fuellner et. al..
'''

################################################################################
# Necessary Imports
################################################################################

from sympy.tensor.array import derive_by_array
from sympy.matrices.dense import matrix2numpy
import sympy as sym
import numpy as np
import numbers
from BoundingProcedures import midpoint, zentrischeform
from numpy.linalg import inv
from scipy.optimize import linprog
from TestProblem import *

################################################################################
# Help Functions
################################################################################

def get_edge(bnds):
    '''
    Builds Edge Vector for the parameter bnds.

    Parameters
    ----------
    bnds : list of ndarrays
        Box for which the edge vector should be determined

    Returns
    -------
    edge_vec : ndarray
        Edge Vector of box defined by bnds
    '''
    edge_vec = []
    for i in range(0, len(bnds)):
        edge_i = np.zeros(len(bnds))
        edge_i[i] = bnds[i][1] - bnds[i][0]
        edge_vec.append(edge_i)
    return edge_vec

def get_vert(bnds):
    '''
    Builds vertex for the parameter bnds.

    Parameters
    ----------
    bnds : list of ndarrays
        Box for which the lowest vertice should be determined

    Returns
    -------
    vert : ndarray
        Lowest vertice of box defined by bnds
    '''
    vert = [i[0] for i in bnds]
    return np.array(vert, dtype='float64')

def get_facets(bnds):
    '''
    Determines the facets of a box defined by as list of ndarrays.

    Parameters
    ----------
    bnds : list of ndarrays
        Box for which the facets should be determined.

    Returns
    -------
    facets : list of ndarrays
        Facets of box defined by bnds.
    '''
    facets = []
    for i in range(0, len(bnds)):
        facet_up = list(bnds)
        facet_low = list(bnds)
        facet_low[i] = bnds[i][0]
        facet_up[i] = bnds[i][1]
        facets.append([facet_low, facet_up])
    return facets

################################################################################
# Functions for the Miranda based Method
################################################################################

def min_bounding_box(prob, edge, lv):
    '''
    Builds a Minimum Bounding box around an n-Parallelepiped.

    Parameters
    ----------
    edge :
        Edge Vectors of n-Parallelepiped
    lv :
        Lower vertice of n-Parallelepiped

    Returns
    -------
    min_bounding_box : list of ndarrays
        Minimum Bounding Box around n-Parallelepiped
    '''
    dim = len(prob.bnds)
    #build constraint Matrix A:
    A = []
    for i in range(0, dim):
        ri = list(np.zeros(dim))
        ri[i] = 1
        rt = []
        for j in range(0, dim):
            ele = -1 * edge[j][i]
            rt.append(ele)
        for j in rt:
            ri.append(j)
        A.append(ri)
    #--------------------------------------
    #build bounds:
    bnds_lin = []
    for i in range(0, dim):
        bnds_lin.append((None, None))
    for i in range(0, dim):
        bnds_lin.append((0, 1))
    #--------------------------------------
    #build b:
    b = list(lv)
    #--------------------------------------
    min_bounding_box = []
    #build c:
    for i in range(0, dim):
        c = np.zeros(dim*2)
        c[i] = 1
        c_m = np.zeros(dim*2)
        c_m[i] = -1
        sol_min = linprog(c, A_eq=A, b_eq=b, bounds=bnds_lin).fun
        sol_max = -1 * linprog(c_m, A_eq=A, b_eq=b, bounds=bnds_lin).fun

        sol = np.array([sol_min, sol_max])
        min_bounding_box.append(sol)

    return min_bounding_box

def enlarge(bnds):
    '''
    Enlarges a box in a way as phase one in Fuellner et al.

    Parameters
    ----------
    bnds : list of np.arrays
        Box to be enlarged

    Returns
    -------
    bnds : list of np.arrays
        Extended or unchanged input prameter bnds
    '''
    sflag = True #flag indicating if edgelengths < 1
    for i in bnds:
        if i[1] - i[0] < 1:
            pass
        else:
            sflag = False
    if sflag:
        mp = midpoint(bnds)
        enlbnds = []
        for i in range(0, len(bnds)):
            val = (bnds[i][1]-bnds[i][0])
            enlside = 0.5 * math.sqrt(val)
            enlbnds.append(np.array([mp[i] - enlside, mp[i] + enlside]))
        return enlbnds
    else:
        return bnds

def transform(prob, cons, bnds):
    '''
    Phase two of Miranda-based Method in Fuellner et al.

    Parameters
    ----------
    prob : OptimizationProblem
        Problem to transform
    bnds : list of np.arrays
        Box to transform
    cons : list of dictonaries
        Constraints to transform

    Returns
    -------
    A : ndarray
        Inverse of Transformation Matrix
    A_inv : ndarray
        Transformation Matrix
    bnds_trans : list of ndarrays
        Minimum Bounding Box.
    cons_trans : list of dictonaries
        Transformed Constraints
    cons_obj : sympy expression
        Transformed Objective Function
    '''
    #---------------------------------------------------------------------------
    consfunc = sym.Matrix([i['func'] for i in cons]) #generates multivariate function
    jacobian = consfunc.jacobian(prob.vars) #builds jacobian
    repldic = {k:v for k, v in zip(prob.vars, midpoint(bnds))} # build dictonary for evaluation
    #---------------------------------------------------------------------------
    # Matrix Construction
    if len(cons) == len(bnds): #case n = m
        A_inv = matrix2numpy(jacobian.subs(repldic)).astype('float64') # evaluate jacobian in midpoint
    else: #case n > m
        #build the nullspace and append it as rows to the matrix
        A_inv = jacobian
        nullspace = jacobian.nullspace()
        k = A_inv.shape[0]
        for i in nullspace:
            k = k + 1
            A_inv = A_inv.row_insert(k, i.T)
        A_inv = A_inv.subs(repldic)
        A_inv = np.array(A_inv, dtype='float64')

    #---------------------------------------------------------------------------
    #For test purposes - swap rows of the Matrix

    #A_inv[[0, 1]] = A_inv[[1, 0]]
    #A_inv[[0, 2]] = A_inv[[2, 0]]
    #A_inv[[0, 3]] = A_inv[[3, 0]]
    #A_inv[[0, 4]] = A_inv[[4, 0]]

    #---------------------------------------------------------------------------
    # Build Inverse Matrix:
    A = inv(A_inv) #build inverse of transformation matrix
    #---------------------------------------------------------------------------
    # Build transdic
    vars_trans = A.dot(np.array(prob.vars))
    transdic = {k:v for k, v in zip(prob.vars, vars_trans)}
    #---------------------------------------------------------------------------
    # Constraints Transformation
    if cons is None:
        cons_trans = None
    else:
        cons_trans = [i['func'].subs(transdic) for i in cons]
    cons_trans = [{'func':i, 'type':'eq'} for i in cons_trans]
    #---------------------------------------------------------------------------
    # Objective Transformation
    if prob.symobj is None:
        obj_trans = None
    elif isinstance(prob.symobj, numbers.Number):
        obj_trans = prob.symobj
    else:
        obj_trans = prob.symobj.subs(transdic)
    #---------------------------------------------------------------------------
    # Build Minimum Bounding Box
    untrans_edge = get_edge(bnds)
    trans_edge = [A_inv.dot(i) for i in untrans_edge]
    untrans_vert = get_vert(bnds)
    trans_vert = A_inv.dot(untrans_vert)
    bnds_trans = min_bounding_box(prob, trans_edge, trans_vert)

    return [A, A_inv, bnds_trans, cons_trans, obj_trans]

def retransform(prob, bnds, matrix):
    '''
    Retransforms the box and builds a Minimum Bounding Box around it.

    Parameters
    ----------
    prob : OptimizationProblem
        The Optimization Problem considered.
    bnds : list of ndarrays
        Bounds that need to be retransformed.
    matrix : ndarray
        The matrix that is used to linearly transform bnds.

    Returns
    -------
    retrans_bnds : list of ndarrays
        Minimum Bounding Box around transformed bnds.
    '''
    # get edge vector of transformed box
    edge_trans = get_edge(bnds)
    # retransform box to n-Parallelepiped
    edge_retrans = [matrix.dot(i) for i in edge_trans]
    #---------------------------------------------
    #get one vertice of retransformed box
    vert_trans = get_vert(bnds)
    vert_retrans = matrix.dot(vert_trans)
    #---------------------------------------------
    #build minimum bounding box
    retrans_bnds = min_bounding_box(prob, edge_retrans, vert_retrans)
    #---------------------------------------------
    return retrans_bnds

def check_if_in_bnds(prob, bnds):
    '''
    Checks if bnds is a subset of prob.bnds.
    Returns True if this is the case.

    Parameters
    ----------
    prob : OptimizationProblem
        Optimization Problem considered.
    bnds : list of ndarrays
        Box considered

    Returns
    -------
    inbnds : boolean
        True if bnds is a subset of prob.bnds
    '''
    for i, j in zip(prob.bnds, bnds):
        if j[0] < i[0] or j[1] > i[1]:
            inbnds = False
            return inbnds
        else:
            pass
    inbnds = True
    return inbnds

def combinations(facets, constraints):
    allocations = [list(zip(x,constraints)) for x in itertools.permutations(facets,len(constraints))]
    return allocations


################################################################################
# Functions for allocation of facets to constraints
################################################################################

def standard_allocation(facets, cons_list):
    '''
    Allocates facets to constraints in the standard way.
    '''
    allocation = [[cons_list[i], facets[i]] for i in range(0, len(cons_list))]
    return allocation

def random_allocation(facets, cons_list):
    '''
    Allocates facets to constraints in a random way.
    '''
    random.shuffle(cons_list)
    allocation = [[cons_list[i], facets[i]] for i in range(0, len(cons_list))]
    return allocation

def all_combinations_verify_feasibility(prob, bnds, cons, debug, allocation_method):
    '''
    Checks the conditions of Miranda's Theorem for all possible combinations
    of facets and constraints.
    Returns True if the conditions are satisfied for at least one combination.

    Parameters
    ----------
    prob : OptimizationProblem
        The Optimization Problem considered.
    bnds : list of ndarrays
        The Box in which a feasible point should be verified.
    cons : list of dictonaries
        The Constraints used for evaluation of Miranda's Theorem.
    debug : boolean
        If true print values each iteration
    allocation_method : int
        if == 0 use standard allocation, if == 1 use random allocation
    Returns
    -------
    feas : boolean
        True if Miranda's Theorem is satisfied, else False.
    '''
    facets = get_facets(bnds)
    cons_list = [cons[i]['func'] for i in range(0, len(cons))]
    allocations = combinations(facets, cons_list)
    counter = 0
    for j in allocations:
        verified_flag = True
        counter = counter + 1
        allocation = j
        for i in range(0, len(allocation)):
            constraint_i = allocation[i][1] # constraint considered
            lower_facet = allocation[i][0][0] # lower facet
            upper_facet = allocation[i][0][1] # upper facet
            # check which variable needs to be fixed
            index = 0
            for k in range(0, len(lower_facet)):
                if isinstance(lower_facet[k], float) or isinstance(lower_facet[k], int):
                    index = k
                else:
                    pass
            # build substitution dictonaries
            subs_lf = {}
            subs_lf[prob.vars[index]] = lower_facet[index]
            subs_uf = {}
            subs_uf[prob.vars[index]] = upper_facet[index]
            # fix the considered constraint on facet i
            constraint_lf = constraint_i.subs(subs_lf)
            constraint_uf = constraint_i.subs(subs_uf)
            # build bnds and vars of all free variables
            bnds_facet = list(bnds)
            bnds_facet.pop(index)
            vars_facet = list(prob.vars)
            vars_facet.pop(index)
            # calculate lower and upper bounds on each facet
            ub = zentrischeform(constraint_lf, bnds_facet, vars_facet)[1]
            lb = zentrischeform(constraint_uf, bnds_facet, vars_facet)[0]
            if ub is None or lb is None:
                lb = -1
                ub = 1
                verified_flag = False
            if lb > -1e-10 and lb < 0: 
                lb = 0
            if ub < 1e-10 and ub > 0:
                ub = 0
            if debug:
                print(''.join(['feas_check: ', str(counter), ' - ', str(lb), ' ', str(ub)]))
            else:
                pass
            if lb >= 0 and ub <= 0:
                pass
            else:
                verified_flag = False
        if verified_flag:
            feas = True
            return feas
        else:
            pass
    feas = False
    return feas

def verify_feasibility(prob, bnds, cons, debug, allocation_method):
    '''
    Checks the conditions of Miranda's Theorem.
    Returns True if the conditions are satisfied.

    Parameters
    ----------
    prob : OptimizationProblem
        The Optimization Problem considered.
    bnds : list of ndarrays
        The Box in which a feasible point should be verified.
    cons : list of dictonaries
        The Constraints used for evaluation of Miranda's Theorem.
    debug : boolean
        If true print values each iteration
    allocation_method : int
        if == 0 use standard allocation, if == 1 use random allocation
    Returns
    -------
    feas : boolean
        True if Miranda's Theorem is satisfied, else False.
    '''

    # determine facets of bnds
    facets = get_facets(bnds)
    cons_list = [cons[i]['func'] for i in range(0, len(cons))]

    random.shuffle(cons_list)


    '''
    if allocation_method == 1: # reorder facets so random allocation is possible
        random.shuffle(cons_list)
    else: # keep order as intended, normal allocation
        pass
    '''
    # allocate each constraint to a facet
    '''
    try:
        allocation = [[cons_list[1], facets[3]], [const_list[0], facets[1]]]
    except:
        allocation = [[cons_list[i], facets[i]] for i in range(0, len(cons))]
    '''

    #allocation = [[cons_list[i], facets[i]] for i in range(0, len(cons))]
    allocation = [[cons_list[i], facets[i]] for i in range(0, len(cons))]

    #iterate over all facet allocations
    for i in range(0, len(allocation)):
        constraint_i = allocation[i][0] # constraint considered
        lower_facet = allocation[i][1][0] # lower facet
        upper_facet = allocation[i][1][1] # upper facet
        # build substitution dictonaries
        subs_lf = {}
        subs_lf[prob.vars[i]] = lower_facet[i]
        subs_uf = {}
        subs_uf[prob.vars[i]] = upper_facet[i]
        # fix the considered constraint on facet i
        constraint_lf = constraint_i.subs(subs_lf)
        constraint_uf = constraint_i.subs(subs_uf)
        # build bnds and vars of all free variables
        bnds_facet = list(bnds)
        bnds_facet.pop(i)
        vars_facet = list(prob.vars)
        vars_facet.pop(i)
        # calculate lower and upper bounds on each facet
        ub = zentrischeform(constraint_lf, bnds_facet, vars_facet)[1]
        lb = zentrischeform(constraint_uf, bnds_facet, vars_facet)[0]
        if lb > -1e-5  and lb < 0: # ------> change the value -1e-5 to define when to account for a bound as zero
            lb = 0
        if ub < 1e-5 and ub > 0: # ------> change the value -1e-5 to define when to account for a bound as zero
            ub = 0
        if debug:
            print(''.join(['feas_check (lb, ub): ', str(lb), ' ', str(ub)]))
        if lb >= 0 and ub <= 0:
            pass
        else:
            #print(False)
            feas = False
            return feas

    #print(True)
    feas = True
    return feas

################################################################################
# Final Miranda based Method
################################################################################


def miranda_method(prob, bnds, cons, bbiter, numit_transformation=1, coordinate_transformation=True, check_bounds_violation=True, allocation_method=0, debug=False):
    '''
    Performs the miranda method from Fuellner et. al. by combining the previous
    functions.

    Parameters
    ----------
    prob : OptimizationProblem
        optimization problem
    bnds : list of ndarrays
    cons : list of dictonaries
    mode : boolean
        if mode == true do not check if B is in verified box
    bbiter : int
        gives current iteration of bandb algorithm
    allocation_method : int
        if 1 use random facet allocation, if 0 use standard facet allocation
    Returns
    -------
    ub : float or None
        if conditions satisfied returns float, otherwise None
    '''

    transform_flag = coordinate_transformation
    try:
        if verify_feasibility(prob, bnds, cons, False, allocation_method):
            ub = zentrischeform(prob.symobj, bnds, prob.vars)[1]
            return ub
        else:
            enlarged_bnds = enlarge(bnds)
            if verify_feasibility(prob, enlarged_bnds, cons, False, allocation_method):
                if check_bounds_violation:
                    if check_if_in_bnds(prob, enlarged_bnds):
                        ub = zentrischeform(prob.symobj, enlarged_bnds, prob.vars)[1]
                        return ub
                else:
                    ub = zentrischeform(prob.symobj, enlarged_bnds, prob.vars)[1]
                    return ub

            if transform_flag and bbiter % numit_transformation == 0:
                sol_transform = transform(prob, cons, enlarged_bnds)
                if verify_feasibility(prob, sol_transform[2], sol_transform[3], False, allocation_method):
                    if check_bounds_violation:
                        sol_retransform = retransform(prob, sol_transform[2], sol_transform[0])
                        if check_if_in_bnds(prob, sol_retransform):
                            ub = zentrischeform(prob.symobj, sol_transform[2], prob.vars)[1]
                        else:
                            ub = None
                    else:
                        ub = zentrischeform(prob.symobj, sol_transform[2], prob.vars)[1]
                else:
                    ub = None
            else:
                ub = None

                print('ub Miranda: ', ub)
            return ub

    except np.linalg.LinAlgError: # handles the case where the transformation matrix is not invertable
        print('np.linalg.LinAlgError')
        return None
    
  
    except TypeError: # handles the case where the transformation matrix contains nonnumeric values (inf, -inf, nan)
        print('TypeError')
        return None

    
    except ValueError: # handles the case where the transformation matrix contains nonnumeric values (inf, -inf, nan)
        print('ValueError')
        return None
    
