import json
from os import getenv
from pathlib import Path
from .run import Run

from . import types


class DataFileInterface:
    def __init__(self, data_file: str) -> None:
        self.data_file: str = data_file
        self.saves_path: str = ""
        self.undertale_data_path: str = ""
        self.currentRun: Run | None = None
        self.runs: dict[str, Run] = {}

        data_file_data = self._read()
        self._parse(data_file_data)

    def _read(self) -> types.DataFileStructure:
        try:
            with open(self.data_file, "r") as dataFile:
                raw_data = json.load(dataFile)
            return raw_data
        except FileNotFoundError:
            return dict()

    def _parse(self, data_file_data: types.DataFileStructure):
        self.saves_path = str(data_file_data.get(
            "savesPath", str((Path(self.data_file).parent / "saves").resolve())))
        self.undertale_data_path = str(data_file_data.get(
            "undertaleDataPath",
            str(Path(getenv("LOCALAPPDATA", str(Path.home()))) / "UNDERTALE")
        ))
        runs_data = data_file_data.get("runs")
        if type(runs_data) != list:
            runs_data = []
        
        for run_data in runs_data:
            run = Run.fromDict(self.saves_path,run_data)
            self.runs[run.uuid] = run
    
    def toDict(self) -> types.DataFileStructure:
        out:types.DataFileStructure = {
            "savesPath": self.saves_path,
            "undertaleDataPath": self.undertale_data_path,
            "runs": [run.toDict() for run in self.getRuns()]
        }
        return out

    def getRuns(self):
        return [run for _, run in self.runs.items()]
