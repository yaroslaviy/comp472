import random
import re
import numpy as np
from Solver import Solver
import sys
import getopt


goal_states = np.array(([[1, 2, 3, 4],
                         [5, 6, 7, 0]], [[1, 3, 5, 7],
                                         [2, 4, 6, 0]]))


def Greedy(puzzleNum, init_state, goal_states, heuristic):
    solver = Solver(puzzleNum, init_state, goal_states, heuristic)
    path, done_time = solver.solve("gbfs")
    file = open('./output/solution/' + str(puzzleNum) + '_gbfs-' +
                heuristic + '_solution.txt', 'w')
    if len(path) > 0:
        for state in reversed(path):
            if not state.get_prev_state():
                file.write(
                    "0 0 " + re.sub(r',|\[|\]', r'', str(state.get_state())) + '\n')
                continue

            for cur, par in zip(state.get_state(), state.get_prev_state().get_state()):
                if(cur != par):
                    changedtile = cur+par
            file.write(str(changedtile) + " " +
                       str(state.get_cost() - state.get_prev_state().get_cost()) + " " + re.sub(r',|\[|\]', r'', str(state.get_state())) + '\n')

        file.write(str(done_time) + " " + str(path[0].get_cost()))
    else:
        file.write('no solution')


def UCS(puzzleNum, init_state, goal_states, heuristic):
    solver = Solver(puzzleNum, init_state, goal_states, heuristic)
    path, done_time = solver.solve("ucs")
    file = open('./output/solution/' + str(puzzleNum) +
                '_ucs_solution.txt', 'w')
    if len(path) > 0:
        for state in reversed(path):
            if not state.get_prev_state():
                file.write(
                    "0 0 " + re.sub(r',|\[|\]', r'', str(state.get_state())) + '\n')
                continue

            for cur, par in zip(state.get_state(), state.get_prev_state().get_state()):
                if(cur != par):
                    changedtile = cur+par
            file.write(str(changedtile) + " " +
                       str(state.get_cost() - state.get_prev_state().get_cost()) + " " + re.sub(r',|\[|\]', r'', str(state.get_state())) + '\n')

        file.write(str(done_time) + " " + str(path[0].get_cost()))
    else:
        file.write('no solution')


def Astar(puzzleNum, init_state, goal_states, heuristic):
    solver = Solver(puzzleNum, init_state, goal_states, heuristic)
    path, done_time = solver.solve("astar")
    file = open('./output/solution/' + str(puzzleNum) + '_astar-' +
                heuristic + '_solution.txt', 'w')
    if len(path) > 0:
        for state in reversed(path):
            if not state.get_prev_state():
                file.write(
                    "0 0 " + re.sub(r',|\[|\]', r'', str(state.get_state())) + '\n')
                continue

            for cur, par in zip(state.get_state(), state.get_prev_state().get_state()):
                if(cur != par):
                    changedtile = cur+par
            file.write(str(changedtile) + " " +
                       str(state.get_cost() - state.get_prev_state().get_cost()) + " " + re.sub(r',|\[|\]', r'', str(state.get_state())) + '\n')

        file.write(str(done_time) + " " + str(path[0].get_cost()))
    else:
        file.write('no solution')


if __name__ == "__main__":
    file1 = open('./input.txt', 'r')
    lines = file1.readlines()
    for i, line in enumerate(lines):
        numbers = line.split()
        numbers = [int(i) for i in numbers]
        init_state = np.array(numbers).reshape(
            goal_states[0].shape[0], goal_states[0].shape[1])
        Greedy(i, init_state, goal_states, "h1")
        UCS(i, init_state, goal_states, "h1")
        Astar(i, init_state, goal_states, "h1")
        Greedy(i, init_state, goal_states, "h2")
        Astar(i, init_state, goal_states, "h2")


# Generate 50 random puzzles and write them into a text file by line
my_file = open("my_50_puzzles.txt", "w")

for i in range(50):
    possible_numbers = [0, 1, 2, 3, 4, 5, 6, 7]
    random.shuffle(possible_numbers)

    # .write() only takes strings as argument, so we use str() to write integer as a string into the file.
    for numb in possible_numbers:
        my_file.write(str(numb))
        my_file.write(" ")
    # creates a new line after each puzzle's contents are written in the file
    my_file.write("\n")

my_file.close()
