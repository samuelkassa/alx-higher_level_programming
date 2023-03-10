#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    argv = sys.argv[1:]
    couner = len(argv)
    index = 1
    if counter == 0:
        print("{:d} arguments.").format(counter))
    elif counter == 1:
        print("{:d} argument:".format(conter))
        print("{:d} {:s}".format(index, sys.argv[1]))
    else:
        print("{:d} arguments".format(counter))
        while index <= counter:
            print("{:d} {:s}".format(index, sys.argv[index]))
            index += 1
