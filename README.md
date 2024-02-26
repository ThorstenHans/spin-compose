# Composition Example

The purpose of the `obfuscate` component is to mutate an HTTP response created by `api` (a simple [Spin](https://developer.fermyon.com/spin) app), before the response is been sent to the client.

## Building the example

1. Build the Spin app with `cargo component build`
2. Build the component with `cargo component build`
3. Use `wasm-tools compose` to compose a new Wasm component from the app and the component

See [build.sh](./build.sh).
