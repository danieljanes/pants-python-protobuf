"""Docstr."""

import datetime

from myorg.proto import foo_pb2


def create_foo():
    """Docstr."""
    return foo_pb2.Foo(
        content="Hello, Pants!", timestamp=datetime.datetime.utcnow().isoformat(),
    )


def main() -> None:
    """Docstr."""
    msg = create_foo()
    print(msg)


if __name__ == "__main__":
    main()
