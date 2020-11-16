
from queue import PriorityQueue, Queue

from numpy.core import path
from Puzzle import PuzzleState
import numpy as np
import time


class Solver():
    def __init__(self, startState, goalState, heuristic, maxtime=60):
        self.startState = startState
        self.goalState = goalState
        self.heuristic = heuristic
        self.maxtime = maxtime
        self.solutionPath = []

        def getPath(self):
            return path

        def solveUCS(self):
            return

        def solveA(self):
            return

        def solveGBFS(self):
            return
