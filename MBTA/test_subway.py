'''
Robert Passas
CS5001
Lab 7 - tester
tests set of functions for lab 7 (every other,
abbreviate, sum of evens, and partition)
'''


import subway

EPSILON = .001

def subway_tester(start_list, expected):
    '''
Function: every_other_tester  -- test eevery_other
Params:   start_list    -- the list to be converted
          expected      -- expected output
Returns boolean indicating passing/failing
    '''
    print('Testing directions from', start, 'to', end)
    actual = every_other(start_list)
    return actual == expected


def every_other_tests():
    '''
function: every_other_tests
parameters: none
returns: an int, number of tests that failed
'''
    fails = 0

    # test 1
    if every_other_tester(['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                          ['a', 'c', 'e', 'g']):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if every_other_tester([1, 2, 3, 4, 5, 6],
                          [1, 3, 5]):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 3
    if every_other_tester([0],
                          [0]):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 4
    if every_other_tester(['bob', 'aleef', 'shamir', 'maxim'],
                          ['bob', 'shamir']):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 5
    if every_other_tester([],
                          []):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1
    print(fails, 'fails')
    return fails


def abbreviate_tester(word, expected):
    '''
Function: abbreviate_tester  -- test abbreviate
Params:   word    -- the word to be converted
          expected      -- expected output
Returns boolean indicating passing/failing
    '''
    print('Testing conversion of', word, 'to', expected)
    actual = abbreviate(word)
    return actual == expected


def abbreviate_tests():
    '''
function: abbreviate_tests
parameters: none
returns: an int, number of tests that failed
'''
    fails = 0

    # test 1
    if abbreviate_tester('chum bucket', 'chm bckt'):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if abbreviate_tester('', ''):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 3
    if abbreviate_tester('HelLO', 'HlL'):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 4
    if abbreviate_tester('123', '123'):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 5
    if abbreviate_tester('-*5&a', '-*5&'):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1
    print(fails, 'fails')
    return fails


def even_sum_tester(int_list, expected):
    '''
Function: even_sum_tester  -- test even_sum
Params:   int_list    -- the list of integers
          expected      -- expected output
Returns boolean indicating passing/failing
    '''
    print('Testing evaluation of', int_list, 'to', expected)
    actual = even_sum(int_list)
    return actual == expected


def even_sum_tests():
    '''
function: even_sum_tests
parameters: none
returns: an int, number of tests that failed
    '''
    fails = 0

    # test 1
    if even_sum_tester([1.2, 6, 9, 8, 4], 18):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if even_sum_tester([1.2, 6, 9, 'a', 4], 10):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 3
    if even_sum_tester([], 0):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 4
    if even_sum_tester([-4, 7.3, 2.4, 2], -2):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 5
    if even_sum_tester([-4.1, 7.3, 2.4, 2.9], 0):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1
    print(fails, 'fails')
    return fails


def partition_tester(list1, list2, list3, expected):
    '''
Function: partition_tester  -- test partition
Params:   int_list    -- the list of integers
          expected      -- expected output
Returns boolean indicating passing/failing
    '''
    print('Testing evaluation of', list1, 'to', expected)
    actual = partition(list1, list2, list3)
    return actual == expected


def partition_tests():
    '''
function: partition_tests
parameters: none
returns: an int, number of tests that failed
    '''
    fails = 0

    # test 1
    if partition_tester([1, 2, 3, 0, 0, -3], [6, 3], [-2, 4, 1], 2):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if partition_tester([1, 2, 3, 0, 0, -3], [0, 6, 3], [-2, 4, 1], 0):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 3
    if partition_tester([0, 0, 0], [6], [-2, 4, 1], 3):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 4
    if partition_tester([], [], [], 0):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 5
    if partition_tester(['f', 2, 3, 'a'], [6, 'f'], [-2, 4, 1], 0):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1
    print(fails, 'fails')
    return fails


def main():
    print('Run every_other tests')
    failed_every_other = every_other_tests()
    print('\n')

    print('Run abbreviate tests')
    failed_abbreviate = abbreviate_tests()
    print('\n')

    print('Run even_sum tests')
    failed_even_sum = even_sum_tests()
    print('\n')

    print('Run partition tests')
    failed_partition = partition_tests()
    print('\n')

    if (failed_every_other == 0 and failed_abbreviate == 0
        and failed_every_other == 0 and failed_partition == 0):
        print('all passed')
    else:
        print('not all passed')


if __name__ == "__main__":
    main()
