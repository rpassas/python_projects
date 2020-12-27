'''
Robert Passas
CS5001
hw9 - substitution.py
encrypt and decrypt functions implement the substitution cipher or reverse it
respectively as the function names indicate.
'''
import utils
import string


def encrypt(text, key):
    '''
    Function -- encrypt
    encrypts plain text by replacing letters according to their positions
    in the key
    paramters:
    text -- plain text string
    key -- plain text string of len 26
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

    if not utils.check_full(key):
        raise ValueError('key must contain only each letter of alphabet once')

    # alphabet and cipher
    alphabet_str = string.ascii_uppercase
    alphabet = list(alphabet_str)
    cipher = ''
    # iterate through text and replace letter by key index
    for letter in text:
        if letter in alphabet:
            cipher = cipher + key[alphabet.index(letter)]
        else:
            raise ValueError('text and key must only contain valid letters')
    return cipher


def decrypt(text, key):
    '''
    Function -- decrypt
    decrypts cipher text by replacing letters in the text with
    letters in the alphabet based on key index
    paramters:
    text -- cipher text string
    key -- plain text string of len 26
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

    if not utils.check_full(key):
        raise ValueError('key must contain only each letter of alphabet once')

    # alphabet and cipher
    alphabet_str = string.ascii_uppercase
    alphabet = list(alphabet_str)
    plain = ''
    # iterate through text and replace letter by key index
    for letter in text:
        if letter in alphabet:
            plain = plain + alphabet[key.index(letter)]
        else:
            raise ValueError('text and key must only contain valid letters')
    return plain
