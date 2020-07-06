from pynumerals.numerals_utils import *


def test_int_en():
    assert int_to_en(3) == 'three'
    assert int_to_en(37) == 'thirty seven'
    assert int_to_en(30) == 'thirty'
    assert int_to_en(100) == 'hundred'
    assert int_to_en(200) == 'two hundred'
    assert int_to_en(1000) == 'thousand'
    assert int_to_en(2000) == 'two thousand'
    assert int_to_en(1000000) == 'million'
    assert int_to_en(2000000) == 'two million'
    assert int_to_en(1000000000) == 'one billion'
    assert int_to_en(2000000000) == 'two billion'
    assert int_to_en(1000000000000) == 'one trillion'
    assert int_to_en(2000000000000) == 'two trillion'
    assert int_to_en(222222222222222) ==\
        'two hundred and twenty two trillion, two hundred and twenty two billion,'\
        ' two hundred and twenty two million, two hundred and twenty two thousand,'\
        ' two hundred and twenty two'


def test_make():
    assert make_index_link("raw/a b.c") == "* [a b.c](a%20b.c)"
    assert make_chan_link("a b.c", "r/") == " ([Source](r/a%20b.c))"
    assert make_language_name("a") == " (a)"
    assert make_language_name("") == ""


def test_check_for_problems():
    assert check_for_problems([{'Problematic': True}]) == " **(Problems)**"
    assert check_for_problems([{'Problematic': False}]) == ""


def test_split_form_table():
    assert str(split_form_table(
        {'FormTable': [{'Language_ID': 'b'}, {'Language_ID': 'a'}]}))\
        == "[[{'Language_ID': 'a'}], [{'Language_ID': 'b'}]]"
