import pytest


@pytest.mark.xfail
def test_exceptions_import():
    from sloper_pocket_crimp import exceptions
