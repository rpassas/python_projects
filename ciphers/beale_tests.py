'''
Robert Passas
CS5001
lab 13 -- straddle_tests.py
Tests cases for beale.py, a beale cipher algorithm.
'''

from beale import encrypt, decrypt
import unittest


class BealeTest(unittest.TestCase):
    def test_evaluate(self):
        '''
        Testing both instances generating errors and valid outputs
        '''
        # working instances
        en1 = encrypt('Oh hi, Mark!', 'zoroastrianism.txt', '3000')
        en2 = encrypt('DENNY', 'trump.txt', '420')
        en3 = encrypt('hahaha', 'zoroastrianism.txt', '0')
        de1 = decrypt('1 2 2 3', 'zoroastrianism.txt')
        de2 = decrypt('745 344 629 15 8817 1109', 'zoroastrianism.txt')
        de3 = decrypt('6 3320 7977 6 3798 5498', 'zoroastrianism.txt')
        # tests
        self.assertEqual(en1, '19 2291 6092 72 1124 450 137 3414')
        self.assertEqual(en2, '13 507 231 224 2')
        self.assertEqual(en3, '745 344 629 15 8817 1109')
        self.assertEqual(de1, 'ZOOM')
        self.assertEqual(de2, 'HAHAHA')
        self.assertEqual(de3, 'OKBOSS')
        # test errors
        # encrypt
        msg = 'letters in text must match first letter >= 1 word in key'
        self.assertRaisesRegex(ValueError,
                               'both text and key values must be given',
                               encrypt, 'Oh hi, Mark!',
                               '',
                               '24')
        self.assertRaisesRegex(TypeError,
                               'key must be a string',
                               encrypt, 'Oh hi, Mark!',
                               ['zoroastrianism.txt'],
                               '24')
        self.assertRaisesRegex(TypeError,
                               'text must be a string',
                               encrypt, ['Oh hi, Mark!'],
                               'zoroastrianism.txt',
                               '24')
        self.assertRaisesRegex(ValueError,
                               'seed must be an integer',
                               encrypt, 'Oh hi, Mark!',
                               'zoroastrianism.txt',
                               '2.4')
        self.assertRaisesRegex(ValueError,
                               'key is an invalid filename',
                               encrypt, 'Oh h1, Mark!',
                               'zoroastrianism.tt',
                               '24')
        self.assertRaisesRegex(ValueError,
                               'text must only contain valid letters',
                               encrypt, 'Oh h1, Mark!',
                               'zoroastrianism.txt',
                               '24')
        self.assertRaisesRegex(ValueError,
                               'key is an invalid filename',
                               encrypt, 'Oh hi, Mark!',
                               'zoroastrianis.txt',
                               '24')
        self.assertRaisesRegex(ValueError,
                               msg,
                               encrypt, 'Xerxes at the zoo',
                               'trump.txt',
                               '24')

        # decrypt
        self.assertRaisesRegex(TypeError,
                               'key must be a string',
                               decrypt, 'Oh hi, Mark!',
                               ['zoroastrianism.txt'])
        self.assertRaisesRegex(TypeError,
                               'text must be a string',
                               decrypt, ['Oh hi, Mark!'],
                               'zoroastrianism.txt')
        self.assertRaisesRegex(ValueError,
                               'cipher text must consist of integer literals',
                               decrypt, 'Oh hi, Mark!',
                               'zoroastrianism.txt')
        self.assertRaisesRegex(ValueError,
                               'key is an invalid filename',
                               decrypt, '3',
                               'zoroastrianism.tt')
        self.assertRaisesRegex(ValueError,
                               'key is an invalid filename',
                               decrypt, '3',
                               'zoroastrianis.txt')


if __name__ == '__main__':
    unittest.main(verbosity=5)

main()
