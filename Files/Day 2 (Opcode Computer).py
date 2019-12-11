# opcode computer

opcode_input = [1, 0, 0, 0]

# Opcode 1 Function
def opcode_1(*args):
    index_values = list(args)
    index_1 = int(index_values[1])
    index_2 = int(index_values[2])
    index_3 = int(index_values[3])

    output = index_values[index_1] + index_values[index_2]
    opcode_input[index_3] = output
    print(opcode_input)

# Opcode 2 Function
def opcode_2(*args):
    index_values = list(args)
    index_1 = int(index_values[1])
    index_2 = int(index_values[2])
    index_3 = int(index_values[3])

    output = index_values[index_1] * index_values[index_2]
    opcode_input[index_3] = output
    print(opcode_input)

#for every slice of 4 from the list, do the below.

if opcode_input[0] == 1:
    opcode_1(*opcode_input)
elif opcode_input[0] == 2:
    opcode_2(*opcode_input)
elif opcode_input[0] == 99:
    print("Program has finished.")
else:
    print('Something went wrong, Encountered an unknown Opcode.')

