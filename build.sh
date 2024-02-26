#! /bin/bash

pushd api
echo "Building component in ${pwd}"
cargo component build --release
popd

pushd obfuscate
echo "Building component in ${pwd}"
cargo component build --release
popd

wasm-tools compose -d ./obfuscate/target/wasm32-wasi/release/obfuscate.wasm ./api/target/wasm32-wasi/release/api.wasm -o ./api/composed.wasm
