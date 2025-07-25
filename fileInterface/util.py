from __future__ import annotations
from functools import wraps
from typing import Callable, Concatenate, ParamSpec, TypeVar, TYPE_CHECKING
if TYPE_CHECKING:
    from .dataFileInterface import DataFileInterface
    
class AutoSaveable:
    def getDataFileInterface(self) -> DataFileInterface:
        raise NotImplementedError("Must be implemented by subclass")

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T",bound="AutoSaveable")

def autosave(func: Callable[Concatenate[T, P], R]) -> Callable[Concatenate[T, P], R]:
    @wraps(func)
    def wrapper(self: T, *args: P.args, **kwargs: P.kwargs) -> R:
        result: R = func(self, *args, **kwargs)
        print("Called the autosave decorator from", type(self))
        dfi: DataFileInterface = self.getDataFileInterface()
        if dfi.autosave:
            dfi.save()
        return result
    return wrapper

