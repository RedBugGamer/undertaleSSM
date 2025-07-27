from __future__ import annotations
from datetime import datetime
import enum
import os
from pathlib import Path
import shutil
import stat
from typing import TYPE_CHECKING, Any, Callable
import uuid

from dirhash import dirhash
from .util import AutoSaveable, autosave
from . import types

if TYPE_CHECKING:
    from .dataFileInterface import DataFileInterface
    from .run import Run


class SaveType(enum.Enum):
    UNKNOWN = "unknown"
    DEATH = "death"
    SAVE = "save"
    START = "start"
    SAVE_POINT = "save_point"


class Save(AutoSaveable):
    @classmethod
    def fromEmpty(cls, run: Run) -> Save:
        return cls.fromDict(run, {})

    @classmethod
    def fromDict(cls, run: Run, data: types.SaveData) -> Save:
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
            run,
            uuidStr,
            SaveType(data.get("type", SaveType.UNKNOWN)),
            datetime.fromtimestamp(
                timestamp),
            previous,
            nextUUIDs,
            hash
        )

    def __init__(self, run: Run, uuid: str, type: SaveType, timestamp: datetime, previousUUID: str | None, nextUUIDs: list[str], hash: str):
        self.uuid: str = uuid
        self.dataFileInterface: DataFileInterface = run.getDataFileInterface()
        self.run: Run = run
        self.directory: str = str(
            Path(self.dataFileInterface.saves_path)/self.uuid)
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

    def pullDirectory(self):
        dfi: DataFileInterface = self.getDataFileInterface()
        src_path: str = dfi.undertale_data_path
        target_path: str = self.directory
        shutil.copytree(src_path, target_path)

        self.hash = dirhash(target_path, "sha1")

    def _onFileError(self,func: Callable[[str], Any], path: str, _: Any):
        try:
            os.chmod(path, stat.S_IWRITE)
            func(path)
        except Exception:
            pass

    def pushDirectory(self):
        dfi: DataFileInterface = self.getDataFileInterface()
        src_path: str = self.directory
        target_path: str = dfi.undertale_data_path

        shutil.rmtree(target_path, onexc=self._onFileError)
        shutil.copytree(src_path, target_path)

        self.run.travelToSave(self)

    def rmDir(self):
        shutil.rmtree(self.directory,
                      onexc=self._onFileError)

    def stitchToPrevious(self, previousSave: Save):
        self.previousUUID = previousSave.uuid

        previousSave.nextUUids.append(self.uuid)

    def removeStitches(self):
        if self.previous is not None:
            self.previous.nextUUids.remove(self.uuid)
            self.previous.nextUUids.extend(self.nextUUids)

            for nextUUID in self.nextUUids:
                nextSave: Save | None = self.run.getSaveByUUID(nextUUID)
                if nextSave is None:
                    continue
                nextSave.previous = self.previous
            if self.run.latestSave == self:
                self.run.latestSaveUUID = self.previousUUID

    @property
    def previous(self) -> Save | None:
        if not self.previousUUID:
            return None
        return self.run.getSaveByUUID(self.previousUUID)

    @previous.setter
    def previous(self, save: Save):
        self.previousUUID = save.uuid

    def __eq__(self, value: object) -> bool:
        return type(value) == self.__class__ and self.uuid == value.uuid
