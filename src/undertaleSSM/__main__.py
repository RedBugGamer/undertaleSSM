import typer

from .fileInterface.run import Run
from .fileInterface.saveStateManager import SaveStateManager


app = typer.Typer()


@app.command()
def record(file: str, run: str | None = None):
    """Starts recording of save files with the options from a data.json file"""
    ssm = SaveStateManager(file)
    try:
        ssm.autosave = True
        run_obj = None
        if run:
            typer.echo("Trying to select run "+run)
            run_obj = ssm.getRunByUUID(run)
        if not run_obj:
            run_obj = ssm.createRun()
            typer.echo("Creating new run with uuid "+run_obj.uuid)
            
        ssm.currentRun = run_obj
        typer.echo("Starting recording session")
        ssm.startObserver()
        typer.pause("Press any key to stop recording session...")
    finally:
        typer.echo("Stopping")
        ssm.stopObserver()


@app.command()
def list(file:str, saves:bool = typer.Option(False,"--saves","-s",is_flag=True),run:str|None = None):
    """Lists all runs"""
    ssm = SaveStateManager(file)
    if run:
        run_obj = ssm.getRunByUUID(run)
        if run_obj:
            listRun(saves,run_obj)
        else:
            typer.echo("Run with the given uuid does not exist")
        return
    for run_obj in ssm.getRuns():
        listRun(saves, run_obj)

def listRun(saves:bool, run:Run):
    typer.echo("Run "+run.uuid)
    if saves:
        for save in run.getSaves():
            typer.echo("  Save "+save.uuid+" saved at "+str(save.timestamp))


if __name__ == "__main__":
    app()
