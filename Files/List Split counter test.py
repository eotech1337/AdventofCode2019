ints_raw = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2]
task_counter = 0


def segment_splitter():
    opcodes = ints_raw[int(task_counter):int(task_counter + 4)]
    return opcodes

'''for n in ints_raw[0::4]:
    
    print(n)'''


print(segment_splitter())
