# opcode computer

ints_raw = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 6, 19, 1, 19, 5, 23, 2, 13, 23, 27, 1, 10, 27, 31, 2,
            6, 31, 35, 1, 9, 35, 39, 2, 10, 39, 43, 1, 43, 9, 47, 1, 47, 9, 51, 2, 10, 51, 55, 1, 55, 9, 59, 1, 59, 5,
            63, 1, 63, 6, 67, 2, 6, 67, 71, 2, 10, 71, 75, 1, 75, 5, 79, 1, 9, 79, 83, 2, 83, 10, 87, 1, 87, 6, 91, 1,
            13, 91, 95, 2, 10, 95, 99, 1, 99, 6, 103, 2, 13, 103, 107, 1, 107, 2, 111, 1, 111, 9, 0, 99, 2, 14, 0, 0]
ints_reset = ints_raw[:]
start_index = 0
segment_count = int(len(ints_raw) // 4)
task_counter = 0
input_required = ()


# Opcode 1 Function (addition)
def opcode_1(segment):
    index_1 = int(segment[1])
    index_2 = int(segment[2])
    index_3 = int(segment[3])

    output = ints_raw[index_1] + ints_raw[index_2]
    ints_raw[index_3] = output


# Opcode 2 Function (multiplication)
def opcode_2(segment):
    index_1 = int(segment[1])
    index_2 = int(segment[2])
    index_3 = int(segment[3])

    output = ints_raw[index_1] * ints_raw[index_2]
    ints_raw[index_3] = output


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
        print("Program has finished.", index_0)
    else:
        print('Something went wrong, Encountered an unknown Opcode.', index_0)


# loop through the two inputs producing the output for each pair of inputs (will add condition for answer later)
noun = 1
verb = 1

#  Iterate the noun and verb
while verb <= 99:
    noun += 1
    if noun == 99:
        noun = 1
        verb += 1

    #  Insert their values into the ints list
    ints_raw[1] = noun
    ints_raw[2] = verb

    #  run the Program
    while task_counter < segment_count:
        check_opcode(segment_splitter())
        start_index += 4
        task_counter += 1

    #  reset the program counters
    start_index = 0
    task_counter = 0

    #  conditional to output the needed program input
    if ints_raw[0] == 19690720:
        input_required = [noun, verb]
    ints_raw = ints_reset.copy()

print(input_required)
print(100 * input_required[0] + input_required[1])

