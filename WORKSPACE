workspace(name = "dadguide_protos")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "build_stack_rules_proto",
    sha256 = "78e378237c6e7bd7cfdda155d4f7010b27723f26ebfa6345e79675bddbbebc11",
    strip_prefix = "rules_proto-56665373fe541d6f134d394624c8c64cd5652e8c",
    urls = ["https://github.com/stackb/rules_proto/archive/56665373fe541d6f134d394624c8c64cd5652e8c.tar.gz"],
)

# Python rules
load("@build_stack_rules_proto//python:deps.bzl", "python_proto_compile")

python_proto_compile()

# Dart rules
load("@build_stack_rules_proto//dart:deps.bzl", "dart_proto_compile")

dart_proto_compile()

# rules_go used here to compile a wrapper around the protoc-gen-grpc plugin
load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains()

load("@io_bazel_rules_dart//dart/build_rules:repositories.bzl", "dart_repositories")

dart_repositories()

load("@dart_pub_deps_protoc_plugin//:deps.bzl", dart_protoc_plugin_deps = "pub_deps")

dart_protoc_plugin_deps()
