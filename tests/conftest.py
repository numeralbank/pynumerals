import pytest
import zipfile
from pathlib import Path


@pytest.fixture
def create_repo(tmpdir, autouse=True):
    with zipfile.ZipFile(str(Path(__file__).parent / 'repo_data.zip'), 'r') as z:
        z.extractall(str(Path(tmpdir)))
