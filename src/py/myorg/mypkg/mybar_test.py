"""Docstr."""

from .mybar import create_foo


def test_msg():
    """Docstr."""
    assert create_foo().content == "Hello, Pants!"
