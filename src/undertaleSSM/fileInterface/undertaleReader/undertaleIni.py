from PySide6.QtCore import QSettings

from .flags import IniFlags
from .rooms import Rooms


class UndertaleIni:
    def __init__(self, path: str) -> None:
        self.file: QSettings = QSettings(
            path, QSettings.Format.IniFormat)
        self._parse()

    def getAsStr(self, key: IniFlags) -> str | None:
        return self.file.value(key.value)

    def getAsInt(self, key: IniFlags) -> int|None:
        as_str = self.getAsStr(key)
        if as_str:
            return int(float(as_str))
        return
    def getAsRoom(self, key: IniFlags) -> Rooms|None:
        as_int = self.getAsInt(key)
        if as_int:
            return Rooms(as_int)
        return

    def _parse(self):
        self.general_name = self.getAsStr(IniFlags.GENERAL_NAME)
        self.general_time = self.getAsInt(IniFlags.GENERAL_TIME)
        self.general_room = self.getAsRoom(IniFlags.GENERAL_ROOM)
        self.general_gameover = self.getAsInt(IniFlags.GENERAL_GAMEOVER)
        self.general_kills = self.getAsInt(IniFlags.GENERAL_KILLS)
        self.general_love = self.getAsInt(IniFlags.GENERAL_LOVE)
        self.general_fun = self.getAsInt(IniFlags.GENERAL_FUN)
        self.general_capital_fun = self.getAsInt(IniFlags.GENERAL_CAPITAL_FUN)
        self.general_tale = self.getAsInt(IniFlags.GENERAL_TALE)
        self.general_won = self.getAsInt(IniFlags.GENERAL_WON)
        self.general_bw = self.getAsInt(IniFlags.GENERAL_BW)
        self.general_bc = self.getAsInt(IniFlags.GENERAL_BC)
        self.general_cp = self.getAsInt(IniFlags.GENERAL_CP)
        self.general_bp = self.getAsInt(IniFlags.GENERAL_BP)
        self.general_ch = self.getAsInt(IniFlags.GENERAL_CH)
        self.general_bh = self.getAsInt(IniFlags.GENERAL_BH)
        self.reset_reset = self.getAsInt(IniFlags.RESET_RESET)
        self.reset_s_key = self.getAsInt(IniFlags.RESET_S_KEY)
        self.flowey_met1 = self.getAsInt(IniFlags.FLOWEY_MET1)
        self.flowey_k = self.getAsInt(IniFlags.FLOWEY_K)
        self.flowey_nk = self.getAsInt(IniFlags.FLOWEY_NK)
        self.flowey_ik = self.getAsInt(IniFlags.FLOWEY_IK)
        self.flowey_sk = self.getAsInt(IniFlags.FLOWEY_SK)
        self.flowey_floweyexplain1 = self.getAsInt(IniFlags.FLOWEY_FLOWEYEXPLAIN1)
        self.flowey_ex = self.getAsInt(IniFlags.FLOWEY_EX)
        self.flowey_change = self.getAsInt(IniFlags.FLOWEY_CHANGE)
        self.flowey_ak = self.getAsInt(IniFlags.FLOWEY_AK)
        self.flowey_af = self.getAsInt(IniFlags.FLOWEY_AF)
        self.flowey_alter = self.getAsInt(IniFlags.FLOWEY_ALTER)
        self.flowey_alter2 = self.getAsInt(IniFlags.FLOWEY_ALTER2)
        self.flowey_truename = self.getAsInt(IniFlags.FLOWEY_TRUENAME)
        self.flowey_specialk = self.getAsInt(IniFlags.FLOWEY_SPECIALK)
        self.toriel_bscotch = self.getAsInt(IniFlags.TORIEL_BSCOTCH)
        self.toriel_ts = self.getAsInt(IniFlags.TORIEL_TS)
        self.toriel_tk = self.getAsInt(IniFlags.TORIEL_TK)
        self.sans_m1 = self.getAsInt(IniFlags.SANS_M1)
        self.sans_endmet = self.getAsInt(IniFlags.SANS_ENDMET)
        self.sans_meetlv1 = self.getAsInt(IniFlags.SANS_MEETLV1)
        self.sans_meetlv2 = self.getAsInt(IniFlags.SANS_MEETLV2)
        self.sans_meetlv = self.getAsInt(IniFlags.SANS_MEETLV)
        self.sans_pass = self.getAsInt(IniFlags.SANS_PASS)
        self.sans_intro = self.getAsInt(IniFlags.SANS_INTRO)
        self.sans_f = self.getAsInt(IniFlags.SANS_F)
        self.sans_mp = self.getAsInt(IniFlags.SANS_MP)
        self.sans_sk = self.getAsInt(IniFlags.SANS_SK)
        self.sans_ss = self.getAsInt(IniFlags.SANS_SS)
        self.sans_ss2 = self.getAsInt(IniFlags.SANS_SS2)
        self.papyrus_m1 = self.getAsInt(IniFlags.PAPYRUS_M1)
        self.papyrus_ps = self.getAsInt(IniFlags.PAPYRUS_PS)
        self.papyrus_pd = self.getAsInt(IniFlags.PAPYRUS_PD)
        self.papyrus_pk = self.getAsInt(IniFlags.PAPYRUS_PK)
        self.fffff_f = self.getAsInt(IniFlags.FFFFF_F)
        self.fffff_d = self.getAsInt(IniFlags.FFFFF_D)
        self.fffff_p = self.getAsInt(IniFlags.FFFFF_P)
        self.fffff_e = self.getAsInt(IniFlags.FFFFF_E)
        self.undyne_ud = self.getAsInt(IniFlags.UNDYNE_UD)
        self.mettaton_bossmet = self.getAsInt(IniFlags.METTATON_BOSSMET)
        self.mett_o = self.getAsInt(IniFlags.METT_O)
        self.mtt_essayno = self.getAsInt(IniFlags.MTT_ESSAYNO)
        self.asgore_killyou = self.getAsInt(IniFlags.ASGORE_KILLYOU)
        self.alphys_ad = self.getAsInt(IniFlags.ALPHYS_AD)
        self.f7_f7 = self.getAsInt(IniFlags.F7_F7)
        self.endf_endf = self.getAsInt(IniFlags.ENDF_ENDF)
