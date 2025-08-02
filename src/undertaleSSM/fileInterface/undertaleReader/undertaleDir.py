from __future__ import annotations
from pathlib import Path

from .undertaleIni import UndertaleIni
from .undertaleFile import UndertaleFile
# from .undertaleIni import UndertaleIni


class UndertaleDirectory:
    """
    This class allows reading a directory, which contains undertale game files (file[0-9] and undertale.ini).

    Example:
    >>> ud = UndertaleDirectory("/path/to/undertale/directory/")
    >>> print(ud.file0.room)
    """

    def __init__(self, path: str) -> None:
        pathlib_path: Path = Path(path)
        file_paths = list(pathlib_path.glob("file[0-9]*"))
        self.files: dict[str, UndertaleFile] = {}
        for file in file_paths:
            self.files[file.name] = UndertaleFile(str(file))
        self.file0: UndertaleFile | None = self.files.get("file0")
        self.file1: UndertaleFile | None = self.files.get("file1")
        self.file2: UndertaleFile | None = self.files.get("file2")
        self.file3: UndertaleFile | None = self.files.get("file3")
        self.file4: UndertaleFile | None = self.files.get("file4")
        self.file5: UndertaleFile | None = self.files.get("file5")
        self.file6: UndertaleFile | None = self.files.get("file6")
        self.file7: UndertaleFile | None = self.files.get("file7")
        self.file8: UndertaleFile | None = self.files.get("file8")
        self.file9: UndertaleFile | None = self.files.get("file9")

        self.iniFile: UndertaleIni = UndertaleIni(
            str(pathlib_path/"undertale.ini"))

    def __eq__(self, other: object) -> bool:
        if type(other) != self.__class__:
            return False
        for f_name, file in self.files.items():
            if file != other.files.get(f_name):
                return False
        if self.iniFile != other.iniFile:
            return False
        return True

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
