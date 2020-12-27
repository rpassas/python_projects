'''
Robert Passas
CS5001
lab 13 -- rotaluclac_tests.py
Tests cases for rotaluclac.py, a simple reverse polish notation calculator.
'''

from rotaluclac import apply, evaluate
import unittest


class CalcTest(unittest.TestCase):
    def test_evaluate(self):
        '''
        Testing both instances generating errors and valid outputs
        '''
        # working instances
        stack1 = evaluate('4      5   +')
        stack2 = evaluate('7  8 %')
        stack3 = evaluate('8 7 %')
        stack4 = evaluate('4 3 2 + *')
        stack5 = evaluate('4 3 2 / -')
        stack6 = evaluate('11 4 2 / -')
        stack7 = evaluate('4 3 -')
        stack8 = evaluate('20 5 / 7 2 - *')
        stack9 = evaluate('-10 5 + 7 -2 - *')
        # tests
        self.assertEqual(stack1, 9)
        self.assertEqual(stack2, 7)
        self.assertEqual(stack3, 1)
        self.assertEqual(stack4, 20)
        self.assertEqual(stack5, 3)
        self.assertEqual(stack6, 9)
        self.assertEqual(stack7, 1)
        self.assertEqual(stack8, 20)
        self.assertEqual(stack9, -45)
        # test errors
        self.assertRaisesRegex(TypeError, 'Invalid equation: not a string',
                               evaluate, ['2 4 +'])
        self.assertRaisesRegex(ValueError, 'Invalid operator',
                               evaluate, '2 4 &')
        self.assertRaisesRegex(ValueError, 'Invalid operator',
                               evaluate, '2 4 a')
        self.assertRaisesRegex(ValueError, 'Invalid number of operands',
                               evaluate, '2 4 3 +')
        self.assertRaisesRegex(ValueError, 'Invalid number of operands',
                               evaluate, '2  +')
        self.assertRaisesRegex(ValueError, 'Cannot divide by zero',
                               evaluate, '2 0 /')
        self.assertRaisesRegex(ValueError, 'Cannot divide by zero',
                               evaluate, '2 0 %')
        self.assertRaisesRegex(ValueError, 'Invalid literal - cannot be float',
                               evaluate, '2.3 4 +')


if __name__ == '__main__':
    unittest.main(verbosity=5)

main()
