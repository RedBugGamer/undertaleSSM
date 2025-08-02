from __future__ import annotations
import json
from os import getenv
import os
from pathlib import Path

from .undertaleReader.undertaleDir import UndertaleDirectory
from .run import Run
from .util import autosave, AutoSaveable

from . import types


class DataFileInterface(AutoSaveable):
    """
    This class provides most logic for interfacing with the `data.json` file, as well as creation of `Run` objects
    """
    def __init__(self, data_file: str) -> None:
        """
        Initializer for `DataFileInterface`
        Args:
            data_file (str): A file path, where all data should be stored
        """
        self.data_file: str = data_file
        self.saves_path: str = ""
        self.undertale_data_path: str = ""
        self.autosave: bool = False
        """This sets wether to automatically save the data file if something changes"""
        self._runs: dict[str, Run] = {}
        self.activeRun: Run | None = None

        data_file_data = self._read()
        self._parse(data_file_data)

    def getDataFileInterface(self) -> DataFileInterface:
        """
            An instance of the DataFileInterface associated with this object.
        Returns:
            DataFileInterface
        """
        return self

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
        """
        This method allows creation of a new `Run` object, which is linked to the current DataFileInterface, but **NOT** registered for this object. If you do want to register this object please use `createRun()` instead.
        Args:
            run_data (types.RunData,optional): a dict containing raw data, from which to create a run. Defaults to an empty dict.
        Returns:
            A newly created `Run` object
        """
        return Run.fromDict(self, run_data)

    def toDict(self) -> types.DataFileStructure:
        """
        This method serializes this object and all connected `Runs`/`Saves` into a dict
        Returns:
            A dict containing all data
        """
        out: types.DataFileStructure = {
            "savesPath": self.saves_path,
            "undertaleDataPath": self.undertale_data_path,
            "runs": [run.toDict() for run in self.getRuns()]
        }
        return out

    def getRuns(self) -> list[Run]:
        """
        This method lists all `Run` objects
        Returns:
            All connected `Run` objects
        """
        return [run for _, run in self._runs.items()]

    def save(self):
        """
        This method saves all data to the data file and keeps a copy of the old version with the suffix "_old"
        """
        if os.path.exists(self.data_file + "_old"):
            os.remove(self.data_file + "_old")
        if os.path.exists(self.data_file):
            os.rename(self.data_file, self.data_file + "_old")
        with open(self.data_file, "w") as f:
            json.dump(self.toDict(), f, indent=4)

    @autosave
    def appendRun(self, run: Run):
        self._runs[run.uuid] = run

    def createRun(self) -> Run:
        """
        This method allows creation of a new `Run` object, which is linked to the current DataFileInterface and registered.
        Returns:
            A newly created `Run` object
        """
        run = self.getNewRun()
        self.appendRun(run)
        return run

    def getReader(self) -> UndertaleDirectory:
        """
        This method returns an `UndertaleDirectory` object, which was initialized with the undertale game directory.
        Returns:
            an `UndertaleDirectory` object
        """
        return UndertaleDirectory(self.undertale_data_path)
    
    def getRunByUUID(self,uuid:str) ->Run | None:
        """
        This method allows access to registered runs
        Args:
            uuid (str): The uuid of the wanted `Run` object
        Returns:
            The wanted `Run` object or `None` if a run with this uuid does not exist
        """
        return self._runs.get(uuid)
