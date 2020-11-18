import numpy as np


class PuzzleState:
    def __init__(self, state, goals, cost, prevState, algo, heuristic="default"):
        self.state = state
        self.goals = goals
        self.prev_state = prevState
        self.cost = cost
        self.heuristic = heuristic
        self.hscore = 0
        self.fscore = 0

        self.calculateScores(algo)

    def get_state(self):
        return self.state

    def get_goals(self):
        return self.goals

    def get_prev_state(self):
        return self.prev_state

    def get_cost(self):
        return self.cost

    def get_fscore(self):
        return self.fscore

    def get_hscore(self):
        return self.hscore

    def __lt__(self, other):
        return self.fscore < other.fscore

    def __eq__(self, other):
        return self.fscore == other.fscore

    def __gt__(self, other):
        return self.fscore > other.fscore

    def calculateScores(self, algo):
        if self.heuristic == "h0":
            if self.state[len(self.state) - 1] == 0:
                self.hscore = 0
            else:
                self.hscore = 1
        if self.heuristic == "h1":
            count1 = 0
            count2 = 0
            for state_tile, goal_tile in zip(self.state, self.goals[0].flatten().tolist()):
                if state_tile != goal_tile:
                    count1 += 1
            for state_tile, goal_tile in zip(self.state, self.goals[1].flatten().tolist()):
                if state_tile != goal_tile:
                    count2 += 1
            self.hscore = min(count1, count2)

        if(algo == 'gbfs'):
            self.fscore = self.hscore
        elif(algo == 'astar'):
            self.fscore = self.hscore + self.cost
        elif(algo == 'ucs'):
            self.fscore = self.cost
