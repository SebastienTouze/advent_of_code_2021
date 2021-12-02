# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 02

import re


def move_submarine_part1(commands_file):
    # Position is [horizontal, depth]
    position = [0, 0]

    command = re.compile('(forward|down|up) ([0-9]+)')

    with open(commands_file) as file:
        for line in file:
            match = command.match(line)
            if 'forward' == match.group(1):
                position[0] += int(match.group(2))
            else:
                position[1] += int(match.group(2)) * (1 if 'down' == match.group(1) else -1)

        print(position)
        print('result: ' + str(position[0] * position[1]))


def move_submarine_part2(commands_file):
    # Position is [horizontal, depth, aim]
    position = [0, 0, 0]

    command = re.compile('(forward|down|up) ([0-9]+)')

    with open(commands_file) as file:
        for line in file:
            match = command.match(line)
            if 'forward' == match.group(1):
                position[0] += int(match.group(2))
                position[1] += int(match.group(2)) * position[2]
            else:
                position[2] += int(match.group(2)) * (1 if 'down' == match.group(1) else -1)

        print(position)
        print('result: ' + str(position[0] * position[1]))


print("### Part 1 ###")
move_submarine_part1('data/day2example')
move_submarine_part1('data/day2input')

print("\n### Part 2 ###")
move_submarine_part2('data/day2example')
move_submarine_part2('data/day2input')
