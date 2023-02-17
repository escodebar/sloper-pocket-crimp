from sloper_pocket_crimp import exceptions
import pytest


def test_InvalidGesture_exists():
    assert getattr(exceptions, "InvalidGesture", False)
