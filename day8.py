# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 08

import re


REMARKABLE_CONVERT = ['1', '4', '7', '8']


def count_remarkable_digits(sequence):
    counter = 0
    for digits in sequence:
        if (2 <= len(digits) <= 4) or 7 == len(digits):
            counter += 1
    return counter


def parse_and_count_remarkable_output(filname):
    re_str = ' '.join(['([abcdefg]{2,7})'] * 10) + ' \| ' + ' '.join(['([abcdefg]{2,7})'] * 4)
    line_mask = re.compile(re_str)
    counter = 0
    with open(filname) as file:
        for line in file:
            data = line_mask.match(line.strip()).groups()
            if 14 == len(data):
                # array of input, output
                counter += count_remarkable_digits(data[10:14])
            else:
                raise Exception("Not enough data in line.")
    return counter


def get_remarkable(input_sequence):
    remarkable = [''] * 4
    for digits in input_sequence:
        if 2 == len(digits):
            remarkable[0] = digits
        elif 3 == len(digits):
            remarkable[2] = digits
        elif 4 == len(digits):
            remarkable[1] = digits
        elif 7 == len(digits):
            remarkable[3] = digits
    return remarkable


def get_number_from_remarkable(digits, remarkable):
    for i in range(4):
        if len(digits) == len(remarkable[i]):
            return REMARKABLE_CONVERT[i]


def count_digits_contained(digits, test_is_inside):
    counter = 0
    for digit in test_is_inside:
        if digit in digits:
            counter += 1
    return counter


def parse_and_solve(filname):
    re_str = ' '.join(['([abcdefg]{2,7})'] * 10) + ' \| ' + ' '.join(['([abcdefg]{2,7})'] * 4)
    line_mask = re.compile(re_str)
    counter = 0
    output_sum = 0
    with open(filname) as file:
        for line in file:
            line_output = [''] * 4
            data = line_mask.match(line.strip()).groups()
            if 14 != len(data):
                raise Exception("Not enough data in line.")
            remarkable = get_remarkable(data[0:10])
            # We will solve each number based on a heuristic
            for i in range(4):
                if 2 <= len(data[10 + i]) <= 4 or 7 == len(data[10 + i]):
                    line_output[i] = get_number_from_remarkable(data[10 + i], remarkable)
                elif 5 == len(data[10 + i]):  # 2, 3, 5
                    if 2 == count_digits_contained(data[10 + i], remarkable[0]):
                        line_output[i] = '3'
                    else:
                        if 3 == count_digits_contained(data[10 + i], remarkable[1]):
                            line_output[i] = '5'  # 3 digits are in common between 5 and 4
                        else:
                            line_output[i] = '2'  # only 2 digits in common with 4
                else:  # 6 digits : 6, 9 or 0
                    if 2 == count_digits_contained(data[10 + i], remarkable[0]):  # is 1 contained in this group of digits ?
                        # We have a 0 or 9
                        if 4 == count_digits_contained(data[10 + i], remarkable[1]):
                            line_output[i] = '9'
                        else:
                            line_output[i] = '0'
                    else:
                        line_output[i] = '6'
            output_sum += int(''.join(line_output))
    return output_sum


print('### part 1 ###')
print(str(parse_and_count_remarkable_output('data/day8example')) + ' expected: 26.')
print(parse_and_count_remarkable_output('data/day8input'))

print('### part 2 ###')
print(str(parse_and_solve('data/day8example')) + ' expected: 61229')
print(parse_and_solve('data/day8input'))
