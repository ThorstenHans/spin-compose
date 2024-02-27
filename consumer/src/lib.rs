use anyhow::bail;
use data_encoding::HEXUPPER;
use spin_sdk::http::{IntoResponse, Request, Response};
use spin_sdk::http_component;
mod bindings;
use bindings::fermyon::hmac::verify::verify;

/// A simple Spin HTTP component.
#[http_component]
fn handle_consumer(req: Request) -> anyhow::Result<impl IntoResponse> {
    let key_value = "Vh7eWs5iEfHkkEFomlYDAKLdWrPFdQAqRsXj".as_bytes();
    let body = req.body();
    let tag = req.header("X-Signature").unwrap().as_bytes();
    //let tag = HEXUPPER.decode(tag.as_bytes())?;
    match verify(body, key_value, tag) {
        true => Ok(Response::builder().status(200).body(()).build()),
        false => Ok(Response::builder().status(500).body(()).build()),
    }
}
