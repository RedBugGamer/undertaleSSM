from PySide6.QtCore import QSettings


class UndertaleIni:
    def __init__(self, path: str) -> None:
        self.file: QSettings = QSettings(
            path, QSettings.Format.IniFormat)
        self._parse()

    def getAsStr(self, key: str) -> str:
        return self.file.value(key)

    def getAsInt(self, key: str) -> int:
        return int(float(self.getAsStr(key)))

    def _parse(self):
        self.asgoreKillYou: int = self.getAsInt("Asgore/KillYou")
        self.mttEssayNo: int = self.getAsInt("MTT/EssayNo")
        self.mettO: int = self.getAsInt("Mett/O")
        self.sansMeetLv1: int = self.getAsInt("Sans/MeetLv1")
        self.sansMeetLv2: int = self.getAsInt("Sans/MeetLv2")
        self.sansM1: int = self.getAsInt("Sans/M1")
        self.sansEndMet: int = self.getAsInt("Sans/EndMet")
        self.floweyK: int = self.getAsInt("Flowey/K")
        self.floweyMet1: int = self.getAsInt("Flowey/Met1")
        self.floweySK: int = self.getAsInt("Flowey/SK")
        self.generalWon: int = self.getAsInt("Won")
        self.generalBC: int = self.getAsInt("BC")
        self.generalFun: int = self.getAsInt("fun")
        self.generalName: str = self.getAsStr("Name")
        self.generalLove: int = self.getAsInt("Love")
        self.generalTime: int = self.getAsInt("Time")
        self.generalKills: int = self.getAsInt("Kills")
        self.generalRoom: int = self.getAsInt("Room")
        self.generalGameover: int = self.getAsInt("Gameover")
        self.generalTale: int = self.getAsInt("Tale")
        self.torielTS: int = self.getAsInt("Toriel/TS")
        self.torielTK: int = self.getAsInt("Toriel/TK")
        self.torielBscotch: int = self.getAsInt("Toriel/Bscotch")
        self.papyrusPD: int = self.getAsInt("Papyrus/PD")
        self.papyrusPK: int = self.getAsInt("Papyrus/PK")
        self.papyrusPS: int = self.getAsInt("Papyrus/PS")
        self.papyrusM1: int = self.getAsInt("Papyrus/M1")
        self.mettatonBossMet: int = self.getAsInt("Mettaton/BossMet")
        self.fffffP: int = self.getAsInt("FFFFF/P")
        self.fffffF: int = self.getAsInt("FFFFF/F")
        self.fffffD: int = self.getAsInt("FFFFF/D")
        self.fffffE: int = self.getAsInt("FFFFF/E")
