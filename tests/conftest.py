import pytest
from pathlib import Path

from clldutils.path import copytree


@pytest.fixture
def tmprepo():
    p = Path(__file__).parent / 'repo_data'
    return {'raw': p / 'raw', 'glottolog': p / 'glottolog_repo'}


@pytest.fixture
def tmppath(tmpdir):
    return Path(str(tmpdir))


@pytest.fixture
def test_dataset(tmppath):
    copytree(Path(__file__).parent / 'repo_data' / 'test_dataset', tmppath / 'test_dataset')
    return tmppath / 'test_dataset' / 'td.py'
