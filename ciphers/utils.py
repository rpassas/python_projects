'''
Robert Passas
CS5001
hw8 - utils.py
This file contains helper functions for ciphers.
'''
import string


def strip(word):
    '''
    Function -- strip
    strips string of spaces and punctuation
    Parameters:
    word -- a string
    returns a stripped string
    '''
    # strip the punctuation out
    for c in string.punctuation:
        word = word.replace(c, "")
    # strip the space out
    word = word.strip()
    word = word.replace(" ", "")
    return word


def process_text(word):
    '''
    Function -- process_text
    makes sure that the string is only latin letters and capitalizes them
    parameters:
    word -- a string
    returns an all caps string if it is only valid letters (not just latin)
    '''
    if not word.isalpha():
        raise ValueError('text must only contain valid letters')
    word = word.upper()
    return word


def latin_caps(word):
    '''
    Function -- latin_caps
    makes sure that the string is only capital latin letters
    parameters:
    word -- a string
    returns an all caps string if it is only latin letters
    '''
    for x in word:
        if ord(x) >= 65 and ord(x) <= 90:
            pass
        else:
            raise ValueError('text must only contain valid letters')
    return word


def check_int(num):
    '''
    Function -- check_int
    makes sure that the string input is a int
    parameters:
    num -- a string (hopefully representing an int)
    returns boolean indicating if an int
    '''
    try:
        int(num)
        return True
    except ValueError:
        print('input must be an integer')
        return False


def check_latin(word):
    '''
    Function -- check_latin
    makes sure that the string input contains only latin letters
    parameters:
    word -- a string (hopefully representing letters)
    returns boolean indicating if word contains only latin letters
    '''
    # strip the punctuation and space
    for c in string.punctuation:
        word = word.replace(c, "")
    word = word.replace(" ", "")
    # check letters
    count = 0
    for x in word:
        if ord(x) >= 65 and ord(x) <= 90:
            count += 1
        else:
            count += 0
    for x in word:
        if ord(x) >= 97 and ord(x) <= 122:
            count += 1
        else:
            count += 0
    if count == len(word):
        return True
    else:
        return False


def check_full(word):
    '''
    Function -- check_full
    makes sure that the string input
    contains only all 26 uppercase letters of the alphabet
    parameters:
    word -- a string (hopefully containing capital letters)
    returns boolean indicating if word
    contains each letter in the alphabet once
    '''
    msg = ('alpha_key must contain only each letter of alphabet once')
    if len(word) != 26:
        raise ValueError(msg)
    word = word.upper()
    # alphabet
    alphabet_str = string.ascii_uppercase
    alphabet = list(alphabet_str)
    # check letters
    for i in range(len(word)):
        if word[i] in alphabet:
            alphabet.remove(word[i])
        else:
            raise ValueError(msg)
    if len(alphabet) == 0:
        return True
    else:
        return False
