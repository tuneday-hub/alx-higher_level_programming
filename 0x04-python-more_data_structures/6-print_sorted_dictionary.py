#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = list(a_dictinary.keys())

    new_list.sort()

    for i in new_list:
        print(f"{i}: {a_dictionary[i]}")
