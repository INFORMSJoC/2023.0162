[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# Feasibility verification and upper bound computation using approximate active index sets

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [MIT License](LICENSE).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the [paper](https://doi.org/10.1287/ijoc.2023.0162) by C. Füllner, P. Kirst, H. Otto and S. Rebennack. 

## Cite

To cite the contents of this repository, please cite both the paper and this repo, using their respective DOIs.

https://doi.org/10.1287/ijoc.2023.0162

https://doi.org/10.1287/ijoc.2023.0162.cd

Below is the BibTex for citing this snapshot of the repository.

```
@article{FuellnerTest,
  author =        {C. F\"ullner and P. Kirst and H. Otto and S. Rebennack},
  publisher =     {INFORMS Journal on Computing},
  title =         {Repository to ``Feasibility verification and upper bound computation using approximate active index sets''},
  year =          {2024},
  doi =           {10.1287/ijoc.2023.0162.cd},
  url =           {https://github.com/INFORMSJoC/2023.0162},
}  
```

## Description

The goal of this software is to demonstrate the effect of our proposed feasibility verification and upper bound computation procedure 
for global optimization with continuous variables and possibly non-convex inequality and equality constraints.
The procedure is integrated into a spatial branch-and-bound method. 

The feasibility verification method has two main ingredients: The first one is a reformulation of inequality constraints based on
so-called approximate active index sets. The second one is the Miranda theorem based feasibility verification method for purely box- and
equality-constrained problems that was presented in an earlier [paper](https://link.springer.com/article/10.1007/s10107-020-01493-2) by Füllner, Kirst and Stein.

The main contribution is that under certain assumptions, the proposed method is sufficient to
guarantee convergence of the spatial branch-and-bound method.

For comparison, alternative feasibility verification procedures based on interval Newton methods can be used.

## Building

Our experiments where conducted using Python 3.7 with the package versions as specified in the
requirements.txt file.

To replicate the experiments or test the code on different problems, make sure that you run

```
pip install -r requirements.txt
```

to install the required packages.

## Running the code

The code can be run by executing the files "exe.py" (for our proposed method) or "exe_newton.py" (for comparison with different methods)
in the "scripts" directory.

The directory also contains a README file providing more details on how to prepare experiments and which parameters
can be set by the user.

## Results

The results of our computational tests as presented in the paper are stored in the "results" directory.
It contains a README file providing more details on the interpretation and replication of the results.

## Test Problems

The data for the considered test problems is stored in the "data" directory.
It contains a README file providing more details on the structure of the problems and how to create new ones.


## Support

For support in using this software, submit an issue via 
[e-mail](christian.fuellner@kit.edu).
