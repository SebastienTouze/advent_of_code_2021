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


def make_group_fishes(filename):
    fishes = make_fishes(filename)
    group_fishes = [0] * 9
    for i in fishes:
        group_fishes[i] += 1
    return group_fishes


def run_day(fishes):
    for i in range(len(fishes) - 1, -1, -1):
        if 0 == fishes[i]:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1


def run_day_on_group(fishes):
    matures = fishes[0]
    for i in range(1, 9):
        fishes[i - 1] = fishes[i]
    fishes[8] = matures
    fishes[6] += matures


print("### Part 1 ###")
f = make_fishes('data/day6example')
f_group = make_group_fishes('data/day6example')
print(f)
print(f_group)
for i in range(80):
    run_day(f)
    run_day_on_group(f_group)

print("Result, direct method (expect 5934): ", len(f))
print("Result, better method (expect 5934): ", sum(f_group))


f = make_fishes('data/day6input')
f_group = make_fishes('data/day6input')
for i in range(80):
    run_day(f)
    run_day_on_group(f_group)

print("Result: ", len(f))

print("\n### Part 2 ###")
f_group = make_group_fishes('data/day6example')
for i in range(256):
    run_day_on_group(f_group)

print("Result (expect 26984457539): ", sum(f_group), str(26984457539 == sum(f_group)))

f_group = make_group_fishes('data/day6input')
for i in range(256):
    run_day_on_group(f_group)

print("End result by time before birth: ", f_group)

print("Result: ", sum(f_group))



