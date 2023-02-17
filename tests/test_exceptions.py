from sloper_pocket_crimp import exceptions
import pytest


def test_InvalidGesture_exists():
    assert getattr(exceptions, "InvalidGesture", False)


@pytest.mark.xfail
def test_InvalidGesture_is_an_exception():
    assert issubclass(exceptions.InvalidGesture, Exception)
