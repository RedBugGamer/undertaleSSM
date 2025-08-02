from __future__ import annotations
from functools import wraps
from typing import Callable, Concatenate, ParamSpec, TypeVar, TYPE_CHECKING
if TYPE_CHECKING:
    from .dataFileInterface import DataFileInterface


class AutoSaveable:
    """This is a helper class from which subclasses can be created. It contains only the method `getDataFileInterface()`, which should be overridden by all subclasses"""
    def getDataFileInterface(self) -> DataFileInterface:
        raise NotImplementedError("Must be implemented by subclass")


P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T", bound=AutoSaveable)


def autosave(func: Callable[Concatenate[T, P], R]) -> Callable[Concatenate[T, P], R]:
    """
    This decorator provides an easy way for methods of subclasses of `AutoSaveable` to autosave after a change happened
    """
    @wraps(func)
    def wrapper(self: T, *args: P.args, **kwargs: P.kwargs) -> R:
        result: R = func(self, *args, **kwargs)
        dfi: DataFileInterface = self.getDataFileInterface()
        if dfi.autosave:
            dfi.save()
        return result
    return wrapper
