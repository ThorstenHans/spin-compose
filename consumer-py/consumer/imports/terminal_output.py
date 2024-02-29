"""
Terminal output.

In the future, this may include functions for querying the terminal
size, being notified of terminal size changes, querying supported
features, and so on.
"""
from typing import TypeVar, Generic, Union, Optional, Union, Protocol, Tuple, List, Any, Self
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some


class TerminalOutput:
    """
    The output side of a terminal.
    """
    
    def __enter__(self):
        """Returns self"""
        return self
                                                                    
    def __exit__(self, *args):
        """
        Release this resource.
        """
        raise NotImplementedError



