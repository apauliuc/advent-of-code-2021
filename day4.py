import numpy as np
from helpers import read_input

part = 2

input_data = read_input(4)
called_numbers = list(map(int, input_data[0].split(',')))
boards = []

idx = 2
while idx < len(input_data):
    rows = []
    for r_idx in range(idx, idx + 5):
        rows.append(list(map(int, input_data[r_idx].split())))
    boards.append(np.array(rows))
    idx += 6
boards = np.stack(boards)
mask = np.zeros_like(boards)

if part == 1:
    winning_board = -1
    last_number = 0
    for number in called_numbers:
        mask[boards == number] = 1

        sum_cols = np.sum(mask, axis=1)
        sum_rows = np.sum(mask, axis=2)

        if np.sum(sum_cols == 5):
            winning_board = np.where(sum_cols == 5)[0][0]
            last_number = number
            break
        elif np.sum(sum_rows == 5):
            winning_board = np.where(sum_rows == 5)[0][0]
            last_number = number
            break

    print(last_number * np.sum(boards[winning_board] * np.where(mask[winning_board] == 1, 0, 1)))

elif part == 2:
    winning_boards = []
    last_numbers = []
    final_values = []
    for number in called_numbers:
        current_winners = []

        mask[boards == number] = 1

        sum_cols = np.sum(mask, axis=1)
        sum_rows = np.sum(mask, axis=2)

        if np.sum(sum_cols == 5):
            current_winners = np.where(sum_cols == 5)[0]
            for b in current_winners:
                if b not in winning_boards:
                    winning_boards.append(b)
                    last_numbers.append(number)
                    final_values.append(number * np.sum(boards[b] * np.where(mask[b] == 1, 0, 1)))

        if np.sum(sum_rows == 5):
            current_winners = np.where(sum_rows == 5)[0]
            for b in current_winners:
                if b not in winning_boards:
                    winning_boards.append(b)
                    last_numbers.append(number)
                    final_values.append(number * np.sum(boards[b] * np.where(mask[b] == 1, 0, 1)))

    print(final_values[-1])
