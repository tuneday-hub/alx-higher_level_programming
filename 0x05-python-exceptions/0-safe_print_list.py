#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Print x elememts of a list.
     Args:
        y_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
     Returns:
        The number of elements printed.
    """
    noOfPrintedElement = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            noOfPrintedElement += 1
    except IndexError:
        break
    print("")
    return noOfPrintedElement
