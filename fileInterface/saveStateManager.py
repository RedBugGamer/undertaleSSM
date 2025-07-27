from watchdog.observers.api import BaseObserver
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from .dataFileInterface import DataFileInterface

class DirectoryEventHandler(FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()
    def on_any_event(self, event: FileSystemEvent) -> None:
        print(event)

class SaveStateManager(DataFileInterface):
    def __init__(self, data_file: str) -> None:
        super().__init__(data_file)
        self.observer: BaseObserver | None = None

    def startObserver(self): # TODO
        if self.observer is None:
            self.observer = Observer()
            
