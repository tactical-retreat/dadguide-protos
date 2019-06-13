#!/usr/bin/env bash

bazel build protos:monster_dart_proto
cp bazel-bin/protos/monster_dart_proto/protos/*.dart dart/

bazel build protos:monster_python_proto
cp bazel-bin/protos/*.py python/
