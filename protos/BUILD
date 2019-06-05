load("@build_stack_rules_proto//python:python_proto_compile.bzl", "python_proto_compile")
load("@build_stack_rules_proto//dart:dart_proto_compile.bzl", "dart_proto_compile")

proto_library(
    name = "monster_proto",
    srcs = ["monster.proto"],
    deps = ["@com_google_protobuf//:any_proto"],
)

python_proto_compile(
    name = "monster_python_proto",
    deps = [":monster_proto"],
)

dart_proto_compile(
    name = "monster_dart_proto",
    deps = [":monster_proto"],
)
