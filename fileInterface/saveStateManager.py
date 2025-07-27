from threading import Timer
from typing import Callable
from watchdog.observers.api import BaseObserver
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from .dataFileInterface import DataFileInterface


class DirectoryEventHandler(FileSystemEventHandler):
    FILE_DELAY = 0.1

    def __init__(self, callback: Callable[[], None]) -> None:
        super().__init__()
        self.callback = callback
        self.timer: Timer | None = None

    def timerRunOutCallback(self):
        self.timer = None
        self.callback()
        
    def on_any_event(self, event: FileSystemEvent) -> None:
        if self.timer is None:
            self.timer = Timer(self.FILE_DELAY, self.timerRunOutCallback)
            self.timer.start()


class SaveStateManager(DataFileInterface):
    def __init__(self, data_file: str) -> None:
        super().__init__(data_file)
        self.observer: BaseObserver | None = None

    def _observerCallback(self):
        if self.activeRun:
            self.activeRun.createSave()

    def startObserver(self):
        if self.observer is None:
            self.observer = Observer()
            self.observer.schedule(DirectoryEventHandler(
                self._observerCallback), self.undertale_data_path)
            self.observer.start()

    def stopObserver(self):
        if self.observer is None:
            return
        self.observer.stop()
        self.observer = None
