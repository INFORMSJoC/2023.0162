# Running the code

The code can be run by executing the files "exe.py" (for our proposed method) or "exe_newton.py" (for comparison with different methods)
in the "scripts" directory.


## Data preparation

To test a specific problem, it has to be prepared as described in the "data" directory. Then, it should be included in the problem list
in the exe file, for instance

```
problem_list = [ simpllpb, extrasim, hs006, maratos, tame ]
```

## Parameter choices

The user can use the "exe.py" (or "exe_newton.py") file to define several parameters for the experiments.

**debug_init**: This defines if summary of each branch-and-bound iteration should be printed to the console for debugging purposes.

**tol_init**: This is a stopping tolerance for the spatial branch-and-bound method.

**maxiter_init**: Specifies a maximum number of iterations for the spatial branch-and-bound method.

**maxtime_init**: Specifies a maximum time in seconds for the spatial branch-and-bound method.

**use_obbt_init**: If true, then optimality based bounds tightening techniques are used to reduce the initial box constraints before the branch-and-bound method is started.

**use_fbbt_init**: If true, then feasibility based bounds tightening techniques are used throughout the algorithm.

CAUTION: This did not work properly for all test problems, so we recommend not to use it. It was also not used in our computational tests for the paper.

**enlarge_box_constraints_init**: If true, then the initial box constraints are considered as standard inequality constraints and slightly larger box constraints are introduced.
This is required, as the Miranda theorem based feasibility verification method has theoretical guarantees only if the feasible points are not located on the boundary of a box.
Similary, interval Newton methods can fail to verify the existence of feasible points on the boundary of a box.

**tunnel_approach_init**: If true, then instead of a standard spatial branch-and-bound method, only one specific path through the branching tree is considered (deep search).
This path is constructed around the known approximately optimal solution specified in the test problem definition (see directory "data").

**strict_removal_init**: The default is true. If false, then lines 3 to 4 of Algorithm 1 from the paper are not used. This is sometimes required for the tunneling approach
if the provided approximate solution is slightly infeasible.

**var_lifting_init**: If true, then instead of using the proposed reformulation approach from the paper using approximate active index sets, all inequality constraints are 
reformulated as equality constraints using slack variables. Then, the Miranda theorem based method is applied to the obtained system of equations.

Specifically for the alternative approaches based on interval Newton methods (see "exe_newton.py"), we have the following parameters.

**narrow_box_init**: If true, then a local solver (either IPOPT or SLSQP) is used to compute a local solution on the current box in each iteration. Then, a narrow box is constructed around it,
in which it is attempted to verify the existence of feasible points.

**narrow_box_tol_init**: Can be used to define the length of the constructed narrow box.

**local_solver**: Can be used to specify the local solver. Should be either IPOPT or SLSQP.

For the parameter configurations that we used for the computational experiments presented in the paper, see "results" directory.


## Running the code

After the data is prepared and the parameters are set, the spatial branch-and-bound method can be run by simply executing the files "exe.py" (for our proposed method) or "exe_newton.py" (for comparison with different methods).

## Result logging

The results for new experiments are stored in the directory "run logs". In order to change this, the line 

```
with open(''.join(['../run logs/', i.name,'.csv']), mode='w') as solutions_file:
```

has to be adapted.

CAUTION: Files are overwritten if the same problem is tested again, so you might want to move them to a different folder before starting another batch of tests.

