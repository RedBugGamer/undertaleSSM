from __future__ import annotations
from .cellphone import Cellphone
from .items import Items
from .rooms import Rooms


class UndertaleFile:
    def __init__(self, path: str) -> None:
        self.raw_data: list[str] = []
        with open(path, "r") as f:
            for line in f.readlines():
                self.raw_data.append(line.strip("\n"))
        self._parse()

    def getLineStr(self, index: int) -> str:
        return self.raw_data[index-1]

    def getLineInt(self, index: int) -> int:
        return int(self.getLineStr(index))

    def _parse(self):
        """
        Thanks to https://github.com/crumblingstatue/FloweysTimeMachine/blob/gh-pages/research/savefile.md for the research!
        """
        self.character_name: str = self.getLineStr(1)
        self.lv: int = self.getLineInt(2)
        self.hp: int = self.getLineInt(3)
        self.at: int = self.getLineInt(5)
        self.weapon_at: int = self.getLineInt(6)
        self.df: int = self.getLineInt(7)
        self.armor_df: int = self.getLineInt(8)
        self.exp: int = self.getLineInt(10)
        self.gold: int = self.getLineInt(11)
        self.kills: int = self.getLineInt(12)
        self.inventory_slot_1: Items = Items(self.getLineInt(13))
        self.cellphone_talk_option_1: Cellphone = Cellphone(
            self.getLineInt(14))
        self.inventory_slot_2: Items = Items(self.getLineInt(15))
        self.cellphone_talk_option_2: Cellphone = Cellphone(
            self.getLineInt(16))
        self.inventory_slot_3: Items = Items(self.getLineInt(17))
        self.cellphone_talk_option_3: Cellphone = Cellphone(
            self.getLineInt(18))
        self.inventory_slot_4: Items = Items(self.getLineInt(19))
        self.cellphone_talk_option_4: Cellphone = Cellphone(
            self.getLineInt(20))
        self.inventory_slot_5: Items = Items(self.getLineInt(21))
        self.cellphone_talk_option_5: Cellphone = Cellphone(
            self.getLineInt(22))
        self.inventory_slot_6: Items = Items(self.getLineInt(23))
        self.cellphone_talk_option_6: Cellphone = Cellphone(
            self.getLineInt(24))
        self.inventory_slot_7: Items = Items(self.getLineInt(25))
        self.cellphone_talk_option_7: Cellphone = Cellphone(
            self.getLineInt(26))
        self.inventory_slot_8: Items = Items(self.getLineInt(27))
        self.cellphone_talk_option_8: Cellphone = Cellphone(
            self.getLineInt(28))
        self.weapon: int = self.getLineInt(29)
        self.armor: int = self.getLineInt(30)
        self.hotland_genocide_0_1_mettaton: int = self.getLineInt(39)
        self.talked_to_training_dummy: int = self.getLineInt(41)
        self.toriel_house_snowdin: int = self.getLineInt(42)
        self.killed_training_dummy_froggit: int = self.getLineInt(43)
        self.killed_training_dummy_talked: int = self.getLineInt(45)
        self.hotland_genocide_1_0: int = self.getLineInt(46)
        self.core_genocide_0_1: int = self.getLineInt(47)
        self.waterfall_genocide_0_1_3: int = self.getLineInt(51)
        self.toriel_house_0_1: int = self.getLineInt(55)
        self.save_count: int = self.getLineInt(56)
        self.met_first_froggit: int = self.getLineInt(61)
        self.candies_taken: int = self.getLineInt(65)
        self.toriel_house_0_3_3_4: int = self.getLineInt(76)
        self.snowdin_genocide_no_moving_dog: int = self.getLineInt(83)
        self.snowdin_genocide_dog_guards: int = self.getLineInt(84)
        self.snowdin_genocide_greater_dog: int = self.getLineInt(85)
        self.comedian_got_away: int = self.getLineInt(88)
        self.snowdin_genocide_0_1_a: int = self.getLineInt(93)
        self.snowdin_genocide_0_1_b: int = self.getLineInt(95)
        self.snowdin_genocide_papyrus: int = self.getLineInt(98)
        self.snowdin_genocide_0_1_c: int = self.getLineInt(99)
        self.snowdin_genocide_0_1_d: int = self.getLineInt(101)
        self.papyrus_friendship_progress: int = self.getLineInt(119)
        self.waterfall_genocide_shyren: int = self.getLineInt(112)
        self.waterfall_genocide_0_2: int = self.getLineInt(121)
        self.waterfall_genocide_0_10: int = self.getLineInt(122)
        self.second_save_point: int = self.getLineInt(231)
        self.kills_unknown: int = self.getLineInt(232)
        self.ruins_kills: int = self.getLineInt(233)
        self.snowdin_kills: int = self.getLineInt(234)
        self.waterfall_kills: int = self.getLineInt(235)
        self.hotland_kills: int = self.getLineInt(236)
        self.nobody_came: int = self.getLineInt(252)
        self.nobody_came_snowdin: int = self.getLineInt(253)
        self.waterfall_genocide_undyne_1: int = self.getLineInt(282)
        self.waterfall_genocide_mad_dummy: int = self.getLineInt(283)
        self.waterfall_genocide_before_cave_bridge: int = self.getLineInt(301)
        self.throne_room_genocide_sans: int = self.getLineInt(302)
        self.snowdin_genocide_0_4: int = self.getLineInt(284)
        self.waterfall_genocide_undyne_2: int = self.getLineInt(381)
        self.waterfall_genocide_0_1_e: int = self.getLineInt(385)
        self.waterfall_genocide_0_1_f: int = self.getLineInt(387)
        self.waterfall_genocide_4_6: int = self.getLineInt(388)
        self.waterfall_genocide_0_8: int = self.getLineInt(389)
        self.waterfall_genocide_0_1_0: int = self.getLineInt(391)
        self.waterfall_genocide_0_0_08_0: int = self.getLineInt(392)
        self.waterfall_genocide_0_0_5: int = self.getLineInt(393)
        self.waterfall_genocide_0_272_neg1: int = self.getLineInt(394)
        self.waterfall_genocide_273_neg1: int = self.getLineInt(395)
        self.hotland_genocide_0_10: int = self.getLineInt(413)
        self.hotland_genocide_0_6: int = self.getLineInt(427)
        self.hotland_genocide_0_1_muffet: int = self.getLineInt(428)
        self.hotland_genocide_0_4_no_kills: int = self.getLineInt(429)
        self.hotland_genocide_0_1_bro_guards: int = self.getLineInt(433)
        self.hotland_genocide_3_4: int = self.getLineInt(439)
        self.hotland_genocide_0_1_mettaton_b: int = self.getLineInt(456)
        self.hotland_genocide_0_1_after_mettaton: int = self.getLineInt(462)
        self.hotland_genocide_0_1_after_mettaton_b: int = self.getLineInt(463)
        self.hotland_genocide_0_17_flowey_dialogue: int = self.getLineInt(481)
        self.hotland_genocide_0_1_g: int = self.getLineInt(483)
        self.hotland_genocide_0_1_h: int = self.getLineInt(484)
        self.hotland_genocide_0_1_i: int = self.getLineInt(485)
        self.hotland_genocide_0_2: int = self.getLineInt(486)
        self.hotland_genocide_0_1_j: int = self.getLineInt(487)
        self.toriel_intervene_asgore: int = self.getLineInt(524)
        self.waterfall_genocide_0_neg1: int = self.getLineInt(527)
        self.ruins_progress_marker: int = self.getLineInt(543)
        self.player_has_cellphone: int = self.getLineInt(546)
        self.nobody_came_waterfall_genocide: int = self.getLineInt(547)
        self.player_room: Rooms = Rooms(self.getLineInt(548))
        self.game_time: int = self.getLineInt(549)

    def compare_to(self, other: UndertaleFile) -> list[str]:
        attrs = [
            'character_name', 'lv', 'hp', 'at', 'weapon_at', 'df', 'armor_df', 'exp', 'gold', 'kills',
            'inventory_slot_1', 'cellphone_talk_option_1', 'inventory_slot_2', 'cellphone_talk_option_2',
            'inventory_slot_3', 'cellphone_talk_option_3', 'inventory_slot_4', 'cellphone_talk_option_4',
            'inventory_slot_5', 'cellphone_talk_option_5', 'inventory_slot_6', 'cellphone_talk_option_6',
            'inventory_slot_7', 'cellphone_talk_option_7', 'inventory_slot_8', 'cellphone_talk_option_8',
            'weapon', 'armor', 'hotland_genocide_0_1_mettaton', 'talked_to_training_dummy',
            'toriel_house_snowdin', 'killed_training_dummy_froggit', 'killed_training_dummy_talked',
            'hotland_genocide_1_0', 'core_genocide_0_1', 'waterfall_genocide_0_1_3', 'toriel_house_0_1',
            'save_count', 'met_first_froggit', 'candies_taken', 'toriel_house_0_3_3_4',
            'snowdin_genocide_no_moving_dog', 'snowdin_genocide_dog_guards', 'snowdin_genocide_greater_dog',
            'comedian_got_away', 'snowdin_genocide_0_1_a', 'snowdin_genocide_0_1_b',
            'snowdin_genocide_papyrus', 'snowdin_genocide_0_1_c', 'snowdin_genocide_0_1_d',
            'papyrus_friendship_progress', 'waterfall_genocide_shyren', 'waterfall_genocide_0_2',
            'waterfall_genocide_0_10', 'second_save_point', 'kills_unknown', 'ruins_kills',
            'snowdin_kills', 'waterfall_kills', 'hotland_kills', 'nobody_came', 'nobody_came_snowdin',
            'waterfall_genocide_undyne_1', 'waterfall_genocide_mad_dummy',
            'waterfall_genocide_before_cave_bridge', 'throne_room_genocide_sans', 'snowdin_genocide_0_4',
            'waterfall_genocide_undyne_2', 'waterfall_genocide_0_1_e', 'waterfall_genocide_0_1_f',
            'waterfall_genocide_4_6', 'waterfall_genocide_0_8', 'waterfall_genocide_0_1_0',
            'waterfall_genocide_0_0_08_0', 'waterfall_genocide_0_0_5', 'waterfall_genocide_0_272_neg1',
            'waterfall_genocide_273_neg1', 'hotland_genocide_0_10', 'hotland_genocide_0_6',
            'hotland_genocide_0_1_muffet', 'hotland_genocide_0_4_no_kills',
            'hotland_genocide_0_1_bro_guards', 'hotland_genocide_3_4',
            'hotland_genocide_0_1_mettaton_b', 'hotland_genocide_0_1_after_mettaton',
            'hotland_genocide_0_1_after_mettaton_b', 'hotland_genocide_0_17_flowey_dialogue',
            'hotland_genocide_0_1_g', 'hotland_genocide_0_1_h', 'hotland_genocide_0_1_i',
            'hotland_genocide_0_2', 'hotland_genocide_0_1_j', 'toriel_intervene_asgore',
            'waterfall_genocide_0_neg1', 'ruins_progress_marker', 'player_has_cellphone',
            'nobody_came_waterfall_genocide', 'player_room', 'game_time'
        ]
        diffs: list[str] = []
        for attr in attrs:
            if not hasattr(self, attr) or not hasattr(other, attr):
                continue
            if getattr(self, attr) != getattr(other, attr):
                diffs.append(attr)
        return diffs
