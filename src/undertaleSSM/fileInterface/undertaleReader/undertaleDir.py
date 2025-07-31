from pathlib import Path

from fileInterface.undertaleReader.undertaleIni import UndertaleIni
from .undertaleFile import UndertaleFile
# from .undertaleIni import UndertaleIni


class UndertaleDirectory:
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
        
        self.iniFile: UndertaleIni = UndertaleIni(str(pathlib_path/"undertale.ini"))
