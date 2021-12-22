# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 09

import copy


def count_low_points_and_risk(filename, max_lines=None):
    with open(filename) as file:
        line_up = file.readline().strip()
        line = file.readline().strip()
        line_length = len(line)
        nb_lines = line_length if max_lines is None else max_lines
        local_min_counter = 0
        risk_level_sum = 0
        min_points = []
        heightmap = [[-1] * line_length for i in range(nb_lines)]
        for i in range(line_length):
            heightmap[0][i] = int(line_up[i])
            if ((i > 0 and line_up[i] < line_up[i - 1]) or 0 == i) and line_up[i] < line[i] and \
                    (line_length - 1 == i or (i < line_length - 1 and line_up[i] < line_up[i + 1])):
                local_min_counter += 1
                risk_level_sum += int(line_up[i]) + 1
                min_points.append((i, 0))

        y = 0
        for line_down in file:
            y += 1
            for i in range(line_length):
                heightmap[y][i] = int(line[i])
                if (0 == i or line[i] < line[i - 1]) and line[i] < line_down[i] and \
                        line[i] < line_up[i] and (line_length - 1 == i or line[i] < line[i + 1]):
                    local_min_counter += 1
                    risk_level_sum += int(line[i]) + 1
                    min_points.append((i, y))

            line_up = line
            line = line_down

        for i in range(line_length):
            heightmap[nb_lines - 1][i] = (int(line_down[i]))
            if (line[i] < line[i - 1] or 0 == i) and line[i] < line_up[i] and \
                    (line_length - 1 == i or line[i] < line[i + 1]):
                local_min_counter += 1
                risk_level_sum += int(line_down[i]) + 1
                min_points.append((i, nb_lines - 1))

        return local_min_counter, risk_level_sum, heightmap, min_points


def propagate_bassin(matrix, x, y):
    if -1 == x or -1 == y or len(matrix[0]) <= x or len(matrix) <= y:
        return 0
    if 9 == matrix[y][x]:
        return 0

    matrix[y][x] = 9
    return 1 + propagate_bassin(matrix, x - 1, y) + propagate_bassin(matrix, x + 1, y) + \
           propagate_bassin(matrix, x, y - 1) + propagate_bassin(matrix, x, y + 1)


def get_top_bassin_sizes(matrix, minimum_list):
    bassin_sizes = []
    for minimum in range(len(minimum_list)):
        bassin_sizes.append(propagate_bassin(matrix, *minimum_list[minimum]))

    ordered_maxes = [0, 0, 0]
    for i in range(len(bassin_sizes)):
        for j in range(3):
            if ordered_maxes[j] < bassin_sizes[i]:
                for k in range(2 - j):
                    ordered_maxes[2 - k] = ordered_maxes[2 - k - 1]
                ordered_maxes[j] = bassin_sizes[i]
                break
    return ordered_maxes


print('### Part 1 ###')
nb_min_example, risk_sum_example, matrix_height_example, mins_example = count_low_points_and_risk('data/day9example', 5)
print(str(risk_sum_example) + ', expected: 15')
nb_min, risk_sum, matrix_height, mins = count_low_points_and_risk('data/day9input')
print(risk_sum)

print('### Part 2 ###')
top_maxes = get_top_bassin_sizes(matrix_height_example, mins_example)
print(top_maxes, top_maxes[0] * top_maxes[1] * top_maxes[2], 'expect 1134')
top_maxes = get_top_bassin_sizes(matrix_height, mins)
print(top_maxes, top_maxes[0] * top_maxes[1] * top_maxes[2])
