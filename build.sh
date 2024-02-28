#! /bin/bash

pushd api
echo "Building component in ${pwd}"
cargo component build --release
popd

pushd consumer
echo "Buidling compontent in ${pwd}"
cargo component build --release
popd

pushd hmac
echo "Building component in ${pwd}"
cargo component build --release
popd

echo "Composing API..."
wasm-tools compose -d ./hmac/target/wasm32-wasi/release/hmac.wasm ./api/target/wasm32-wasi/release/api.wasm -o ./api/composed.wasm

echo "Composing Consumer..."
wasm-tools compose -d ./hmac/target/wasm32-wasi/release/hmac.wasm ./consumer/target/wasm32-wasi/release/consumer.wasm -o ./consumer/composed.wasm