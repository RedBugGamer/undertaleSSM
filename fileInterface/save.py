from __future__ import annotations
from datetime import datetime
import enum
from pathlib import Path
import uuid
from . import types

class SaveType(enum.Enum):
    UNKNOWN = "unknown"
    DEATH = "death"
    SAVE = "save"
    START = "start"
    SAVE_POINT = "save_point"


class Save:
    @classmethod
    def fromDict(cls, saves_directory: str, data: types.SaveData) -> Save:
        uuidStr = data.get("uuid")
        if type(uuidStr) != str:
            uuidStr = str(uuid.uuid4())

        timestamp = data.get("timestamp")
        if type(timestamp) != float:
            timestamp = datetime.now().timestamp()

        previous = data.get("previous")
        if type(previous) != str and previous is not None:
            previous = None

        nextUUIDs = data.get("nextUUIDs")
        if type(nextUUIDs) != list:
            nextUUIDs = []
            
        hash = data.get("hash")
        if type(hash) != str: hash = ""
        return cls(
            saves_directory,
            uuidStr,
            SaveType(data.get("type", SaveType.UNKNOWN)),
            datetime.fromtimestamp(
                timestamp),
            previous,
            nextUUIDs,
            hash
        )

    def __init__(self, saves_directory: str, uuid: str, type: SaveType, timestamp: datetime, previousUUID: str | None, nextUUIDs: list[str], hash: str):
        self.uuid: str = uuid
        self.directory: str = str(Path(saves_directory)/self.uuid)
        self.type: SaveType = type
        self.timestamp: datetime = timestamp
        self.previousUUID: str | None = previousUUID
        self.nextUUids: list[str] = nextUUIDs
        self.hash: str = hash
    def toDict(self) -> types.SaveData:
        out:types.SaveData = {
            "uuid": self.uuid,
            "hash": self.hash,
            "type": self.type.value,
            "timestamp": int(self.timestamp.timestamp()),
            "previous": self.previousUUID,
            "nextUUIDs": self.nextUUids
        }
        return out
