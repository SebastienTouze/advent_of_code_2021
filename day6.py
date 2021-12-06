# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 06

reproduction_rate = 7  # days
days_before_mature = 2


def make_fishes(filename):
    file = open(filename, 'rt')
    line = file.readline()
    fishes = line.strip().split(',')
    file.close()
    fishes = list(map(int, fishes))
    return fishes


def run_day(fishes):
    for i in range(len(fishes) - 1, -1, -1):
        if 0 == fishes[i]:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1


f = make_fishes('data/day6example')
print(f)
for i in range(80):
    run_day(f)
    # print("day " + str(i+1), f)

print("Result: ", len(f))


f = make_fishes('data/day6input')
print(f)
for i in range(80):
    run_day(f)
    # print("day " + str(i+1), f)

print("Result: ", len(f))

