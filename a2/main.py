import numpy as np
from Solver import Solver
import sys
import getopt

goal_state = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 0]])

init_state = np.array([[1, 5, 3, 4],
                       [2, 6, 7, 0]])


def Greedy(init_state, goal_state, heuristic):
    solver = Solver(init_state, goal_state, heuristic)
    path = solver.solveGBFS()


if __name__ == "__main__":
    Greedy(init_state, goal_state, "default")
