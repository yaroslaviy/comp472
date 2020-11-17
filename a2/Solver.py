
import heapq
from Puzzle import PuzzleState
import numpy as np
import time


class Solver():
    def __init__(self, startState, goalState, heuristic, maxtime=60):
        self.startState = startState
        self.goalState = goalState
        self.heuristic = heuristic
        self.maxtime = maxtime
        self.path = []

    def getPath(self):
        return self.path

    def solveGBFS(self):

        # initiate everything
        x_axis = [1, 0, -1,  0]
        y_axis = [0, 1,  0, -1]
        openlist = []
        closedlist = set()
        cost = 0

        # start timer
        start_time = time.time()

        # starting position
        start_node = PuzzleState(self.startState.flatten().tolist(), self.goalState.flatten(
        ).tolist(), cost, prevState=None, heuristic=self.heuristic)
        heapq.heappush(openlist, start_node)

        iterations = 0
        # while there are nodes to explore and it's less then 60 sec
        while len(openlist) > 0 and time.time() - start_time < 60:

            iterations += 1
            # pop the best node
            cur_node = openlist.pop()
            cur_state = cur_node.get_state()

            # if this node been explored already, skip it
            if str(cur_state) in closedlist:
                continue

            # mark explored
            closedlist.add(str(cur_state))

            # reached final state
            if cur_state == self.goalState.flatten().tolist():
                print('done with puzzle' + str(cur_state))
                while cur_node.get_prev_state():
                    self.path.append(cur_node)
                    cur_node = cur_node.get_prev_state()

            # find 0 tile and its coordinates
            empty_tile = cur_state.index(0)
            r, c = empty_tile // self.goalState.shape[1], empty_tile % self.goalState.shape[1]

            # reshape current state to be 2D array instead of 1D
            cur_state = np.array(cur_state).reshape(
                self.goalState.shape[0], self.goalState.shape[1])

            # check base movements
            for x, y in zip(x_axis, y_axis):

                # create new state
                new_state = np.array(cur_state)
                if r+x >= 0 and r+x < self.goalState.shape[0] and c+y >= 0 and c+y < self.goalState.shape[1]:
                    # switch tiles in new state
                    new_state[r, c], new_state[r+x, c +
                                               y] = new_state[r+x, c+y], new_state[r, c]
                    new_node = PuzzleState(new_state.flatten().tolist(), self.goalState.flatten(
                    ).tolist(), cur_node.get_cost() + 1, cur_node, self.heuristic)

                    # if state hasn't been explored before add to open
                    if str(new_node.get_state()) not in closedlist:
                        heapq.heappush(
                            openlist, new_node)

            # check diagonal wrap movements
            if (r == 0 or r == self.goalState.shape[0] - 1) and (c == 0 or c == self.goalState.shape[1] - 1):
                new_state = np.array(cur_state)

                # left top or right bottom corner
                if (r == 0 and c == 0) or (r == self.goalState.shape[0] - 1 and c == self.goalState.shape[1] - 1):
                    # switch tiles in new state
                    new_state[0, 0], new_state[self.goalState.shape[0] - 1, self.goalState.shape[1] -
                                               1] = new_state[self.goalState.shape[0] - 1, self.goalState.shape[1] - 1], new_state[0, 0]

                # right top or left bottom corner
                else:
                    # switch tiles in new state
                    new_state[self.goalState.shape[0] - 1, 0], new_state[0, self.goalState.shape[1] -
                                                                         1] = new_state[0, self.goalState.shape[1] - 1], new_state[self.goalState.shape[0] - 1, 0]
                new_node = PuzzleState(new_state.flatten().tolist(), self.goalState.flatten(
                ).tolist(), cur_node.get_cost() + 3, cur_node, self.heuristic)

                # if state hasn't been explored before add to open
                if str(new_node.get_state()) not in closedlist:
                    heapq.heappush(
                        openlist,  new_node)

            # check diagonal reg movements
            if (r == 0 or r == self.goalState.shape[0] - 1) and (c == 0 or c == self.goalState.shape[1] - 1):
                diag_moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
                for x, y in diag_moves:
                    # create new state
                    new_state = np.array(cur_state)
                    if r+x >= 0 and r+x < self.goalState.shape[0] and c+y >= 0 and c+y < self.goalState.shape[1]:
                        new_state[r, c], new_state[r+x, c +
                                                   y] = new_state[r+x, c+y], new_state[r, c]
                        new_node = PuzzleState(new_state.flatten().tolist(), self.goalState.flatten(
                        ).tolist(), cur_node.get_cost() + 3, cur_node, self.heuristic)

                        # if state hasn't been explored before add to open
                        if str(new_node.get_state()) not in closedlist:
                            heapq.heappush(
                                openlist,  new_node)
            # check row wraps movements
            if (c == 0 or c == self.goalState.shape[1] - 1):
                new_state = np.array(cur_state)

                new_state[r, 0], new_state[r, self.goalState.shape[1] -
                                           1] = new_state[r, self.goalState.shape[1] - 1], new_state[r, 0]

                new_node = PuzzleState(new_state.flatten().tolist(), self.goalState.flatten(
                ).tolist(), cur_node.get_cost() + 2, cur_node, self.heuristic)

                if str(new_node.get_state()) not in closedlist:
                    heapq.heappush(
                        openlist,  new_node)

        return self.path
