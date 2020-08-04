# Pants/Python/ProtoBuf

The repo tries to use Pants 2.0 to build/test a Python/ProtoBuf example.

## Progress

- Build and run `.pex`:
  - `./pants binary src/py/myorg/mypkg:mypkg-bin`
  - `./dist/mypkg-bin.pex`
- Run tests:
  - `./pants test ::`
- Auto-format code:
  - `./pants fmt ::`
- Lint code with `Pylint`/`black`/`isort`:
  - `./pants lint ::`

## Open Issues

- `gRPC` support when compiling `.proto` files
- Typechecking with `mypy`:
  - `./pants typecheck ::`
- Build `.whl` file:
  - `./pants setup-py --args="bdist_wheel" src/py/myorg/mypkg`

## Details

### gRPC support when compiling `.proto` files

Building target `./pants binary src/py/myorg/mypkg:mypkg-bin` results in a `.pex` containing `myorg/proto/foo_pb2.py`, but the expected `myorg/proto/foo_pb2_grpc.py` is missing.

### Mypy error log

```shell
$ ./pants typecheck ::
𐄂 MyPy failed.
src/py/myorg/__init__.py: error: Duplicate module named 'myorg' (also at 'src/proto/myorg/__init__.py')
Found 1 error in 1 file (checked 7 source files)

12:50:28 [ERROR] unrecognized exit code 2 provided to LocalPantsRunner.exit() -- interpreting as a failure in the run tracker

(Use --print-exception-stacktrace to see more error details.)
12:50:28 [ERROR] unrecognized exit code 2 provided to LocalPantsRunner.exit() -- interpreting as a failure in the run tracker
```

### Build `.whl` files

```shell
$ ./pants setup-py --args="bdist_wheel" src/py/myorg/mypkg
12:55:19 [ERROR] 1 Exception encountered:

  NoOwnerError: No exported target owner found for src/py/myorg/__init__.py

(Use --print-exception-stacktrace to see more error details.)
```
