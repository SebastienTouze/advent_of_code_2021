# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 03

import os


def get_power(stats, supremum):
    d_max = pow(2, len(stats)) -1
    gamma = 0
    for i in range(len(stats)):
        if supremum/2 < stats[len(stats) - i - 1]:
            gamma += pow(2, i)

    # power = epsilon * gamma
    # but we have epsilon + gamma = d_max, so we ca make this to be more simple
    power = gamma * (d_max - gamma)
    return power


def make_stats(filename):
    with open(filename) as file:
        line = file.readline()
        num_bits = len(line) - 1
        stats = [0] * num_bits
        count_lines = 1
        for i in range(num_bits):
            stats[i] += int(line[i])

        for line in file:
            count_lines += 1
            for i in range(num_bits):
                stats[i] += int(line[i])

    return stats, count_lines


def get_oxygen_co2(path_filename, indicator, bit_to_check):
    (stats, count_lines) = make_stats(path_filename)
    output_filename = (path_filename.split("/"))[1].split("_")[0]
    count_written_lines = 0
    last_write = ""
    with open(path_filename, 'rt') as input_file, \
            open('tmp/' + output_filename, 'wt') as output_file:
        predominant = 1 if count_lines / 2 <= stats[bit_to_check] else 0
        for line in input_file:
            if ('oxygen' == indicator and predominant == int(line[bit_to_check])) or \
                    ('co2' == indicator and 1 - predominant == int(line[bit_to_check])):
                output_file.write(line)
                count_written_lines += 1
                last_write = line
    if 1 < count_written_lines:
        # File rotation to avoid tmp files proliferation
        os.rename('tmp/' + output_filename, 'tmp/' + output_filename + '_old')
        return get_oxygen_co2('tmp/' + output_filename + '_old', indicator, bit_to_check + 1)
    else:
        return last_write.strip()  # removing the \n


print("### Example P1 ###")
(s, nb_lines) = make_stats("data/day3example")
print(str(get_power(s, nb_lines)) + ', target is 198')

print("### Part 1 ###")
(s, nb_lines) = make_stats("data/day3input")
print(get_power(s, nb_lines))


print("\n\n### Part 2 ###")
print("### Example ###")
rco = get_oxygen_co2('data/day3example', 'oxygen', 0)
print("O2: " + rco + ", decimal: " + str(int(rco, 2)))
ro = get_oxygen_co2('data/day3example', 'co2', 0)
print("CO2: " + ro + ", decimal: " + str(int(ro, 2)))

print('result : ' + str(int(rco, 2) * int(ro, 2)) + ', target is 230')

print("\nReal set")
rco = get_oxygen_co2('data/day3input', 'oxygen', 0)
print("O2: " + rco + ", decimal: " + str(int(rco, 2)))
ro = get_oxygen_co2('data/day3input', 'co2', 0)
print("CO2: " + ro + ", decimal: " + str(int(ro, 2)))

print('result : ' + str(int(rco, 2) * int(ro, 2)))
