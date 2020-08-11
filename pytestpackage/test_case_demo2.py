import pytest

@pytest.yield_fixture()
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")

def test_methodA():
    print("Running method A")


def test_methodB():
    print("Running method B")