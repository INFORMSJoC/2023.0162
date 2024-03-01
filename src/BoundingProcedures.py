from __future__ import division

import sys
sys.path.append('../data')

'''
In this file, centered forms and interval_arithmetic methods are implemented,
that determine valid lower and upper bounds for the values of functions on
a given box B.
'''

################################################################################
# Necessary Imports
################################################################################
import sympy as sym
import numbers
from sympy.tensor.array import derive_by_array
import numpy as np
import intvalpy as ip
from TestProblem import *
import random

################################################################################
# Auxiliary Functions
################################################################################

def midpoint(bnds):
    '''
    Calculates the midpoint of a box.

    Parameters
    ----------
    bnds : [np.array,...]
        Bounds of the box where a midpoint should be calculated.

    Returns
    -------
    mp : [np.array,...]
        Midpoint of the input box bnds.
    '''
    mp = [(i[1]+i[0])/2 for i in bnds]
    return np.array(mp)

def symvars_to_pyvars(symexpr):
    '''
    Takes a string of a sympy expression as input and returns a string that through
    eval can be used to define a function in standard python format.

    Note: Works only for dim <= 10 for now.

    Parameters
    ----------
    symexpr : sympy expression
        A sympy expression

    Returns
    -------
    pystr : callable
        Runnable Python code
    '''

    #---------------------------------------------------------------------------
    # Variable replacement
    symlist = ['x10', 'x9', 'x8', 'x7', 'x6', 'x5', 'x4', 'x3', 'x2', 'x1']
    pylist = ['x[9]', 'x[8]', 'x[7]', 'x[6]', 'x[5]', 'x[4]', 'x[3]', 'x[2]', 'x[1]', 'x[0]']
    #---------------------------------------------------------------------------
    pystr = str(symexpr)
    for i, j in zip(symlist, pylist):
        pystr = pystr.replace(i, j)
    #---------------------------------------------------------------------------
    # Function replacement
    symfuncs = ['sin', 'cos', 'sqrt', 'exp', 'pi', 'log']
    pyfuncs = ['np.sin', 'np.cos', 'np.sqrt', 'np.exp', 'np.pi', 'np.log']
    for i, j in zip(symfuncs, pyfuncs):
        pystr = pystr.replace(i, j)
    #---------------------------------------------------------------------------
    return pystr

def interval_extension(sym, vars, bnds):
    '''
    Takes a string of a sympy expression and replaces all free variables with the interval
    they are bounded by. Results in the native interval extension, which can be
    used by bounding methods such as alphaBB.

    Parameters
    ----------
    sym : string
        Sympy expression in string format
    vars : list of sympy Symbols
    bnds : list of ndarrays

    Returns
    -------
    str_sym : string
        Natural interval extension of sym in string format.
    '''
    str_iv = ['ip.Interval(' + str(i[0]) + ',' + str(i[1]) + ')' for i in reversed(bnds)]
    str_vars = [str(i) for i in reversed(vars)]
    str_sym = sym
    for i, j in zip(str_vars, str_iv):
        str_sym = str_sym.replace(i, j)
    for i, j in zip(['sin', 'cos', 'sqrt', 'exp', 'pi', 'abs'], ['np.sin', 'np.cos', 'np.sqrt', 'np.exp', 'np.pi', 'abs']):
        str_sym = str_sym.replace(i, j)
    return str_sym


def interval_to_arrayList(intv):
    '''
    Takes an interval from intvalpy and transforms it to a numpy array or a list of numpy arrays
    '''

    # single interval
    if type(intv) == ip.RealInterval.ClassicalArithmetic:
        result = np.array([float(intv.a), float(intv.b)])

    # multi-dimensional interval
    elif type(intv) == ip.RealInterval.ArrayInterval:
        result = [np.array([float(i.a), float(i.b)]) for i in intv]

    return result



################################################################################
# Bounding Procedures used
################################################################################

def zentrischeform(func, bnds, vars):
    '''
    Returns lower and upper bound calculated by centered forms.

    Parameters
    ----------
    func : sympy expression
        Function for which bounds should be calculated
    bnds : list of ndarrays
        Bounds for the function evaluation
    vars : list of sympy Symbols
        Variables contained in the function

    Returns
    -------
    FXz : 2D ndarray
    '''

    
    try:
        #Handle case where objective is a constant
        if isinstance(func, numbers.Number):
            return np.array([func, func])
        # F(X, z) := f(z) + F'(X) * (X - z)
        #---------------------------------------------------------------------------
        # f(z)
        z = midpoint(bnds)
        fz = sym.lambdify(vars, func)(*z)
        #---------------------------------------------------------------------------
        # F'(X)
        fx = derive_by_array(func, vars)
        FX = eval(interval_extension(str(fx), vars, bnds))
        #---------------------------------------------------------------------------
        # (X - z)
        Xmz = [i - j for i, j in zip(vars, list(z))]
        Xmz = eval(interval_extension(str(Xmz), vars, bnds))
        #---------------------------------------------------------------------------
        # F'(X) * (X - z)
        sol = 0
        for i, j in zip(FX, Xmz):
            sol = sol + i * j
        FXz = fz + sol
        # FXz = FXz[0]
        FXz = interval_to_arrayList(FXz)
        return FXz
    except NameError:
        return None
    

    

def interval_arithmetic(func, bnds, vars):
    '''
    Returns lower and upper bound calculated by standard interval arithmetic.

    Parameters
    ----------
    func : sympy expression
        Function for which bounds should be calculated
    bnds : list of ndarrays
        Bounds for the function evaluation
    vars : list of sympy Symbols
        Variables contained in the function

    Returns
    -------
    func : 2D ndarray
    '''
    func = eval(interval_extension(str(func), vars, bnds))
    func = interval_to_arrayList(func)

    return func
