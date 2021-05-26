# Python3 - Protocol Buffer (ProtoBuf) Template



## Intro

It has been developed in order to serialize-deserialize data independently of the programming language.



> Referance Guide: https://developers.google.com/protocol-buffers/docs/proto

> Download from: https://developers.google.com/protocol-buffers/docs/downloads



Briefly followed steps are as follows;

1. Preparing .proto files by creating data structures with Proto Buffer syntax
2. Compiling the .proto files created with the Proto Buffer syntax and creating the language-specific wrapper files to be used.
3. Serialize-deserialize data using wrapper files.



## Tutorial

1. Preparing .proto files with Proto Buffer syntax

   1. *Prepared .proto files are located under ./protos/ directory.*

2. Compiling .proto files

   1. ```bash
      >> protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto
      >> protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/timestamp.proto
      ```

3. Using wrapper files
   1. To see the main components: *example_01_introduction.py*
   2. Application example: *example_02_serialize.py - example_02_deserialize.py*

