# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 10

import numpy as np


COUPLES = {'<': ">", '{': "}", '[': "]", '(': ")"}
INVALID_POINTS_CONVERSION = {')': 3, ']': 57, '}': 1197, '>': 25137}
INCOMPLETE_POINTS_CONVERSION = {')': 1, ']': 2, '}': 3, '>': 4}


def is_open_chunk(char):
    return char in COUPLES


class ChunkNode:

    def __init__(self, char, parent):
        self.chunk = [char, '']
        self.parent = parent

    def set_closing(self, char):
        self.chunk[1] = char

    def get_valid_closing(self):
        return COUPLES[self.chunk[0]]

    def is_valid(self):
        if '' == self.chunk[1]:
            return True
        elif COUPLES[self.chunk[0]] == self.chunk[1]:
            return True
        else:
            return False


def score_line_validity(line, line_nb):
    current_chunk = None
    for char in line:
        if is_open_chunk(char):
            current_chunk = ChunkNode(char, current_chunk)
        else:
            current_chunk.set_closing(char)
            if current_chunk.is_valid():
                current_chunk = current_chunk.parent
            else:
                print("In line %i: invalid : expected %s, get %s" % (line_nb, COUPLES[current_chunk.chunk[0]], char))
                return INVALID_POINTS_CONVERSION[char]
    return current_chunk


def score_line_incomplete(chunk_leaf, line_nb):
    chunk = chunk_leaf
    score = 0
    closing_sequence = ''
    while chunk.parent is not None:
        closing_sequence += chunk.get_valid_closing()
        score = score * 5 + INCOMPLETE_POINTS_CONVERSION[chunk.get_valid_closing()]
        chunk = chunk.parent
    closing_sequence += chunk.get_valid_closing()
    score = score * 5 + INCOMPLETE_POINTS_CONVERSION[chunk.get_valid_closing()]
    print("In line %i: incomplete, missing %s" % (line_nb, closing_sequence))
    return score


def read_and_build_tree(filename):
    line_counter = 0
    with open(filename) as file:
        incomplete_line_scores = []
        invalidity_points = 0
        for line in file:
            line_counter += 1
            line_nb_points = score_line_validity(line.strip(), line_counter)
            if type(line_nb_points) is int:
                invalidity_points += line_nb_points
            else:
                incomplete_line_scores.append(score_line_incomplete(line_nb_points, line_counter))

    return invalidity_points, incomplete_line_scores


print('### Part 1 & 2 ###')
example_result = read_and_build_tree('data/day10example')
print('Part1: ', example_result[0], ' expect 26397')
print('Part2: ', int(np.median(example_result[1])), ' expect 288957')

result = read_and_build_tree('data/day10input')
print('Part1: ', result[0])
print('Part2: ', int(np.median(result[1])))
