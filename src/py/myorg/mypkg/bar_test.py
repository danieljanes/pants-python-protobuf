from .bar import create_foo


def test_msg():
    assert create_foo().content == "Hello, Pants!"
