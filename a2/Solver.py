
import heapq
from Puzzle import PuzzleState
import numpy as np
import time
import re


class Solver():
    def __init__(self, puzzleNum, startState, goalStates, heuristic, maxtime=60):
        self.startState = startState
        self.goalStates = goalStates
        self.heuristic = heuristic
        self.maxtime = maxtime
        self.path = []
        self.puzzleNum = puzzleNum

    def getPath(self):
        return self.path

    def solveGBFS(self):
        file = open('./' + str(self.puzzleNum) + '-gbfs-search.txt', 'w')

        # initiate everything
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        openlist = []
        closedlist = set()
        cost = 0

        # start timer
        start_time = time.time()

        # starting position
        start_node = PuzzleState(self.startState.flatten().tolist(
        ), self.goalStates, cost, prevState=None, heuristic=self.heuristic)
        heapq.heappush(openlist, start_node)

        iterations = 0
        # while there are nodes to explore and it's less then 60 sec
        while len(openlist) > 0 and time.time() - start_time < 60:

            iterations += 1
            # pop the best node
            cur_node = heapq.heappop(openlist)
            cur_state = cur_node.get_state()
            file.write(str(cur_node.get_score()) + " 0 " +
                       str(cur_node.get_score()) + " " + re.sub(r',|\[|\]', r'', str(cur_state)) + '\n')
            # if this node been explored already, skip it
            if str(cur_state) in closedlist:
                continue

            # mark explored
            closedlist.add(str(cur_state))

            # reached final state
            if cur_state == self.goalStates[0].flatten().tolist() or cur_state == self.goalStates[1].flatten().tolist():
                done_time = time.time() - start_time
                print('Done with puzzle #' + str(self.puzzleNum) +
                      ' in: ' + str(done_time) + " seconds.")
                self.path.append(cur_node)

                while cur_node.get_prev_state():
                    cur_node = cur_node.get_prev_state()
                    self.path.append(cur_node)
                break

            # find 0 tile and its coordinates
            empty_tile = cur_state.index(0)
            r, c = empty_tile // self.goalStates[0].shape[1], empty_tile % self.goalStates[0].shape[1]

            # reshape current state to be 2D array instead of 1D
            cur_state = np.array(cur_state).reshape(
                self.goalStates[0].shape[0], self.goalStates[0].shape[1])

            # check base movements
            for x, y in moves:

                # create new state
                new_state = np.array(cur_state)
                if r+x >= 0 and r+x < self.goalStates[0].shape[0] and c+y >= 0 and c+y < self.goalStates[0].shape[1]:
                    # switch tiles in new state
                    new_state[r, c], new_state[r+x, c +
                                               y] = new_state[r+x, c+y], new_state[r, c]
                    new_node = PuzzleState(new_state.flatten().tolist(
                    ), self.goalStates, cur_node.get_cost() + 1, cur_node, self.heuristic)

                    # if state hasn't been explored before add to open
                    if str(new_node.get_state()) not in closedlist:
                        heapq.heappush(
                            openlist, new_node)

            # check diagonal wrap movements
            if (r == 0 or r == self.goalStates[0].shape[0] - 1) and (c == 0 or c == self.goalStates[0].shape[1] - 1):
                new_state = np.array(cur_state)

                # left top or right bottom corner
                if (r == 0 and c == 0) or (r == self.goalStates[0].shape[0] - 1 and c == self.goalStates[0].shape[1] - 1):
                    # switch tiles in new state
                    new_state[0, 0], new_state[self.goalStates[0].shape[0] - 1, self.goalStates[0].shape[1] -
                                               1] = new_state[self.goalStates[0].shape[0] - 1, self.goalStates[0].shape[1] - 1], new_state[0, 0]

                # right top or left bottom corner
                else:
                    # switch tiles in new state
                    new_state[self.goalStates[0].shape[0] - 1, 0], new_state[0, self.goalStates[0].shape[1] -
                                                                             1] = new_state[0, self.goalStates[0].shape[1] - 1], new_state[self.goalStates[0].shape[0] - 1, 0]
                new_node = PuzzleState(new_state.flatten().tolist(
                ), self.goalStates, cur_node.get_cost() + 3, cur_node, self.heuristic)

                # if state hasn't been explored before add to open
                if str(new_node.get_state()) not in closedlist:
                    heapq.heappush(
                        openlist,  new_node)

            # check diagonal reg movements
            if (r == 0 or r == self.goalStates[0].shape[0] - 1) and (c == 0 or c == self.goalStates[0].shape[1] - 1):
                diag_moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
                for x, y in diag_moves:
                    # create new state
                    new_state = np.array(cur_state)
                    if r+x >= 0 and r+x < self.goalStates[0].shape[0] and c+y >= 0 and c+y < self.goalStates[0].shape[1]:
                        new_state[r, c], new_state[r+x, c +
                                                   y] = new_state[r+x, c+y], new_state[r, c]
                        new_node = PuzzleState(new_state.flatten().tolist(
                        ), self.goalStates, cur_node.get_cost() + 3, cur_node, self.heuristic)

                        # if state hasn't been explored before add to open
                        if str(new_node.get_state()) not in closedlist:
                            heapq.heappush(
                                openlist,  new_node)
            # check row wraps movements
            if (c == 0 or c == self.goalStates[0].shape[1] - 1):
                new_state = np.array(cur_state)

                new_state[r, 0], new_state[r, self.goalStates[0].shape[1] -
                                           1] = new_state[r, self.goalStates[0].shape[1] - 1], new_state[r, 0]

                new_node = PuzzleState(new_state.flatten().tolist(
                ), self.goalStates, cur_node.get_cost() + 2, cur_node, self.heuristic)

                if str(new_node.get_state()) not in closedlist:
                    heapq.heappush(
                        openlist,  new_node)

        return (self.path, done_time)
