'''
Robert Passas
CS5001
hw9 - straddle.py
encrypt and decrypt functions implement the straddle cipher or reverse it
respectively as the function names indicate.
'''
import utils
import string


def encrypt(text, alpha_key, num_key, add_key):
    '''
    Function -- encrypt
    encrypts plain text by filling a 3x10 key using the first two keys. Letters
    in the plain text are then assigned numbers via the key square. The digits
    of this set of numbers is added sequentially to the add_key to yield the
    final cipher number.
    paramters:
    text -- plain text string
    alpha_key -- full alphabet in any order (str)
    num_key -- 2 digit integer (string or int)
    add_key -- int of any length
    returns encrypted cipher text version of the plain text (int)
    '''
    # check validity of the inputs
    if add_key == '' or num_key == '' or alpha_key == '' or text == '':
        raise ValueError('both text and key values must be given')

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    if not isinstance(alpha_key, str):
        raise TypeError('all keys must be strings')
    '''
    if not isinstance(num_key, str):
        raise TypeError('all keys must be strings')

    if not isinstance(add_key, str):
        raise TypeError('all keys must be strings')
    '''
    num_key = str(num_key)
    if (len(num_key) != 2
       or not num_key[0].isnumeric() or not num_key[1].isnumeric()
       or num_key[0] == num_key[1]):
        raise ValueError('num_key must be have 2 unique integer digits')

    if int(num_key[0]) == 0 or int(num_key[1]) == 0:
        raise ValueError('digits of num_key must be greater than 0')

    if not utils.check_full(alpha_key):
        msg = ('alpha_key must contain only each letter of alphabet once')
        raise ValueError(msg)
    alpha_key = alpha_key.upper()

    try:
        int(num_key)
        num_key = str(num_key)
        add_key = int(add_key)
        if int(num_key) < 0 or int(add_key) < 0:
            print('Warning: negative keys will be assumed to be positive')
    except ValueError:
        raise ValueError('num_key and add_key must be ints')

    try:
        text = utils.strip(text)
        text = utils.process_text(text)
        text = utils.latin_caps(text)
    except ValueError:
        raise ValueError('text must only contain valid letters')

    # construct cipher square
    key_square = {}
    # first row
    key_square[0] = [alpha_key[i] for i in range(8)]
    if int(num_key[0]) > int(num_key[1]):
        key_square[0].insert(int(num_key[1]), '')
        key_square[0].insert(int(num_key[0]), '')
    else:
        key_square[0].insert(int(num_key[0]), '')
        key_square[0].insert(int(num_key[1]), '')
    # next rows
    key_square[int(num_key[0])] = [alpha_key[i] for i in range(8, 18)]
    key_square[int(num_key[1])] = [alpha_key[i] for i in range(18, 26)]
    key_square[int(num_key[1])].append('0')
    key_square[int(num_key[1])].append('1')
    # generate numeric text
    num_text = ''
    for letter in text:
        if letter in key_square[0]:
            num_text = num_text + str(key_square[0].index(letter))
        elif letter in key_square[int(num_key[0])]:
            combo = num_key[0] + str(key_square[int(num_key[0])].index(letter))
            num_text = num_text + combo
        elif letter in key_square[int(num_key[1])]:
            combo = num_key[1] + str(key_square[int(num_key[1])].index(letter))
            num_text = num_text + combo
        else:
            raise ValueError('letters in plain text must be latin')
    # add the adder text
    adder = ''
    for i in range(len(num_text)):
        added = int(num_text[i]) + int(str(add_key)[i % len(str(add_key))])
        adder = adder + str(added)[-1]
    # make cipher text via the grid
    cipher = ''
    count = 0
    while count < len(adder):
        num = int(adder[count])
        if key_square[0][num] == '':
            if (count + 1) >= len(adder):
                count += 2
            else:
                next_num = int(adder[count + 1])
                cross = key_square[num][next_num]
                cipher = cipher + cross
                count += 2
        else:
            cipher += key_square[0][num]
            count += 1
    return cipher


def decrypt(text, alpha_key, num_key, add_key):
    '''
    Function -- decrypt
    decrypts cipher text by reversing the cipher algorithm starting with
    adder text that is converted to numeric text and finally plain text
    using a key grid.
    paramters:
    text -- cipher text string of int literals
    alpha_key -- full alphabet in any order (str)
    num_key -- 2 digit integer (string or int)
    add_key -- int of any length
    returns decrypted plain text version of the cipher text
    '''
    # check validity of the inputs
    if add_key == '' or num_key == '' or alpha_key == '' or text == '':
        raise ValueError('both text and key values must be given')

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    if not isinstance(alpha_key, str):
        raise TypeError('all keys must be strings')
    '''
    if not isinstance(num_key, str):
        raise TypeError('all keys must be strings')

    if not isinstance(add_key, str):
        raise TypeError('all keys must be strings')
    '''
    num_key = str(num_key)
    if (len(str(num_key)) != 2
       or not num_key[0].isnumeric() or not num_key[1].isnumeric()):
        raise ValueError('num_key must be have 2 unique integer digits')

    if int(str(num_key)[0]) == 0 or int(str(num_key)[1]) == 0:
        raise ValueError('digits of num_key must be greater than 0')

    if not utils.check_full(alpha_key):
        msg = ('alpha_key must contain only each letter of alphabet once')
        raise ValueError(msg)
    alpha_key = alpha_key.upper()

    try:
        int(num_key)
        num_key = str(num_key)
        add_key = int(add_key)
        if int(num_key) < 0 or int(add_key) < 0:
            print('Warning: negative keys will be assumed to be positive')
    except ValueError:
        raise ValueError('num_key and add_key must be ints')

    try:
        text = utils.strip(text)
        text = text.upper()
        for x in text:
            if (ord(x) >= 65 and ord(x) <= 90) or x == '1' or x == '0':
                pass
            else:
                raise ValueError('text must only contain valid letters')
    except ValueError:
        raise ValueError('text must only contain valid letters')

    # construct cipher square
    key_square = {}
    # first row
    key_square[0] = [alpha_key[i] for i in range(8)]
    if int(num_key[0]) > int(num_key[1]):
        key_square[0].insert(int(num_key[1]), '')
        key_square[0].insert(int(num_key[0]), '')
    else:
        key_square[0].insert(int(num_key[0]), '')
        key_square[0].insert(int(num_key[1]), '')
    # next rows
    key_square[int(num_key[0])] = [alpha_key[i] for i in range(8, 18)]
    key_square[int(num_key[1])] = [alpha_key[i] for i in range(18, 26)]
    key_square[int(num_key[1])].append('0')
    key_square[int(num_key[1])].append('1')
    # generate adder text
    adder = ''
    for letter in text:
        if letter in key_square[0]:
            adder = adder + str(key_square[0].index(letter))
        elif letter in key_square[int(num_key[0])]:
            combo = num_key[0] + str(key_square[int(num_key[0])].index(letter))
            adder = adder + combo
        elif letter in key_square[int(num_key[1])]:
            combo = num_key[1] + str(key_square[int(num_key[1])].index(letter))
            adder = adder + combo
        else:
            raise ValueError('letters in plain text must be latin')
    # generate numeric text
    num_text = ''
    for i in range(len(adder)):
        subbed = int(adder[i]) - int(str(add_key)[i % len(str(add_key))])
        if subbed < 0:
            new_sub = list(range(10))[subbed]
            num_text = num_text + str(new_sub)
        else:
            num_text = num_text + str(subbed)[-1]
    # generate original plain text
    plain = ''
    count = 0
    while count < len(num_text):
        num = int(num_text[count])
        if key_square[0][num] == '':
            if (count + 1) >= len(num_text):
                count += 2
            else:
                next_num = int(num_text[count + 1])
                cross = key_square[num][next_num]
                plain = plain + cross
                count += 2
        else:
            plain += key_square[0][num]
            count += 1
    return plain
