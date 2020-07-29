python_library(
    dependencies = [
        "src/py/myorg/proto",
        "src/py/myorg/proto:init",
    ],
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
    entry_point = "myorg.mypkg.bar:main",
)
