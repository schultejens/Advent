def get_strings(filename):
    with open(filename, "r") as fp:
        num = fp.readlines()
    return [str(i.rstrip()) for i in num]