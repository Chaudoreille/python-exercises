import sys
import pytest
import io
import os

from .. import *

def fill_tmp_file(contents):
    filename='tmp-test-file'

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(contents)

    return filename

def test_mower():
    filename = fill_tmp_file("""5 5
    1 2 N
    LFLFLFLFF
    3 3 E
    FFRFFRFRRF""")
    expected_results = [
        '1 3 N',
        '5 1 E'
    ]
    # assert(stuff)
    # pytest.fail("message")

    
    for test_number, result in enumerate(mower_generator(filename)):
        assert(result == expected_results[test_number])

