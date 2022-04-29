from helpers import read_input

commands = read_input('02', str.split)
horiz = depth = aim = 0

for command, value in commands:
    if command == "forward":
        horiz += int(value)
        depth += int(value) * aim
    elif command == "down":
        aim += int(value)
    elif command == "up":
        aim -= int(value)

print("Part 1: ", horiz * aim)
print("Part 2: ", horiz * depth)
