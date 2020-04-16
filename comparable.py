# Implement comparable

from __future__ import annotations
from typing import TypeVar, List, Any
from typing_extensions import Protocol

C = TypeVar('C', bound="Comparable")


class Comparable(Protocol):

    def __eq__(selfself, other: Any) -> bool:
        ...

    def __lt__(selfself, other: Any) -> bool:
        ...

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other
