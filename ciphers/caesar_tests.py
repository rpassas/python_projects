'''
Robert Passas
CS5001
hw8 - caesar_tests.py
tests the encryption and decryption of the caesar cipher
'''


from caesar import encrypt, decrypt


def encrypt_tester(text, key, expected):
    '''
Function: encrypt_tester
test the output of the caesar encryption against the expected output
Params:   text     -- plain text string
key -- integer giving cipher magnitude and direction
expected -- expected output
Returns boolean indicating proper output
'''
    print('Testing caesar encryption')
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
    if (encrypt_tester("let's puT punCtuation. and.     space.  !?",
                       6, 'RKZYVAZVATIZAGZOUTGTJYVGIK')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if (encrypt_tester('how about a NEGATIVE key',
                       - 2, 'FMUYZMSRYLCEYRGTCICW')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 3
    if (encrypt_tester('what if the key does nothing?',
                       0, 'WHATIFTHEKEYDOESNOTHING')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 4
    if (encrypt_tester('really big key',
                       111, 'YLHSSFIPNRLF')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 5
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

    # test 6
    try:
        (encrypt_tester('bad string 55',
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

    # test 7
    try:
        (encrypt_tester('bad string ξ',
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
    print('Testing caesar decryption')
    actual = decrypt(text, key)
    return actual == expected


def decrypt_tests():
    '''
function: decrypt_tests
catalogs the fails of decrypt_tester across cases
parameters: none
returns number of fails
'''
    fails = 0

    # test 1
    if (decrypt_tester("BIGKEY",
                       111, 'UBZDXR')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if (decrypt_tester('NEGATIVE',
                       - 31, 'SJLFYNAJ')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 3
    if (decrypt_tester('what if the key does nothing?',
                       0, 'WHATIFTHEKEYDOESNOTHING')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 4
    if (decrypt_tester('SOME PUNCS .... &!',
                       2, 'QMKCNSLAQ')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 5
    try:
        (decrypt_tester('bad key',
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

    # test 6
    try:
        (decrypt_tester('bad string 55',
                        3, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'text must only contain latin letters':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 7
    try:
        (decrypt_tester('bad string ξ',
                        3, 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'text must only contain latin letters':
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
    print('Run caesar encrypt tests')
    failed_encrypt = encrypt_tests()
    print('\n')

    print('Run caesar decrypt tests')
    failed_decrypt = decrypt_tests()
    print('\n')

    if (failed_encrypt == 0 and failed_decrypt == 0):
        print('all passed')
    else:
        print('not all passed')


if __name__ == "__main__":
    main()
