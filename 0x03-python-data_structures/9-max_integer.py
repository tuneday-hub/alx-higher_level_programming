#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max_num = my_list[0]
        for list in my_list:
            if list > max_num:
                max_num = list
        return max_num
