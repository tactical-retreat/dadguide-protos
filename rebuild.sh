#!/usr/bin/env bash

bazel build protos:monster_dart_proto
cp bazel-genfiles/protos/*.dart dart/dadguide/

bazel build protos:monster_python_proto
cp bazel-genfiles/protos/*.py python/dadguide/
