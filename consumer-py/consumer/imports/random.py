"""
WASI Random is a random data API.

It is intended to be portable at least between Unix-family platforms and
Windows.
"""
from typing import TypeVar, Generic, Union, Optional, Union, Protocol, Tuple, List, Any, Self
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some



def get_random_bytes(len: int) -> bytes:
    """
    Return `len` cryptographically-secure random or pseudo-random bytes.
    
    This function must produce data at least as cryptographically secure and
    fast as an adequately seeded cryptographically-secure pseudo-random
    number generator (CSPRNG). It must not block, from the perspective of
    the calling program, under any circumstances, including on the first
    request and on requests for numbers of bytes. The returned data must
    always be unpredictable.
    
    This function must always return fresh data. Deterministic environments
    must omit this function, rather than implementing it with deterministic
    data.
    """
    raise NotImplementedError

def get_random_u64() -> int:
    """
    Return a cryptographically-secure random or pseudo-random `u64` value.
    
    This function returns the same type of data as `get-random-bytes`,
    represented as a `u64`.
    """
    raise NotImplementedError

