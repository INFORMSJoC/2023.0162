import sys
sys.path.append('../data')

import intvalpy as ip
from TestProblem import *
from BoundingProcedures import *
import sympy as sym
import numbers

'''
This file contains a basic implementation of feasibility-based bounds tightening techniques.
Note that this had some issues, so it was not used in our tests for the paper.
'''

class Node(object):
    def __init__(self, data, parent):
        self.data = data
        self.iv = None
        self.children = []
        self.parent = parent

    def add_children(self, child):
        self.children.append(child)

    def get_siblings(self):
        siblings = []
        for i in self.parent.children:
            if i.data != self.data and i.children != self.children:
                siblings.append(i)
            else:
                pass
        return siblings


    def calc_iv(self):
        if self.iv is None:
            children_iv = [i.iv for i in self.children]
            if str(self.data) == "<class 'sympy.core.add.Add'>":
                self.iv = sum(children_iv)
            elif str(self.data) == "<class 'sympy.core.mul.Mul'>":
                self.iv = np.prod(children_iv)
            else:
                pass
        else:
            pass



    def __str__(self):
        return(str(self.data))

def build_expression_tree(expr):
    """
    Generates an Expression Tree using the Node Class defined in this file.

    Parameters
    ----------
    expr : sympy expression

    Returns
    -------
    Node
        The root node of the built expression tree.

    """
    root = None
    node_list = []
    remaining_list = 1
    while remaining_list:
        if root is None:
            remaining_list = []
            root = Node(expr.func, None)
            node_list.append(root)
            remaining_list.append([root, list(expr.args)])
        else:
            par, child = remaining_list.pop()
            new_nodes = []
            for i in child:
                if not i.args:
                    new_node = Node(i, par)
                    node_list.append(new_node)
                    new_nodes.append(new_node)
                    par.add_children(new_node)
                else:
                    if str(i.func) == "<class 'sympy.core.power.Pow'>":
                        #This part handles the replacement of Pow with Mul.
                        sub_expr = i.args[0]
                        sub_expr_pow = i.args[1]
                        args = [sub_expr for i in range(0, sub_expr_pow)]
                        new_node = Node(sym.mul.Mul, par)
                    else:
                        new_node = Node(i.func, par)
                        args = list(i.args)
                    par.add_children(new_node)
                    node_list.append(new_node)
                    remaining_list.append([new_node, list(args)])

    return root, node_list

def initialize_tree(root, vars, bnds):
    """
    Initializes an expression tree built by the build_expression_tree method.
    Allocates the right intervals to the corresponding leafs of the tree.

    Parameters
    ----------
    root : Node
        Root Node of the considered Expression Tree.
    vars : List of sym.Symbols
        Variables in the expression.
    bnds : list of ndarrays
        Initial Boxes for each variable in the expression.

    Returns
    -------
    Node
        Root Node of the modified tree.

    """

    inter_dic = {}
    for i, j in zip(vars, bnds):
        inter_dic[i] = ip.Interval(j[0], j[1])

    remain = [root]
    while remain:
        curr = remain.pop()
        if isinstance(curr.data, numbers.Number):
            curr.iv = ip.Interval(curr.data, curr.data)
        elif isinstance(curr.data, sym.symbol.Symbol):
            curr.iv = inter_dic[curr.data]
        else:
            pass
        for i in curr.children:
            remain.append(i)
    return root

def visualize_tree(root):
    """
    Generates a simple output for a given Expression Tree.

    Parameters
    ----------
    root : Node
        Root node of the considered Expression Tree.

    Returns
    -------
    None
    """

    print([root.data, root.iv])
    remain = [root]
    par = None
    layer = []
    while remain:
        curr = remain.pop()
        if curr.children:
            for i in curr.children:
                remain.append(i)
        else:
            pass

        layer.append(curr.data)
        for j in curr.children:
            layer.append([j.data, j.iv])
        if len(layer) > 1:
            print(layer)
        layer = []

def up(node):
    """
    Performs an upward step of the FBBT Algorithm. Recursive Function.

    Parameters
    ----------
    node : Node
        Node for which the up step should be performed.
    """

    children_iv = [i.iv for i in node.children]
    if None in children_iv:
        for i in node.children:
            if i.iv is None:
                up(i)
            else:
                pass
        up(node)
    else:
        if str(node.data) == "<class 'sympy.core.add.Add'>":
            node.iv = sum(children_iv)
        elif str(node.data) == "<class 'sympy.core.mul.Mul'>":
            iv = 1
            for i in children_iv:
                iv = iv * i
            node.iv = iv

        else:
            pass

def up_intersect(node, iv):
    node.iv = node.iv & iv

def iv_dif(node, sibl):
    dif = node.iv
    for i in sibl:
        dif = dif - i.iv
    if dif == ip.Interval():
        dif = ip.Interval(-iv.inf, iv.inf)
    return dif

def iv_div(node, sibl):
    div = node.iv
    for i in sibl:
        div = div * 1/i.iv
    if div == ip.Interval():
        div = ip.Interval(-iv.inf, iv.inf)
    return div

def down(node):
    inverse_operation_map = {"<class 'sympy.core.add.Add'>" : iv_dif,
                             "<class 'sympy.core.mul.Mul'>" : iv_div}
    if node.children:
        for i in node.children:
            #build list of siblings
            siblings = []
            for j in node.children:
                if j != i:
                    siblings.append(j)
            #test if the child i is a constant
            if isinstance(i.data, numbers.Number):
                pass
            else:
                new_iv = i.iv & (inverse_operation_map[str(node.data)](node, siblings))
                i.iv = new_iv

        for i in node.children:
            down(i)

def extract_bnds(node_list, vars):
    dic = {}
    for i in node_list:
        if isinstance(i.data, sym.symbol.Symbol):
            dic[i.data] = np.array([i.iv[0].inf, i.iv[0].sup])
    return dic

###############################################################################

def fbbt(cons, vars, orig_bnds, numiter):
    curr_bnds = list(orig_bnds)
    #print('Original Bounds', curr_bnds)
    for j in range(0, numiter):
        #print('Iteration', j)
        print(curr_bnds)
        for i in cons:
            if i['type'] == 'ineq':
                intersect = ip.Interval(-iv.inf, 0)
            else:
                intersect = ip.asinterval(0)
            expr = i['func']
            root, node_list = build_expression_tree(expr)
            root_init = initialize_tree(root, vars, curr_bnds)
            up(root_init)
            up_intersect(root_init, intersect)
            down(root_init)
            new_bnds = extract_bnds(node_list, vars)
            bnds_list = []
            for k, s in zip(vars, curr_bnds):
                try:
                    bnds_list.append(new_bnds[k])
                except KeyError:
                    bnds_list.append(s)
            curr_bnds = bnds_list

    #print(curr_bnds)
    #print(orig_bnds)

    return curr_bnds
