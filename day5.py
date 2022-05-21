from helpers import read_input
import numpy as np


def split_input(line_):
    v1, v2 = line_.split('->')
    return tuple(map(int, v1.split(',') + v2.split(',')))


coordinates = read_input(5, func=split_input)

size = 1000
grid = np.zeros((size, size))
diagonal_lines = []

for x1, y1, x2, y2 in coordinates:
    points = []
    if x1 == x2:
        points = [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    elif y1 == y2:
        points = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    else:
        diagonal_lines.append((x1, y1, x2, y2))

    for x, y in points:
        grid[x, y] += 1

print(f'Only horizontal: {np.sum(grid >= 2)}')

for x1, y1, x2, y2 in diagonal_lines:
    range_x = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
    range_y = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)

    for x, y in zip(range_x, range_y):
        grid[x, y] += 1

print(f'Full grid: {np.sum(grid >= 2)}')
