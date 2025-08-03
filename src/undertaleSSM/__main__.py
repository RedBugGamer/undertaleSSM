"""
This allows usage of undertaleSSM via cli
Example:
    >>> python -m undertaleSSM --help
"""

import threading
from typing import Any
import typer
from PySide6.QtCore import QCoreApplication
import sys
from .fileInterface.run import Run
from .fileInterface.save import Save
from .fileInterface.saveStateManager import SaveStateManager
from .fileInterface.undertaleReader.rooms import Rooms


app = typer.Typer()


@app.command()
def record(file: str, run: str | None = None, info: bool = typer.Option(False, "--info", "-i", is_flag=True)):
    """Starts recording of save files with the options from a data.json file"""
    ssm = SaveStateManager(file)
    ssm.autosave = True
    run_obj = None
    if run:
        typer.echo("Trying to select run "+run)
        run_obj = ssm.getRunByUUID(run)
    if not run_obj:
        run_obj = ssm.createRun()
        typer.echo("Creating new run with uuid "+run_obj.uuid)

    ssm.activeRun = run_obj

    def on_autosave(save: Save):
        typer.echo(f"[{save.timestamp}] Saved save with uuid {save.uuid}")
        if info:
            reader = save.getReader()
            file0 = reader.file0
            if file0:
                attrs:dict[str,Any] = {
                    "room":file0.room
                }
                if Rooms.isRuins(file0.room):
                    attrs["area"] = "ruins"
                    attrs["gonocide_done"] = file0.genocide_ruins
                    attrs["kills"] = file0.kills_ruins
                elif Rooms.isTundra(file0.room):
                    attrs["area"] = "tundra"
                    attrs["gonocide_done"] = file0.genocide_tundra
                    attrs["kills"] = file0.kills_tundra
                elif Rooms.isWaterfall(file0.room):
                    attrs["area"] = "waterfall"
                    attrs["gonocide_done"] = file0.genocide_water
                    attrs["kills"] = file0.kills_water
                elif Rooms.isHotland(file0.room):
                    attrs["area"] = "Hotland"
                    attrs["gonocide_done"] = file0.genocide_hotland
                    attrs["kills"] = file0.kills_hotland
                for lbl,attr in attrs.items():
                    typer.echo(f"   {lbl}:{attr}")
    ssm.signals.auto_saved.connect(on_autosave)

    typer.confirm(
        "You set the info flag. This might spoil some things. Do you want to proceed anyway?", abort=True)

    typer.echo("Starting recording session")
    ssm.startObserver()

    qapp = QCoreApplication(sys.argv)

    def runrecorder():
        try:
            input()
        finally:
            typer.echo("Stopping")
            qapp.quit()
            ssm.stopObserver()

    typer.echo("Press ENTER to stop recording session...")
    threading.Thread(target=runrecorder, daemon=True).start()
    qapp.exec()


@app.command()
def list(file: str, saves: bool = typer.Option(False, "--saves", "-s", is_flag=True), run: str | None = None):
    """Lists all runs"""
    ssm = SaveStateManager(file)
    if run:
        run_obj = ssm.getRunByUUID(run)
        if run_obj:
            listRun(saves, run_obj)
        else:
            typer.echo("Run with the given uuid does not exist")
        return
    for run_obj in ssm.getRuns():
        listRun(saves, run_obj)


def listRun(saves: bool, run: Run):
    typer.echo("Run "+run.uuid)
    if saves:
        for save in run.getSaves():
            typer.echo("  Save "+save.uuid+" saved at "+str(save.timestamp))


@app.command()
def load(file: str, run: str, save: str):
    """Loads a given save"""
    ssm = SaveStateManager(file)
    ssm.autosave = True
    if run:
        run_obj = ssm.getRunByUUID(run)
        if run_obj:
            save_obj = run_obj.getSaveByUUID(save)
            if save_obj:
                save_obj.pushDirectory()
                file0 = save_obj.getReader().file0
                if file0:
                    room = file0.room
                    typer.echo(
                        "Succesfully loaded. you are now in room "+str(room))
                else:
                    typer.echo("Succesfully loaded")
            else:
                typer.echo("Save with the given uuid does not exist")
        else:
            typer.echo("Run with the given uuid does not exist")
        return
    ssm.save()


if __name__ == "__main__":
    app()
