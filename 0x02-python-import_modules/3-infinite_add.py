#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    tot_arg = len(argv) - 1
    if tot_arg == 0:
        print("{}".format(tot_arg))
    else:
        result = []
        for i in range(1, tot_arg + 1):
            result.append(int(argv[i]))
        print("{}".format(sum(result)))
