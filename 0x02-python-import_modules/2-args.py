#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    if len(sys.argv) == 0:
        print("0 arguments.")
    else:
        for i in range(len(sys.argv)):
            if len(sys.argv) == 1:
                print("1 argument:")
            else:
                print("{} arguments:".format(len(sys.argv)))
            print("{}: {}".format(sys.argv.index(i) + 1, i))
