use std::str;

use bindings::{exports::fermyon::components::obfuscate::Guest, fermyon::components::types::Error};

mod bindings;

struct Component;

impl Guest for Component {
    fn obfuscate(
        payload: wit_bindgen::rt::vec::Vec<u8>,
    ) -> Result<wit_bindgen::rt::vec::Vec<u8>, Error> {
        let Ok(value) = str::from_utf8(&payload) else {
            return Err(String::from("Error while converting payload to string"));
        };
        return Ok((0..value.len()).map(|_| "*").collect::<String>().into());
    }
}
