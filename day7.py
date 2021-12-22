# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 07

def load_file(filename):
    file = open(filename)

    positions = file.readline().split(',')
    positions = list(map(int, positions))

    pos_min = min(positions)
    pos_max = max(positions)

    return positions, pos_min, pos_max


def do_part1(filename):
    positions, pos_min, pos_max = load_file(filename)

    # this variable will store the end values : optimum position, fuel used. Initialized with fuel big enough so that
    # first run with pos_min must be better
    optimum = [pos_min, sum(positions)]
    for optimum_candidate in range(pos_min, pos_max + 1):
        dist_total = 0
        for i in range(len(positions)):
            dist_total += abs(positions[i] - optimum_candidate)
        if dist_total < optimum[1]:
            optimum = [optimum_candidate, dist_total]

    print(optimum)


def do_part2(filename):
    positions, pos_min, pos_max = load_file(filename)

    optimum = [pos_min, pow(sum(positions) + 1, 2)]
    for optimum_candidate in range(pos_min, pos_max + 1):
        dist_total = 0
        for i in range(len(positions)):
            dist = abs(positions[i] - optimum_candidate)
            dist_total += dist * (1 + dist) / 2  # Arithmetic sum
        if dist_total < optimum[1]:
            optimum = [optimum_candidate, dist_total]

    print(optimum)


print("### Part 1 ###")
do_part1('data/day7input')

print("### Part 2 ###")
do_part2('data/day7example')
do_part2('data/day7input')


