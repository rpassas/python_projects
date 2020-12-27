'''
Robert Passas
CS5001
lab 13 -- straddle_tests.py
Tests cases for straddle.py, a straddle cipher algorithm.
'''

from straddle import encrypt, decrypt
import unittest


class StraddleTest(unittest.TestCase):
    def test_evaluate(self):
        '''
        Testing both instances generating errors and valid outputs
        '''
        # working instances
        en1 = encrypt('Oh hi, Mark!',
                      'comhlberfjauwpztvxskinygdq', '24', '125')
        en2 = encrypt('DENNY',
                      'yxhkbnpmzulswagqdijftcerov', '19',
                      '1254571114568573932')
        en3 = encrypt('youre tearing me apart lisa!',
                      'cqgkytezriwjdunohlsfxpbvma', '94', '0')
        de1 = decrypt('Sure!?',
                      'ELKGRFZDWVBQOXHTMNUJAPSYIC', '17', '420')
        de2 = decrypt('WCPNBLCWMNZMNZW1MCEPGOCPN',
                      'CEYMOGNPRDSBXHIJAFTQZWLUKV', '28', '67')
        de3 = decrypt('YOURETEARINGMEAPARTLISA',
                      'cqgkytezriwjdunohlsfxpbvma', '32', '0')
        # tests
        self.assertEqual(en1, 'TCH0MYHM')
        self.assertEqual(en2, 'XYKMS')
        self.assertEqual(en3, 'YOURETEARINGMEAPARTLISA')
        self.assertEqual(de1, 'KLIKE')
        self.assertEqual(de2, 'IMDONEWITHTHISWORLD')
        self.assertEqual(de3, 'YOURETEARINGMEAPARTLISA')
        # test errors
        # encrypt
        alpha = 'alpha_key must contain only each letter of alphabet once'
        self.assertRaisesRegex(ValueError,
                               'both text and key values must be given',
                               encrypt, '',
                               'comhlberfjauwpztvxskinygdq',
                               '24', '125')
        self.assertRaisesRegex(ValueError,
                               'text must only contain valid letters',
                               encrypt, 'Oh h1, Mark!',
                               'comhlberfjauwpztvxskinygdq',
                               '24', '125')
        self.assertRaisesRegex(ValueError,
                               'num_key and add_key must be ints',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '24', '1a5')
        self.assertRaisesRegex(ValueError,
                               'num_key and add_key must be ints',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '24', '12.5')
        self.assertRaisesRegex(ValueError,
                               alpha,
                               encrypt, 'Oh hi, Mark!',
                               'comhllberfjauwpztvxskin1gdq', '24', '125')
        self.assertRaisesRegex(ValueError,
                               alpha,
                               encrypt, 'Oh hi, Mark!',
                               'comhberfjauwpztvxskinygdq', '24', '125')
        self.assertRaisesRegex(ValueError,
                               alpha,
                               encrypt, 'Oh hi, Mark!',
                               'comhllberfjauwpztvxskinygdq', '24', '125')
        self.assertRaisesRegex(ValueError,
                               'digits of num_key must be greater than 0',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '04', '125')
        self.assertRaisesRegex(ValueError,
                               'num_key must be have 2 unique integer digits',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '44', '125')
        self.assertRaisesRegex(ValueError,
                               'num_key must be have 2 unique integer digits',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', 'a4', '125')
        self.assertRaisesRegex(ValueError,
                               'num_key must be have 2 unique integer digits',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '234', '125')
        self.assertRaisesRegex(ValueError,
                               'num_key must be have 2 unique integer digits',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '2.4', '125')
        self.assertRaisesRegex(TypeError,
                               'text must be a string',
                               encrypt, ['Oh hi, Mark!'],
                               'comhlberfjauwpztvxskinygdq', '24', '125')
        self.assertRaisesRegex(TypeError,
                               'all keys must be strings',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', 24, '125')
        self.assertRaisesRegex(TypeError,
                               'all keys must be strings',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '24', 125)
        self.assertRaisesRegex(TypeError,
                               'all keys must be strings',
                               encrypt, 'Oh hi, Mark!',
                               ['comhlberfjauwpztvxskinygdq'], 24, '125')

        # decrypt
        self.assertRaisesRegex(ValueError,
                               'text must only contain valid letters',
                               encrypt, 'Oh h5, Mark!',
                               'comhlberfjauwpztvxskinygdq',
                               '24', '125')
        self.assertRaisesRegex(ValueError,
                               'num_key and add_key must be ints',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '34', '1a5')
        self.assertRaisesRegex(ValueError,
                               'num_key and add_key must be ints',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '23', '12.5')
        self.assertRaisesRegex(ValueError,
                               alpha,
                               encrypt, 'Oh hi, Mark!',
                               'comhllberfjauwpztvxskin1gdq', '24', '125')
        self.assertRaisesRegex(ValueError,
                               alpha,
                               encrypt, 'Oh hi, Mark!',
                               'comhberfjauwpztvxskinygdq', '23', '125')
        self.assertRaisesRegex(ValueError,
                               alpha,
                               encrypt, 'Oh hi, Mark!',
                               'comhllberfjauwpztvxskinygdq', '24', '125')
        self.assertRaisesRegex(ValueError,
                               'digits of num_key must be greater than 0',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '04', '125')
        self.assertRaisesRegex(ValueError,
                               'num_key must be have 2 unique integer digits',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '44', '125')
        self.assertRaisesRegex(ValueError,
                               'num_key must be have 2 unique integer digits',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', 'a4', '125')
        self.assertRaisesRegex(ValueError,
                               'num_key must be have 2 unique integer digits',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '234', '125')
        self.assertRaisesRegex(ValueError,
                               'num_key must be have 2 unique integer digits',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '2.4', '125')
        self.assertRaisesRegex(TypeError,
                               'text must be a string',
                               encrypt, ['Oh hi, Mark!'],
                               'comhlberfjauwpztvxskinygdq', '24', '125')
        self.assertRaisesRegex(TypeError,
                               'all keys must be strings',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', 24, '125')
        self.assertRaisesRegex(TypeError,
                               'all keys must be strings',
                               encrypt, 'Oh hi, Mark!',
                               'comhlberfjauwpztvxskinygdq', '24', 125)
        self.assertRaisesRegex(TypeError,
                               'all keys must be strings',
                               encrypt, 'Oh hi, Mark!',
                               ['comhlberfjauwpztvxskinygdq'], 24, '125')


if __name__ == '__main__':
    unittest.main(verbosity=5)

main()
