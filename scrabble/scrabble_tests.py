'''
Robert Passas
CS5001
Lab 11 - Scrabble_tests
purpose
'''


from scrabble import (read_text_file, store_words, interpret_input, get_words,
                      get_scores, print_scores, get_new_length)

EPSILON = .001


def read_text_file_tester(expected):
    '''
Function: read_text_file_tester   -- tests read_text_file
Params:   expected      -- expected output type
Returns boolean indicating proper output
'''
    print('Testing read_text output')
    actual = read_text_file()
    return isinstance(actual, expected)


def read_text_file_tests():
    '''
function: test cases for read_text_file
parameters:
returns: number of fails
'''
    fails = 0

    # test 1
    if (read_text_file_tester(list)):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    return fails


def store_words_tester(file_data, expected):
    '''
Function: store_words_tester   -- tests store_words
Params:   expected      -- expected output (dict)
file_data - list of strings to be sorted
Returns boolean indicating proper output given
'''
    print('Testing store_words output')
    actual = store_words(file_data)
    print(actual)
    return actual == expected


def store_words_tests():
    '''
function: test cases for read_text_file
parameters:
returns: number of fails
'''
    fails = 0

    # test 1
    if store_words_tester([], {}):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if store_words_tester(['asdf', 'as', 'df'],
                          {4: ['asdf'], 2: ['as', 'df']}):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    return fails


def interpret_input_tester(data, expected_out, expected_let):
    '''
Function: interpret_input_tester   -- tests interpret_input
Params:   expected_out      -- expected outputs (string)
expected_let - expected letters (string)
data - string to be evaluated as input
Returns boolean indicating proper output given
'''
    print('Testing interpret_input output')
    actual = interpret_input(data)
    return actual == expected_out, expected_let


def interpret_input_tests():
    '''
function: test cases for read_text_file
parameters:
returns: number of fails
'''
    fails = 0

    # test 1
    if interpret_input_tester('', '', ''):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if interpret_input_tester('qz 4', '4', 'qz'):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    return fails


def get_words_tester(max_length, word_dict, letters, expected):
    '''
Function: get_words_tester   -- tests get_words
Params:   expected      -- expected output (list)
word_dict -- dictionary to draw words from
max_length -- int indicating length of words
letters -- letters dictating word selection
Returns boolean indicating proper output given
'''
    print('Testing  get_words output')
    actual = get_words(max_length, word_dict, letters)
    return actual == expected


def get_words_tests():
    '''
function: test cases for get_words
parameters:
returns: number of fails
'''
    fails = 0

    # test 1
    if get_words_tester(2, {4: ['asdf'], 2: ['as', 'df']}, 'd', ['df']):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if get_words_tester(4, {4: ['asdf'], 2: ['as', 'df']},
                        'd', ['asdf', 'df']):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 3
    if get_words_tester(3.9, {4: ['asdf'], 2: ['as', 'df']},
                        'd', ['asdf', 'df']):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 4
    if get_words_tester(0, {4: ['asdf'], 2: ['as', 'df']}, 'd', []):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    return fails


def get_scores_tester(words, expected):
    '''
Function: get_scores_tester   -- tests get_scores
Params:   expected      -- dict where key = score, value = list of words
words - list of strings of input words
Returns boolean indicating proper output given
'''
    print('Testing interpret_input output')
    actual = get_scores(words)
    return actual == expected


def get_scores_tests():
    '''
function: test cases for get_scores
parameters:
returns: number of fails
'''
    fails = 0

    # test 1
    if get_scores_tester(['aa', 'b', 'aaa'], {2: ['aa'], 3: ['b', 'aaa']}):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if get_scores_tester([], {}):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 3
    if get_scores_tester(['quiz', 'at'], {22: ['quiz'], 2: ['at']}):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    return fails


def print_scores_tester(scores, numbers, expected):
    '''
Function: print_scores_tester   -- tests print_scores
Params:   expected      -- highest-scoring words printed
scores -- dictionary filled with points as keys and words as values
number -- number of highest scoring words to display
Returns boolean indicating proper output given
'''
    print('Testing print_scores output')
    actual = print_scores(scores, numbers)
    return actual == expected


def print_scores_tests():
    '''
function: test cases for print_scores
parameters:
returns: number of fails
'''
    fails = 0

    # test 1
    if print_scores_tester({2: ['aa'], 3: ['b', 'aaa']}, 1,
                           print('1 b 3')):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    return fails


def get_new_length_tester(cmd, expected):
    '''
Function: get_new_length_tester   -- tests get_new_length
Params:   expected      -- highest-scoring words printed
scores -- dictionary filled with points as keys and words as values
number -- number of highest scoring words to display
Returns boolean indicating proper output given
'''
    print('Testing get_new_length output')
    actual = get_new_length(cmd)
    return actual == expected


def get_new_length_tests():
    '''
function: test cases for print_scores
parameters:
returns: number of fails
'''
    fails = 0

    # test 1
    if get_new_length_tester('2', 2):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    # test 2
    if get_new_length_tester('0', 0):
        print('PASSED')
    else:
        print('FAILED')
        fails += 1

    return fails


def main():
    print('Run read_text_file tests')
    failed_read_text_file = read_text_file_tests()
    print('\n')

    print('Run store_words tests')
    failed_store_words = store_words_tests()
    print('\n')

    print('Run interpret_input tests')
    failed_interpret_input = interpret_input_tests()
    print('\n')

    print('Run get_words tests')
    failed_get_words = get_words_tests()
    print('\n')

    print('Run get_scores tests')
    failed_get_scores = get_scores_tests()
    print('\n')

    print('Run print_scores tests')
    failed_print_scores = print_scores_tests()
    print('\n')

    print('Run get_new_length tests')
    failed_get_new_length = get_new_length_tests()
    print('\n')

    if (failed_read_text_file == 0 and failed_store_words == 0
            and failed_interpret_input == 0 and failed_get_words == 0 and
            failed_get_scores == 0 and failed_print_scores == 0
            and failed_get_new_length == 0):
        print('all passed')
    else:
        print('not all passed')


if __name__ == "__main__":
    main()
