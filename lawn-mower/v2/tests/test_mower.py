import sys
import pytest
import io
import os

from ..app import MowerSyntaxError,get_lawn_dimensions,get_instruction_set,get_mower_starting_position

lawn_dimensions_test_set = {
    '5 5'        : True,
    '10 210'     : True,
    '    8 7   ' : True,
    '    9 30'   : True,
    '0 0   '     : True,
    '0 F'        : False,
    'A B'        : False,
    '10'         : False,
    ' '          : False,
    'MIAM'       : False,
    '0 1 2'      : False,
    '12 %'       : False,
    '$ 20'       : False
}

mower_starting_position_test_set = {
    '5 5 N'        : True,
    '10 210 W'     : True,
    '    8 7   E'  : True,
    '70 8 S'       : True,
    '7 0 W'        : True,
    '75 80 NS'     : False,
    '7 8 N S'      : False,
    ''             : False,
    'N'            : False,
    '78N'          : False,
    '6 5 X'        : False,
}

instruction_test_set = {
    'LRFRFLFLLFRRRLFLRFLFLF': True,
    'L'                     : True,
    ' LRFLRFLRFLRFL        ': True,
    '   LRFLLLLLLLLFFF     ': True,
    'LRFRFLFLLFRRXLFLRFLFL' : False,
    '4                     ': False,
    ' LRF%FLRLR            ': False,
    ' LRF FLEEF FELELEE    ': False,
    ' LLLLLLLLLLLLL|LLLL'   : False,    
}

def fill_tmp_file(contents):
    filename='tmp-test-file'

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(contents)

    return filename

def run_test_set(test_function, test_set):
    for test_case,should_succeed in test_set.items():
        try:
            test_function(test_case)
            assert(should_succeed)
        except MowerSyntaxError:
            assert(not should_succeed)

def test_get_lawn_dimensions():
    run_test_set(test_function=get_lawn_dimensions, test_set=lawn_dimensions_test_set)

def test_get_mower_starting_position():
    run_test_set(test_function=get_mower_starting_position, test_set=mower_starting_position_test_set)

def test_get_instruction_set():
    run_test_set(test_function=get_instruction_set, test_set=instruction_test_set)

def test_instructions_lexer():
    pass

def test_mower():
    pass
    # filename = fill_tmp_file("""5 5
    # 1 2 N
    # LFLFLFLFF
    # 3 3 E
    # FFRFFRFRRF""")
    # expected_results = [
    #     '1 3 N',
    #     '5 1 E'
    # ]
    # # assert(stuff)
    # # pytest.fail("message")

    
    # for test_number, result in enumerate(mower_generator(filename)):
    #     assert(result == expected_results[test_number])

