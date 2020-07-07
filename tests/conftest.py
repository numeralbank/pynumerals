import pytest
from pathlib import Path


@pytest.fixture
def tmprepo():
    p = Path(__file__).parent / 'repo_data'
    return {'raw': p / 'raw', 'glottolog': p / 'glottolog_repo'}
