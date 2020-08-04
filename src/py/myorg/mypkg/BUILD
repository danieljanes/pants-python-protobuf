python_library(
    dependencies = [
        "src/proto/myorg/proto",
        "src/proto/myorg/proto:init",
    ],
    provides = setup_py(
        name='myorg.mypkg',
        version='0.0.1',
        description='MyOrg MyPkg.',
    ),
)

python_tests(
    name = "tests",
    dependencies = [
        ":mypkg",
    ],
)

python_binary(
    name = "mypkg-bin",
    dependencies = [
        ":mypkg",
    ],
    entry_point = "myorg.mypkg.mybar:main",
)
