from __future__ import division

import sys
sys.path.append('../data')

################################################################################
# Necessary Imports
################################################################################

from operator import itemgetter
from BoundingProcedures import *
from MirandaMethod import *
from copy import deepcopy
from TestProblem import *
from Transformation import *
from Ineqtransformation import *
from time import time
from lifting_approach import *
from OBBT import *
from FBBT import *
from lifting_approach import *
from IntervalNewton import *

'''
Implementation of a spatial branch and bound algorithm that implements the miranda based method to determine if the current box contains a feasible point.
'''



################################################################################
# Help Functions (used for some operations inside the mainfunctions)
################################################################################

def branch(box):
    '''
    Divides a box along its longest edge into two subboxes.

    Parameters
    ----------
    box : list of numpy arrays
        Box to be divided

    Returns
    -------
    (box1, box2) : tuple of lists of ndarrays
        Subboxes of box, obtained through dividing box along longest edge
    '''
    # determine which edge is the longest
    edge_length = [i[1] - i[0] for i in box]
    longest_inde = edge_length.index(max(edge_length))
    longest_edge = box[longest_inde]
    # calculate midpoint of that edge
    midpoint_edge = (longest_edge[0] + longest_edge[1])/2
    # create copy of box with changed side
    box1 = deepcopy(box)
    box1[longest_inde] = np.array([longest_edge[0], midpoint_edge])
    # create copy of box with changed side
    box2 = deepcopy(box)
    box2[longest_inde] = np.array([midpoint_edge, longest_edge[1]])
    return [box1, box2]

def index_withlb(lis):
    '''
    Determines the index for the tuple element of a list where the second element
    of the tuple is minimal.

    Parameters
    ----------
    lis : list of tuples

    Returns
    -------
    index : int
        index of the smallest list element
    '''
    smallest = lis[0][1]
    index = 0
    for i in range(0, len(lis)):
        if lis[i][1] < smallest:
            index = i
        else:
            pass
    return index

def index_lvguv(lis, val):
    '''
    Returns indexes in a list of all elements > val.

    Parameters
    ----------
    lis : list of tuples
    val : float

    Returns
    -------
    indexes : list of ints
    '''
    indexes = []
    for i in range(0, len(lis)):
        if lis[i][1] > val:
            indexes.append(i)
    return indexes

def index_finder(lis):
    '''
    Determines the index of the smallest element of a list.
    '''
    smallest = lis[0][1]
    index = 0
    for i in range(0, len(lis)):
        if lis[i][1] < smallest:
            smallest = lis[i][1]
            index = i
        else:
            pass
    return index


def tunnel_boxes(opt, boxes):
    opt_list = opt.tolist()
    new_boxes = []
    for box in boxes:
        pnt_in_box = True
        for i, j in zip(opt_list, box):
            if i >= j[0] and i <= j[1]:
                pass
            else:
                pnt_in_box = False
        if pnt_in_box:
            new_boxes.append(box)
    return new_boxes

################################################################################
# The Branch-and-Bound Method
################################################################################


def sBaB(problem, tol=0.01, maxiter=10000, maxtime=10800, enlarge_box_constraints=False, extended_miranda=True, use_obbt=False, use_fbbt=(False, 10), var_lifting=False, debug=True, inversion_phase=True, transform_interval=1, tunnel_approach=False, strict_removal=True):
    # enlarge starting box by 1 and model box constraints as inequality constraints if required
    if enlarge_box_constraints:
        prob = transform_problem(problem)
    else:
        prob = problem
    # perform the slack variable lifting_approach if required
    if var_lifting:
        prob = variable_lifting(prob)
        extended_miranda = False
    else:
        pass
    # set vars to determine first upper bound determination time and iteration
    first_time = None
    first_iter = None
    updated_flag = False
    # set iteration counter
    k = 0
    # set initial lower bound
    v_lb = -float('inf')
    # set initial upper bound
    v_ub = float('inf')
    # set best known feasible point
    x_ub = None
    # perform optimation based bounds tightening (optional)
    if use_obbt:
        initial_bnds = obbt(prob)
    else:
        initial_bnds = prob.bnds
    # initialize branching list
    L = [(initial_bnds, v_lb)]
    # save time of start
    starting_time = time()
    # begin iteration
    while v_ub - v_lb > tol and k < maxiter and time()-starting_time < maxtime and L:
        # increase iteration counter
        k = k + 1
        # get the element of L with the lowest lower bound
        index = index_finder(L)
        current = L.pop(index)
        # branch the current box into two sub-boxes along the longest edge
        branch_list = branch(current[0])
        if debug:
            print(''.join(['Length of List: ', str(len(branch_list))]))
        if tunnel_approach is False:
            pass
        else: 
            branch_list = tunnel_boxes(prob.sol, branch_list)
        # initialize list of potential feasible points and corresponding upper bounds
        upper_bounds = [(x_ub, v_ub)]
        if extended_miranda:
            for i in branch_list:
                # perform feasibility based bounds tightening (optional)
                if use_fbbt[0]:
                    bnds_i = fbbt(prob.cons, prob.vars, i, use_fbbt[1])
                else:
                    bnds_i = i
                # determine active index set
                cons_i = activeIndexSet(prob, bnds_i, strict_removal)
                if cons_i is None:
                    if debug:
                        print('cons_i is None - aborted Iteration')
                else:
                    # determine lower bound for the current box
                    lb_i = zentrischeform(prob.symobj, bnds_i, prob.vars)[0]
                    L.append((bnds_i, lb_i))
                    # stop if number of constraints > dimension (LICQ violated)
                    if len(cons_i) > len(bnds_i):
                        ub = None
                    else:
                        # determine upper bound for current box
                        ub = miranda_method(prob, bnds_i, cons_i, k, coordinate_transformation=inversion_phase, numit_transformation=transform_interval)
                    if ub is None or ub < lb_i: # if no ub is determined or ub < lb (through rounding) - do not continue
                        pass
                    else:
                        upper_bounds.append((bnds_i, ub))

        else:
            for i in branch_list:
                # perform feasibility based bounds tightening (optional)
                if use_fbbt[0]:
                    bnds_i = fbbt(prob.cons, prob.vars, i, use_fbbt[1])
                else:
                    bnds_i = i
                # determine lower bound for the current box
                lb_i = zentrischeform(prob.symobj, bnds_i, prob.vars)[0]
                L.append((bnds_i, lb_i))
                # determine upper bound for current box
                ub = miranda_method(prob, bnds_i, prob.cons, k, coordinate_transformation=inversion_phase, numit_transformation=transform_interval)
                if ub is None or ub < lb_i: # if no ub is determined or ub < lb (through rounding) - do not continue
                    pass
                else:
                    upper_bounds.append((bnds_i, ub))

        smalles_ind = index_finder(upper_bounds)
        smalles_ele = upper_bounds[smalles_ind]
        v_ub = smalles_ele[1]

        if v_ub != float('inf') and not updated_flag: #save num iterations and time when first ub is determined
            first_time = time() - starting_time
            first_iter = k
            updated_flag = True

        x_ub = smalles_ele[0]
        indices = index_lvguv(L, v_ub)
        for index in sorted(indices, reverse=True):
            del L[index]

        if not L:
            status = 'Error: List is empty.'
        else:
            ij = index_finder(L)
            v_lb = L[ij][1]

        if debug:
            print('')
            print('Iteration', k)
            print('---------------------')
            print('Problem: ', prob.name)
            for i in branch_list:
                print(i)
            print('Box with ub =', x_ub)
            print('Upper bound =', v_ub)
            print('Lower Bound =', v_lb)
            print('---------------------')
        else:
            print('Iteration', k)

    ending_time = time()
    time_passed = ending_time - starting_time

    print(time_passed, v_ub, v_lb, k, len(L))

    if v_ub - v_lb < tol:
        return SolutionObject('Success', prob.name, v_lb, v_ub, x_ub, first_iter, k, first_time, time_passed)
    if k >= maxiter:
        return SolutionObject('Maxiter', prob.name, v_lb, v_ub, x_ub, first_iter, k, first_time, time_passed)
    if not L:
        return SolutionObject('List Empty', prob.name, v_lb, v_ub, x_ub, first_iter, k, first_time, time_passed)
    if time_passed >= maxtime:
        return SolutionObject('Maxtime', prob.name, v_lb, v_ub, x_ub, first_iter, k, first_time, time_passed)


