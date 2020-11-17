import numpy as np


class PuzzleState:
    def __init__(self, state, goals, cost, prevState, heuristic="default"):
        self.state = state
        self.goals = goals
        self.prev_state = prevState
        self.cost = cost
        self.heuristic = heuristic
        self.calculateScore()

    def get_state(self):
        return self.state

    def get_goals(self):
        return self.goals

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
        if self.heuristic == "misplaced":
            count1 = 0
            count2 = 0
            for state_tile, goal_tile in zip(self.state, self.goals[0].flatten().tolist()):
                if state_tile != goal_tile:
                    count1 += 1
            for state_tile, goal_tile in zip(self.state, self.goals[1].flatten().tolist()):
                if state_tile != goal_tile:
                    count2 += 1
            self.score = min(count1, count2)
