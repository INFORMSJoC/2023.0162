from OBBT import *
from sympy.matrices.dense import matrix2numpy
import numpy as np
from copy import deepcopy
from numpy.linalg import inv
from scipy.linalg import null_space
from scipy.optimize import minimize
from cyipopt import minimize_ipopt
from BoundingProcedures import midpoint, zentrischeform

'''
This file contains functionality to apply Interval Newton operators such as the Krawczyk operator or the Hansen-Sengupta
operator, similar to the description by Domes & Neumaier (2015).
'''

def solve_local(prob, bnds, cons, local_solver):
    """
    Solves the given problem using a local solver.

    Parameters
    ----------
    prob : OptimizationProblem
        optimization problem
    bnds : list of ndarrays
    cons : list of dictionaries
    local_solver : String of local solver to be used

    Returns
    -------
    sol_point : ndarray
            optimal point of the problem
    """

    #build bounds
    bounds_list = [(i[0], i[1]) for i in bnds]

    # build constraints in the right format
    cons_list = build_lambdified_constraint(cons, prob.vars) #transform to python format

    x_0 = np.zeros(len(bnds))

    obj_func = sym.lambdify(prob.vars, prob.symobj)

    def obj_func_min_newton(x):
        return obj_func(*tuple(x))

    if local_solver == 'ipopt':
        sol_min = minimize_ipopt(obj_func_min_newton, x_0, constraints=cons_list, bounds=bounds_list)
    elif local_solver == 'slsqp':
        sol_min = minimize(obj_func_min_newton, x_0, method='SLSQP', constraints=cons_list, bounds=bounds_list)

    if sol_min.success:
        sol_point = sol_min.x
    else:
        sol_point = None

    return sol_point


def check_for_fixing(sol_point, prob, bnds, cons):
    """
    Checks if variables have to be fixed (because m < n, that is, the system being underdetermined) and if so,
    which indices should be fixed. As proposed by Kearfott we fix the variables which correspond to rows in the
    Jacobian with minimal row-sum.

    Parameters
    ----------
    sol_point : ndarray
            optimal point of the problem
    prob : OptimizationProblem
        optimization problem
    bnds : list of ndarrays
    cons : list of dictionaries

    Returns
    -------
    narrow_bnds : list of ndarrays
            narrow box around local solution
    """

    if len(cons) == len(bnds): #case n = m
        indices_to_fix = []
    else:   # case n > m
        k = len(bnds) - len(cons)

        # We have to fix k variables, since the system is underdetermined
        # Determine the nullspace of the Jacobian at sol_point
        consfunc = sym.Matrix([i['func'] for i in cons]) #generates multivariate function
        jacobian = consfunc.jacobian(prob.vars) #builds jacobian
        evaluated_jacobian = sym.lambdify(prob.vars, jacobian)(*sol_point)
        nullspace = null_space(evaluated_jacobian)

        # Determine the row sums of this nullspace and return the k indices with the smallest entries
        rowsums = nullspace.sum(axis=1)
        indices_to_fix = np.argpartition(rowsums, k)[:k].tolist()

    return indices_to_fix

def fix_variables(sol_point, prob, bnds, cons, indices_to_fix):
    """
    Fixes the variables specified in indices_to_fix. This means that the dimension of the system is reduced.

    Parameters
    ----------
    sol_point : ndarray
            optimal point of the problem
    prob : OptimizationProblem
        optimization problem
    bnds : list of ndarrays
    cons : list of dictionaries
    indices_to_fix : list of int
        indices of variables which have to be fixed.

    Returns
    -------
    sol_point_restr : ndarray
            optimal point of the problem, but without the fixed variables (we need it in smaller dimension)
    bnds_restr : list of ndarrays
            bounds describing the current box, but without the fixed variables (we need it in smaller dimension)
    bnds_fixed : list of ndarrays
            bounds describing the current box, including the fixed components (we need this to compute upper bounds later)
    cons_restr : list of dictionaries
    vars_restr : list
            variables, but without the fixed ones (we need them in smaller dimension)
    """

    # Make deep copies of all required elements
    sol_point_restr = deepcopy(sol_point)
    bnds_restr = deepcopy(bnds)
    bnds_fixed = deepcopy(bnds)
    cons_restr = deepcopy(cons)

    # Delete the fixed variables in the sol_point
    sol_point_restr = np.delete(sol_point_restr, indices_to_fix)

    # Delete the fixed variables in the bnds
    reversed_indices = sorted(indices_to_fix, reverse=True)
    for idx in reversed_indices:
        bnds_restr.pop(idx)

    # Fix the fixed variables in the bnds
    for idx in reversed_indices:
        bnds_fixed[idx] = np.array([sol_point[idx], sol_point[idx]])

    # Fix the fixed variables in the cons
    for cons_idx in range(0, len(cons)):
        for var_idx in reversed_indices:
            var_comp = prob.vars[var_idx]
            cons_restr[cons_idx]['func'] = cons_restr[cons_idx]['func'].subs(var_comp, sol_point[var_idx])

    # Reduce the variable vector
    vars_restr = deepcopy(prob.vars)
    for idx in reversed_indices:
        vars_restr.pop(idx)

    return sol_point_restr, bnds_restr, bnds_fixed, cons_restr, vars_restr


def construct_narrow_box(sol_point, prob, cons_restr, bnds_restr, epsilon=1e-5):
    """
    Creates a small box around the local solution.

    Parameters
    ----------
    sol_point : ndarray
            optimal point of the problem
    prob : OptimizationProblem
        optimization problem
    cons_restr : list of dictionaries
    bnds_restr : list of ndarrays
    epsilon : Float
            parameter to determine the size of the box

    Returns
    -------
    narrow_bnds : list of ndarrays
            narrow box around local solution of dimension m
    """

    # Build bounds for a narrow box around the local solution
    narrow_bnds = []
    for i in range(0, len(bnds_restr)):
        narrow_comp = np.array([sol_point[i] - epsilon, sol_point[i] + epsilon])
        narrow_bnds.append(narrow_comp)

    return narrow_bnds


def krawczyk(prob, cons, bnds, vars):
    """
    Performs a step with the Krawczyk operator to check if the equation system has a zero.
    This does not work for m < n, so the equation system has been reduced in advance by fixing variables.

    Parameters
    ----------
    prob : OptimizationProblem
        optimization problem
    cons : list of dictionaries
        problem constraints that have to be considered
    bnds : list of ndarrays
        Bounds for the function evaluation
    vars : list
        Variables to be considered

    Returns
    -------
    K : list of ndarrays
        A box as a result of applying the Krawczyk operator
    """

    try:
        # Construct a multidimensional function containing all the single constraints
        consfunc = sym.Matrix([i['func'] for i in cons])

        # K(X, z) := z - Z * f(z) + (I - Z * F'(X)) * (X - z)
        #---------------------------------------------------------------------------
        # We choose z as the midpoint of the current box (this will be sol_point_restr)
        z = midpoint(bnds)
        # Evaluate the constraint function at this point
        fz = sym.lambdify(vars,consfunc)(*z)

        #---------------------------------------------------------------------------
        # F'(X)
        fx = derive_by_array(consfunc, vars) # note that this representation of the Jacobian is required for interval_extension
        FX = eval(interval_extension(str(fx), vars, bnds))

        #---------------------------------------------------------------------------
        # Identity matrix I
        I = np.eye(len(bnds))

        #---------------------------------------------------------------------------
        # Preconditioning matrix Z
        jacobian = consfunc.jacobian(vars) # note that this representation of the Jacobian is required for inverting
        Z = inv(sym.lambdify(vars, jacobian)(*z))

        #---------------------------------------------------------------------------
        # Z * f(z)
        term_1a = 0
        for i, j in zip(np.transpose(Z),fz):
            term_1a = term_1a + i * j

        #---------------------------------------------------------------------------
        # z - Z * f(z)
        term_1b = [i - j for i, j in zip(list(z), term_1a)]

        #---------------------------------------------------------------------------
        # Z * F'(X)
        term_2a = np.ndarray([int(np.shape(Z)[0]), len(FX[0])], dtype=object)
        for i in range(0, int(np.shape(Z)[0])):
            for j in range(0, len(FX[0])):
                FX_column = [row[j] for row in FX]
                term_2a[i][j] = 0
                for s in range(0, len(FX_column)):
                    term_2a[i][j] = term_2a[i][j] + FX_column[s][0] * Z[i,s]

        #---------------------------------------------------------------------------
        # I - z * F'(X)
        term_2b = I - term_2a

        #---------------------------------------------------------------------------
        # (X - z)
        Xmz = [i - j for i, j in zip(vars, list(z))]
        Xmz = eval(interval_extension(str(Xmz), vars, bnds))

        #---------------------------------------------------------------------------
        # (I - z * F'(X)) * (X - z)
        term_3a = []
        for i in range(0, len(term_2b[0])):
            element = 0
            for j in range(0, len(Xmz)):
                element = element + term_2b[i][j] * Xmz[j]
            term_3a.append(interval_to_arrayList(element))

        #---------------------------------------------------------------------------
        # Full term
        K = [(i + j) for i, j in zip(term_1b, term_3a)]

        return K
    except np.linalg.LinAlgError: # handles the case where the transformation matrix is not invertable
        print('np.linalg.LinAlgError')
        return None


def check_if_in_bnds_newton_used(bnds, operator_bnds):
    '''
    Checks if the box returned by the interval Newton operator is a subset of the given bnds.
    Returns True if this is the case.

    Parameters
    ----------
    operator_bnds : list of ndarrays
        Box returned by the interval Newton operator
    bnds : list of ndarrays
        Box considered

    Returns
    -------
    inbnds : boolean
        True if bnds is a subset of prob.bnds
    '''
    for i, j in zip(bnds, operator_bnds):
        if j[0] <= i[0] or j[1] >= i[1]:
            inbnds = False
            return inbnds
        else:
            pass
    inbnds = True
    return inbnds


def check_if_in_bnds_initial(bnds_considered, bnds_initial):
    '''
    Checks if the considered narrow box is completely contained in the initial box of the problem.
    Returns True if this is the case.

    Parameters
    ----------
    bnds_considered : list of ndarrays
        Narrow box considered
    bnds_initial : list of ndarrays
        Initial box of the optimization problem

    Returns
    -------
    inbnds : boolean
        True if bnds is a subset of prob.bnds
    '''
    for i, j in zip(bnds_initial, bnds_considered):
        if j[0] < i[0] or j[1] > i[1]:
            inbnds = False
            return inbnds
        else:
            pass
    inbnds = True
    return inbnds


def get_bnds_for_ub(bnds_fixed, used_bnds, indices_to_fix):

    # We initialize the box for the upper bound computation with the box with fixed bounds
    bnds_for_ub = deepcopy(bnds_fixed)

    # For all non-fixed bounds, we still have to consider the epsilon deviation though.
    # Iterate over all original indices
    for idx in range(0, len(bnds_for_ub)):
        if idx in indices_to_fix:
            pass
        else:
            bnds_for_ub[idx] = used_bnds[0]
            used_bnds.pop(0)

    return bnds_for_ub


def interval_newton_method(prob, bnds, cons, narrow_box_flag=True, narrow_epsilon=1e-5, local_solver='ipopt', debug=False):
    '''
    Applies an interval newton method (Krawczyk operator) for feasibility verification and if the verification is
    successful computes an upper bound.

    Parameters
    ----------
    prob : OptimizationProblem
        The Optimization Problem considered.
    bnds : list of ndarrays
        The Box in which a feasible point should be verified.
    cons : list of dictionaries
        The Constraints used for evaluation of Miranda's Theorem.
    narrow_box_flag : boolean
        If true, the interval newton method is applied to a narrow box around a local minimal solution. Otherwise,
        it is applied to the original box using the midpoint.
    narrow_epsilon : Float64
        Epsilon value which is used to construct the narrow box.
    debug : boolean
        If true print values each iteration

    Returns
    -------
    ub : float or None
        if conditions satisfied returns float, otherwise None
    '''

    if narrow_box_flag:
        # First compute a local solution
        sol_point = solve_local(prob, bnds, cons, local_solver)

    else:
        # Use the box midpoint
        sol_point = midpoint(bnds)

    if sol_point is None:
        ub = None
        if debug:
            print('ub Krawczyk: ', ub, '. No local solution.')

    else:

        # Fix some variables to the local solution if required
        indices_to_fix = check_for_fixing(sol_point, prob, bnds, cons)
        sol_point_restr, bnds_restr, bnds_fixed, cons_restr, vars_restr = fix_variables(sol_point, prob, bnds, cons, indices_to_fix)

        # Box to be used for the Krawczyk operator. Default: use the original box
        # Construct a narrow box around the local solution
        if narrow_box_flag:
            used_bnds = construct_narrow_box(sol_point, prob, cons_restr, bnds_restr, narrow_epsilon)
        # Use the original box (in lower dimension)
        else:
            used_bnds = bnds_restr

        # Apply the Krawczyk operator for feasibility verification
        krawczyk_bnds = krawczyk(prob, cons_restr, used_bnds, vars_restr)

        if krawczyk_bnds is None:
            ub = None
            if debug:
                print('ub Krawczyk: ', ub, '. Singular in Matrix in Krawczyk formula.')
        else:
            # Check for feasibility (Newton operator output has to be in the interior(!) of the considered box)
            inbnds_used = check_if_in_bnds_newton_used(used_bnds, krawczyk_bnds)

            inbnds_initial = False
            if narrow_box_flag:
                # Check for feasibility (If we use the narrow box instead of the true one, then the narrow box might
                # overlap with the initial box; so we have to check if it is included)
                inbnds_initial = check_if_in_bnds_initial(used_bnds, prob.bnds)
            else:
                inbnds_initial = True

            if inbnds_used and inbnds_initial:
                # Get the box in which feasibility was verified
                # Note that we may have fixed some variables, so we have to re-include these missing variables
                bnds_for_ub = get_bnds_for_ub(bnds_fixed, used_bnds, indices_to_fix)

                # Compute an upper bound
                ub = zentrischeform(prob.symobj, bnds_for_ub, prob.vars)[1]
                if debug:
                    print('ub Krawczyk: ', ub, '. Upper bound found.')

            else:
                ub = None
                if debug:
                    print('ub Krawczyk: ', ub, '. Bound property not satisfied.')

        return ub




