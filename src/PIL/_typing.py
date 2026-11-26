from __future__ import annotations

import os
import sys
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Protocol, TypeVar

# Ensure typing-only names that are exported (e.g. IntegralLike) exist at
# runtime even though TYPE_CHECKING is False during normal execution.
if not TYPE_CHECKING:
    # Provide a simple runtime fallback so imports like
    # 'from PIL._typing import IntegralLike' do not fail at runtime.
    IntegralLike = int

TYPE_CHECKING = False
if TYPE_CHECKING:
    from numbers import _IntegralLike as IntegralLike

    try:
        import numpy.typing as npt

        NumpyArray = npt.NDArray[Any]
    except ImportError:
        pass

if sys.version_info >= (3, 13):
    from types import CapsuleType
else:
    CapsuleType = object

if sys.version_info >= (3, 12):
    from collections.abc import Buffer
else:
    Buffer = Any


_Ink = float | tuple[int, ...] | str

Coords = Sequence[float] | Sequence[Sequence[float]]


_T_co = TypeVar("_T_co", covariant=True)


class SupportsRead(Protocol[_T_co]):
    def read(self, length: int = ..., /) -> _T_co: ...


StrOrBytesPath = str | bytes | os.PathLike[str] | os.PathLike[bytes]


__all__ = ["Buffer", "IntegralLike", "StrOrBytesPath", "SupportsRead"]
