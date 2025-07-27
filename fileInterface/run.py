from __future__ import annotations
from uuid import uuid4
from typing import TYPE_CHECKING

from .save import Save
from .util import AutoSaveable, autosave
from . import types
if TYPE_CHECKING:
    from .dataFileInterface import DataFileInterface


class Run(AutoSaveable):
    @classmethod
    def fromDict(cls, dataFileInterface: DataFileInterface, data: types.RunData) -> Run:
        description = data.get("description")
        if type(description) != str:
            description = ""

        uuid = data.get("uuid")
        if type(uuid) != str:
            uuid = str(uuid4())

        latestSaveUUID = data.get("latestSaveUUID")
        if type(latestSaveUUID) != str and latestSaveUUID is not None:
            latestSaveUUID = None

        startSaveUUID = data.get("startUUID")
        if type(startSaveUUID) != str and startSaveUUID is not None:
            startSaveUUID = None

        raw_saves = data.get("saves")
        if type(raw_saves) != list:
            raw_saves = []

        return cls(
            dataFileInterface,
            description,
            uuid,
            latestSaveUUID,
            startSaveUUID,
            raw_saves
        )

    def __init__(self, dataFileInterface: DataFileInterface, description: str, uuid: str, latestSaveUUID: str | None, startSaveUUID: str | None, raw_saves: types.SavesList) -> None:
        self.directory: str = dataFileInterface.saves_path
        self.dataFileInterface: DataFileInterface = dataFileInterface
        self._description: str = description
        self.uuid: str = uuid
        self.latestSaveUUID: str | None = latestSaveUUID
        self.startSaveUUID: str | None = startSaveUUID

        saves = [Save.fromDict(self, saveData)
                 for saveData in raw_saves]
        self.saves: dict[str, Save] = self._parse(saves)

    def getDataFileInterface(self) -> DataFileInterface:
        return self.dataFileInterface

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    @autosave
    def description(self, value: str):
        self._description = value

    def _parse(self, raw_saves: list[Save]) -> dict[str, Save]:
        saves: dict[str, Save] = {}
        for save in raw_saves:
            saves[save.uuid] = save
        return saves

    def toDict(self) -> types.RunData:
        save_data: types.SavesList = [save.toDict()
                                      for save in self.getSaves()]
        out: types.RunData = {
            "description": self._description,
            "uuid": self.uuid,
            "latestSaveUUID": self.latestSaveUUID,
            "startUUID": self.startSaveUUID,
            "saves": save_data
        }
        return out

    def getSaves(self) -> list[Save]:
        return [save for _, save in self.saves.items()]

    def getSaveByUUID(self, uuid: str) -> Save | None:
        return self.saves.get(uuid)

    @property
    def latestSave(self) -> Save | None:
        if self.latestSaveUUID is None:
            return
        return self.getSaveByUUID(self.latestSaveUUID)

    def travelToSave(self, save: Save):
        self.latestSaveUUID = save.uuid

    @autosave
    def appendSave(self, save: Save):
        self.saves[save.uuid] = save

    def createSave(self) -> Save:
        save = Save.fromEmpty(self)
        save.pullDirectory()

        if self.latestSave is not None:
            save.stitchToPrevious(self.latestSave)
        self.travelToSave(save)

        if self.startSaveUUID is None:
            self.startSaveUUID = save.uuid

        self.appendSave(save)
        return save
    @autosave
    def removeSave(self,save:Save):
        save.removeStitches()
        self.saves.pop(save.uuid)
