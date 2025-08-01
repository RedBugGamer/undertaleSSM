from threading import Timer
from typing import Callable
from watchdog.observers.api import BaseObserver
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler, EVENT_TYPE_DELETED
from .save import Save
from .dataFileInterface import DataFileInterface
from PySide6.QtCore import QObject, Signal

class AutoSaveSignalEmitter(QObject):
    auto_saved = Signal(Save)

class DirectoryEventHandler(FileSystemEventHandler):
    FILE_DELAY = 0.1

    def __init__(self, callback: Callable[[], None], restartCallback: Callable[[], None]) -> None:
        super().__init__()
        self.callback = callback
        self.restartCallback = restartCallback
        self.timer: Timer | None = None

    def timerRunOutCallback(self):
        self.timer = None
        self.callback()

    def on_any_event(self, event: FileSystemEvent) -> None:
        if event.event_type == EVENT_TYPE_DELETED and event.is_directory:
            self.restartCallback()
        elif self.timer is None and not event.is_directory and event.event_type != EVENT_TYPE_DELETED:
            self.timer = Timer(self.FILE_DELAY, self.timerRunOutCallback)
            self.timer.start()


class SaveStateManager(DataFileInterface):
    def __init__(self, data_file: str) -> None:
        super().__init__(data_file)
        self.observer: BaseObserver | None = None
        self.signals = AutoSaveSignalEmitter()

    def _observerCallback(self):
        if self.activeRun:
            save = self.activeRun.createSave()
            self.signals.auto_saved.emit(save)

    def _observerRestartCallback(self):
        self.stopObserver()
        timer = Timer(DirectoryEventHandler.FILE_DELAY, self.startObserver)
        timer.daemon = True
        timer.start()

    def startObserver(self):
        if self.observer is None:
            self.observer = Observer()
            self.observer.daemon = True
            self.observer.schedule(DirectoryEventHandler(
                self._observerCallback, self._observerRestartCallback), self.undertale_data_path)
            self.observer.start()

    def stopObserver(self):
        if self.observer is None:
            return
        self.observer.stop()
        self.observer = None

    @property
    def observerRunning(self) -> bool:
        return self.observer is not None
