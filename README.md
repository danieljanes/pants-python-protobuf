# Pants/Python/ProtoBuf

The repo tries to use Pants 2.0 to build/test a Python/ProtoBuf example.

> Note: This repo uses a pre-release version of Pants 2.0 which requires the
> following environment variable to be exported:
> `PANTS_SHA=6c90064f91442feb55ced0f982676a1d1f99c6c5`

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
- Typechecking with `mypy`:
  - `./pants typecheck ::`

## Open Issues

- `gRPC` support when compiling `.proto` files:
  - Related issue: https://github.com/pantsbuild/pants/issues/10497
- `mypy-protobuf` support when compiling `.proto` files:
  - Related issue: https://github.com/pantsbuild/pants/issues/10497
- Build `.whl` file:
  ```shell
  $ ./pants setup-py --args="bdist_wheel" src/py/myorg
  13:35:12 [ERROR] 1 Exception encountered:

    NoOwnerError: No exported target owner found for src/proto/myorg/proto

  (Use --print-exception-stacktrace to see more error details.)
  ```
