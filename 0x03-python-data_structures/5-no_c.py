#!/usr/bin/python3
def no_c(my_string):
    my_dict = {ord(c): None, ord(C): None}
    new_string = my_string.translate(my_dict)
    return new_string
