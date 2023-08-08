# Solving Sudoku with AI

This is the final project of the course CS 246 "Artificial Intelligence" by 
Ararat Ghazaryan, Hovhannes Hovhannisyan and Aram Adamyan.

## sudoku.ipynb

This notebook contains all the algorithms implemented for solving the sudoku puzzle 
including the Backtracking algorithm, the Genetic algorithm, the Simulated algorithm, 
the Hill Climbing algorithm, and the AHA algorithm (custom). 
Additionally, it contains a visualization of each of the algorithms' performance.

## app.py

This application is the interface of the sudoku puzzle implemented by us 
which initializes a sudoku puzzle (4x4, 9x9, and 16x16) and solves it using 
either the Backtracking algorithm or the AHA algorithm. 
The other algorithms are not present here, as they are more complex 
and require more time and computational power to run successfully.
* This application is designed only for visualization purposes, 
it initializes a predefined puzzle for each size without 
any randomness and solves it.

## sudoku.csv

This dataset is taken from the 
[Kaggle](https://www.kaggle.com/datasets/radcliffe/3-million-sudoku-puzzles-with-ratings) datasets.

## Simulated annealing

The Simulated annealing algorithm's implementation is taken from
[GitHub](https://github.com/tcompa/sudoku_simulated_annealing/blob/master/lib_simulated_annealing.py)
