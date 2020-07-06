import pytest
import zipfile
from pathlib import Path
from pyglottolog import Glottolog

from pynumerals.numerals_html import NumeralsEntry
from pynumerals.number_parser import parse_number
from pynumerals.value_parser import value_parser
from pynumerals.process_html import find_tables, get_file_paths


def test_init_repo(tmpdir):
    with zipfile.ZipFile(str(Path(__file__).parent / 'repo_data.zip'), 'r') as zip_ref:
        zip_ref.extractall(tmpdir)
    pytest.raw_htmls = Path(tmpdir) / 'raw'
    gl_repos = Path(tmpdir) / 'glottolog_repo'
    glottolog = Glottolog(gl_repos)
    pytest.gc_codes = glottolog.languoids_by_code()
    pytest.gc_iso = glottolog.iso.languages


def test_numeral_tables():
    d = list(find_tables([pytest.raw_htmls / 'Abui.htm']))[0]
    assert len(d) == 7
    entry = NumeralsEntry(
        base_name=d[0],
        tables=d[1],
        file_name=d[2],
        title_name=d[3],
        codes=pytest.gc_codes,
        iso=pytest.gc_iso,
        source=d[4],
        base=d[5],
        comment=d[6],
    )
    assert len(entry.tables) == 8
    assert entry.get_numeral_lexemes()[0][0][6][0] == 'tä.ˈlä.mä'


def test_num_entry():
    expected_gl_codes = ['abui1241', 'copa1236', 'bank1259']
    for i, f in enumerate([pytest.raw_htmls / 'Abui.htm',
                          pytest.raw_htmls / 'Zoque-Copainala.htm',
                          pytest.raw_htmls / 'Dogon-Bankan-Tey.htm']):
        d = list(find_tables([f]))[0]
        entry = NumeralsEntry(
            base_name=d[0],
            tables=d[1],
            file_name=d[2],
            title_name=d[3],
            codes=pytest.gc_codes,
            iso=pytest.gc_iso,
            source=d[4],
            base=d[5],
            comment=d[6],
        )
        assert entry.base_name == Path(f).stem
        assert entry.glottocodes[0] == expected_gl_codes[i]


def test_parse_number():
    with pytest.raises(ValueError):
        parse_number("No number in here!")
    with pytest.raises(ValueError):
        parse_number("1 foo")

    assert parse_number("1 ː") == 1
    assert parse_number("1,000.") == 1000
    assert parse_number("1,000.15 .") == 1000.15
    assert pytest.approx(parse_number("1,22:")) == 1.22


def test_fuzzy_number_matching():
    d = list(find_tables([pytest.raw_htmls / 'Aari.htm']))[0]
    entry = NumeralsEntry(
        base_name=d[0],
        tables=d[1],
        file_name=d[2],
        title_name=d[3],
        codes=pytest.gc_codes,
        iso=pytest.gc_iso,
        source=d[4],
        base=d[5],
        comment=d[6],
    )
    numeral_table = entry.tables[1]
    table_elements = numeral_table.find_all('tr')
    cell_content = []

    for row in table_elements:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        cell_content.append([ele for ele in cols if ele])

    # Table is roughly structured like this:
    # 1 | 21
    # 2 | 22
    # 3 | 23
    # ...
    # 10 | 30
    # ..
    # 20 | 2000

    assert parse_number(cell_content[0][0]) == 1
    assert parse_number(cell_content[0][1]) == 21
    assert parse_number(cell_content[9][0]) == 10
    assert parse_number(cell_content[19][1]) == 2000


def test_get_file_paths():
    assert len(get_file_paths(pytest.raw_htmls)) == 4


def test_value_parser(tmpdir):
    val, comment, other_form, loan = value_parser("ab [AB] (<Ido)   {c} (o)")
    assert val == 'AB'
    assert comment == '(<Ido)   {c} (o)'
    assert other_form == 'ab'
    assert loan is True
    val, comment, other_form, loan = value_parser("ab(c)  <Ido (c) {AA}1")
    assert val == 'ab(c)'
    assert comment == '{AA}1 (c), < Ido '
    assert other_form is None
    assert loan is True
    tmpdir.remove()
