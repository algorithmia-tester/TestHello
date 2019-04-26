from . import TestHello

def test_TestHello():
    assert TestHello.apply("Jane") == "hello Jane"
