from functools import reduce
input_range = range(165432, 707912)
# input_range = range(111111, 123456)
potential_passwords_list = []


def is_ascending(args):

    def ascend_check(prev, item):
        return prev <= item

    if reduce(ascend_check, args, False):
        return True
    else:
        return False


print(is_ascending([1, 1, 1, 1, 1, 1]))
