import shlex
import pathlib
import openpyxl

from cldfbench.__main__ import main


def _main(cmd, **kw):
    main(['--no-config'] + shlex.split(cmd), **kw)


def test_create_language_sheet(test_dataset):
    _main('pynumerals.create_language_sheet --lang-id "aari1239-1" {}'.format(
        test_dataset)
    )

    wb_path = test_dataset.parent / 'raw' / 'xlsx' / 'numerals-aari1239-1.xlsx'
    assert wb_path.exists()

    wb = openpyxl.load_workbook(wb_path)
    wa = wb['Data']
    assert wa['B2'].value == 'wólːáq'
    assert wa['E4'].value == 'maken'
    assert wa['A5'].value is None
    wm = wb['Metadata']
    assert wm['B2'].value == 'aiw'


def test_create_language_sheet_template(test_dataset):
    _main('pynumerals.create_language_sheet --lang-id "template" {}'.format(
        test_dataset)
    )

    wb_path = test_dataset.parent / 'raw' / 'xlsx' / 'numerals-{glottocode}-{x}.xlsx'
    assert wb_path.exists()

    wb = openpyxl.load_workbook(wb_path)
    wa = wb['Data']
    assert wa['A5'].value == 4

