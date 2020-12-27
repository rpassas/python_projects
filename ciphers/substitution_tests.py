'''
Robert Passas
CS5001
lab 13 -- straddle_tests.py
Tests cases for substitution.py, a substitution cipher algorithm.
'''

from substitution import encrypt, decrypt
import unittest


class SubstitutionTest(unittest.TestCase):
    def test_evaluate(self):
        '''
        Testing both instances generating errors and valid outputs
        '''
        # working instances
        en1 = encrypt('Oh hi, Mark!', 'tkpvrloiuwzsbecjamgqhfnxdy')
        en2 = encrypt('DENNY', 'tbocfnpqyhevisxzljgdrmkwau')
        en3 = encrypt('good thinking!', 'ynqbkcuirjadptgzvlmwfshoxe')
        de1 = decrypt('JQBJSJAAIBT', 'bietrwdqgclzvmahuksjfynpxo')
        de2 = decrypt('QNEI', 'coxriqfvnlmyuehdpswtjzabgk')
        de3 = decrypt('qzssc', 'fjqgshwztyxkndbcirvmlpeuoa')
        # tests
        self.assertEqual(en1, 'CIIUBTMZ')
        self.assertEqual(en2, 'CFSSA')
        self.assertEqual(en3, 'UGGBWIRTARTU')
        self.assertEqual(de1, 'THATSTOOBAD')
        self.assertEqual(de2, 'FINE')
        self.assertEqual(de3, 'CHEEP')
        # test errors
        # encrypt
        msg = 'key must contain only each letter of alphabet once'
        self.assertRaisesRegex(ValueError,
                               'both text and key values must be given',
                               encrypt, '',
                               'comhlberfjauwpztvxskinygdq')
        self.assertRaisesRegex(ValueError,
                               'both text and key values must be given',
                               encrypt, 'asdfasdf',
                               '')
        self.assertRaisesRegex(TypeError,
                               'key must be a string',
                               encrypt, 'Oh hi, Mark!',
                               ['tbocfnpqyhevisxzljgdrmkwau'])
        self.assertRaisesRegex(TypeError,
                               'text must be a string',
                               encrypt, ['Oh hi, Mark!'],
                               'tbocfnpqyhevisxzljgdrmkwau')
        self.assertRaisesRegex(ValueError,
                               'text and key must only contain valid letters',
                               encrypt, 'asdf',
                               'comhlberfjauwp2tvxskinygdq')
        self.assertRaisesRegex(ValueError,
                               msg,
                               encrypt, 'asdf',
                               'ttocfnpqyhevisxzljgdrmkwau')

        # decrypt
        self.assertRaisesRegex(ValueError,
                               'both text and key values must be given',
                               decrypt, '',
                               'comhlberfjauwpztvxskinygdq')
        self.assertRaisesRegex(ValueError,
                               'both text and key values must be given',
                               decrypt, 'asdfasdf',
                               '')
        self.assertRaisesRegex(TypeError,
                               'key must be a string',
                               decrypt, 'Oh hi, Mark!',
                               ['tbocfnpqyhevisxzljgdrmkwau'])
        self.assertRaisesRegex(TypeError,
                               'text must be a string',
                               decrypt, ['Oh hi, Mark!'],
                               'tbocfnpqyhevisxzljgdrmkwau')
        self.assertRaisesRegex(ValueError,
                               'text and key must only contain valid letters',
                               decrypt, 'asdf',
                               'comhlberfjauwp2tvxskinygdq')
        self.assertRaisesRegex(ValueError,
                               msg,
                               decrypt, 'asdf',
                               'ttocfnpqyhevisxzljgdrmkwau')


if __name__ == '__main__':
    unittest.main(verbosity=5)

main()
