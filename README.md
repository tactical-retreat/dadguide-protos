# dadguide-protos

Run rebuild.sh to rebuild the proto bindings. Assumes you have Bazel installed.

Only the `protos` folder has editable info; `dart`, `firestore`, and `python`
all contain generated output.

After any changes to the protos, the bindings should be regenerated and checked in.