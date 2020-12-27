'''
Robert Passas
CS5001
hw8 - railfence.py
encrypt and decrypt functions implement the rail fence cipher or reverse it
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
    key -- integer indicating number of rails
    returns encrypted string cipher text version of the plain text
    '''
    # check validity of the inputs
    if key == '' or text == '':
        raise ValueError('both text and key values must be given')

    if not isinstance(key, int):
        raise TypeError('key must be an integer')

    if key < 2:
        raise ValueError('key must be at least 2')

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    try:
        text = utils.strip(text)
        text = utils.process_text(text)
    except ValueError:
        raise ValueError('text must only contain valid letters')

    key = int(key)
    cipher = ''

    # create rail matrix
    matrix = []
    for i in range(key):
        matrix.append([])
    # fill it up
    cycle = len(matrix) - 1
    prev_rail = 0
    current_rail = 0
    for x in text:
        if current_rail - prev_rail == 0:
            matrix[current_rail].append(x)
            current_rail += 1
        elif current_rail - prev_rail > 0:
            matrix[current_rail].append(x)
            if current_rail >= cycle:
                current_rail -= 1
                prev_rail += 1
            else:
                current_rail += 1
                prev_rail += 1
        elif current_rail - prev_rail < 0:
            matrix[current_rail].append(x)
            if current_rail <= 0:
                current_rail += 1
                prev_rail -= 1
            else:
                current_rail -= 1
                prev_rail -= 1

    # get cipher text
    for level in matrix:
        cipher += ''.join(level)
    return cipher


def decrypt(text, key):
    '''
    Function -- decrypt
    decrypts cipher text putting letters into matrices indicating length
    and arrangement of rails to generate plain text
    paramters:
    text -- cipher text string
    key -- integer indicating number of rails
    returns decrypted string plain text version of the cipher text
    '''
    # check validity of the inputs
    if key == '' or text == '':
        raise ValueError('both text and key values must be given')

    if not isinstance(key, int):
        raise TypeError('key must be an integer')

    if key < 2:
        raise ValueError('key must be at least 2')

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    try:
        text = utils.strip(text)
        text = utils.process_text(text)
    except ValueError:
        raise ValueError('text must only contain valid letters')

    key = int(key)
    # decrypt the string
    plain = ''
    # create rail matrix
    matrix = []
    for i in range(key):
        matrix.append([])
    # find rail lens
    total = len(text)
    cycle = (key * 2) - 2
    rail_lens = []
    if total % cycle == 0:
        top = total / cycle
        bot = top
        mid = 2 * top
        # add top
        rail_lens.append([top])
        # add middle rows
        for x in range(key - 2):
            rail_lens.append([mid])
        # add bottom
        rail_lens.append([bot])
    else:
        top = (total // cycle)
        bot = top
        mid = 2 * top
        # add top
        rail_lens.append([top + 1])
        # add middle rows
        for x in range(key - 2):
            rail_lens.append([mid])
        # add bottom and leftovers
        rail_lens.append([bot])
        left_over = int(total % cycle)
        for i in range(1, left_over):
            if i <= key - 1:
                rail_lens[i].append(1)
            else:
                rail_lens[cycle - i].append(1)
    for i in range(len(rail_lens)):
        rail_lens[i] = [sum(rail_lens[i])]
    # generate matrix
    base = 0
    for i in range(len(rail_lens)):
        for j in range(base, rail_lens[i][0] + base):
            matrix[i].append(text[j])
        base = base + rail_lens[i][0]
    # build plain text
    prev_rail = 0
    current_rail = 0
    for letter in range(total):
        if current_rail - prev_rail == 0:
            plain = plain + matrix[current_rail].pop(0)
            current_rail += 1
        elif current_rail - prev_rail > 0:
            plain = plain + matrix[current_rail].pop(0)
            if current_rail >= key - 1:
                current_rail -= 1
                prev_rail += 1
            else:
                current_rail += 1
                prev_rail += 1
        elif current_rail - prev_rail < 0:
            plain = plain + matrix[current_rail].pop(0)
            if current_rail <= 0:
                current_rail += 1
                prev_rail -= 1
            else:
                current_rail -= 1
                prev_rail -= 1
    return plain
