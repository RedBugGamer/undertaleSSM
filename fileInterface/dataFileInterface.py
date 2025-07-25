from __future__ import annotations
import json
from os import getenv
from pathlib import Path
from .run import Run
from .util import autosave

from . import types

class DataFileInterface:
    def __init__(self, data_file: str) -> None:
        self.data_file: str = data_file
        self.saves_path: str = ""
        self.undertale_data_path: str = ""
        self.currentRun: Run | None = None
        self.autosave: bool = False
        self._runs: dict[str, Run] = {}

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
            run = self.getNewRun(run_data)
            self._runs[run.uuid] = run

    def getNewRun(self, run_data: types.RunData = {}) -> Run:
        return Run.fromDict(self.saves_path, run_data)

    def toDict(self) -> types.DataFileStructure:
        out: types.DataFileStructure = {
            "savesPath": self.saves_path,
            "undertaleDataPath": self.undertale_data_path,
            "runs": [run.toDict() for run in self.getRuns()]
        }
        return out

    def getRuns(self) -> list[Run]:
        return [run for _, run in self._runs.items()]

    def save(self):
        with open(self.data_file, "w") as dataFile:
            json.dump(self.toDict(), dataFile, indent=4)

    @autosave
    def appendRun(self, run: Run):
        self._runs[run.uuid] = run

    def createRun(self) -> Run:
        run = self.getNewRun()
        self.appendRun(run)
        return run
