import pytest

from log_report.reports import get_report


def test_get_valid_report():
    """
    Test that a known report name returns a callable function.
    """
    func = get_report("average")
    assert callable(func)


def test_get_invalid_report():
    """
    Test that an unknown report name raises a ValueError.
    """
    with pytest.raises(ValueError):
        get_report("unknown")
