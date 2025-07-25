from __future__ import annotations
from datetime import datetime
import enum
from pathlib import Path
from typing import TYPE_CHECKING
import uuid
from .util import AutoSaveable, autosave
from . import types

if TYPE_CHECKING:
    from .dataFileInterface import DataFileInterface


class SaveType(enum.Enum):
    UNKNOWN = "unknown"
    DEATH = "death"
    SAVE = "save"
    START = "start"
    SAVE_POINT = "save_point"


class Save(AutoSaveable):
    @classmethod
    def fromDict(cls, dataFileInterface: DataFileInterface, data: types.SaveData) -> Save:
        uuidStr = data.get("uuid")
        if type(uuidStr) != str:
            uuidStr = str(uuid.uuid4())

        timestamp = data.get("timestamp")
        if type(timestamp) != int:
            timestamp = datetime.now().timestamp()

        previous = data.get("previous")
        if type(previous) != str and previous is not None:
            previous = None

        nextUUIDs = data.get("nextUUIDs")
        if type(nextUUIDs) != list:
            nextUUIDs = []

        hash = data.get("hash")
        if type(hash) != str:
            hash = ""
        return cls(
            dataFileInterface,
            uuidStr,
            SaveType(data.get("type", SaveType.UNKNOWN)),
            datetime.fromtimestamp(
                timestamp),
            previous,
            nextUUIDs,
            hash
        )

    def __init__(self, dataFileInterface: DataFileInterface, uuid: str, type: SaveType, timestamp: datetime, previousUUID: str | None, nextUUIDs: list[str], hash: str):
        self.uuid: str = uuid
        self.dataFileInterface: DataFileInterface = dataFileInterface
        self.directory: str = str(Path(dataFileInterface.saves_path)/self.uuid)
        self._type: SaveType = type
        self.timestamp: datetime = timestamp
        self.previousUUID: str | None = previousUUID
        self.nextUUids: list[str] = nextUUIDs
        self.hash: str = hash

    def getDataFileInterface(self) -> DataFileInterface:
        return self.dataFileInterface

    @property
    def type(self) -> SaveType:
        return self._type

    @type.setter
    @autosave
    def type(self, value: SaveType):
        self._type = value

    def toDict(self) -> types.SaveData:
        out: types.SaveData = {
            "uuid": self.uuid,
            "hash": self.hash,
            "type": self.type.value,
            "timestamp": int(self.timestamp.timestamp()),
            "previous": self.previousUUID,
            "nextUUIDs": self.nextUUids
        }
        return out
