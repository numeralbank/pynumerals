import pytest
from pynumerals.errorcheck import errorchecks

good_ones = ["lima", "li.ma", "liorma"]
bad_ones = ["1. lima", "lima <Tongan", "5", "English",
            "lima or rima", "IPA", "～", "or:"]


@pytest.mark.parametrize("x", good_ones)
def test_error_checks(x):
    assert not any(check(x) for check in errorchecks)


@pytest.mark.parametrize("x", bad_ones)
def test_error_checks_bad(x):
    assert any(check(x) for check in errorchecks)
