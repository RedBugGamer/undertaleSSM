from __future__ import annotations
from functools import wraps
from typing import Callable, Concatenate, ParamSpec, TypeVar, TYPE_CHECKING
if TYPE_CHECKING:
    from .dataFileInterface import DataFileInterface

P = ParamSpec("P")
R = TypeVar("R")


def autosave(func: Callable[Concatenate[DataFileInterface, P], R]) -> Callable[Concatenate[DataFileInterface, P], R]:
    @wraps(func)
    def _out(self: DataFileInterface, *args: P.args, **kwargs: P.kwargs) -> R:
        result: R = func(self, *args, **kwargs)
        if self.autosave:
            self.save()
        return result
    return _out
