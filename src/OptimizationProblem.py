from __future__ import division
'''
This file contains the class definition of the OptimizationProblem class
that is used to define optimization problems for the solver.
'''

class OptimizationProblem(object):
    '''
    A class for the definition of Optimization Problems.

    Attributes
    ----------
    name : str
        Name of the problem (e.g. taken from a benchmark)
    obj : function
        Objective function of the optimization problem (currently not used)
    cons : list of dictonaries
        Dictonary containing the constraints of the problem
    bnds : list of 1D ndarrays
        List containing the box constraints of the problem
    '''
    def __init__(self, name, sol, symobj, cons, vars, bnds):
        '''
        Parameters
        ----------
        name : str
            Name of the problem (e.g. taken from a benchmark)
        sol : ndarray
            optimal point of the problem
        symobj : sympy expression
            Objective function of self in sympy format
        cons : list of dictonaries
            Dictonary containing the constraints of the problem
        vars : list of sympy Symbols
            Symbols used in symobjective
        bnds : list of 1D ndarrays
            List containing the box constraints of the problem
        '''
        self.name = name
        self.sol = sol
        self.obj = None
        self.symobj = symobj
        self.cons = cons
        self.vars = vars
        self.bnds = bnds

    def __str__(self):
        cons_print = []
        for i in self.cons:
            if i['type'] == 'eq':
                cons_str = str(i['func']) + ' = 0'
                cons_print.append(cons_str)
            else:
                cons_str = str(i['func']) + ' <= 0'
                cons_print.append(cons_str)
        cons = '\n'.join(cons_print)

        bnds = '['
        for i in self.bnds:
            bnds = bnds + str(tuple(i))
        bnds = bnds + ']'

        obj = 'minimize ' + str(self.symobj)

        return '\n'.join([self.name, obj, cons, bnds])


class SolutionObject(object):
    '''
    Class for passing the Solution from the branch-and-bound method to the database.
    '''
    def __init__(self, status, name, lb, ub, box, iters_first, iters_term, time_first, time_term):
        self.status = status
        self.name = name
        self.lb = lb
        self.ub = ub
        self.box = box
        self.iters_first = iters_first
        self.iters_term = iters_term
        self.time_first = time_first
        self.time_term = time_term
