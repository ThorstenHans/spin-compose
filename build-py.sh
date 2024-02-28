#! /bin/bash

pushd consumer-py
echo "Buidling Python App compontent in ${pwd}"
spin py2wasm app -o app.wasm
python3 -m venv .venv
source ./.venv/bin/activate
popd

pushd hmac
echo "Building HMAC component in ${pwd}"
cargo component build --release
popd

echo "Composing Consumer (Python)..."
wasm-tools compose -d ./hmac/target/wasm32-wasi/release/hmac.wasm ./consumer-py/app.wasm -o ./consumer-py/composed.wasm