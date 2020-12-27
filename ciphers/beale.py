'''
Robert Passas
CS5001
hw9 - beale.py
encrypt and decrypt functions implement the beale cipher or reverse it
respectively as the function names indicate.
'''
import utils
import string
import random
import os


def encrypt(text, key, seed):
    '''
    Function -- encrypt
    encrypts plain text by providing a number indicating word position in key
    for each letter in the text
    paramters:
    text -- plain text string
    key -- name of text file
    seed - integer seed for choosing random word from key
    returns encrypted cipher text version of the plain text
    '''
    # check validity of the inputs
    if key == '' or text == '':
        raise ValueError('both text and key values must be given')

    if not isinstance(key, str):
        raise TypeError('key must be a string')

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    try:
        seed = int(seed)
    except ValueError:
        raise ValueError('seed must be an integer')

    if isinstance(key, str) and key[-4:] == '.txt':
        pass
    else:
        raise ValueError('key is an invalid filename')

    try:
        text = utils.strip(text)
        text = utils.process_text(text)
        text = utils.latin_caps(text)
    except ValueError:
        raise ValueError('text must only contain valid letters')

    if not os.path.exists(key):
        raise ValueError('key is an invalid filename')

    key_dict = {}
    # read data
    file = open(key, 'r')
    file_data = file.read().upper()
    # process key
    file_data = file_data.split()
    keywords = []
    for word in file_data:
        stripped = word.strip(string.punctuation + ' ')
        if stripped != '':
            keywords.append(stripped)
    # second loop to go over cleaned up words
    for word in keywords:
        if word[0] in string.ascii_uppercase:
            if word[0].upper() in key_dict.keys():
                key_dict[word[0]].append(keywords.index(word) + 1)
            elif word[0] in string.ascii_uppercase:
                key_dict[word[0]] = [keywords.index(word) + 1]
    file.close()
    # seed
    random.seed(int(seed))
    # cipher output
    cipher = ''
    # iterate through text and generate a cipher text
    for letter in text:
        if letter in key_dict.keys():
            picker = random.randint(0, (len(key_dict[letter]) - 1))
            cipher = cipher + str(int(key_dict[letter][picker])) + ' '
        else:
            msg = 'letters in text must match first letter >= 1 word in key'
            raise ValueError(msg)
    cipher = cipher.strip(' ')
    return cipher


def decrypt(text, key):
    '''
    Function -- decrypt
    decrypts cipher text by matching the given number with
    paramters:
    text -- cipher text string, consisting of a series of ints
    key -- name of text file
    returns decrypted plain text version of the cipher text
    '''
    # check validity of the inputs
    if key == '' or text == '':
        raise ValueError('both text and key values must be given')

    if not isinstance(key, str):
        raise TypeError('key must be a string')

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    if isinstance(key, str) and key[-4:] == '.txt':
        pass
    else:
        raise ValueError('key is an invalid filename')

    if not os.path.exists(key):
        raise ValueError('key is an invalid filename')

    # read data
    file = open(key, 'r')
    file_data = file.read().upper()
    # process key
    file_data = file_data.split()
    keywords = []
    for word in file_data:
        stripped = word.strip(string.punctuation + ' ')
        if stripped != '':
            keywords.append(stripped)
    file.close()

    # plain text output
    plain = ''
    # go through the cipher and generate plain text
    cipher = text.strip().split()
    for letter in cipher:
        try:
            plain = plain + keywords[int(letter) - 1][0]
        except ValueError:
            msg = 'cipher text must consist of integer literals'
            raise ValueError(msg)
    return plain
