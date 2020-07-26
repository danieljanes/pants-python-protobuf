# Pants/Python/ProtoBuf

The repo tries to use Pants 2.0 to build/test a Python/ProtoBuf example.

Build the PEX:

```shell
./pants binary src/py/myorg/mypkg:mypkg-bin
```

Run the PEX:

```shell
./dist/mypkg-bin.pex
```
