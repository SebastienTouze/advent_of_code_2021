# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 01

# Parse a file and print the count of depth increases and the file line number
def parse_file_and_count_depth_increase(full_path_filename):
    increase_count = 0
    line_count = 1
    with open(full_path_filename, "rt") as file:
        old_depth = int(file.readline())
        for line in file:
            line_count += 1
            depth = int(line)
            if depth > old_depth:
                increase_count += 1
            old_depth = depth

    print(str(increase_count) + ' increase in ' + str(line_count) + ' lines.')


# Parse the input file to create a temp file with sum on window of 3 depths
def write_sliding_window_file(filename):
    windows_sums = [0, 0, 0]
    line_count = 2
    with open("data/" + filename, "rt") as input_file, open("tmp/" + filename, "wt") as output_file:
        windows_sums[0] += int(input_file.readline())
        second_line_depth = int(input_file.readline())
        windows_sums[0] += second_line_depth
        windows_sums[1] += second_line_depth
        for line in input_file:
            line_count += 1
            windows_sums[0] += int(line)
            windows_sums[1] += int(line)
            windows_sums[2] += int(line)
            if 0 == line_count % 3:
                output_file.write(str(windows_sums[0]) + "\n")
                windows_sums[0] = 0
            elif 1 == line_count % 3:
                output_file.write(str(windows_sums[1]) + "\n")
                windows_sums[1] = 0
            else:
                output_file.write(str(windows_sums[2]) + "\n")
                windows_sums[2] = 0


parse_file_and_count_depth_increase("data/day1input")

print("Example P2")
write_sliding_window_file("day1exemple")
parse_file_and_count_depth_increase("tmp/day1exemple")

print("Part2")
write_sliding_window_file("day1input")
parse_file_and_count_depth_increase("tmp/day1input")
