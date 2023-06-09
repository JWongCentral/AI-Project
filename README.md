# AI-Projects
This repository contains some common AI problems that have been solved using a multitude of AI algorithms to solve the problem.
## Jug-Problem
The Jug problem is when you have 2 different sized jugs with 4 functions...
    1. Transfer from jug 1 to jug 2
    2. Transfer from jug 2 to jug 1
    3. Empty jug 2
    4. Empty jug 1
The purpose of this project is to see/predict if we can reach a certain goal using A* (A-star), BFS, and DFS.
## Sudoku
Sudoku is a game with simple rules regarding how to solve the puzzle.
It is a 9x9 grid that contains only numbers 1-9 and with 3 rules regarding how to select the numbers
    1. All numbers in a row must be unique and numbered 1-9
    2. All numbers in a column must be unique and numbered 1-9
    3. All numbers in a 3x3 grid must be unique and numbered 1-9

There are a couple of ways to solve the problem, the ones implemented in the code is using domain and then a domain reducing algorithm, AC3.

The first way which is the easiest and most ineffective is to randomly go through each one of the empty cells and assign a random number and check if it is a possible solution as we go.

The second way involves creating a domain for each empty cell and using backtracking.
The domain contains a set of numbers 1-9 and they are only removed when there is no possibility of using that number.
Such as when you add in a number 3 to a cell, the entire row cells remove 3 from the domain.
Same for the column and the 3x3 grid.
When we reach an empty domain and an unassigned cell we must back track to a previous state to continue another possibility
This is a better solution but it can still be improved

The third way involves a forward checking algorithm by using most contrained variable (MCV) or LCV(least constained variable). 
In this case MCV will give a better result as we can prune  more possibilities early on improving overall runtime.
It will first search for the domain with the lowest size, as that is the most constrained variable.
Then it will assign those numbers using the second way, but using a forward checking procedure to guide which cell we go through first.