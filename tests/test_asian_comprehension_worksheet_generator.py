import pytest
import sys

from run import asian_comprehension_worksheet_generator as acwg

def test_split():
    assert acwg.split(acwg, "ABCD") == ['A', 'B', 'C', 'D']

def test_raw_text_to_list_of_vertical_column_less_than_num_y_cell():
    input_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    expected = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '', '']]
    assert acwg.raw_text_to_list_of_vertical_column(acwg,  input_value) == expected

def test_raw_text_to_list_of_vertical_column_equal_to_num_y_cell():
    input_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
    expected = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']]
    assert acwg.raw_text_to_list_of_vertical_column(acwg,  input_value) == expected

def test_raw_text_to_list_of_vertical_column_more_than_num_y_cell():
    input_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L']
    expected = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], ['L', '', '', '', '', '', '', '', '', '']]
    assert acwg.raw_text_to_list_of_vertical_column(acwg,  input_value) == expected

def test_add_empty_column_single_column():
    input_value = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']]
    expected =  [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''], 
                 ['', '', '', '', '', '', '', '', '', ''], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''], 
                 ['', '', '', '', '', '', '', '', '', ''], 
                 ['', '', '', '', '', '', '', '', '', ''], 
                 ['', '', '', '', '', '', '', '', '', '']]
    assert acwg.add_empty_columns(acwg, input_value) == expected

def test_add_empty_column_two_column():
    input_value = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']]
    expected =  [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''], 
                 ['', '', '', '', '', '', '', '', '', ''], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''], 
                 ['', '', '', '', '', '', '', '', '', ''], 
                 ['', '', '', '', '', '', '', '', '', ''], 
                 ['', '', '', '', '', '', '', '', '', '']]
    assert acwg.add_empty_columns(acwg, input_value) == expected

def test_add_empty_column_six_column():
    input_value = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']]
    expected =  [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '']]
    assert acwg.add_empty_columns(acwg, input_value) == expected

def test_add_empty_column_eight_column():
    input_value = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']]
    expected =  [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'], 
                 ['', '', '', '', '', '', '', '', '', ''],
                 ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                 ['', '', '', '', '', '', '', '', '', '']]
    assert acwg.add_empty_columns(acwg, input_value) == expected
