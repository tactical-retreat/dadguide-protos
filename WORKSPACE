workspace(name = "dadguide_protos")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# proto bindings
http_archive(
    name = "build_stack_rules_proto",
    sha256 = "78e378237c6e7bd7cfdda155d4f7010b27723f26ebfa6345e79675bddbbebc11",
    strip_prefix = "rules_proto-56665373fe541d6f134d394624c8c64cd5652e8c",
    urls = ["https://github.com/stackb/rules_proto/archive/56665373fe541d6f134d394624c8c64cd5652e8c.tar.gz"],
)

# Possibly necessary for rules generation. The Bazel version and protobuf library are
# really irritating dependencies to keep in sync.

# Depending on which version of Bazel is installed and com_google_protobuff is used, these flags
# might be necessary:
# --incompatible_new_actions_api=false
# --incompatible_no_support_tools_in_action_inputs=false
#
# I also tracked down a bug inside com_google_protobuf/protobuf.bzl inside _proto_gen_impl.
# For some reason, outs isn't getting populated correctly; if you manually populate it by editing
# that file locally it seems to work (at least in the example for firebase rules).

# Force override the proto version for the firebase transitive requirements
#load("@build_stack_rules_proto//protobuf:deps.bzl", "protobuf")
#
#protobuf(com_google_protobuf = "v3.8.0")
#protobuf(com_google_protobuf = "4fcb36c51c1c0355c2a23b1f06ec583f2428cd30")

# Flags that are possibly necessary for rule generation?

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

# Firebase rules gen
# Disabled; having problems setting this up
#proto_gen_firebase_rules_commit = "7797b8c08051a5f05620ba79dec6e6fb79b83c68"
#
#http_archive(
#    name = "proto_gen_firebase_rules",
#    sha256 = "84edd24d80ef54f6c4404a653b2f24e37c6e3ce2984dabb36e0b18cdb738488f",
#    strip_prefix = "protobuf-rules-gen-" + proto_gen_firebase_rules_commit,
#    url = "http://github.com/FirebaseExtended/protobuf-rules-gen/archive/" + proto_gen_firebase_rules_commit + ".tar.gz",
#)
#
#load("@proto_gen_firebase_rules//bazel:repositories.bzl", "protobuf_rules_gen_repositories")
#
#protobuf_rules_gen_repositories()
