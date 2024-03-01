from __future__ import division

import sys
sys.path.append('../data')

'''
This file does not contain the spatial branch-and-bound method used by the algorithm -> this is specified in sBaB.py
However, this file contains essential helper functions and should not be modified.
'''

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

################################################################################
# Auxiliary Functions (used for some operations inside the main functions)
################################################################################

def branch(box):
    '''
    Divides a box along its longest edge into two sub-boxes.

    Parameters
    ----------
    box : list of numpy arrays
        Box to be divided

    Returns
    -------
    (box1, box2) : tuple of lists of ndarrays
        Sub-boxes of box, obtained through dividing box along longest edge
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

