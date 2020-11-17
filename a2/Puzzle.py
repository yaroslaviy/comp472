import numpy as np


class PuzzleState:
    def __init__(self, state, goal, cost, prevState, heuristic="default"):
        self.state = state
        self.goal = goal
        self.prev_state = prevState
        self.cost = cost
        self.heuristic = heuristic
        self.calculateScore()

    def get_state(self):
        return self.state

    def get_goal(self):
        return self.goal

    def get_prev_state(self):
        return self.prev_state

    def get_cost(self):
        return self.cost

    def get_score(self):
        return self.score

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return self.score > other.score

    def calculateScore(self):
        if self.heuristic == "default":
            if self.state[len(self.state) - 1] == 0:
                self.score = 1
            else:
                self.score = 0
