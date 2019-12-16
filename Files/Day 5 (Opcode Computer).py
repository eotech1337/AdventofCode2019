# opcode computer

'''
to do...

- create opcode 3 (done)
- create opcode 4 (output the modified user input if modified?) (done?)
- add new opcodes to check opcodes (done)
- create parameter/immediate modes
- create switch for parameter/immediate modes
- rework task counter (think this should work)
- rework segment count method (partly done)
'''

ints_raw = [3, 0, 4, 0]
start_index = 0
segment_count = len(ints_raw)
task_counter = 0
user_input_index = 0


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


# Opcode 3 Function (Input Function)
def opcode_3(segment):
    global user_input_index
    user_input = input('Please provide an input... ')
    try:
        val = int(user_input)
        index_1 = int(segment[1])
        ints_raw[index_1] = val
        user_input_index = index_1
    except ValueError:
        print('Invalid input, program will terminate.')


# Opcode 4 Function (Output Function)
def opcode_4(segment):
    print(ints_raw[user_input_index])


# segment_splitter splits the segment out from the inits_raw list
def segment_splitter():
    if ints_raw[start_index] == 1:
        opcodes = ints_raw[int(start_index):int(start_index + 4)]
        return opcodes
    elif ints_raw[start_index] == 2:
        opcodes = ints_raw[int(start_index):int(start_index + 4)]
        return opcodes
    elif ints_raw[start_index] == 3:
        opcodes = ints_raw[int(start_index):int(start_index + 2)]
        print(opcodes)
        return opcodes
    elif ints_raw[start_index] == 4:
        opcodes = ints_raw[int(start_index):int(start_index + 2)]
        print(opcodes)
        return opcodes


# check_opcode checks the first value in the segment, to determine which operation to run
def check_opcode(segment):
    index_0 = segment[0]
    if index_0 == 1:
        opcode_1(segment)
    elif index_0 == 2:
        opcode_2(segment)
    elif index_0 == 3:
        opcode_3(segment)
    elif index_0 == 4:
        opcode_4(segment)
    elif index_0 == 99:
        print("Program has finished.")
    else:
        print('Something went wrong, Encountered an unknown Opcode.')


while task_counter < segment_count:
    try:
        check_opcode(segment_splitter())
    except IndexError:
        print('Program Finished.')
    if len(segment_splitter()) == 2:
        start_index += 2
    elif len(segment_splitter()) == 4:
        start_index += 4
    task_counter += 1


# currently only out puts on input of 3 or 4. issue is somewhere in segment splitter or main while loop at bottom.
