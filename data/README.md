# Data for replication

The files "TestProblem.py" and "TestProblem_all.txt" contain the definitions of several benchmark problems from the COCONUT Benchmark Library. 
The Problems are implemented as objects of the OptimizationProblem class, defined in OptimizationProblem.py in the "src" directory.

For the original raw data, see the COCONUT Benchmark library, available under <https://arnold-neumaier.at/glopt/coconut/Benchmark/Benchmark.html>.


## Using the data
In order to use a test problem in experiments using our code, that problem has to be included in the file "TestProblem.py".

Note that not all problems considered in the paper are contained in that file in its current form, but only a subset is included here. 
The reason is that importing TestProblem.py with all problems in it, slows down the initial steps of the code a lot. 
If a problem not contained in this file should be tested, it first has to be copied to this file from TestProblem_all.txt, which includes all problem formulations.

## How to define new problems

To understand the OptimizationProblem class and being able to add new problems, consider the example hs006:

```
symobj_hs006 = (1-x1)**2
sol_hs006 = np.array([1., 1.])
eq1_hs006 = 10*(x2 - x1**2)
cons_hs006 = [{'func':eq1_hs006, 'type':'eq', 'prop':'non-convex'}]
vars_hs006 = [x1, x2]
bnds_hs006 = [np.array([-10000, 10000]), np.array([-10000, 10000])]
hs006 = OptimizationProblem('hs006', sol_hs006, symobj_hs006, cons_hs006, vars_hs006, bnds_hs006)
```

We look at each line in detail.

```
symobj_hs006 = (1-x1)**2
```

This line defines the objective function in Sympy format.

```
sol_hs006 = np.array([1., 1.])
```

This line defines an array which contains the (approximate) optimal solution provided by the COCONUT Benchmark library.
Note that sometimes the provided solution is slightly infeasible, so we replaced it by a better approximation obtained from BARON.

```
eq1_hs006 = 10*(x2 - x1**2)
cons_hs006 = [{'func':eq1_hs006, 'type':'eq', 'prop':'non-convex'}]
```

This part defines the constraints. First, we define a function in Sympy format. Then, all constraints are stored in a list in the cons object. 
Note that type defines whether we have an equality ('eq') or an inequality ('ineq') constraint, where the latter always assume
a <=-type of inequality. Further note that 'prop' allows to define if a constraint is convex or non-convex (or unknown).
This is relevant for the OBBT where convexity can be exploited, but not relevant for the actual branch-and-bound method.

```
vars_hs006 = [x1, x2]
```

This line defines the required variables.

```
bnds_hs006 = [np.array([-10000, 10000]), np.array([-10000, 10000])]
```

This line defines the initial box constraints. If no variable bounds were defined in the COCONUT Benchmark library, we 
used -10000 and 10000 as the default bounds.

```
hs006 = OptimizationProblem('hs006', sol_hs006, symobj_hs006, cons_hs006, vars_hs006, bnds_hs006)
```

Finally, all previously defined elements are used to create an OptimizationProblem object.


