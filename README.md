# dadguide-protos

Install protoc:
https://github.com/protocolbuffers/protobuf/releases

```bash
cd ~/development
wget https://github.com/protocolbuffers/protobuf/releases/download/v3.8.0/protoc-3.8.0-linux-x86_64.zip
unzip protoc-3.8.0-linux-x86_64.zip
rm protoc-3.8.0-linux-x86_64.zip
export PATH=$PATH:~/development/protoc-3.8.0/bin
```


## Dart setup

Dart must be installed for this to work, and the bin dir on your path. Install the Dart protoc plugin:

```bash
pub global activate protoc_plugin
export PATH=$PATH:$HOME/.pub-cache/bin
```

## Regenerate protos

```bash
protoc -I protos --dart_out=dart --python_out=python --js_out=js protos/*.proto
```




I'm using this plugin for generating firebase rules:
https://github.com/FirebaseExtended/protobuf-rules-gen

Download the Firebase plugin: https://github.com/FirebaseExtended/protobuf-rules-gen/releases


