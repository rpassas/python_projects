'''
Robert Passas
CS5001
hw8 - cipher.py
This file implements a set of ciphers that algorithmically encrypt or decrypt
given text based on a key.
'''
import caesar
import railfence
import playfair
import substitution
import beale
import straddle
import utils
import string


def main():
    ciphers = 'caesar (c), railfence (r), playfair (p)\
               substitution (su), beale (b), straddle (st)'
    while True:
        cmd = input('encrypt, decrypt, or exit (en, de, ex)? ')
        # ENCRYPT
        while cmd == 'en':
            enc = input('select cipher: \n \
                        caesar (c), railfence (r), playfair (p) \n \
                        substitution (su), beale (b), straddle (st): \n')
            # caesar
            if enc == 'c':
                t = input('enter plain text: ')
                if t != '' and utils.check_latin(t):
                    pass
                else:
                    print('text can only consist of latin letters')
                    break
                k = input('enter integer key: ')
                if utils.check_int(k):
                    print(caesar.encrypt(t, int(k)))
                    cmd = ''
                else:
                    cmd = ''
            # railfence
            elif enc == 'r':
                t = input('enter plain text: ')
                k = input('enter integer key: ')
                if utils.check_int(k):
                    if int(k) > 1:
                        print(railfence.encrypt(t, int(k)))
                        cmd = ''
                    else:
                        print('key must be at least 2')
                        cmd = ''
                else:
                    cmd = ''
            # playfair
            elif enc == 'p':
                t = input('enter plain text: ')
                if t != '' and utils.check_latin(t):
                    pass
                else:
                    print('text can only consist of latin letters')
                    break
                k = input('enter string key: ')
                if k != '' and utils.check_latin(k):
                    print(playfair.encrypt(t, k))
                    pass
                else:
                    print('key can only consist of latin letters')
                    break
                cmd = ''
            # substitution
            elif enc == 'su':
                t = input('enter plain text: ')
                if t != '' and utils.check_latin(t):
                    pass
                else:
                    print('text can only consist of latin letters')
                    break
                k = input('enter string key: ')
                if k != '' and utils.check_latin(k):
                    try:
                        utils.check_full(k)
                    except ValueError:
                        print('key should bee full alphabet')
                        break
                    try:
                        print(substitution.encrypt(t, k))
                    except ValueError:
                        print('check errors for parameter issues')
                    pass
                else:
                    print('key can only consist of latin letters')
                    break
                cmd = ''
            # beale
            elif enc == 'b':
                t = input('enter plain text: ')
                if t != '' and utils.check_latin(t):
                    pass
                else:
                    print('text can have letters + punctuation')
                    break
                k = input('enter file name key: ')
                if k != '':
                    pass
                s = input('enter an integer seed: ')
                if s != '':
                    try:
                        s = int(s)
                    except ValueError:
                        print('seed must be integer')
                        break
                    try:
                        print(beale.encrypt(t, k, s))
                    except ValueError:
                        print('make sure your file is correct')
                    pass
                else:
                    print('text cannot be empty')
                    break
                cmd = ''
            # straddle
            elif enc == 'st':
                t = input('enter plain text: ')
                warn = 0
                for x in t:
                    if (t not in string.ascii_letters
                       and t != '0' and t != '1' and t != ' '):
                        warn += 1
                if warn > 0:
                    print('warning: text should include only letters, 0, or 1')
                if t != '':
                    pass
                else:
                    print('text cannot be empty')
                    break
                alk = input('enter alpha key: ')
                if alk != '':
                    pass
                else:
                    print('alpha_key cannot be empty')
                    break
                try:
                    utils.check_full(alk)
                except ValueError:
                    print('alpha_key must be full alphabet')
                    break
                nk = input('enter 2 digit numeric key: ')
                if nk != '':
                    pass
                if (len(nk) != 2
                   or not nk[0].isnumeric()
                   or not nk[1].isnumeric()
                   or '0' in nk):
                    print('num_key must be a 2 digit int with unique digits')
                    print('cannot contain 0')
                    break
                adk = input('enter adding key:')
                if adk != '':
                    try:
                        print(straddle.encrypt(t, alk, nk, adk))
                    except ValueError:
                        print('make sure your add key is an integer')
                    pass
                else:
                    print('input cannot be empty')
                    break
                cmd = ''
            else:
                print('Please enter a valid input for a cipher.')
        # DECRYPT
        while cmd == 'de':
            dec = input('select cipher: \n \
                        caesar (c), railfence (r), playfair (p) \n \
                        substitution (su), beale (b), straddle (st): \n')
            # caesar
            if dec == 'c':
                t = input('enter cipher text: ')
                if t != '' and utils.check_latin(t):
                    pass
                else:
                    print('text can only consist of latin letters')
                    break
                k = input('enter integer key: ')
                if utils.check_int(k):
                    print(caesar.decrypt(t, int(k)))
                    cmd = ''
                else:
                    cmd = ''
            # railfence
            elif dec == 'r':
                t = input('enter cipher text: ')
                k = input('enter integer key: ')
                if utils.check_int(k):
                    if int(k) > 1:
                        print(railfence.decrypt(t, int(k)))
                        cmd = ''
                    else:
                        print('key must be at least 2')
                        cmd = ''
                else:
                    cmd = ''
            # playfair
            elif dec == 'p':
                t = input('enter cipher text: ')
                if t != '' and utils.check_latin(t):
                    pass
                else:
                    print('text can only consist of latin letters')
                    break
                k = input('enter string key: ')
                if k != '' and utils.check_latin(k):
                    print(playfair.decrypt(t, k))
                    pass
                else:
                    print('text can only consist of latin letters')
                    break
                cmd = ''
            # substitution
            elif dec == 'su':
                t = input('enter cipher text: ')
                if t != '' and utils.check_latin(t):
                    pass
                else:
                    print('text can only consist of latin letters')
                    break
                k = input('enter string key: ')
                if k != '' and utils.check_latin(k):
                    try:
                        utils.check_full(k)
                    except ValueError:
                        print('key should be full alphabet')
                        break
                    try:
                        print(substitution.decrypt(t, k))
                    except ValueError:
                        print('check errors for parameter issues')
                    pass
                else:
                    print('key can only consist of latin letters')
                    break
                cmd = ''
            # beale
            elif dec == 'b':
                t = input('enter cipher text: ')
                for x in t:
                    if x != ' ':
                        if not x.isnumeric():
                            print('text should consist of int literals')
                            break
                if t != '':
                    pass
                else:
                    print('warning: text should only consist of integers')
                    break
                k = input('enter file name key: ')
                if k != '':
                    try:
                        print(beale.decrypt(t, k))
                    except ValueError:
                        print('check that your text file is correct')
                    pass
                else:
                    print('text cannot be empty')
                    break
                cmd = ''
            # straddle
            elif dec == 'st':
                t = input('enter cipher text: ')
                warn = 0
                for x in t:
                    if (t not in string.ascii_letters
                       and t != '0' and t != '1' and t != ' '):
                        warn += 1
                if warn > 0:
                    print('warning: text should include only letters, 0, or 1')
                if t != '':
                    pass
                else:
                    print('text cannot be empty')
                    break
                alk = input('enter alpha key: ')
                if alk != '':
                    pass
                else:
                    print('alpha_key cannot be empty')
                    break
                try:
                    utils.check_full(alk)
                except ValueError:
                    print('alpha_key must be full alphabet')
                    break
                nk = input('enter 2 digit numeric key: ')
                if nk != '':
                    pass
                if (len(nk) != 2
                   or not nk[0].isnumeric()
                   or not nk[1].isnumeric()
                   or '0' in nk):
                    print('num_key must be a 2 digit int with unique digits')
                    print('cannot contain 0')
                    break
                adk = input('enter adding key:')
                if adk != '':
                    try:
                        print(straddle.decrypt(t, alk, nk, adk))
                    except ValueError:
                        print('make sure your add key is an integer')
                    pass
                else:
                    print('text cannot be empty')
                    break
                cmd = ''
            else:
                print('Please enter a valid input for a cipher.')
        if cmd == 'ex':
            print('exit')
            return False
        elif cmd == '' or cmd == 'en' or cmd == 'de':
            pass
        else:
            print('Please enter a valid input of en, de, or ex.')


if __name__ == '__main__':
    main()
