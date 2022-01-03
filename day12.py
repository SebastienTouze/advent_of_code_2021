# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 12

import re
import networkx as nx

LOWER_CASE = re.compile('[a-z]{2}')


def build_caves_graph(filename):
    reg = re.compile('(start|end|[a-z]{2}|[1-Z]{2})-(start|end|[a-z]{2}|[1-Z]{2})')
    graph = nx.Graph()
    with open(filename) as file:
        for line in file:
            matches = reg.match(line.strip())
            group = matches.groups()
            graph.add_edge(group[0], group[1])
    return graph


def percolate_caves(cave_network, paths, cave, path, small_cave_double_visited=False):
    path.append(cave)
    if 'end' == cave:
        paths.append(path)
        return
    for next_cave in nx.neighbors(cave_network, cave):
        if 'start' == next_cave:
            continue
        if next_cave in path and LOWER_CASE.match(next_cave):
            if small_cave_double_visited:
                continue
            else:
                percolate_caves(cave_network, paths, next_cave, path.copy(), True)
                continue
        percolate_caves(cave_network, paths, next_cave, path.copy(), small_cave_double_visited)


g = build_caves_graph('data/day12example1')
print('Part 1 example 1')
p = []
percolate_caves(g, p, 'start', [], True)
print(len(p), 'should be 19')
p = []
print('Part 2 example 1')
percolate_caves(g, p, 'start', [])
print(len(p), 'should be 103')

print('Part 1 example 2')
g = build_caves_graph('data/day12example2')
p = []
percolate_caves(g, p, 'start', [], True)
print(len(p), 'should be 226')
print('Part 2 example 2')
p = []
percolate_caves(g, p, 'start', [])
print(len(p), 'should be 3509')

print('Part 1, answer')
g = build_caves_graph('data/day12input')
p = []
percolate_caves(g, p, 'start', [], True)
print(len(p))
print('Part 2, answer')
p = []
percolate_caves(g, p, 'start', [])
print(len(p))
