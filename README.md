# Pants/Python/ProtoBuf

The repo tries to use Pants 2.0 to build/test a Python/ProtoBuf example.

## Developer Flow

### Build

```shell
./pants binary src/py/myorg/mypkg:mypkg-bin
```

Run the PEX:

```shell
./dist/mypkg-bin.pex
```

### Auto-Format (black/isort)

```shell
./pants fmt ::
```

### Lint (black/isort/pylint)

```shell
./pants lint ::
```

### Typecheck (mypy)

```shell
./pants lint ::
```

## Open Issues

### Test failure due to missing proto package

`./pants test ::` raises an `ImportError` related to a missing compiled ProtoBuf.

In theory, this should be covered by the transitive dependency on a `protobuf_library` target: Target `src/py/myorg/mypkg:tests` depends on `src/py/myorg/mypkg:mypkg`, which in turn depends on `src/proto/myorg/proto`, which should include the missing proto.

```shell
$ ./pants test ::
17:29:42.08 [INFO] Completed: Building requirements.pex with 3 requirements: google==3.0.0, grpcio==1.30.0, protobuf==3.12.2
𐄂  src/py/myorg/mypkg:tests
============================= test session starts ==============================
platform linux -- Python 3.7.8, pytest-5.3.5, py-1.9.0, pluggy-0.13.1
rootdir: /tmp/process-executionWL0dFp
plugins: cov-2.8.1, timeout-1.3.4
collected 0 items / 1 error

==================================== ERRORS ====================================
______________ ERROR collecting src/py/myorg/mypkg/mybar_test.py _______________
ImportError while importing test module '/tmp/process-executionWL0dFp/src/py/myorg/mypkg/mybar_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
src/py/myorg/mypkg/mybar_test.py:3: in <module>
    from .mybar import create_foo
src/py/myorg/mypkg/mybar.py:5: in <module>
    from myorg.proto import foo_pb2
E   ImportError: cannot import name 'foo_pb2' from 'myorg.proto' (/tmp/process-executionWL0dFp/src/py/myorg/proto/__init__.py)
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================


src/py/myorg/mypkg:tests                                                        .....   FAILURE
```

### Pylint failure due to missing proto package

Running `./pants lint ::` results in the following error:

```shell
𐄂  Pylint failed.
************* Module myorg.mypkg.mybar
src/py/myorg/mypkg/mybar.py:5:0: E0611: No name 'foo_pb2' in module 'myorg.proto' (no-name-in-module)

------------------------------------------------------------------
```

### Mypy does not see the generated protos

```shell
$ ./pants typecheck ::
𐄂  MyPy failed.
src/py/myorg/mypkg/mybar.py:5: error: Module 'myorg.proto' has no attribute 'foo_pb2'
src/proto/myorg/proto/foo_pb2.py:16: error: Unexpected keyword argument "serialized_options" for "FileDescriptor"; did you mean "serialized_pb"?
/home/daniel/.pex/installed_wheels/0c3b3b1abe5fe08e286294484e6b0df6d39a5a01/mypy-0.782-cp36-cp36m-manylinux1_x86_64.whl/mypy/typeshed/third_party/2and3/google/protobuf/descriptor.pyi:279: note: "FileDescriptor" defined here
src/proto/myorg/proto/foo_pb2.py:34: error: Unexpected keyword argument "serialized_options" for "FieldDescriptor"
/home/daniel/.pex/installed_wheels/0c3b3b1abe5fe08e286294484e6b0df6d39a5a01/mypy-0.782-cp36-cp36m-manylinux1_x86_64.whl/mypy/typeshed/third_party/2and3/google/protobuf/descriptor.pyi:168: note: "FieldDescriptor" defined here
src/proto/myorg/proto/foo_pb2.py:41: error: Unexpected keyword argument "serialized_options" for "FieldDescriptor"
/home/daniel/.pex/installed_wheels/0c3b3b1abe5fe08e286294484e6b0df6d39a5a01/mypy-0.782-cp36-cp36m-manylinux1_x86_64.whl/mypy/typeshed/third_party/2and3/google/protobuf/descriptor.pyi:168: note: "FieldDescriptor" defined here
src/proto/myorg/proto/foo_pb2.py:27: error: Unexpected keyword argument "serialized_options" for "Descriptor"
/home/daniel/.pex/installed_wheels/0c3b3b1abe5fe08e286294484e6b0df6d39a5a01/mypy-0.782-cp36-cp36m-manylinux1_x86_64.whl/mypy/typeshed/third_party/2and3/google/protobuf/descriptor.pyi:72: note: "Descriptor" defined here
src/proto/myorg/proto/foo_pb2.py:85: error: Unexpected keyword argument "serialized_options" for "MethodDescriptor"
/home/daniel/.pex/installed_wheels/0c3b3b1abe5fe08e286294484e6b0df6d39a5a01/mypy-0.782-cp36-cp36m-manylinux1_x86_64.whl/mypy/typeshed/third_party/2and3/google/protobuf/descriptor.pyi:260: note: "MethodDescriptor" defined here
src/proto/myorg/proto/foo_pb2.py:76: error: Unexpected keyword argument "serialized_options" for "ServiceDescriptor"
/home/daniel/.pex/installed_wheels/0c3b3b1abe5fe08e286294484e6b0df6d39a5a01/mypy-0.782-cp36-cp36m-manylinux1_x86_64.whl/mypy/typeshed/third_party/2and3/google/protobuf/descriptor.pyi:246: note: "ServiceDescriptor" defined here
Found 7 errors in 2 files (checked 6 source files)
```
