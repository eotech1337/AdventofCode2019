# sum of fuel requirements
import math

puzzle_input_file = r'C:\Users\matthew.wootton\PycharmProjects\AdventofCode\Files\Masses.txt'
puzzle_input = []
fuel_per_module = []

with open(r'C:\Users\matthew.wootton\PycharmProjects\AdventofCode\Files\Masses.txt') as masses:
    for line in masses:
        clean_line = int(line.rstrip('\n'))
        puzzle_input.append(clean_line)


def round_down(n):
    return math.floor(n)


for mass in puzzle_input:
    fuel_per_module.append(round_down(mass / 3) - 2)


fuel_required = sum(fuel_per_module)

print(fuel_required)
