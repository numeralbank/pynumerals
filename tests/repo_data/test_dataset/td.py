import pathlib

import pylexibank


class Dataset(pylexibank.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "test"
