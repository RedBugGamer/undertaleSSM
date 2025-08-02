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
        """
        This Method creates a new `Run` object, which uses data from a `DataFileInterface` object
        Args:
            dataFileInterface (DataFileInterface): a `DataFileInterface` object
            data (dict): A dict containing raw data as a dict. missing keys will be set to default values
        """
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
        """
        The initializer for the `Run` class
        Args:
            dataFileInterface (DataFileInterface):
            description (str):
            uuid (str):
            latestSaveUUID (str | None):
            startSaveUUID (str | None):
            raw_saves (types.SavesList):
        """
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
        """
            An instance of the DataFileInterface associated with this object.
        Returns:
            DataFileInterface
        """
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
        """
        This method serializes this object and all connected `Saves` into a dict
        Returns:
            A dict containing all data
        """
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
        """
        This method lists all `Save` objects
        Returns:
            All connected `Save` objects
        """
        return [save for _, save in self.saves.items()]

    def getSaveByUUID(self, uuid: str) -> Save | None:
        """
        This method allows access to registered saves
        Args:
            uuid (str): The uuid of the wanted `Save` object
        Returns:
            The wanted `Save` object or `None` if a save with this uuid does not exist
        """
        return self.saves.get(uuid)

    @property
    def latestSave(self) -> Save | None:
        if self.latestSaveUUID is None:
            return
        return self.getSaveByUUID(self.latestSaveUUID)

    @autosave
    def travelToSave(self, save: Save):
        """
        This method allows jumping to a previous save. This does **NOT** load the save. If you want to load a `Save` object, use `save.pushDirectory()`
        Args:
            save (Save): The save to jump to
        """
        self.latestSaveUUID = save.uuid

    @autosave
    def appendSave(self, save: Save):
        """
        This method registers a `Save` object to this `Run` object
        Args:
            save (Save): The save to register
        """
        self.saves[save.uuid] = save

    def createSave(self,force:bool = False) -> Save | None:
        """
        This method creates a new `Save` object, and integrates it fully into the data structure.
        Args:
            force (bool): Wether to skip comparison to previous save
        Returns:
            The newly created `Save` object or `None` if save was skipped
        """
        if not force and self.latestSave and self.latestSave.getReader()==self.getDataFileInterface().getReader():
            return None
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
    def removeSave(self, save: Save):
        """
        This method deletes a `Save` object and removes it compleatly from the datastructure
        Args:
            save (Save): The `Save` object, which should be deleted
        """
        save.removeStitches()
        save.rmDir()
        self.saves.pop(save.uuid)
