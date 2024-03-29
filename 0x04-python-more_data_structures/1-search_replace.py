#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
     A function that traverse through a list for an element that matches
     search and modify it with replace then returns a new list.

     @elem: Elements
    '''
    if len(my_list) == 0:
        return my_list

    new_lst = [i if i != search else replace for i in my_list]
    return new_lst
