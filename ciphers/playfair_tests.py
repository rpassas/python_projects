'''
Robert Passas
CS5001
hw8 - playfair_tests.py
tests the encryption and decryption of the playfair cipher
'''

from playfair import encrypt, decrypt


def encrypt_tester(text, key, expected):
    '''
Function: encrypt_tester
test the output of the playfair encryption against the expected output
Params:   text     -- plain text string
key -- string replacing starting letters in the pf square
expected -- expected output
Returns boolean indicating proper output
'''
    print('Testing playfair encryption')
    actual = encrypt(text, key)
    return actual == expected


def encrypt_tests():
    '''
function: encrypt_tests
catalogs the fails of encrypt_tester across cases
parameters: none
returns number of fails
'''
    fails = 0

    # test 1
    if (encrypt_tester("JJJJ JJJ",
                       'I', 'BVBVBVBV')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if (encrypt_tester("ABCDXYND / ... !",
                       'bcda', 'ECDAYZSH')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 3
    if (encrypt_tester("JJJJ JJJ",
                       'J', 'BVBVBVBV')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 4
    try:
        encrypt_tester("also a bad key",
                       'δ', 'soo bad')
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'text and key must only contain valid letters':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 5
    try:
        encrypt_tester("bad key",
                       2, 'soo bad')
        print("failed because it did not raise the error")
        fails += 1
    except TypeError as ex:
        if str(ex) == 'key must be a string':
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
                        'asdf 55', 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'text and key must only contain valid letters':
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
                        'sadf', 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'text and key must only contain valid letters':
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
                        'a', 'whatever'))
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
                        'f', 'whatever'))
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
test the output of the playfair decryption against the expected output
Params:   text     -- cipher text string
key -- string replacing starting letters in the of square
expected -- expected output
Returns boolean indicating proper output
'''
    print('Testing playfair encryption')
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
    if (decrypt_tester('BVBVBVBV',
                       'I', 'IXIXIXIX')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if (decrypt_tester("fjk -.,dz",
                       'azq', 'DLIEBV')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 3
    if (decrypt_tester("JJJJ JJJ",
                       'J', 'BVBVBVBV')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 4
    try:
        decrypt_tester("also a bad key",
                       'δ', 'soo bad')
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'text and key must only contain valid letters':
            print("PASSED")
        else:
            print("failed with wrong error message")
            fails += 1
    except Exception:
        print("failed with wrong error raised")
        fails += 1

    # test 5
    try:
        decrypt_tester("bad key",
                       2, 'soo bad')
        print("failed because it did not raise the error")
        fails += 1
    except TypeError as ex:
        if str(ex) == 'key must be a string':
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
                        'asdf 55', 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'text and key must only contain valid letters':
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
                        'sadf', 'whatever'))
        print("failed because it did not raise the error")
        fails += 1
    except ValueError as ex:
        if str(ex) == 'text and key must only contain valid letters':
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
                        'a', 'whatever'))
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
                        'f', 'whatever'))
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

    # test 11
    if (decrypt_tester("ayej",
                       'iy nwpdyvs', 'VWCY')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1
    return fails


def main():
    print('Run playfair encrypt tests')
    failed_encrypt = encrypt_tests()
    print('\n')

    print('Run playfair decrypt tests')
    failed_decrypt = decrypt_tests()
    print('\n')

    if (failed_encrypt == 0 and failed_decrypt == 0):
        print('all passed')
    else:
        print('not all passed')


if __name__ == "__main__":
    main()
