from typing import TypeVar, Generic, Union, Optional, Union, Protocol, Tuple, List, Any, Self
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import types


def get_directories() -> List[Tuple[types.Descriptor, str]]:
    """
    Return the set of preopened directories, and their path.
    """
    raise NotImplementedError

