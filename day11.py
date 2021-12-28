# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 11


def read_matrix(filename):
    matrix = []
    with open(filename) as file:
        for line in file:
            for char in line.strip():
                matrix.append([int(char), 0])
    return matrix


def recursive_flash(matrix, position):
    if 9 < matrix[position][0]:
        if 0 == matrix[position][1]:
            matrix[position][1] = 1
            if 0 < position and 0 < position % 10:
                matrix[position - 1][0] += 1
                recursive_flash(matrix, position - 1)
            if len(matrix) - 1 > position and 9 > position % 10:
                matrix[position + 1][0] += 1
                recursive_flash(matrix, position + 1)
            if 8 < position and 9 > position % 10:
                matrix[position - 9][0] += 1
                recursive_flash(matrix, position - 9)
            if 9 < position:
                matrix[position - 10][0] += 1
                recursive_flash(matrix, position - 10)
            if 10 < position and 0 < position % 10:
                matrix[position - 11][0] += 1
                recursive_flash(matrix, position - 11)
            if len(matrix) - 9 > position and 0 < position % 10:
                matrix[position + 9][0] += 1
                recursive_flash(matrix, position + 9)
            if len(matrix) - 10 > position:
                matrix[position + 10][0] += 1
                recursive_flash(matrix, position + 10)
            if len(matrix) - 11 > position and 9 > position % 10:
                matrix[position + 11][0] += 1
                recursive_flash(matrix, position + 11)
    return


def play_step(matrix):
    count_flash = 0
    for i in range(len(matrix)):
        matrix[i][0] += 1

    for i in range(len(matrix)):
        recursive_flash(matrix, i)

    for i in range(len(matrix)):
        if matrix[i][0] > 9:
            count_flash += 1
            matrix[i][0] = 0
            matrix[i][1] = 0

    return count_flash, matrix


def pretty_print_matrix(matrix):
    for i in range(10):
        for j in range(10):
            print(matrix[i * 10 + j][0], end=', ')
        print('\n')


def play_simulation(filename, nb_steps=100, until_all_flashes=False):
    total_nb_flashes, octopuses_positions = play_step(read_matrix(filename))
    for step in range(nb_steps - 1):
        nb_flashes, octopuses_positions = play_step(octopuses_positions)
        if until_all_flashes and 100 == nb_flashes:
            return total_nb_flashes, step + 2
        total_nb_flashes += nb_flashes
    return total_nb_flashes, nb_steps


print('### part 1 ###')
flashes_example = play_simulation('data/day11example', 100)
print(flashes_example[0], "expected: 1656")

flashes = play_simulation('data/day11input', 100)
print(flashes[0])

print('### part 2 ###')
nb_steps_example = play_simulation('data/day11example', 200, True)
print(nb_steps_example[1], "expected: 195")

steps_to_all_on = play_simulation('data/day11input', 550, True)
print(steps_to_all_on[1])
