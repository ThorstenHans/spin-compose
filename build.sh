#! /bin/bash

pushd api
echo "Building component in ${pwd}"
cargo component build --release
popd

pushd obfuscate
echo "Building component in ${pwd}"
cargo component build --release
popd

# Incoming HTTP POST 
#   -> Foo (Spin App) 
#     -> Returns an HTTP response 
#   -> Obfuscate mutate the HTTP response created in the previous step


wasm-tools compose -d ./obfuscate/target/wasm32-wasi/release/obfuscate.wasm ./api/target/wasm32-wasi/release/api.wasm -o ./api/composed.wasm
