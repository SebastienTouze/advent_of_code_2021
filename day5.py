# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 05

import math
import re


def pretty_print(matrix):
    d_size = int(math.sqrt(len(matrix) + 1))
    for i in range(d_size):
        print(matrix[d_size * i: d_size + i * d_size])


def build_diagram(filename, diagram_size):
    diagram = [0] * pow(diagram_size, 2)
    p = re.compile('^([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)$')
    with open(filename) as file:
        for line in file:
            matches = p.match(line)
            (x1, y1, x2, y2) = map(int, matches.groups())
            if x1 == x2:  # vertical
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    diagram[x1 + i * diagram_size] += 1
            if y1 == y2:  # horizontal
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    diagram[i + y1 * diagram_size] += 1
            if abs(x1 - x2) == abs(y1 - y2):  # diagonal
                distance = abs(x2 - x1)  # horizontal distance, same as vertical distance
                x_direction = int((x2 - x1)/distance)
                y_direction = int((y2 - y1)/distance)
                for i in range(distance + 1):
                    diagram[(x1 + x_direction * i) + ((y1 + y_direction * i) * diagram_size)] += 1
    return diagram


def count_dangerous_zones(diagram):
    counter = 0
    for i in diagram:
        counter += 1 if 1 < i else 0
    return counter


print('### Part 1 ###')
print('### Example ###')
d = build_diagram('data/day5example', 10)
pretty_print(d)
print("Number of dangerous areas: " + str(count_dangerous_zones(d)))

print('### Real data ###')
d = build_diagram('data/day5input', 991)
print("Number of dangerous areas: " + str(count_dangerous_zones(d)))
