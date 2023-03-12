#!/usr/bin/python3

''' A Module that creates a Square object '''


class Square:
    ''' Creating an Object template '''

    def __init__(self, size=0):
        '''
        The init method initializes the class instance

        @self:
            A parameter used to refer to the class instance

        @size:
            The size of the square, must be a +ve integer
        '''
        self.size = size

    @property
    '''Getter for size'''

    def size(self):
        '''Retrieving the value of size'''
        return self.__size

    @size.setter
    '''Setter for size'''

    def size(self, value):
        '''Value of square size'''
        try:
            if type(value) is int:
                if value < 0:
                    raise ValueError('Size must be >= 0')
                else:
                    self.__size = value
            else:
                raise TypeError
        except TypeError:
            print('Size must be an integer')
