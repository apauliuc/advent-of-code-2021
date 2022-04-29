from helpers import read_input

data = read_input("01", int)

sum_part_1 = sum(a < b for a, b in zip(data, data[1:]))
print("Part 1: ", sum_part_1, "\n")

# Really lazy way summing numbers
# sum_part_2 = 0
# for idx in range(0, len(data) - 3):
#     sum_part_2 += sum(data[idx:idx + 3]) < sum(data[idx + 1:idx + 4])
sum_part_2 = sum(a < b for a, b in zip(data, data[3:]))
print("Part 2: ", sum_part_2)
