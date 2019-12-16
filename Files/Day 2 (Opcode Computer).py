# opcode computer

ints_raw = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 6, 19, 1, 19, 5, 23, 2, 13, 23, 27, 1, 10, 27, 31, 2,
            6, 31, 35, 1, 9, 35, 39, 2, 10, 39, 43, 1, 43, 9, 47, 1, 47, 9, 51, 2, 10, 51, 55, 1, 55, 9, 59, 1, 59, 5,
            63, 1, 63, 6, 67, 2, 6, 67, 71, 2, 10, 71, 75, 1, 75, 5, 79, 1, 9, 79, 83, 2, 83, 10, 87, 1, 87, 6, 91, 1,
            13, 91, 95, 2, 10, 95, 99, 1, 99, 6, 103, 2, 13, 103, 107, 1, 107, 2, 111, 1, 111, 9, 0, 99, 2, 14, 0, 0]
start_index = 0
segment_count = int(len(ints_raw) // 4)
task_counter = 0


# Opcode 1 Function (addition)
def opcode_1(segment):
    index_1 = int(segment[1])
    index_2 = int(segment[2])
    index_3 = int(segment[3])

    output = ints_raw[index_1] + ints_raw[index_2]
    ints_raw[index_3] = output
    # print(segment)


# Opcode 2 Function (multiplication)
def opcode_2(segment):
    index_1 = int(segment[1])
    index_2 = int(segment[2])
    index_3 = int(segment[3])

    output = ints_raw[index_1] * ints_raw[index_2]
    ints_raw[index_3] = output
    # print(output)


# segment_splitter splits the segment out from the inits_raw list
def segment_splitter():
    opcodes = ints_raw[int(start_index):int(start_index + 4)]
    return opcodes


# check_opcode checks the first value in the segment, to determine which operation to run
def check_opcode(segment):
    index_0 = segment[0]
    if index_0 == 1:
        opcode_1(segment)
    elif index_0 == 2:
        opcode_2(segment)
    elif index_0 == 99:
        print("Program has finished.")
    else:
        print('Something went wrong, Encountered an unknown Opcode.')


# "before running the program, replace position 1 with the value 12 and replace position 2 with the value 2."
ints_raw[1] = 12
ints_raw[2] = 2


while task_counter < segment_count:
    check_opcode(segment_splitter())
    start_index += 4
    task_counter += 1

print(ints_raw[0])
