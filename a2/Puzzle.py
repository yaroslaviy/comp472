import numpy as np


class PuzzleState:
    def __init__(self, state, goal, level, prevState, heuristic):
        self.state = state
        self.goal = goal
        self.prev_state = prev_state
        self.level = level
        self.heuristic = heuristic

    def get_state(self):
        return self.state

    def get_goal(self):
        return self.goal

    def get_prev_state(self):
        return self.prev_state
