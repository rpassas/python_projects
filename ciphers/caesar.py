'''
Robert Passas
CS5001
hw8 - caesar.py
encrypt and decrypt functions implement the caesar cipher or reverse it
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

    if not isinstance(key, int):
        raise TypeError('key must be an integer')

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    try:
        text = utils.strip(text)
        text = utils.process_text(text)
    except ValueError:
        raise ValueError('text must only contain valid letters')

    key = int(key) % 26

    # encrypt the string
    cipher = ''
    a_index = list(range(0, 26))
    for x in text:
        if ord(x) >= 65 and ord(x) <= 90:
            cipher += chr(a_index[((ord(x) - 65) + key) % 26] + 65)
        else:
            raise ValueError('text must only contain valid letters')
    return cipher


def decrypt(text, key):
    '''
    Function -- decrypt
    decrypts cipher text by shifting letter indices to the left in the
    alphabet per the key (reversed if negative)
    paramters:
    text -- cipher text string
    key -- integer indicating magnitude and direction of index shift
    returns decrypted plain text version of the cipher text
    '''
    # check validity of inputs
    if key == '' or text == '':
        raise ValueError('both text and key values must be given')

    if not isinstance(key, int):
        raise TypeError('key must be an integer')

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    try:
        text = utils.strip(text)
        text = utils.process_text(text)
    except ValueError:
        raise ValueError('text must only contain latin letters')

    key = key % 26

    # decrypt the string
    plain = ''
    a_index = list(range(0, 26))
    for x in text:
        if ord(x) >= 65 and ord(x) <= 90:
            plain += chr(a_index[((ord(x) - 65) - key) % 26] + 65)
        else:
            raise ValueError('text must only contain latin letters')
    return plain
