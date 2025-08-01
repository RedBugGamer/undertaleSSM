from __future__ import annotations

from .cellphone import Cellphone
from .items import Items
from .rooms import Rooms
from .flags import Flags


class UndertaleFile:
    def __init__(self, path: str) -> None:
        self.raw_data: list[str] = []
        with open(path, "r") as f:
            for line in f.readlines():
                self.raw_data.append(line.strip("\n").strip())
        self._parse()

    def getLineStr(self, flag: Flags) -> str:
        return self.raw_data[flag.value-1]

    def getLineInt(self, flag: Flags) -> int:
        return int(self.getLineStr(flag))

    def getLineFloat(self, flag: Flags) -> float:
        return float(self.getLineStr(flag))

    def getLineItem(self, flag: Flags) -> Items:
        return Items(self.getLineInt(flag))

    def getLineCell(self, flag: Flags) -> Cellphone:
        return Cellphone(self.getLineInt(flag))

    def getLineRoom(self, flag: Flags) -> Rooms:
        return Rooms(self.getLineInt(flag))

    def _parse(self):
        self.character_name = self.getLineStr(Flags.CHARACTER_NAME)
        self.love = self.getLineInt(Flags.LOVE)
        self.max_hp = self.getLineInt(Flags.MAX_HP)
        self.max_en = self.getLineInt(Flags.MAX_EN)
        self.attack_dmg = self.getLineInt(Flags.ATTACK_DMG)
        self.weapon_strength = self.getLineInt(Flags.WEAPON_STRENGTH)
        self.defense = self.getLineInt(Flags.DEFENSE)
        self.armor_defense = self.getLineInt(Flags.ARMOR_DEFENSE)
        self.sp = self.getLineInt(Flags.SP)
        self.exp = self.getLineInt(Flags.EXP)
        self.gold = self.getLineInt(Flags.GOLD)
        self.kills = self.getLineInt(Flags.KILLS)
        self.inventory_0 = self.getLineItem(Flags.INVENTORY_0)
        self.cell_0 = self.getLineCell(Flags.CELL_0)
        self.inventory_1 = self.getLineItem(Flags.INVENTORY_1)
        self.cell_1 = self.getLineCell(Flags.CELL_1)
        self.inventory_2 = self.getLineItem(Flags.INVENTORY_2)
        self.cell_2 = self.getLineCell(Flags.CELL_2)
        self.inventory_3 = self.getLineItem(Flags.INVENTORY_3)
        self.cell_3 = self.getLineCell(Flags.CELL_3)
        self.inventory_4 = self.getLineItem(Flags.INVENTORY_4)
        self.cell_4 = self.getLineCell(Flags.CELL_4)
        self.inventory_5 = self.getLineItem(Flags.INVENTORY_5)
        self.cell_5 = self.getLineCell(Flags.CELL_5)
        self.inventory_6 = self.getLineItem(Flags.INVENTORY_6)
        self.cell_6 = self.getLineCell(Flags.CELL_6)
        self.inventory_7 = self.getLineItem(Flags.INVENTORY_7)
        self.cell_7 = self.getLineCell(Flags.CELL_7)
        self.weapon_item = self.getLineInt(Flags.WEAPON_ITEM)
        self.armor_item = self.getLineInt(Flags.ARMOR_ITEM)
        self.undyne_trigger_override = self.getLineInt(
            Flags.UNDYNE_TRIGGER_OVERRIDE)
        self.fun = self.getLineInt(Flags.FUN)
        self.hardmode = self.getLineInt(Flags.HARDMODE)
        self.true_pacifist = self.getLineInt(Flags.TRUE_PACIFIST)
        self.disable_random_encounters = self.getLineInt(
            Flags.DISABLE_RANDOM_ENCOUNTERS)
        self.spared_last = self.getLineInt(Flags.SPARED_LAST)
        self.escaped_last = self.getLineInt(Flags.ESCAPED_LAST)
        self.killed_last = self.getLineInt(Flags.KILLED_LAST)
        self.bored_last = self.getLineInt(Flags.BORED_LAST)
        self.status_dummy = self.getLineInt(Flags.STATUS_DUMMY)
        self.in_battle = self.getLineInt(Flags.IN_BATTLE)
        self.type_heart_transition = self.getLineInt(
            Flags.TYPE_HEART_TRANSITION)
        self.animation_index = self.getLineInt(Flags.ANIMATION_INDEX)
        self.cooked_noodles = self.getLineInt(Flags.COOKED_NOODLES)
        self.name_color = self.getLineInt(Flags.NAME_COLOR)
        self.spared = self.getLineInt(Flags.SPARED)
        self.escaped = self.getLineInt(Flags.ESCAPED)
        self.dialogues_skipped = self.getLineInt(Flags.DIALOGUES_SKIPPED)
        self.murderlevel_override = self.getLineInt(Flags.MURDERLEVEL_OVERRIDE)
        self.spared_specific = self.getLineInt(Flags.SPARED_SPECIFIC)
        self.fast_text_skip = self.getLineInt(Flags.FAST_TEXT_SKIP)
        self.tutorial_froggit_encountered = self.getLineInt(
            Flags.TUTORIAL_FROGGIT_ENCOUNTERED)
        self.pushed_rock_1 = self.getLineInt(Flags.PUSHED_ROCK_1)
        self.pushed_rock_2 = self.getLineInt(Flags.PUSHED_ROCK_2)
        self.pushed_rock_3 = self.getLineInt(Flags.PUSHED_ROCK_3)
        self.candy_taken = self.getLineInt(Flags.CANDY_TAKEN)
        self.pushed_rock_4 = self.getLineInt(Flags.PUSHED_ROCK_4)
        self.spared_napstablook = self.getLineInt(Flags.SPARED_NAPSTABLOOK)
        self.waited_toriel = self.getLineInt(Flags.WAITED_TORIEL)
        self.greeted_toriel = self.getLineInt(Flags.GREETED_TORIEL)
        self.flirted_toriel = self.getLineInt(Flags.FLIRTED_TORIEL)
        self.call_mom_toriel = self.getLineInt(Flags.CALL_MOM_TORIEL)
        self.ruins_switches_pressed = self.getLineInt(
            Flags.RUINS_SWITCHES_PRESSED)
        self.disobeyed_toriel = self.getLineInt(Flags.DISOBEYED_TORIEL)
        self.status_toriel = self.getLineInt(Flags.STATUS_TORIEL)
        self.choice_flavor = self.getLineInt(Flags.CHOICE_FLAVOR)
        self.status_creepy_tundra = self.getLineInt(Flags.STATUS_CREEPY_TUNDRA)
        self.know_water_sausage = self.getLineInt(Flags.KNOW_WATER_SAUSAGE)
        self.wrong_switches_pressed = self.getLineInt(
            Flags.WRONG_SWITCHES_PRESSED)
        self.status_doggo = self.getLineInt(Flags.STATUS_DOGGO)
        self.status_dogcouple = self.getLineInt(Flags.STATUS_DOGCOUPLE)
        self.status_greaterdog = self.getLineInt(Flags.STATUS_GREATERDOG)
        self.status_lesserdog = self.getLineInt(Flags.STATUS_LESSERDOG)
        self.status_snowman = self.getLineInt(Flags.STATUS_SNOWMAN)
        self.status_snowdrake = self.getLineInt(Flags.STATUS_SNOWDRAKE)
        self.choice_harder_puzzle = self.getLineInt(Flags.CHOICE_HARDER_PUZZLE)
        self.spider_donations_total = self.getLineInt(
            Flags.SPIDER_DONATIONS_TOTAL)
        self.nicecream_donations_total = self.getLineInt(
            Flags.NICECREAM_DONATIONS_TOTAL)
        self.choice_ate_left_spaghetti = self.getLineInt(
            Flags.CHOICE_ATE_LEFT_SPAGHETTI)
        self.xoxo_resets = self.getLineInt(Flags.XOXO_RESETS)
        self.toggled_snow_switch = self.getLineInt(Flags.TOGGLED_SNOW_SWITCH)
        self.got_snowpoff_gold = self.getLineInt(Flags.GOT_SNOWPOFF_GOLD)
        self.flirted_papyrus_fight = self.getLineInt(
            Flags.FLIRTED_PAPYRUS_FIGHT)
        self.status_papyrus = self.getLineInt(Flags.STATUS_PAPYRUS)
        self.fought_papyrus = self.getLineInt(Flags.FOUGHT_PAPYRUS)
        self.bpants_alt_dialogue = self.getLineInt(Flags.BPANTS_ALT_DIALOGUE)
        self.progress_tundra_battles = self.getLineInt(
            Flags.PROGRESS_TUNDRA_BATTLES)
        self.status_inn = self.getLineInt(Flags.STATUS_INN)
        self.stayed_inn = self.getLineInt(Flags.STAYED_INN)
        self.betrayed_gyftrot = self.getLineInt(Flags.BETRAYED_GYFTROT)
        self.armor_papyrus_inquiry = self.getLineInt(
            Flags.ARMOR_PAPYRUS_INQUIRY)
        self.choice_papyrus_inquiry = self.getLineInt(
            Flags.CHOICE_PAPYRUS_INQUIRY)
        self.armor_undyne_saw = self.getLineInt(Flags.ARMOR_UNDYNE_SAW)
        self.strong_tough_glove = self.getLineInt(Flags.STRONG_TOUGH_GLOVE)
        self.nicecream_business = self.getLineInt(Flags.NICECREAM_BUSINESS)
        self.punchcards_bought = self.getLineInt(Flags.PUNCHCARDS_BOUGHT)
        self.status_shyren = self.getLineInt(Flags.STATUS_SHYREN)
        self.papyrus_sink_event_occurred = self.getLineInt(
            Flags.PAPYRUS_SINK_EVENT_OCCURRED)
        self.got_couch_gold = self.getLineInt(Flags.GOT_COUCH_GOLD)
        self.have_umbrella = self.getLineInt(Flags.HAVE_UMBRELLA)
        self.music_statue_on = self.getLineInt(Flags.MUSIC_STATUE_ON)
        self.dated_papyrus = self.getLineInt(Flags.DATED_PAPYRUS)
        self.dated_sans1 = self.getLineInt(Flags.DATED_SANS1)
        self.choice_mkid_umbrella = self.getLineInt(Flags.CHOICE_MKID_UMBRELLA)
        self.interacted_garbage_savepoint = self.getLineInt(
            Flags.INTERACTED_GARBAGE_SAVEPOINT)
        self.status_stable = self.getLineInt(Flags.STATUS_STABLE)
        self.talked_napstablook = self.getLineInt(Flags.TALKED_NAPSTABLOOK)
        self.current_napstablook_song = self.getLineInt(
            Flags.CURRENT_NAPSTABLOOK_SONG)
        self.aaron_woshua_event = self.getLineInt(Flags.AARON_WOSHUA_EVENT)
        self.conversation_emblem = self.getLineInt(Flags.CONVERSATION_EMBLEM)
        self.creepy_friend_seen = self.getLineInt(Flags.CREEPY_FRIEND_SEEN)
        self.saved_mkid = self.getLineInt(Flags.SAVED_MKID)
        self.undyne_difficulty = self.getLineInt(Flags.UNDYNE_DIFFICULTY)
        self.got_ribbon = self.getLineInt(Flags.GOT_RIBBON)
        self.got_toyknife = self.getLineInt(Flags.GOT_TOYKNIFE)
        self.got_bscotch_pie = self.getLineInt(Flags.GOT_BSCOTCH_PIE)
        self.got_quiche = self.getLineInt(Flags.GOT_QUICHE)
        self.got_tutu = self.getLineInt(Flags.GOT_TUTU)
        self.got_ballet_shoes = self.getLineInt(Flags.GOT_BALLET_SHOES)
        self.got_artifact = self.getLineInt(Flags.GOT_ARTIFACT)
        self.got_spacefood = self.getLineInt(Flags.GOT_SPACEFOOD)
        self.got_instant_noodles = self.getLineInt(Flags.GOT_INSTANT_NOODLES)
        self.got_frying_pan = self.getLineInt(Flags.GOT_FRYING_PAN)
        self.got_apron = self.getLineInt(Flags.GOT_APRON)
        self.got_glamburger_trashcan = self.getLineInt(
            Flags.GOT_GLAMBURGER_TRASHCAN)
        self.got_gold_trashcan = self.getLineInt(Flags.GOT_GOLD_TRASHCAN)
        self.got_dagger = self.getLineInt(Flags.GOT_DAGGER)
        self.got_locket = self.getLineInt(Flags.GOT_LOCKET)
        self.spared_froggit = self.getLineInt(Flags.SPARED_FROGGIT)
        self.spared_whimsun = self.getLineInt(Flags.SPARED_WHIMSUN)
        self.spared_moldsmal = self.getLineInt(Flags.SPARED_MOLDSMAL)
        self.spared_loox = self.getLineInt(Flags.SPARED_LOOX)
        self.spared_vegetoid = self.getLineInt(Flags.SPARED_VEGETOID)
        self.spared_migosp = self.getLineInt(Flags.SPARED_MIGOSP)
        self.spared_snowdrake = self.getLineInt(Flags.SPARED_SNOWDRAKE)
        self.spared_icecap = self.getLineInt(Flags.SPARED_ICECAP)
        self.spared_gyftrot = self.getLineInt(Flags.SPARED_GYFTROT)
        self.spared_doggo = self.getLineInt(Flags.SPARED_DOGGO)
        self.spared_lesserdog = self.getLineInt(Flags.SPARED_LESSERDOG)
        self.spared_greatdog = self.getLineInt(Flags.SPARED_GREATDOG)
        self.spared_aaron = self.getLineInt(Flags.SPARED_AARON)
        self.spared_moldsmalx = self.getLineInt(Flags.SPARED_MOLDSMALX)
        self.spared_woshua = self.getLineInt(Flags.SPARED_WOSHUA)
        self.spared_temmie = self.getLineInt(Flags.SPARED_TEMMIE)
        self.spared_maddummy = self.getLineInt(Flags.SPARED_MADDUMMY)
        self.spared_vulkin = self.getLineInt(Flags.SPARED_VULKIN)
        self.spared_tsunderplane = self.getLineInt(Flags.SPARED_TSUNDERPLANE)
        self.spared_pyrope = self.getLineInt(Flags.SPARED_PYROPE)
        self.spared_finalfroggit = self.getLineInt(Flags.SPARED_FINALFROGGIT)
        self.spared_whimsalot = self.getLineInt(Flags.SPARED_WHIMSALOT)
        self.spared_astigmatism = self.getLineInt(Flags.SPARED_ASTIGMATISM)
        self.spared_madjick = self.getLineInt(Flags.SPARED_MADJICK)
        self.spared_finalknight = self.getLineInt(Flags.SPARED_FINALKNIGHT)
        self.spared_endogeny = self.getLineInt(Flags.SPARED_ENDOGENY)
        self.conversation_toriel_pacifist = self.getLineInt(
            Flags.CONVERSATION_TORIEL_PACIFIST)
        self.conversation_sans_pacifist = self.getLineInt(
            Flags.CONVERSATION_SANS_PACIFIST)
        self.conversation_undyne_pacifist = self.getLineInt(
            Flags.CONVERSATION_UNDYNE_PACIFIST)
        self.unlock_napsta_pacifist = self.getLineInt(
            Flags.UNLOCK_NAPSTA_PACIFIST)
        self.conversation_papyrus_pacifist = self.getLineInt(
            Flags.CONVERSATION_PAPYRUS_PACIFIST)
        self.conversation_alphys_pacifist = self.getLineInt(
            Flags.CONVERSATION_ALPHYS_PACIFIST)
        self.conversation_asgore_pacifist = self.getLineInt(
            Flags.CONVERSATION_ASGORE_PACIFIST)
        self.conversation_mettaton_pacifist = self.getLineInt(
            Flags.CONVERSATION_METTATON_PACIFIST)
        self.conversation_napstablook_pacifist = self.getLineInt(
            Flags.CONVERSATION_NAPSTABLOOK_PACIFIST)
        self.kills_area_pointer = self.getLineInt(Flags.KILLS_AREA_POINTER)
        self.kills_other = self.getLineInt(Flags.KILLS_OTHER)
        self.kills_ruins = self.getLineInt(Flags.KILLS_RUINS)
        self.kills_tundra = self.getLineInt(Flags.KILLS_TUNDRA)
        self.kills_water = self.getLineInt(Flags.KILLS_WATER)
        self.kills_hotland = self.getLineInt(Flags.KILLS_HOTLAND)
        self.genocide_ruins = self.getLineInt(Flags.GENOCIDE_RUINS)
        self.genocide_tundra = self.getLineInt(Flags.GENOCIDE_TUNDRA)
        self.genocide_water = self.getLineInt(Flags.GENOCIDE_WATER)
        self.genocide_hotland = self.getLineInt(Flags.GENOCIDE_HOTLAND)
        self.genocide_core = self.getLineInt(Flags.GENOCIDE_CORE)
        self.nicecream_business2 = self.getLineInt(Flags.NICECREAM_BUSINESS2)
        self.killed_undyne_ex = self.getLineInt(Flags.KILLED_UNDYNE_EX)
        self.killed_glad_dummy = self.getLineInt(Flags.KILLED_GLAD_DUMMY)
        self.killed_snowman = self.getLineInt(Flags.KILLED_SNOWMAN)
        self.interacted_crosswords = self.getLineInt(
            Flags.INTERACTED_CROSSWORDS)
        self.robbed_snowdin = self.getLineInt(Flags.ROBBED_SNOWDIN)
        self.robbed_core = self.getLineInt(Flags.ROBBED_CORE)
        self.used_recovery_item = self.getLineInt(Flags.USED_RECOVERY_ITEM)
        self.interacted_fakedog = self.getLineInt(Flags.INTERACTED_FAKEDOG)
        self.delivered_seatea = self.getLineInt(Flags.DELIVERED_SEATEA)
        self.delivered_cinnabun = self.getLineInt(Flags.DELIVERED_CINNABUN)
        self.delivered_hotdog = self.getLineInt(Flags.DELIVERED_HOTDOG)
        self.tem_sell_parameter1 = self.getLineInt(Flags.TEM_SELL_PARAMETER1)
        self.tem_sell_parameter2 = self.getLineInt(Flags.TEM_SELL_PARAMETER2)
        self.status_hotel = self.getLineInt(Flags.STATUS_HOTEL)
        self.allergy_tem_talked = self.getLineInt(Flags.ALLERGY_TEM_TALKED)
        self.glowshrooms_on = self.getLineInt(Flags.GLOWSHROOMS_ON)
        self.fighting_sans = self.getLineInt(Flags.FIGHTING_SANS)
        self.geeettttttt_dunked_on = self.getLineInt(
            Flags.GEEETTTTTTT_DUNKED_ON)
        self.tundra_stick_broken = self.getLineInt(Flags.TUNDRA_STICK_BROKEN)
        self.temmie_college_paid = self.getLineInt(Flags.TEMMIE_COLLEGE_PAID)
        self.fun_call_occurred = self.getLineInt(Flags.FUN_CALL_OCCURRED)
        self.completed_tile_puzzle = self.getLineInt(
            Flags.COMPLETED_TILE_PUZZLE)
        self.interacted_clamgirl = self.getLineInt(Flags.INTERACTED_CLAMGIRL)
        self.conversation_elderpuzzles = self.getLineInt(
            Flags.CONVERSATION_ELDERPUZZLES)
        self.status_sosorry = self.getLineInt(Flags.STATUS_SOSORRY)
        self.encountered_glyde = self.getLineInt(Flags.ENCOUNTERED_GLYDE)
        self.check_papyrus_kitchen_again = self.getLineInt(
            Flags.CHECK_PAPYRUS_KITCHEN_AGAIN)
        self.undyne_spears_anger = self.getLineInt(Flags.UNDYNE_SPEARS_ANGER)
        self.conversation_toriel_sms = self.getLineInt(
            Flags.CONVERSATION_TORIEL_SMS)
        self.conversation_sms_parameters = self.getLineInt(
            Flags.CONVERSATION_SMS_PARAMETERS)
        self.failed_defusing = self.getLineInt(Flags.FAILED_DEFUSING)
        self.stepped_green_tile = self.getLineInt(Flags.STEPPED_GREEN_TILE)
        self.dimensional_box_a_0 = self.getLineItem(Flags.DIMENSIONAL_BOX_A_0)
        self.dimensional_box_a_1 = self.getLineItem(Flags.DIMENSIONAL_BOX_A_1)
        self.dimensional_box_a_2 = self.getLineItem(Flags.DIMENSIONAL_BOX_A_2)
        self.dimensional_box_a_3 = self.getLineItem(Flags.DIMENSIONAL_BOX_A_3)
        self.dimensional_box_a_4 = self.getLineItem(Flags.DIMENSIONAL_BOX_A_4)
        self.dimensional_box_a_5 = self.getLineItem(Flags.DIMENSIONAL_BOX_A_5)
        self.dimensional_box_a_6 = self.getLineItem(Flags.DIMENSIONAL_BOX_A_6)
        self.dimensional_box_a_7 = self.getLineItem(Flags.DIMENSIONAL_BOX_A_7)
        self.dimensional_box_a_8 = self.getLineItem(Flags.DIMENSIONAL_BOX_A_8)
        self.dimensional_box_a_9 = self.getLineItem(Flags.DIMENSIONAL_BOX_A_9)
        self.dimensional_box_b_0 = self.getLineItem(Flags.DIMENSIONAL_BOX_B_0)
        self.dimensional_box_b_1 = self.getLineItem(Flags.DIMENSIONAL_BOX_B_1)
        self.dimensional_box_b_2 = self.getLineItem(Flags.DIMENSIONAL_BOX_B_2)
        self.dimensional_box_b_3 = self.getLineItem(Flags.DIMENSIONAL_BOX_B_3)
        self.dimensional_box_b_4 = self.getLineItem(Flags.DIMENSIONAL_BOX_B_4)
        self.dimensional_box_b_5 = self.getLineItem(Flags.DIMENSIONAL_BOX_B_5)
        self.dimensional_box_b_6 = self.getLineItem(Flags.DIMENSIONAL_BOX_B_6)
        self.dimensional_box_b_7 = self.getLineItem(Flags.DIMENSIONAL_BOX_B_7)
        self.dimensional_box_b_8 = self.getLineItem(Flags.DIMENSIONAL_BOX_B_8)
        self.dimensional_box_b_9 = self.getLineItem(Flags.DIMENSIONAL_BOX_B_9)
        self.status_undyne = self.getLineInt(Flags.STATUS_UNDYNE)
        self.undyne_hp_left = self.getLineInt(Flags.UNDYNE_HP_LEFT)
        self.fought_undyne = self.getLineInt(Flags.FOUGHT_UNDYNE)
        self.poured_water_ground = self.getLineInt(Flags.POURED_WATER_GROUND)
        self.conversation_papyrus_calls = self.getLineInt(
            Flags.CONVERSATION_PAPYRUS_CALLS)
        self.choice_maddummy = self.getLineInt(Flags.CHOICE_MADDUMMY)
        self.completed_piano_puzzle = self.getLineInt(
            Flags.COMPLETED_PIANO_PUZZLE)
        self.progress_water_battles = self.getLineInt(
            Flags.PROGRESS_WATER_BATTLES)
        self.progress_water2_battles = self.getLineInt(
            Flags.PROGRESS_WATER2_BATTLES)
        self.rain_parameters_0 = self.getLineFloat(Flags.RAIN_PARAMETERS_0)
        self.rain_parameters_1 = self.getLineFloat(Flags.RAIN_PARAMETERS_1)
        self.rain_parameters_2 = self.getLineFloat(Flags.RAIN_PARAMETERS_2)
        self.rain_parameters_3 = self.getLineFloat(Flags.RAIN_PARAMETERS_3)
        self.rain_parameters_4 = self.getLineFloat(Flags.RAIN_PARAMETERS_4)
        self.have_water = self.getLineInt(Flags.HAVE_WATER)
        self.disable_alphys_calls = self.getLineInt(Flags.DISABLE_ALPHYS_CALLS)
        self.disable_alphys_statuses = self.getLineInt(
            Flags.DISABLE_ALPHYS_STATUSES)
        self.conversation_alphys_statuses = self.getLineInt(
            Flags.CONVERSATION_ALPHYS_STATUSES)
        self.quick_battle = self.getLineInt(Flags.QUICK_BATTLE)
        self.laser1_off = self.getLineInt(Flags.LASER1_OFF)
        self.laser2_on = self.getLineInt(Flags.LASER2_ON)
        self.laser2_off = self.getLineInt(Flags.LASER2_OFF)
        self.completed_shoot_puzzle1 = self.getLineInt(
            Flags.COMPLETED_SHOOT_PUZZLE1)
        self.completed_shoot_puzzle2 = self.getLineInt(
            Flags.COMPLETED_SHOOT_PUZZLE2)
        self.conveyor_puzzle_variable = self.getLineInt(
            Flags.CONVEYOR_PUZZLE_VARIABLE)
        self.failed_jetpack_segment = self.getLineInt(
            Flags.FAILED_JETPACK_SEGMENT)
        self.hot_dogs_money_spent = self.getLineInt(Flags.HOT_DOGS_MONEY_SPENT)
        self.conversation_hotdogs = self.getLineInt(Flags.CONVERSATION_HOTDOGS)
        self.headdogs = self.getLineInt(Flags.HEADDOGS)
        self.reached_headdogs_limit = self.getLineInt(
            Flags.REACHED_HEADDOGS_LIMIT)
        self.muffet_bribe_price = self.getLineInt(Flags.MUFFET_BRIBE_PRICE)
        self.muffet_bribe_money_spent = self.getLineInt(
            Flags.MUFFET_BRIBE_MONEY_SPENT)
        self.status_yellow_button = self.getLineInt(Flags.STATUS_YELLOW_BUTTON)
        self.reset_bridgeseed_puzzle = self.getLineInt(
            Flags.RESET_BRIDGESEED_PUZZLE)
        self.won_ball_game = self.getLineInt(Flags.WON_BALL_GAME)
        self.fall_animation_parameters = self.getLineInt(
            Flags.FALL_ANIMATION_PARAMETERS)
        self.dated_undyne = self.getLineInt(Flags.DATED_UNDYNE)
        self.undyne_expression = self.getLineInt(Flags.UNDYNE_EXPRESSION)
        self.choice_meal_grillby = self.getLineInt(Flags.CHOICE_MEAL_GRILLBY)
        self.bombs_defused = self.getLineInt(Flags.BOMBS_DEFUSED)
        self.fought_muffet = self.getLineInt(Flags.FOUGHT_MUFFET)
        self.killed_muffet = self.getLineInt(Flags.KILLED_MUFFET)
        self.current_elevator_floor = self.getLineInt(
            Flags.CURRENT_ELEVATOR_FLOOR)
        self.completed_shoot_puzzle3 = self.getLineInt(
            Flags.COMPLETED_SHOOT_PUZZLE3)
        self.completed_shoot_puzzle4 = self.getLineInt(
            Flags.COMPLETED_SHOOT_PUZZLE4)
        self.asked_papyrus_rg = self.getLineInt(Flags.ASKED_PAPYRUS_RG)
        self.killed_rg = self.getLineInt(Flags.KILLED_RG)
        self.spider_sale_big_spendings = self.getLineInt(
            Flags.SPIDER_SALE_BIG_SPENDINGS)
        self.laser3_off = self.getLineInt(Flags.LASER3_OFF)
        self.conversation_wares = self.getLineInt(Flags.CONVERSATION_WARES)
        self.conversation_mettaton = self.getLineInt(
            Flags.CONVERSATION_METTATON)
        self.conversation_alphys = self.getLineInt(Flags.CONVERSATION_ALPHYS)
        self.progress_hotland_battles = self.getLineInt(
            Flags.PROGRESS_HOTLAND_BATTLES)
        self.got_napstablook_friend_req = self.getLineInt(
            Flags.GOT_NAPSTABLOOK_FRIEND_REQ)
        self.dated_sans2 = self.getLineInt(Flags.DATED_SANS2)
        self.got_alphys_advice1 = self.getLineInt(Flags.GOT_ALPHYS_ADVICE1)
        self.got_alphys_advice2 = self.getLineInt(Flags.GOT_ALPHYS_ADVICE2)
        self.got_alphys_advice3 = self.getLineInt(Flags.GOT_ALPHYS_ADVICE3)
        self.got_alphys_advice4 = self.getLineInt(Flags.GOT_ALPHYS_ADVICE4)
        self.progress_core_battles = self.getLineInt(
            Flags.PROGRESS_CORE_BATTLES)
        self.turn_mettaton = self.getLineInt(Flags.TURN_METTATON)
        self.killed_mettaton = self.getLineInt(Flags.KILLED_METTATON)
        self.progress_core_battles2 = self.getLineInt(
            Flags.PROGRESS_CORE_BATTLES2)
        self.alphys_expression = self.getLineInt(Flags.ALPHYS_EXPRESSION)
        self.current_final_floor = self.getLineInt(Flags.CURRENT_FINAL_FLOOR)
        self.rode_long_elevator = self.getLineInt(Flags.RODE_LONG_ELEVATOR)
        self.unlocked_mettaton_house = self.getLineInt(
            Flags.UNLOCKED_METTATON_HOUSE)
        self.choice_flamey_challenge = self.getLineInt(
            Flags.CHOICE_FLAMEY_CHALLENGE)
        self.status_bpants = self.getLineInt(Flags.STATUS_BPANTS)
        self.conversation_mtt = self.getLineInt(Flags.CONVERSATION_MTT)
        self.conversation_girls = self.getLineInt(Flags.CONVERSATION_GIRLS)
        self.water_taken_amount = self.getLineInt(Flags.WATER_TAKEN_AMOUNT)
        self.water_wasted_amount = self.getLineInt(Flags.WATER_WASTED_AMOUNT)
        self.got_gun = self.getLineInt(Flags.GOT_GUN)
        self.got_cowboy_hat = self.getLineInt(Flags.GOT_COWBOY_HAT)
        self.got_mystery_key = self.getLineInt(Flags.GOT_MYSTERY_KEY)
        self.got_face_steak = self.getLineInt(Flags.GOT_FACE_STEAK)
        self.progress_early_story = self.getLineInt(Flags.PROGRESS_EARLY_STORY)
        self.have_castle_key1 = self.getLineInt(Flags.HAVE_CASTLE_KEY1)
        self.have_castle_key2 = self.getLineInt(Flags.HAVE_CASTLE_KEY2)
        self.unlocked_latchkey = self.getLineInt(Flags.UNLOCKED_LATCHKEY)
        self.early_story_parameter1 = self.getLineInt(
            Flags.EARLY_STORY_PARAMETER1)
        self.early_story_parameter2 = self.getLineInt(
            Flags.EARLY_STORY_PARAMETER2)
        self.told_asgore_ready = self.getLineInt(Flags.TOLD_ASGORE_READY)
        self.experience_cosmic_garbage = self.getLineInt(
            Flags.EXPERIENCE_COSMIC_GARBAGE)
        self.riverman_destination = self.getLineInt(Flags.RIVERMAN_DESTINATION)
        self.got_tem_village_hint = self.getLineInt(Flags.GOT_TEM_VILLAGE_HINT)
        self.tem_boat_version = self.getLineInt(Flags.TEM_BOAT_VERSION)
        self.called_already = self.getLineInt(Flags.CALLED_ALREADY)
        self.papyrus_and_undyne = self.getLineInt(Flags.PAPYRUS_AND_UNDYNE)
        self.conversation_undyne_mad = self.getLineInt(
            Flags.CONVERSATION_UNDYNE_MAD)
        self.killed_flowey = self.getLineInt(Flags.KILLED_FLOWEY)
        self.killed_asgore = self.getLineInt(Flags.KILLED_ASGORE)
        self.completed_truelab = self.getLineInt(Flags.COMPLETED_TRUELAB)
        self.truelab_events_0 = self.getLineInt(Flags.TRUELAB_EVENTS_0)
        self.truelab_events_1 = self.getLineInt(Flags.TRUELAB_EVENTS_1)
        self.truelab_events_2 = self.getLineInt(Flags.TRUELAB_EVENTS_2)
        self.truelab_events_3 = self.getLineInt(Flags.TRUELAB_EVENTS_3)
        self.truelab_events_4 = self.getLineInt(Flags.TRUELAB_EVENTS_4)
        self.truelab_events_5 = self.getLineInt(Flags.TRUELAB_EVENTS_5)
        self.truelab_events_6 = self.getLineInt(Flags.TRUELAB_EVENTS_6)
        self.truelab_events_7 = self.getLineInt(Flags.TRUELAB_EVENTS_7)
        self.truelab_events_8 = self.getLineInt(Flags.TRUELAB_EVENTS_8)
        self.truelab_events_9 = self.getLineInt(Flags.TRUELAB_EVENTS_9)
        self.truelab_events_10 = self.getLineInt(Flags.TRUELAB_EVENTS_10)
        self.truelab_events_11 = self.getLineInt(Flags.TRUELAB_EVENTS_11)
        self.dated_alphys = self.getLineInt(Flags.DATED_ALPHYS)
        self.status_undyne_letter = self.getLineInt(Flags.STATUS_UNDYNE_LETTER)
        self.popato_chisps_bought = self.getLineInt(Flags.POPATO_CHISPS_BOUGHT)
        self.conversation_onionsan = self.getLineInt(
            Flags.CONVERSATION_ONIONSAN)
        self.got_sans_room_key = self.getLineInt(Flags.GOT_SANS_ROOM_KEY)
        self.seen_cast = self.getLineInt(Flags.SEEN_CAST)
        self.fighting_asriel = self.getLineInt(Flags.FIGHTING_ASRIEL)
        self.conversation_asriel_fight = self.getLineInt(
            Flags.CONVERSATION_ASRIEL_FIGHT)
        self.but_it_refused = self.getLineInt(Flags.BUT_IT_REFUSED)
        self.dreamed_asriel_fight = self.getLineInt(Flags.DREAMED_ASRIEL_FIGHT)
        self.saved_lost_soul_0 = self.getLineInt(Flags.SAVED_LOST_SOUL_0)
        self.saved_lost_soul_1 = self.getLineInt(Flags.SAVED_LOST_SOUL_1)
        self.saved_lost_soul_2 = self.getLineInt(Flags.SAVED_LOST_SOUL_2)
        self.saved_lost_soul_3 = self.getLineInt(Flags.SAVED_LOST_SOUL_3)
        self.toggle_final_beam = self.getLineInt(Flags.TOGGLE_FINAL_BEAM)
        self.plot_over = self.getLineInt(Flags.PLOT_OVER)
        self.conversation_asriel2 = self.getLineInt(Flags.CONVERSATION_ASRIEL2)
        self.choice_left_toriel = self.getLineInt(Flags.CHOICE_LEFT_TORIEL)
        self.plot = self.getLineFloat(Flags.PLOT)
        self.menuchoice_0 = self.getLineInt(Flags.MENUCHOICE_0)
        self.menuchoice_1 = self.getLineInt(Flags.MENUCHOICE_1)
        self.menuchoice_2 = self.getLineInt(Flags.MENUCHOICE_2)
        self.song = self.getLineInt(Flags.SONG)
        self.room = self.getLineRoom(Flags.ROOM)
        self.game_time = self.getLineInt(Flags.GAME_TIME)

    def compare_to(self, other: UndertaleFile) -> list[str]:
        attrs = ["character_name", "love", "max_hp", "max_en", "attack_dmg", "weapon_strength", "defense", "armor_defense", "sp", "exp", "gold", "kills", "inventory_0", "cell_0", "inventory_1", "cell_1", "inventory_2", "cell_2", "inventory_3", "cell_3", "inventory_4", "cell_4", "inventory_5", "cell_5", "inventory_6", "cell_6", "inventory_7", "cell_7", "weapon_item", "armor_item", "undyne_trigger_override", "fun", "hardmode", "true_pacifist", "disable_random_encounters", "spared_last", "escaped_last", "killed_last", "bored_last", "status_dummy", "in_battle", "type_heart_transition", "animation_index", "cooked_noodles", "name_color", "spared", "escaped", "dialogues_skipped", "murderlevel_override", "spared_specific", "fast_text_skip", "tutorial_froggit_encountered", "pushed_rock_1", "pushed_rock_2", "pushed_rock_3", "candy_taken", "pushed_rock_4", "spared_napstablook", "waited_toriel", "greeted_toriel", "flirted_toriel", "call_mom_toriel", "ruins_switches_pressed", "disobeyed_toriel", "status_toriel", "choice_flavor", "status_creepy_tundra", "know_water_sausage", "wrong_switches_pressed", "status_doggo", "status_dogcouple", "status_greaterdog", "status_lesserdog", "status_snowman", "status_snowdrake", "choice_harder_puzzle", "spider_donations_total", "nicecream_donations_total", "choice_ate_left_spaghetti", "xoxo_resets", "toggled_snow_switch", "got_snowpoff_gold", "flirted_papyrus_fight", "status_papyrus", "fought_papyrus", "bpants_alt_dialogue", "progress_tundra_battles", "status_inn", "stayed_inn", "betrayed_gyftrot", "armor_papyrus_inquiry", "choice_papyrus_inquiry", "armor_undyne_saw", "strong_tough_glove", "nicecream_business", "punchcards_bought", "status_shyren", "papyrus_sink_event_occurred", "got_couch_gold", "have_umbrella", "music_statue_on", "dated_papyrus", "dated_sans1", "choice_mkid_umbrella", "interacted_garbage_savepoint", "status_stable", "talked_napstablook", "current_napstablook_song", "aaron_woshua_event", "conversation_emblem", "creepy_friend_seen", "saved_mkid", "undyne_difficulty", "got_ribbon", "got_toyknife", "got_bscotch_pie", "got_quiche", "got_tutu", "got_ballet_shoes", "got_artifact", "got_spacefood", "got_instant_noodles", "got_frying_pan", "got_apron", "got_glamburger_trashcan", "got_gold_trashcan", "got_dagger", "got_locket", "spared_froggit", "spared_whimsun", "spared_moldsmal", "spared_loox", "spared_vegetoid", "spared_migosp", "spared_snowdrake", "spared_icecap", "spared_gyftrot", "spared_doggo", "spared_lesserdog", "spared_greatdog", "spared_aaron", "spared_moldsmalx", "spared_woshua", "spared_temmie", "spared_maddummy", "spared_vulkin", "spared_tsunderplane", "spared_pyrope", "spared_finalfroggit", "spared_whimsalot", "spared_astigmatism", "spared_madjick", "spared_finalknight", "spared_endogeny", "conversation_toriel_pacifist", "conversation_sans_pacifist", "conversation_undyne_pacifist", "unlock_napsta_pacifist", "conversation_papyrus_pacifist", "conversation_alphys_pacifist", "conversation_asgore_pacifist", "conversation_mettaton_pacifist", "conversation_napstablook_pacifist", "kills_area_pointer", "kills_other", "kills_ruins", "kills_tundra", "kills_water", "kills_hotland", "genocide_ruins", "genocide_tundra", "genocide_water", "genocide_hotland", "genocide_core", "nicecream_business2", "killed_undyne_ex", "killed_glad_dummy", "killed_snowman", "interacted_crosswords", "robbed_snowdin", "robbed_core", "used_recovery_item", "interacted_fakedog", "delivered_seatea", "delivered_cinnabun", "delivered_hotdog", "tem_sell_parameter1", "tem_sell_parameter2", "status_hotel", "allergy_tem_talked", "glowshrooms_on", "fighting_sans", "geeettttttt_dunked_on", "tundra_stick_broken", "temmie_college_paid", "fun_call_occurred", "completed_tile_puzzle", "interacted_clamgirl", "conversation_elderpuzzles", "status_sosorry", "encountered_glyde", "check_papyrus_kitchen_again", "undyne_spears_anger", "conversation_toriel_sms", "conversation_sms_parameters", "failed_defusing", "stepped_green_tile", "dimensional_box_a_0", "dimensional_box_a_1", "dimensional_box_a_2", "dimensional_box_a_3", "dimensional_box_a_4", "dimensional_box_a_5", "dimensional_box_a_6", "dimensional_box_a_7", "dimensional_box_a_8", "dimensional_box_a_9", "dimensional_box_b_0", "dimensional_box_b_1", "dimensional_box_b_2", "dimensional_box_b_3", "dimensional_box_b_4", "dimensional_box_b_5", "dimensional_box_b_6", "dimensional_box_b_7", "dimensional_box_b_8", "dimensional_box_b_9", "status_undyne", "undyne_hp_left", "fought_undyne", "poured_water_ground", "conversation_papyrus_calls", "choice_maddummy", "completed_piano_puzzle", "progress_water_battles", "progress_water2_battles", "rain_parameters_0", "rain_parameters_1", "rain_parameters_2", "rain_parameters_3", "rain_parameters_4", "have_water", "disable_alphys_calls", "disable_alphys_statuses", "conversation_alphys_statuses", "quick_battle", "laser1_off", "laser2_on", "laser2_off", "completed_shoot_puzzle1", "completed_shoot_puzzle2", "conveyor_puzzle_variable", "failed_jetpack_segment", "hot_dogs_money_spent", "conversation_hotdogs", "headdogs", "reached_headdogs_limit", "muffet_bribe_price", "muffet_bribe_money_spent", "status_yellow_button", "reset_bridgeseed_puzzle", "won_ball_game", "fall_animation_parameters", "dated_undyne", "undyne_expression", "choice_meal_grillby", "bombs_defused", "fought_muffet", "killed_muffet", "current_elevator_floor", "completed_shoot_puzzle3", "completed_shoot_puzzle4", "asked_papyrus_rg", "killed_rg", "spider_sale_big_spendings", "laser3_off", "conversation_wares", "conversation_mettaton", "conversation_alphys", "progress_hotland_battles", "got_napstablook_friend_req", "dated_sans2", "got_alphys_advice1", "got_alphys_advice2", "got_alphys_advice3", "got_alphys_advice4", "progress_core_battles", "turn_mettaton", "killed_mettaton", "progress_core_battles2", "alphys_expression", "current_final_floor", "rode_long_elevator", "unlocked_mettaton_house", "choice_flamey_challenge", "status_bpants", "conversation_mtt", "conversation_girls", "water_taken_amount", "water_wasted_amount", "got_gun", "got_cowboy_hat", "got_mystery_key", "got_face_steak", "progress_early_story", "have_castle_key1", "have_castle_key2", "unlocked_latchkey", "early_story_parameter1", "early_story_parameter2", "told_asgore_ready", "experience_cosmic_garbage", "riverman_destination", "got_tem_village_hint", "tem_boat_version", "called_already", "papyrus_and_undyne", "conversation_undyne_mad", "killed_flowey", "killed_asgore", "completed_truelab", "truelab_events_0", "truelab_events_1", "truelab_events_2", "truelab_events_3", "truelab_events_4", "truelab_events_5", "truelab_events_6", "truelab_events_7", "truelab_events_8", "truelab_events_9", "truelab_events_10", "truelab_events_11", "dated_alphys", "status_undyne_letter", "popato_chisps_bought", "conversation_onionsan", "got_sans_room_key", "seen_cast", "fighting_asriel", "conversation_asriel_fight", "but_it_refused", "dreamed_asriel_fight", "saved_lost_soul_0", "saved_lost_soul_1", "saved_lost_soul_2", "saved_lost_soul_3", "toggle_final_beam", "plot_over", "conversation_asriel2", "choice_left_toriel", "plot", "menuchoice_0", "menuchoice_1", "menuchoice_2", "song", "room", "game_time"]
        diffs: list[str] = []
        for attr in attrs:
            if not hasattr(self, attr) or not hasattr(other, attr):
                continue
            if getattr(self, attr) != getattr(other, attr):
                diffs.append(attr)
        return diffs

    @property
    def inventory(self) -> list[Items]:
        raw_items: list[Items] = [
            self.inventory_0,
            self.inventory_1,
            self.inventory_2,
            self.inventory_3,
            self.inventory_4,
            self.inventory_5,
            self.inventory_6,
            self.inventory_7
        ]
        out: list[Items] = []
        for item in raw_items:
            if item != Items.NONE:
                out.append(item)
        return out

    @property
    def dim_box_a(self) -> list[Items]:
        raw_items: list[Items] = [
            self.dimensional_box_a_0,
            self.dimensional_box_a_1,
            self.dimensional_box_a_2,
            self.dimensional_box_a_3,
            self.dimensional_box_a_4,
            self.dimensional_box_a_5,
            self.dimensional_box_a_6,
            self.dimensional_box_a_7,
            self.dimensional_box_a_8,
            self.dimensional_box_a_9,
        ]
        out: list[Items] = []
        for item in raw_items:
            if item != Items.NONE:
                out.append(item)
        return out

    @property
    def dim_box_b(self) -> list[Items]:
        raw_items: list[Items] = [
            self.dimensional_box_b_0,
            self.dimensional_box_b_1,
            self.dimensional_box_b_2,
            self.dimensional_box_b_3,
            self.dimensional_box_b_4,
            self.dimensional_box_b_5,
            self.dimensional_box_b_6,
            self.dimensional_box_b_7,
            self.dimensional_box_b_8,
            self.dimensional_box_b_9
        ]
        out: list[Items] = []
        for item in raw_items:
            if item != Items.NONE:
                out.append(item)
        return out

    @property
    def cellphone(self) -> list[Cellphone]:
        raw_items: list[Cellphone] = [
            self.cell_0,
            self.cell_1,
            self.cell_2,
            self.cell_3,
            self.cell_4,
            self.cell_5,
            self.cell_6,
            self.cell_7
        ]
        out: list[Cellphone] = []
        for item in raw_items:
            if item != Cellphone.NONE:
                out.append(item)
        return out
