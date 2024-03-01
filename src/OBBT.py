import sys
sys.path.append('../data')

import sympy as sym
from TestProblem import *
from BoundingProcedures import *
import numbers
from scipy.optimize import minimize
from copy import deepcopy
from cyipopt import minimize_ipopt
'''
Implementation of optimality based bounds tightening.
'''


def calculate_beta(func, vars, bnds):
    '''
    Calculates a beta for the convex relaxation based on the alphaBB method.
    '''
    #build hessian of func
    hessian = list(sym.derive_by_array(sym.derive_by_array(func, vars), vars))
    beta_list = []
    for j, i in enumerate(hessian):
        a_ii = i[j]
        r_list = [ele for ele in i]
        del r_list[j]
        A_ii = eval(interval_extension(str(a_ii), vars, bnds))
        R_i = 0
        for k in r_list:
            R_i = R_i + eval(interval_extension(str(abs(k)), vars, bnds))
        beta_i = A_ii - R_i
        if isinstance(beta_i, numbers.Number):
            pass
        else:
            beta_i = beta_i[0].inf
        beta_list.append(beta_i)
    beta = min(beta_list)
    return beta

def build_convex_relaxation(cons, vars, bnds):
    convex_cons = []
    lower_bnds, upper_bnds = build_bnds_vectors(bnds)
    vars_vec = sym.Matrix(vars)
    for i in cons:

        if not 'prop' in i:
            # If 'prop' is not defined, use unknown as default
            i['prop'] = 'unknown'

        if i['prop'] == 'convex':
            convex_cons.append(i)
        else:
            if i['type'] == 'ineq':
                fx = i['func']
                phix = 0.5 * (lower_bnds - vars_vec).dot((upper_bnds - vars_vec))
                beta = calculate_beta(fx, vars, bnds)
                alpha = max([0, -beta])
                new_con = {'func' : fx + alpha * phix, 'type' : i['type'], 'prop' : 'convex'}
                convex_cons.append(new_con)
            else:
                fx1 = i['func']
                fx2 = -1 * i['func']
                phix = 0.5 * (lower_bnds - vars_vec).dot((upper_bnds - vars_vec))
                beta1 = calculate_beta(fx1, vars, bnds)
                beta2 = calculate_beta(fx2, vars, bnds)
                alpha1 = max([0, -beta1])
                alpha2 = max([0, -beta2])
                new_con1 = {'func' : fx1 + alpha1 * phix, 'type' : 'ineq', 'prop' : 'convex'}
                new_con2 = {'func' : fx2 + alpha2 * phix, 'type' : 'ineq', 'prop' : 'convex'}
                convex_cons.append(new_con1)
                convex_cons.append(new_con2)

    return convex_cons

#------------------------------------------------------------------------------#


def build_bnds_vectors(bnds):
    """
    Splits list of ndarrays into lower and upper vectors X = [x_lo, x_up]

    Parameters
    ----------
    bnds : list of ndarrays

    Returns
    -------
    tuple of sympy Matrices
    """
    lower = []
    upper = []
    for i in bnds:
        lower.append(i[0])
        upper.append(i[1])
    return (sym.Matrix(lower), sym.Matrix(upper))

def sol_in_bnds(bnds, sol):
    """
    Tests if sol is contained in the box difined by bnds.

    Parameters
    ----------
    bnds : list of ndarrays

    sol : ndarray

    Returns
    -------
    boolean
        return True if sol in bnds.
    """
    for i, j in zip(bnds, sol):
        if j >= i[0] and j <= i[1]:
            pass
        else:
            return False
    return True

def build_lambdified_constraint(cons, vars):
    """
    Transforms the constraints in the format as in the class OptimizationProblem
    into python lambda functions that can be given to scipy.optimize.minimize
    to solve the OBBT problem.

    Parameters
    ----------
    cons : list of dictionaries
        Definition of the constraints of the convex relaxation of the considered problem.

    Returns
    -------
    list of dictionaries
        Constraints in the right format for evaluation of OBBT.
    """

    constraint_list = []
    for i in cons:
        type_i = i['type']

        def lamb_func_v(x, i=i):
            func_i = i['func']
            type_i = i['type']
            if type_i == 'ineq':
                func_i = -1 * func_i

            lamb_func = sym.lambdify(vars, func_i) #convert sympy expr to lambda function

            return lamb_func(*tuple(x)) #convert to vectorized lambda function

        constraint_list.append({'type' : type_i, 'fun' : lamb_func_v})

    return constraint_list

def solve2n_cr(cons, vars, bnds):
    """
    Solves the OBBT problem, by solving 2n convex optimization problems of the form
    min x_n s.t. convex constraints, max x_n s.t. convex constraints.

    Parameters
    ----------
    cons : list of dictionaries
        Definition of the constraints of the convex relaxation of the considered problem.
    vars : list of sympy symbols
        List of all sympy symbols contained in the problem.

    Returns
    -------
    list of ndarrays
        New tighter box constraints for the original OptimizationProblem.
    """
    #build bounds
    bounds_list = [(i[0], i[1]) for i in bnds]

    # build constraints in the right format
    conv_cons = build_convex_relaxation(cons, vars, bnds) #build convex relaxation
    cons_list = build_lambdified_constraint(conv_cons, vars) #transform to python format

    x_0 = np.zeros(len(bnds))
    #x_0 = np.array([np.random.uniform(i[0], i[1]) for i in bnds])
    #print(x_0)

    sol_array = []

    for i,j in zip(vars, bounds_list):
        obj_expr = i
        obj_func = sym.lambdify(vars, obj_expr)

        def obj_func_min(x):
            return obj_func(*tuple(x))

        def obj_func_max(x):
            return -1 * obj_func(*tuple(x))

        sol_min = minimize(obj_func_min, x_0, method='SLSQP', constraints=cons_list, bounds=bounds_list)
        sol_max = minimize(obj_func_max, x_0, method='SLSQP', constraints=cons_list, bounds=bounds_list)

        if sol_min.success:
            sol_min_val = sol_min.fun
        else:
            sol_min_val = j[0]

        if sol_max.success:
            sol_max_val = -1 * sol_max.fun
        else:
            sol_max_val = j[1]

        sol = np.array([np.floor(sol_min_val), np.ceil(sol_max_val)])
        sol_array.append(sol)

    return sol_array

def post_processing(bnds_orig, bnds_new):
    for i, j in zip(bnds_orig, bnds_new):
        if i[0] > j[0]: #handles the case where the new bounds are larger than the original ones
            j[0] = i[0]
        elif i[1] < j[1]:
            j[1] = i[1]
        else:
            pass
    return bnds_new
#------------------------------------------------------------------------------#

def obbt(opt):
    """
    Tightens bounds of an Optimization Problem through the optimality based bound
    tightening method, to increase the speed of branch and bound algorithms

    Parameters
    ----------
    opt : OptimizationProblem
        Optimization Problem for which tightened bounds should be calculated.

    Returns
    -------
    OptimizationProblem
        Optimization Problem with tightened bounds.

    """
    tightened_bnds = solve2n_cr(opt.cons, opt.vars, opt.bnds)
    post_processed_bnds = post_processing(opt.bnds, tightened_bnds)

    return post_processed_bnds
