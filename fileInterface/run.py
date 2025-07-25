from __future__ import annotations
from uuid import uuid4
from .save import Save
from . import types


class Run:
    @classmethod
    def fromDict(cls, saves_directory: str, data: types.RunData) -> Run:
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

        saves = [Save.fromDict(saves_directory, saveData)
                 for saveData in raw_saves]
        return cls(
            saves_directory,
            description,
            uuid,
            latestSaveUUID,
            startSaveUUID,
            saves
        )

    def __init__(self, directory: str, description: str, uuid: str, latestSaveUUID: str | None, startSaveUUID: str | None, saves: list[Save]) -> None:
        self.directory: str = directory
        self.description: str = description
        self.uuid: str = uuid
        self.latestSaveUUID: str | None = latestSaveUUID
        self.startSaveUUID: str | None = startSaveUUID

        self.saves: dict[str, Save] = self._parse(saves)

    def _parse(self, raw_saves: list[Save]) -> dict[str, Save]:
        saves: dict[str, Save] = {}
        for save in raw_saves:
            saves[save.uuid] = save
        return saves

    def toDict(self) -> types.RunData:
        save_data: types.SavesList = [save.toDict()
                                      for save in self.getSaves()]
        out: types.RunData = {
            "description": self.description,
            "uuid": self.uuid,
            "latestSaveUUID": self.latestSaveUUID,
            "startUUID": self.startSaveUUID,
            "saves": save_data
        }
        return out

    def getSaves(self) -> list[Save]:
        return [save for _, save in self.saves.items()]
