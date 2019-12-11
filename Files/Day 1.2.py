# sum of fuel requirements
import math

puzzle_input_file = r'C:\Users\matthew.wootton\PycharmProjects\AdventofCode\Files\Masses.txt'
puzzle_input = []
fuel_per_module = []


with open(r'C:\Users\matthew.wootton\PycharmProjects\AdventofCode\Files\Masses.txt') as masses:
    for line in masses:
        clean_line = int(line.rstrip('\n'))
        puzzle_input.append(clean_line)


for mass in puzzle_input:
    new_fuel = [(math.floor(mass / 3) - 2)]
    while True:
        new_fuel.append(math.floor(new_fuel[-1] / 3) - 2)
        if new_fuel[-1] > 0:
            total_fuel = sum(new_fuel)
        else:
            fuel_per_module.append(total_fuel)
            break

fuel_required = sum(fuel_per_module)

print(fuel_per_module)
print(fuel_required)