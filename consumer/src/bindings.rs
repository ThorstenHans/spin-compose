// Generated by `wit-bindgen` 0.18.0. DO NOT EDIT!
pub mod fermyon {
  pub mod hmac {
    
    #[allow(clippy::all)]
    pub mod verify {
      #[used]
      #[doc(hidden)]
      #[cfg(target_arch = "wasm32")]
      static __FORCE_SECTION_REF: fn() = super::super::super::__link_section;
      #[allow(unused_unsafe, clippy::all)]
      pub fn verify(data: &[u8],keyvalue: &[u8],tag: &[u8],) -> bool{
        
        #[allow(unused_imports)]
        use wit_bindgen::rt::{alloc, vec::Vec, string::String};
        unsafe {
          let vec0 = data;
          let ptr0 = vec0.as_ptr() as i32;
          let len0 = vec0.len() as i32;
          let vec1 = keyvalue;
          let ptr1 = vec1.as_ptr() as i32;
          let len1 = vec1.len() as i32;
          let vec2 = tag;
          let ptr2 = vec2.as_ptr() as i32;
          let len2 = vec2.len() as i32;
          
          #[cfg(target_arch = "wasm32")]
          #[link(wasm_import_module = "fermyon:hmac/verify@0.1.0")]
          extern "C" {
            #[link_name = "verify"]
            fn wit_import(_: i32, _: i32, _: i32, _: i32, _: i32, _: i32, ) -> i32;
          }
          
          #[cfg(not(target_arch = "wasm32"))]
          fn wit_import(_: i32, _: i32, _: i32, _: i32, _: i32, _: i32, ) -> i32{ unreachable!() }
          let ret = wit_import(ptr0, len0, ptr1, len1, ptr2, len2);
          wit_bindgen::rt::bool_lift(ret as u8)
        }
      }
      
    }
    
  }
}

#[cfg(target_arch = "wasm32")]
#[link_section = "component-type:middlewares"]
#[doc(hidden)]
pub static __WIT_BINDGEN_COMPONENT_TYPE: [u8; 255] = [0, 97, 115, 109, 13, 0, 1, 0, 0, 25, 22, 119, 105, 116, 45, 99, 111, 109, 112, 111, 110, 101, 110, 116, 45, 101, 110, 99, 111, 100, 105, 110, 103, 4, 0, 7, 127, 1, 65, 2, 1, 65, 2, 1, 66, 3, 1, 112, 125, 1, 64, 3, 4, 100, 97, 116, 97, 0, 8, 107, 101, 121, 118, 97, 108, 117, 101, 0, 3, 116, 97, 103, 0, 0, 127, 4, 0, 6, 118, 101, 114, 105, 102, 121, 1, 1, 3, 1, 25, 102, 101, 114, 109, 121, 111, 110, 58, 104, 109, 97, 99, 47, 118, 101, 114, 105, 102, 121, 64, 48, 46, 49, 46, 48, 5, 0, 4, 1, 43, 102, 101, 114, 109, 121, 111, 110, 58, 119, 101, 98, 104, 111, 111, 107, 115, 45, 99, 111, 110, 115, 117, 109, 101, 114, 47, 109, 105, 100, 100, 108, 101, 119, 97, 114, 101, 115, 64, 48, 46, 49, 46, 48, 4, 0, 11, 17, 1, 0, 11, 109, 105, 100, 100, 108, 101, 119, 97, 114, 101, 115, 3, 0, 0, 0, 70, 9, 112, 114, 111, 100, 117, 99, 101, 114, 115, 1, 12, 112, 114, 111, 99, 101, 115, 115, 101, 100, 45, 98, 121, 2, 13, 119, 105, 116, 45, 99, 111, 109, 112, 111, 110, 101, 110, 116, 6, 48, 46, 50, 49, 46, 48, 16, 119, 105, 116, 45, 98, 105, 110, 100, 103, 101, 110, 45, 114, 117, 115, 116, 6, 48, 46, 49, 56, 46, 48];

#[inline(never)]
#[doc(hidden)]
#[cfg(target_arch = "wasm32")]
pub fn __link_section() {}
