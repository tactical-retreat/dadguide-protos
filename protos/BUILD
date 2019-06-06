load("@build_stack_rules_proto//python:python_proto_compile.bzl", "python_proto_compile")
load("@build_stack_rules_proto//dart:dart_proto_compile.bzl", "dart_proto_compile")
load("@proto_gen_firebase_rules//bazel:defs.bzl", "firestore_rules_proto_library", "firestore_rules_binary")

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

# Disabled; having problems setting this up
#firestore_rules_proto_library(
#    name = "monster_rules_proto",
#    srcs = ["monster.proto"],
#)
#
#firestore_rules_binary(
#    name = "dadguide",
#    srcs = ["main.rules"],
#    deps = [":monster_rules_proto"],
#)
