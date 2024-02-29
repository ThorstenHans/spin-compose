"""
The insecure interface for insecure pseudo-random numbers.

It is intended to be portable at least between Unix-family platforms and
Windows.
"""
from typing import TypeVar, Generic, Union, Optional, Union, Protocol, Tuple, List, Any, Self
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some



def get_insecure_random_bytes(len: int) -> bytes:
    """
    Return `len` insecure pseudo-random bytes.
    
    This function is not cryptographically secure. Do not use it for
    anything related to security.
    
    There are no requirements on the values of the returned bytes, however
    implementations are encouraged to return evenly distributed values with
    a long period.
    """
    raise NotImplementedError

def get_insecure_random_u64() -> int:
    """
    Return an insecure pseudo-random `u64` value.
    
    This function returns the same type of pseudo-random data as
    `get-insecure-random-bytes`, represented as a `u64`.
    """
    raise NotImplementedError

