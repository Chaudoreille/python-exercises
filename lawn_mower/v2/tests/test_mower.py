import sys
import pytest
import io
import os

from ..app import MowerSyntaxError,get_lawn_dimensions,get_instruction_set,get_mower_starting_position

lawn_dimensions_test_set = {
    '5 5'        : ['5','5'],
    '10 210'     : ['10','210'],
    '    8 7   ' : ['8','7'],
    '    9 30'   : ['9','30'],
    '0 0   '     : ['0','0'],
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
    '5 5 N'        : ['5','5', 'N'],
    '10 210 W'     : ['10', '210', 'W'],
    '    8 7   E'  : ['8', '7', 'E'],
    '70 8 S'       : ['70', '8', 'S'],
    '7 0 W'        : ['7', '0', 'W'],
    '75 80 NS'     : False,
    '7 8 N S'      : False,
    ''             : False,
    'N'            : False,
    '78N'          : False,
    '6 5 X'        : False,
}

instruction_test_set = {
    'LRFRFLFLLFRRRLFLRFLFLF': ['L','R','F','R','F','L','F','L','L','F','R','R','R','L','F','L','R','F','L','F','L','F'],
    'L'                     : ['L'],
    ' LRFLRFLR             ': ['L','R','F','L','R','F','L','R'],
    '   LRFLLLLLLLLFFF     ': ['L','R','F','L','L','L','L','L','L','L','L','F','F','F'],
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
    for test_case,expected_result in test_set.items():
        try:
            result = test_function(test_case)
            assert(result == expected_result)
        except MowerSyntaxError:
            assert(expected_result == False)

@pytest.mark.lexer_test
def test_get_lawn_dimensions():
    run_test_set(test_function=get_lawn_dimensions, test_set=lawn_dimensions_test_set)

@pytest.mark.lexer_test
def test_get_mower_starting_position():
    run_test_set(test_function=get_mower_starting_position, test_set=mower_starting_position_test_set)

@pytest.mark.lexer_test
def test_get_instruction_set():
    run_test_set(test_function=get_instruction_set, test_set=instruction_test_set)

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

