import pytest
from pynumerals.errorcheck import errorchecks

good_ones = ["lima", "li.ma", "liorma"]
bad_ones = ["1. lima", "lima <Tongan", "5", "English",
            "lima or rima", "IPA", "～", "or:"]


@pytest.mark.parametrize("x", good_ones)
def test_error_checks(x):
    r = False
    for check in errorchecks:
        if check(x):
            r = True  # pragma: no cover
    assert not r


@pytest.mark.parametrize("x", bad_ones)
def test_error_checks_bad(x):
    r = False
    for check in errorchecks:
        if check(x):
            r = True
    assert r
