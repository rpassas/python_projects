'''
Robert Passas
CS5001
hw8 - railfence_tests.py
tests the encryption and decryption of the caesar cipher
'''


from railfence import encrypt, decrypt


def encrypt_tester(text, key, expected):
    '''
Function: encrypt_tester
test the output of the railfence encryption against the expected output
Params:   text     -- plain text string
key -- integer giving cipher rail number
expected -- expected output
Returns boolean indicating proper output
'''
    print('Testing railfence encryption')
    actual = encrypt(text, key)
    return actual == expected


def encrypt_tests():
    '''
function: encrypt_tests
catalogs the fails of encryt_tester across cases
parameters: none
returns number of fails
'''
    fails = 0

    # test 1
    if (encrypt_tester("if i was a rich man",
                       4, 'IAAFSRMNIAIHWC')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    try:
        (encrypt_tester('how about a NEGATIVE key',
                        - 2, 'FMUYZMSRYLCEYRGTCICW'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'key must be at least 2':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 3
    if (encrypt_tester("if i ... was a rich man!!",
                       6, 'IHFCMIIAWRNAAS')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 4
    if (encrypt_tester('the key exceeds the text',
                       47, 'THEKEYEXCEEDSTHETEXT')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 5
    try:
        (encrypt_tester('too few rails',
                        1, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'key must be at least 2':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 6
    try:
        (encrypt_tester('bad key',
                        1.1, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except TypeError as ex:
        if str(ex) == 'key must be an integer':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 7
    try:
        (encrypt_tester('bad string 7',
                        3, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'text must only contain valid letters':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 8
    try:
        (encrypt_tester(['not a string'],
                        3, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except TypeError as ex:
        if str(ex) == 'text must be a string':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 9
    try:
        (encrypt_tester('',
                        3, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'both text and key values must be given':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 10
    try:
        (encrypt_tester('asdf',
                        '', 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'both text and key values must be given':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1
    return fails


def decrypt_tester(text, key, expected):
    '''
Function: decrypt_tester
test the output of the caesar decryption against the expected output
Params:   text     -- cipher text string
key -- integer giving cipher magnitude and direction
expected -- expected output
Returns boolean indicating proper output
'''
    print('Testing railfence decryption')
    actual = decrypt(text, key)
    return actual == expected


def decrypt_tests():
    '''
function: decrypt_tests
catalogs the fails of decryt_tester across cases
parameters: none
returns number of fails
'''
    fails = 0

    # test 1
    if (decrypt_tester("BIGKEY.....?",
                       89, 'BIGKEY')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    try:
        (decrypt_tester('how about a NEGATIVE key',
                        - 5, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'key must be at least 2':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 3
    if (decrypt_tester("IHFCMIIAWRNAAS",
                       6, 'IFIWASARICHMAN')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 4
    if (decrypt_tester('the key exceeds the text',
                       47, 'THEKEYEXCEEDSTHETEXT')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 5
    try:
        (decrypt_tester('too few rails',
                        1, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'key must be at least 2':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 6
    try:
        (decrypt_tester('bad key',
                        4.1, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except TypeError as ex:
        if str(ex) == 'key must be an integer':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 7
    try:
        (decrypt_tester('bad string 7',
                        3, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'text must only contain valid letters':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 8
    try:
        (decrypt_tester(['not a string'],
                        3, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except TypeError as ex:
        if str(ex) == 'text must be a string':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 9
    try:
        (decrypt_tester('',
                        3, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'both text and key values must be given':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 10
    try:
        (decrypt_tester('asdf',
                        '', 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'both text and key values must be given':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1
    return fails


def main():
    print('Run railfence encrypt tests')
    failed_encrypt = encrypt_tests()
    print('\n')

    print('Run railfence decrypt tests')
    failed_decrypt = decrypt_tests()
    print('\n')

    if (failed_encrypt == 0 and failed_decrypt == 0):
        print('all passed')
    else:
        print('not all passed')


if __name__ == "__main__":
    main()
