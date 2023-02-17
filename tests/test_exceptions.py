from sloper_pocket_crimp import exceptions
import pytest


@pytest.mark.xfail
def test_InvalidGesture_exists():
    assert getattr(exceptions, "InvalidGesture", False)
