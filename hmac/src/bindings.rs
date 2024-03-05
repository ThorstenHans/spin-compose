// Generated by `wit-bindgen` 0.18.0. DO NOT EDIT!
pub mod exports {
  pub mod fermyon {
    pub mod hmac {
      
      #[allow(clippy::all)]
      pub mod types {
        #[used]
        #[doc(hidden)]
        #[cfg(target_arch = "wasm32")]
        static __FORCE_SECTION_REF: fn() = super::super::super::super::__link_section;
        pub type Error = wit_bindgen::rt::string::String;
        
      }
      
      
      #[allow(clippy::all)]
      pub mod sign {
        #[used]
        #[doc(hidden)]
        #[cfg(target_arch = "wasm32")]
        static __FORCE_SECTION_REF: fn() = super::super::super::super::__link_section;
        pub type Error = super::super::super::super::exports::fermyon::hmac::types::Error;
        const _: () = {
          
          #[doc(hidden)]
          #[export_name = "fermyon:hmac/sign@0.1.0#sign"]
          #[allow(non_snake_case)]
          unsafe extern "C" fn __export_sign(arg0: i32,arg1: i32,arg2: i32,arg3: i32,) -> i32 {
            #[allow(unused_imports)]
            use wit_bindgen::rt::{alloc, vec::Vec, string::String};
            
            // Before executing any other code, use this function to run all static
            // constructors, if they have not yet been run. This is a hack required
            // to work around wasi-libc ctors calling import functions to initialize
            // the environment.
            //
            // This functionality will be removed once rust 1.69.0 is stable, at which
            // point wasi-libc will no longer have this behavior.
            //
            // See
            // https://github.com/bytecodealliance/preview2-prototyping/issues/99
            // for more details.
            #[cfg(target_arch="wasm32")]
            wit_bindgen::rt::run_ctors_once();
            
            let len0 = arg1 as usize;
            let len1 = arg3 as usize;
            let result2 = <_GuestImpl as Guest>::sign(Vec::from_raw_parts(arg0 as *mut _, len0, len0), Vec::from_raw_parts(arg2 as *mut _, len1, len1));
            let ptr3 = _RET_AREA.0.as_mut_ptr() as i32;
            match result2 {
              Ok(e) => { {
                *((ptr3 + 0) as *mut u8) = (0i32) as u8;
                let vec4 = (e).into_boxed_slice();
                let ptr4 = vec4.as_ptr() as i32;
                let len4 = vec4.len() as i32;
                ::core::mem::forget(vec4);
                *((ptr3 + 8) as *mut i32) = len4;
                *((ptr3 + 4) as *mut i32) = ptr4;
              } },
              Err(e) => { {
                *((ptr3 + 0) as *mut u8) = (1i32) as u8;
                let vec5 = (e.into_bytes()).into_boxed_slice();
                let ptr5 = vec5.as_ptr() as i32;
                let len5 = vec5.len() as i32;
                ::core::mem::forget(vec5);
                *((ptr3 + 8) as *mut i32) = len5;
                *((ptr3 + 4) as *mut i32) = ptr5;
              } },
            };ptr3
          }
          
          const _: () = {
            #[doc(hidden)]
            #[export_name = "cabi_post_fermyon:hmac/sign@0.1.0#sign"]
            #[allow(non_snake_case)]
            unsafe extern "C" fn __post_return_sign(arg0: i32,) {
              let l0 = i32::from(*((arg0 + 0) as *const u8));
              match l0 {
                0 => {
                  let l1 = *((arg0 + 4) as *const i32);
                  let l2 = *((arg0 + 8) as *const i32);
                  let base3 = l1;
                  let len3 = l2;
                  wit_bindgen::rt::dealloc(base3, (len3 as usize) * 1, 1);
                },
                _ => {
                  let l4 = *((arg0 + 4) as *const i32);
                  let l5 = *((arg0 + 8) as *const i32);
                  wit_bindgen::rt::dealloc(l4, (l5) as usize, 1);
                },
              }
            }
          };
        };
        use super::super::super::super::super::Component as _GuestImpl;
        pub trait Guest {
          fn sign(data: wit_bindgen::rt::vec::Vec::<u8>,keyvalue: wit_bindgen::rt::vec::Vec::<u8>,) -> Result<wit_bindgen::rt::vec::Vec::<u8>,Error>;
        }
        
        #[allow(unused_imports)]
        use wit_bindgen::rt::{alloc, vec::Vec, string::String};
        
        #[repr(align(4))]
        struct _RetArea([u8; 12]);
        static mut _RET_AREA: _RetArea = _RetArea([0; 12]);
        
      }
      
      
      #[allow(clippy::all)]
      pub mod verify {
        #[used]
        #[doc(hidden)]
        #[cfg(target_arch = "wasm32")]
        static __FORCE_SECTION_REF: fn() = super::super::super::super::__link_section;
        const _: () = {
          
          #[doc(hidden)]
          #[export_name = "fermyon:hmac/verify@0.1.0#verify"]
          #[allow(non_snake_case)]
          unsafe extern "C" fn __export_verify(arg0: i32,arg1: i32,arg2: i32,arg3: i32,arg4: i32,arg5: i32,) -> i32 {
            #[allow(unused_imports)]
            use wit_bindgen::rt::{alloc, vec::Vec, string::String};
            
            // Before executing any other code, use this function to run all static
            // constructors, if they have not yet been run. This is a hack required
            // to work around wasi-libc ctors calling import functions to initialize
            // the environment.
            //
            // This functionality will be removed once rust 1.69.0 is stable, at which
            // point wasi-libc will no longer have this behavior.
            //
            // See
            // https://github.com/bytecodealliance/preview2-prototyping/issues/99
            // for more details.
            #[cfg(target_arch="wasm32")]
            wit_bindgen::rt::run_ctors_once();
            
            let len0 = arg1 as usize;
            let len1 = arg3 as usize;
            let len2 = arg5 as usize;
            let result3 = <_GuestImpl as Guest>::verify(Vec::from_raw_parts(arg0 as *mut _, len0, len0), Vec::from_raw_parts(arg2 as *mut _, len1, len1), Vec::from_raw_parts(arg4 as *mut _, len2, len2));
            match result3 { true => 1, false => 0 }
          }
        };
        use super::super::super::super::super::Component as _GuestImpl;
        pub trait Guest {
          fn verify(data: wit_bindgen::rt::vec::Vec::<u8>,keyvalue: wit_bindgen::rt::vec::Vec::<u8>,tag: wit_bindgen::rt::vec::Vec::<u8>,) -> bool;
        }
        
      }
      
    }
  }
}

#[cfg(target_arch = "wasm32")]
#[link_section = "component-type:signing"]
#[doc(hidden)]
pub static __WIT_BINDGEN_COMPONENT_TYPE: [u8; 376] = [0, 97, 115, 109, 13, 0, 1, 0, 0, 25, 22, 119, 105, 116, 45, 99, 111, 109, 112, 111, 110, 101, 110, 116, 45, 101, 110, 99, 111, 100, 105, 110, 103, 4, 0, 7, 251, 1, 1, 65, 2, 1, 65, 7, 1, 66, 2, 1, 115, 4, 0, 5, 101, 114, 114, 111, 114, 3, 0, 0, 4, 1, 24, 102, 101, 114, 109, 121, 111, 110, 58, 104, 109, 97, 99, 47, 116, 121, 112, 101, 115, 64, 48, 46, 49, 46, 48, 5, 0, 2, 3, 0, 0, 5, 101, 114, 114, 111, 114, 1, 66, 6, 2, 3, 2, 1, 1, 4, 0, 5, 101, 114, 114, 111, 114, 3, 0, 0, 1, 112, 125, 1, 106, 1, 2, 1, 1, 1, 64, 2, 4, 100, 97, 116, 97, 2, 8, 107, 101, 121, 118, 97, 108, 117, 101, 2, 0, 3, 4, 0, 4, 115, 105, 103, 110, 1, 4, 4, 1, 23, 102, 101, 114, 109, 121, 111, 110, 58, 104, 109, 97, 99, 47, 115, 105, 103, 110, 64, 48, 46, 49, 46, 48, 5, 2, 1, 66, 3, 1, 112, 125, 1, 64, 3, 4, 100, 97, 116, 97, 0, 8, 107, 101, 121, 118, 97, 108, 117, 101, 0, 3, 116, 97, 103, 0, 0, 127, 4, 0, 6, 118, 101, 114, 105, 102, 121, 1, 1, 4, 1, 25, 102, 101, 114, 109, 121, 111, 110, 58, 104, 109, 97, 99, 47, 118, 101, 114, 105, 102, 121, 64, 48, 46, 49, 46, 48, 5, 3, 4, 1, 26, 102, 101, 114, 109, 121, 111, 110, 58, 104, 109, 97, 99, 47, 115, 105, 103, 110, 105, 110, 103, 64, 48, 46, 49, 46, 48, 4, 0, 11, 13, 1, 0, 7, 115, 105, 103, 110, 105, 110, 103, 3, 0, 0, 0, 70, 9, 112, 114, 111, 100, 117, 99, 101, 114, 115, 1, 12, 112, 114, 111, 99, 101, 115, 115, 101, 100, 45, 98, 121, 2, 13, 119, 105, 116, 45, 99, 111, 109, 112, 111, 110, 101, 110, 116, 6, 48, 46, 50, 49, 46, 48, 16, 119, 105, 116, 45, 98, 105, 110, 100, 103, 101, 110, 45, 114, 117, 115, 116, 6, 48, 46, 49, 56, 46, 48];

#[inline(never)]
#[doc(hidden)]
#[cfg(target_arch = "wasm32")]
pub fn __link_section() {}
