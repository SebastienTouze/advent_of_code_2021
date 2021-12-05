# Sébastien Touzé
# Script for Advent Of Code 2021
# DAY 04


# Append element to list if not already in it
def append_unique(unique_list, element):
    for i in range(len(unique_list)):
        if element == unique_list[i]:
            return unique_list
    unique_list.append(element)
    return unique_list


# Load the draw sequence then the boards as an list of 25 elements
def load_sequence_and_boards(filename):
    boards = []
    count_boards = -1  # will be set to 0 after the draw sequence is read.
    with open(filename) as input_file:
        sequence = input_file.readline().strip().split(',')
        sequence.reverse()  # easier to use the last element of a list for next steps
        for line in input_file:
            if "\n" != line:
                boards[count_boards] += line.split()
            else:
                boards.append([])
                count_boards += 1

    return sequence, boards


def play_draw(sequence, boards):
    draw = sequence.pop()
    for i in range(len(boards)):
        for j in range(25):
            if draw == boards[i][j]:
                boards[i][j] = None
    return sequence, boards, draw


# Check if a board won return -1 if no board wins, list of all winning boards if any
def winner_check(boards):
    winner_list = []
    for i in range(len(boards)):
        # test columns
        for j in range(5):
            count_nones = 0
            for k in range(5):
                # Counts a cell as validated for board number i and position k in column j
                count_nones += 1 if boards[i][j + 5 * k] is None else 0
            if 5 == count_nones:
                append_unique(winner_list, i)
        # test lines
        for j in range(5):
            count_nones = 0
            for k in range(5):
                # Counts a cell as validated for board number i and position k in line j
                count_nones += 1 if boards[i][5 * j + k] is None else 0
            if 5 == count_nones:
                append_unique(winner_list, i)

    return [-1] if 1 > len(winner_list) else winner_list


def play_until_win(sequence, boards):
    winning_boards, draw = [-1], -1

    while 0 > winning_boards[0]:
        sequence, boards, draw = play_draw(sequence, boards)
        winning_boards = winner_check(boards)

    return boards, winning_boards, draw, sequence


def load_and_play_until_win(filename):
    return play_until_win(*load_sequence_and_boards(filename))


def get_score(board, draw):
    board_sum = 0
    for i in range(len(board)):
        board_sum += int(board[i]) if board[i] is not None else 0
    return board_sum, board_sum * int(draw)


print("### Part 1 ###")
print("### Example ###")
b, wins, r, seq = load_and_play_until_win('data/day4example')
s, score = get_score(b[wins[0]], r)

print(str(s) + ' ' + r + ', expected 188 and 24\nFinal result: ' + str(score) + ', 4512 expected.')

print("### Real data ###")
b, wins, r = load_and_play_until_win('data/day4input')[:3]
# If multiple winners, the first board is counted as winner
s, score = get_score(b[wins[0]], r)

print(str(s) + ' sum, and ' + r + ' last draw,\nFinal result: ' + str(score) + '.')

print("\n\n### Part 2 ###")
print("### Example ###")
b, wins, r = load_and_play_until_win('data/day4example')[:3]
# We may have multiple winners at the same time, remove all winners, starting from the end
wins.reverse()
for win in wins:
    b.pop(win)

# This will play until only one board left in boards list. Last board will not be completed at the end
while 1 < len(b):
    b, wins, r, seq = play_until_win(seq, b)
    wins.reverse()
    for win in wins:
        b.pop(win)

b, wins, r, seq = play_until_win(seq, b)
print(get_score(b[0], r), "expect (148, 1924)")


print("### Real data ###")
real_b, real_wins, real_r, real_seq = load_and_play_until_win('data/day4input')
real_wins.reverse()
for win in real_wins:
    real_b.pop(win)

# This will play until only one board left in boards list. Last board will not be completed at the end
while 1 < len(real_b):
    real_b, real_wins, real_r, real_seq = play_until_win(real_seq, real_b)
    real_wins.reverse()
    for win in real_wins:
        real_b.pop(win)

real_b, real_wins, real_r, real_seq = play_until_win(real_seq, real_b)
final_sum, answer = get_score(real_b[0], real_r)
print(final_sum, "\nFinal result: " + str(answer))
