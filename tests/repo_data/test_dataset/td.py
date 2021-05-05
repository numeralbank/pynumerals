import pathlib

from pynumerals import IDSDataset


class Dataset(IDSDataset):
    dir = pathlib.Path(__file__).parent
    id = "test"
