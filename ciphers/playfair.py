'''
Robert Passas
CS5001
hw8 - playfair.py
encrypt and decrypt functions implement the playfair cipher or reverse it
respectively as the function names indicate.
'''
import utils
import string


def encrypt(text, key):
    '''
    Function -- encrypt
    encrypts plain text by shifting letter indices to the right in the
    alphabet per the key (reversed if negative)
    paramters:
    text -- plain text string
    key -- integer indicating magnitude and direction of index shift
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
        text = utils.strip(text)
        text = utils.process_text(text)
        text = utils.latin_caps(text)
        key = utils.strip(key)
        key = utils.process_text(key)
        key = utils.latin_caps(key)
    except ValueError:
        raise ValueError('text and key must only contain valid letters')

    # remove repeats in the key and other letters
    keys = []
    for letter in key:
        if letter not in keys:
            keys.append(letter)
    keys = [letter if letter != 'J' else 'I' for letter in keys]
    leftover_letters = list(map(chr, range(65, 91)))
    leftover_letters.remove('J')
    for letter in keys:
        if letter in leftover_letters:
            leftover_letters.remove(letter)
    # generate the cipher square
    matrix = [[j for j in range(5)] for i in range(5)]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if len(keys) > 0:
                matrix[row][col] = keys.pop(0)
            else:
                matrix[row][col] = leftover_letters.pop(0)

    # process the plain text (add Xs for duplicates and odd len words)
    first = []
    letters = [char for char in text]
    for i in range(len(letters)):
        if letters[i] == 'J':
            letters[i] = 'I'
        if len(first) == 0:
            first.append(letters[i])
        elif letters[i] != first[-1]:
            first.append(letters[i])
        elif len(first) % 2 == 1:
            first.append('X')
        else:
            first.append(letters[i])
    if len(first) % 2 != 0:
        first.append('X')
    text = ''.join(letters)
    paired = [first[i] + first[i + 1] for i in range(0, len(first), 2)]
    # get letter positions in the matrix
    cipher = ''
    pos_1 = [0, 0]
    pos_2 = [0, 0]
    for pair in paired:
        for row in range(len(matrix)):
            if pair[0] in matrix[row]:
                for col in range(len(matrix[row])):
                    if matrix[row][col] == pair[0]:
                        pos_1[0] = row
                        pos_1[1] = col
            if pair[1] in matrix[row]:
                for col in range(len(matrix[row])):
                    if matrix[row][col] == pair[1]:
                        pos_2[0] = row
                        pos_2[1] = col
        # encrypt
        if pos_1[0] == pos_2[0]:
            cipher += matrix[pos_1[0]][(pos_1[1] + 1) % 5]
            cipher += matrix[pos_2[0]][(pos_2[1] + 1) % 5]
        elif pos_1[1] == pos_2[1]:
            cipher += matrix[(pos_1[0] + 1) % 5][pos_1[1]]
            cipher += matrix[(pos_2[0] + 1) % 5][pos_2[1]]
        else:
            cipher += matrix[pos_1[0]][pos_2[1]]
            cipher += matrix[pos_2[0]][pos_1[1]]
    return cipher


def decrypt(text, key):
    '''
    Function -- decrypt
    decrypts cipher text by generating a playfair square
    and reversing the cipher
    paramters:
    text -- cipher text string
    key -- string to help make the 5 x 5 encryption matrix
    returns decrypted plain text version of the cipher text
    '''
    # check validity of the inputs
    if key == '' or text == '':
        raise ValueError('both text and key values must be given')

    if not isinstance(key, str):
        raise TypeError('key must be a string')

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    try:
        text = utils.strip(text)
        text = utils.process_text(text)
        text = utils.latin_caps(text)
        key = utils.strip(key)
        key = utils.process_text(key)
        key = utils.latin_caps(key)
    except ValueError:
        raise ValueError('text and key must only contain valid letters')

    if len(text) % 2 != 0:
        text = text + 'X'

    # remove repeats in the key and other letters
    keys = []
    for letter in key:
        if letter not in keys:
            keys.append(letter)
    keys = [letter if letter != 'J' else 'I' for letter in keys]
    leftover_letters = list(map(chr, range(65, 91)))
    leftover_letters.remove('J')
    for letter in keys:
        if letter in leftover_letters:
            leftover_letters.remove(letter)
    # generate the cipher square
    matrix = [[j for j in range(5)] for i in range(5)]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if len(keys) > 0:
                matrix[row][col] = keys.pop(0)
            else:
                matrix[row][col] = leftover_letters.pop(0)
    # process the cipher text (add Xs for duplicates and odd len words)
    letters = [char if char != 'J' else 'I' for char in text]
    if len(letters) % 2 != 0:
        letters.append('X')
    paired = [letters[i] + letters[i + 1] for i in range(0, len(letters), 2)]
    pairs = []
    for i in range(len(paired)):
        if paired[i][0] == paired[i][1]:
            paired[i] = paired[i][0] + 'X'
    # get letter positions in the matrix
    plain = ''
    pos_1 = [0, 0]
    pos_2 = [0, 0]
    for pair in paired:
        for row in range(len(matrix)):
            if pair[0] in matrix[row]:
                for col in range(len(matrix[row])):
                    if matrix[row][col] == pair[0]:
                        pos_1[0] = row
                        pos_1[1] = col
            if pair[1] in matrix[row]:
                for col in range(len(matrix[row])):
                    if matrix[row][col] == pair[1]:
                        pos_2[0] = row
                        pos_2[1] = col
        # decrypt
        if pos_1[0] == pos_2[0]:
            plain += matrix[pos_1[0]][(pos_1[1] - 1)]
            plain += matrix[pos_2[0]][(pos_2[1] - 1)]
        elif pos_1[1] == pos_2[1]:
            plain += matrix[(pos_1[0] - 1)][pos_1[1]]
            plain += matrix[(pos_2[0] - 1)][pos_2[1]]
        else:
            plain += matrix[pos_1[0]][pos_2[1]]
            plain += matrix[pos_2[0]][pos_1[1]]

    return plain
