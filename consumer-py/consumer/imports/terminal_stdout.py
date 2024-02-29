"""
An interface providing an optional `terminal-output` for stdout as a
link-time authority.
"""
from typing import TypeVar, Generic, Union, Optional, Union, Protocol, Tuple, List, Any, Self
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import terminal_output


def get_terminal_stdout() -> Optional[terminal_output.TerminalOutput]:
    """
    If stdout is connected to a terminal, return a `terminal-output` handle
    allowing further interaction with it.
    """
    raise NotImplementedError

