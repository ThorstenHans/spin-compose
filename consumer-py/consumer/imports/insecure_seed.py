"""
The insecure-seed interface for seeding hash-map DoS resistance.

It is intended to be portable at least between Unix-family platforms and
Windows.
"""
from typing import TypeVar, Generic, Union, Optional, Union, Protocol, Tuple, List, Any, Self
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some



def insecure_seed() -> Tuple[int, int]:
    """
    Return a 128-bit value that may contain a pseudo-random value.
    
    The returned value is not required to be computed from a CSPRNG, and may
    even be entirely deterministic. Host implementations are encouraged to
    provide pseudo-random values to any program exposed to
    attacker-controlled content, to enable DoS protection built into many
    languages' hash-map implementations.
    
    This function is intended to only be called once, by a source language
    to initialize Denial Of Service (DoS) protection in its hash-map
    implementation.
    
    # Expected future evolution
    
    This will likely be changed to a value import, to prevent it from being
    called multiple times and potentially used for purposes other than DoS
    protection.
    """
    raise NotImplementedError

