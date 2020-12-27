'''
CS 5001 Online -- Summer 2020
Module 13 Lab -- Using Stacks
Author: Nolan Bock, Maria Jump, and Robert Passas

This lab implements an reverse polish-notation calculator.
'''
from calc_stack import Stack


valid_operators = "+-*/%"


def apply(operator, one, two):
    '''
    Method -- returns the result of the operator being used
    on the given operands
    Parameters:
        operator -- the operator for this equation
        one -- the first operand
        two -- the second operand
    Returns the result of this operation
    '''
    result = None
    if operator == "+":
        result = one + two
    elif operator == "-":
        result = one - two
    elif operator == "*":
        result = one * two
    elif operator == "/":
        result = one // two
    elif operator == "%":
        result = one % two
    return result


def evaluate(equation):
    '''
    evaluate -- evaluates the rpn equation using a stack
    Parameters:
        equation -- a string that contains an equation written in rpn
    Returns the result of the equation
    Raises a TypeError if the value of the equation that is passed in is not
        as string
    Raises a ValueError if one of the following is true:
        1. contains an invalid operator
        2. provides the wrong number of inputs for an operand
        3. does not result in a single value
        4. attempts to divide by zero
    '''
    # check input
    if not isinstance(equation, str):
        raise TypeError('Invalid equation: not a string')
    # make list
    eqn_list = equation.split()
    # empty stack
    rpn_stack = Stack()
    # fill the stack
    for char in eqn_list:
        # inputs must be ints and valid operators
        if char.isnumeric():
            rpn_stack.push(int(char))
        elif char[0] == '-' and char[1:].isnumeric():
            rpn_stack.push(int(char))
        elif char in valid_operators:
            if rpn_stack.size() < 2:
                raise ValueError('Invalid number of operands')
            else:
                two = rpn_stack.pop()
                one = rpn_stack.pop()
                if (char == '/' or char == '%') and two == 0:
                    raise ValueError('Cannot divide by zero')
                else:
                    result = apply(char, one, two)
                    rpn_stack.push(result)
        elif '.' in char:
            raise ValueError('Invalid literal - cannot be float')
        else:
            print(char)
            raise ValueError('Invalid operator')
    # give answer
    if rpn_stack.size() == 1:
        return rpn_stack.pop()
    else:
        raise ValueError('Invalid number of operands')


def main():
    done = False
    while not done:
        choice = input("Enter equation or 'quit': ")
        if choice.lower() == 'quit':
            print("Thanks for calculating with us!")
            done = True
        else:
            try:
                answer = evaluate(choice)
                print("Answer is", answer)
            except ValueError as err:
                print(err)
        print()


if __name__ == '__main__':
    main()
