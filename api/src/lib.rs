use anyhow::bail;
use serde::Serialize;
use spin_sdk::http::{IntoResponse, Request, Response};
use spin_sdk::http_component;
mod bindings;
use bindings::fermyon::components::obfuscate;
#[derive(Serialize)]
pub struct Model {
    data: String,
}
/// A simple Spin HTTP component.
#[http_component]
fn handle_simple_http_api(req: Request) -> anyhow::Result<impl IntoResponse> {
    println!("Handling request to {:?}", req.header("spin-full-url"));
    let m = Model {
        data: String::from("Foo"),
    };
    let payload = serde_json::to_vec(&m)?;
    let payload = match obfuscate::obfuscate(payload.as_ref()) {
        Ok(p) => p,
        Err(e) => bail!(e),
    };
    Ok(Response::builder()
        .status(200)
        .header("content-type", "application/json")
        .body(payload)
        .build())
}
