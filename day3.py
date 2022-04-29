from helpers import read_input
from collections import Counter

codes = read_input('03')

gamma, epsilon = [], []
for idx in range(len(codes[0])):
    bits = [int(code[idx]) for code in codes]
    if len(bits) - sum(bits) > sum(bits):
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')

print("Part 1: ", int(''.join(gamma), 2) * int(''.join(epsilon), 2))


def process_numbers(good_indices: list, pos: int, prime_bit=1):
    bits_ = [int(codes[idx_][pos]) for idx_ in good_indices]
    most_common = Counter(bits_).most_common()
    if prime_bit == 1:
        ref_bit = 1 if most_common[0][1] == most_common[1][1] else most_common[0][0]
    else:
        ref_bit = 0 if most_common[0][1] == most_common[1][1] else most_common[1][0]

    new_indices = [idx_ for idx_, bit in zip(good_indices, bits_) if bit == ref_bit]
    if len(new_indices) == 1:
        return codes[new_indices[0]]
    else:
        return process_numbers(new_indices, pos + 1, prime_bit)


oxygen = process_numbers(list(range(len(codes))), 0, 1)
co2 = process_numbers(list(range(len(codes))), 0, 0)

print("Part 2: ", int(oxygen, 2) * int(co2, 2))
