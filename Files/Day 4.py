input_range = range(165432, 707912)
# input_range = range(111111, 123456)
potential_passwords_list = []


def is_ascending(args):
    if len(args) <= 6:
            if args[1] >= args[0]:
                if args[2] >= args[1]:
                    if args[3] >= args[2]:
                        if args[4] >= args[3]:
                            if args[5] >= args[4]:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
    else:
        return False


def has_double(args):
    if len(args) <= 6:
        if args[1] == args[0]:
            return True
        elif args[2] == args[1]:
            return True
        elif args[3] == args[2]:
            return True
        elif args[4] == args[3]:
            return True
        elif args[5] == args[4]:
            return True
        else:
            return False
    else:
        return False


for num in input_range:
    potential_password = [int(x) for x in str(num)]
    if is_ascending(potential_password) is True:
        if has_double(potential_password) is True:
            potential_passwords_list.append(potential_password)
        else:
            continue
    else:
        continue

print(len(potential_passwords_list))