from typing import TypeVar, Generic, Union, Optional, Union, Protocol, Tuple, List, Any, Self
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some



def exit(status: Result[None, None]) -> None:
    """
    Exit the current instance and any linked instances.
    """
    raise NotImplementedError

