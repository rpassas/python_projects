'''
CS 5001 - Online Summer 2020
Module 13 Lab -- Stacks & Queues

This is the implementation of a simple stack that can be used in Lab 13.
'''


class Stack:
    '''
    Class: Stack
        represents a Stack data structure
        code slightly altered from Align Online Module 13
    '''

    def __init__(self):
        '''
        Constructor -- initializes the stack
        Parameters:
           self -- the current object
        '''
        self.data = list()

    def push(self, item):
        ''' 
        push -- adds something to the top of the stack
        Parameters:
           self -- the current object
           item -- the item to add to the stack
        Returns nothing
        '''
        self.data.append(item)

    def pop(self):
        ''' 
        pop -- removes something from the top of the stack
        Parameters:
           self -- the current object
        Returns the top element after removing it from the stack
        '''
        if self.size() == 0:
            raise ValueError("Stack is empty")
        return self.data.pop()

    def size(self):
        ''' length -- gets the size of this stack
        Parameters:
            self -- the current object
        Returns the size of this stack
        '''
        return len(self.data)

    def __str__(self):
        '''
        Returns a string representation of the stack
        '''
        return str(self.data)
