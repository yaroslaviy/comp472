import numpy as np
from Solver import Solver
import sys
import getopt
import random

goal_state = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 0]])

init_state = np.array([[1, 5, 3, 4],
                       [2, 6, 7, 0]])


def Greedy(init_state, goal_state, heuristic):
    solver = Solver(init_state, goal_state, heuristic)
    path = solver.solveGBFS()
    return path


if __name__ == "__main__":
    print(Greedy(init_state, goal_state, "default"))


#Generate 50 random puzzles and write them into a text file by line
my_file = open("my_50_puzzles.txt", "w")

for i in range(50):
    possible_numbers = [0,1,2,3,4,5,6,7]
    random.shuffle(possible_numbers)
    print(possible_numbers)
    
    for numb in possible_numbers:   #.write() only takes strings as argument, so we use str() to write integer as a string into the file.
        my_file.write(str(numb))   
        my_file.write(" ")
    my_file.write("\n")             #creates a new line after each puzzle's contents are written in the file

my_file.close()                     