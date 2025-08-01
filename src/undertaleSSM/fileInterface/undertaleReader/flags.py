import enum


class Flags(enum.Enum):  # I know that flags are only a subset of the save structure but i'll use the Flags enum for all lines
    """
    An enum containing what most lines do in file[0-9]
    """
    CHARACTER_NAME = 1
    LOVE = 2
    MAX_HP = 3
    MAX_EN = 4  # idk what this value is
    ATTACK_DMG = 5
    WEAPON_STRENGTH = 6
    DEFENSE = 7
    ARMOR_DEFENSE = 8
    SP = 9  # idk what this value is either
    EXP = 10
    GOLD = 11
    KILLS = 12
    INVENTORY_0 = 13
    CELL_0 = 14
    INVENTORY_1 = 15
    CELL_1 = 16
    INVENTORY_2 = 17
    CELL_2 = 18
    INVENTORY_3 = 19
    CELL_3 = 20
    INVENTORY_4 = 21
    CELL_4 = 22
    INVENTORY_5 = 23
    CELL_5 = 24
    INVENTORY_6 = 25
    CELL_6 = 26
    INVENTORY_7 = 27
    CELL_7 = 28
    WEAPON_ITEM = 29
    ARMOR_ITEM = 30
    UNDYNE_TRIGGER_OVERRIDE = 34  # debug bool
    FUN = 35  # range
    HARDMODE = 36  # bool
    TRUE_PACIFIST = 37  # bool
    DISABLE_RANDOM_ENCOUNTERS = 38  # bool
    SPARED_LAST = 40  # volatile bool
    ESCAPED_LAST = 41  # volatile bool
    KILLED_LAST = 42  # volatile bool
    BORED_LAST = 43  # volatile bool
    STATUS_DUMMY = 44  # range
    IN_BATTLE = 45  # volatile bool
    TYPE_HEART_TRANSITION = 46  # volatile bool
    ANIMATION_INDEX = 50  # volatile range
    COOKED_NOODLES = 51  # bool
    NAME_COLOR = 52  # range
    SPARED = 53  # counter
    ESCAPED = 54  # counter
    DIALOGUES_SKIPPED = 55  # counter
    MURDERLEVEL_OVERRIDE = 56  # debug range
    SPARED_SPECIFIC = 57  # bool
    FAST_TEXT_SKIP = 58  # debug bool
    TUTORIAL_FROGGIT_ENCOUNTERED = 60  # bool
    PUSHED_ROCK_1 = 61  # bool
    PUSHED_ROCK_2 = 62  # bool
    PUSHED_ROCK_3 = 63  # bool
    CANDY_TAKEN = 64  # range
    PUSHED_ROCK_4 = 65  # bool
    SPARED_NAPSTABLOOK = 66  # bool
    WAITED_TORIEL = 67  # bool
    GREETED_TORIEL = 70  # counter
    FLIRTED_TORIEL = 71  # counter
    CALL_MOM_TORIEL = 72  # bool
    RUINS_SWITCHES_PRESSED = 73  # counter
    DISOBEYED_TORIEL = 74  # counter
    STATUS_TORIEL = 75  # range
    CHOICE_FLAVOR = 76  # range
    STATUS_CREEPY_TUNDRA = 77  # range
    KNOW_WATER_SAUSAGE = 80  # bool
    WRONG_SWITCHES_PRESSED = 81  # counter
    STATUS_DOGGO = 82  # range
    STATUS_DOGCOUPLE = 83  # range
    STATUS_GREATERDOG = 84  # range
    STATUS_LESSERDOG = 85  # range
    STATUS_SNOWMAN = 86  # range
    STATUS_SNOWDRAKE = 87  # range
    CHOICE_HARDER_PUZZLE = 88  # range
    SPIDER_DONATIONS_TOTAL = 89  # range
    NICECREAM_DONATIONS_TOTAL = 90  # range
    CHOICE_ATE_LEFT_SPAGHETTI = 92  # range
    XOXO_RESETS = 93  # counter
    TOGGLED_SNOW_SWITCH = 94  # bool
    GOT_SNOWPOFF_GOLD = 95  # bool
    FLIRTED_PAPYRUS_FIGHT = 96  # bool
    STATUS_PAPYRUS = 97  # range
    FOUGHT_PAPYRUS = 98  # bool
    BPANTS_ALT_DIALOGUE = 99  # debug bool
    PROGRESS_TUNDRA_BATTLES = 100  # counter
    STATUS_INN = 102  # range
    STAYED_INN = 103  # bool
    BETRAYED_GYFTROT = 104  # bool
    ARMOR_PAPYRUS_INQUIRY = 105  # range
    CHOICE_PAPYRUS_INQUIRY = 106  # range
    ARMOR_UNDYNE_SAW = 107  # range
    STRONG_TOUGH_GLOVE = 108  # volatile bool
    NICECREAM_BUSINESS = 109  # bool
    PUNCHCARDS_BOUGHT = 110  # counter
    STATUS_SHYREN = 111  # range
    PAPYRUS_SINK_EVENT_OCCURRED = 112  # bool
    GOT_COUCH_GOLD = 113  # bool
    HAVE_UMBRELLA = 115  # volatile bool
    MUSIC_STATUE_ON = 116  # bool
    DATED_PAPYRUS = 118  # counter
    DATED_SANS1 = 119  # counter
    CHOICE_MKID_UMBRELLA = 120  # range
    INTERACTED_GARBAGE_SAVEPOINT = 121  # bool
    STATUS_STABLE = 122  # range
    TALKED_NAPSTABLOOK = 123  # range
    CURRENT_NAPSTABLOOK_SONG = 124  # volatile range
    AARON_WOSHUA_EVENT = 125  # bool
    CONVERSATION_EMBLEM = 126  # counter
    CREEPY_FRIEND_SEEN = 127  # bool
    SAVED_MKID = 128  # range
    UNDYNE_DIFFICULTY = 129  # volatile counter
    GOT_RIBBON = 130  # bool
    GOT_TOYKNIFE = 132  # bool
    GOT_BSCOTCH_PIE = 133  # bool
    GOT_QUICHE = 134  # bool
    GOT_TUTU = 135  # bool
    GOT_BALLET_SHOES = 136  # bool
    GOT_ARTIFACT = 137  # bool
    GOT_SPACEFOOD = 138  # bool
    GOT_INSTANT_NOODLES = 139  # bool
    GOT_FRYING_PAN = 140  # bool
    GOT_APRON = 141  # bool
    GOT_GLAMBURGER_TRASHCAN = 142  # bool
    GOT_GOLD_TRASHCAN = 143  # bool
    GOT_DAGGER = 144  # bool
    GOT_LOCKET = 145  # bool
    SPARED_FROGGIT = 160  # bool
    SPARED_WHIMSUN = 161  # bool
    SPARED_MOLDSMAL = 162  # bool
    SPARED_LOOX = 163  # bool
    SPARED_VEGETOID = 164  # bool
    SPARED_MIGOSP = 165  # bool
    SPARED_SNOWDRAKE = 166  # bool
    SPARED_ICECAP = 167  # bool
    SPARED_GYFTROT = 168  # bool
    SPARED_DOGGO = 169  # bool
    SPARED_LESSERDOG = 171  # bool
    SPARED_GREATDOG = 172  # bool
    SPARED_AARON = 173  # bool
    SPARED_MOLDSMALX = 174  # bool
    SPARED_WOSHUA = 175  # bool
    SPARED_TEMMIE = 176  # bool
    SPARED_MADDUMMY = 177  # bool
    SPARED_VULKIN = 178  # bool
    SPARED_TSUNDERPLANE = 179  # bool
    SPARED_PYROPE = 180  # bool
    SPARED_FINALFROGGIT = 181  # bool
    SPARED_WHIMSALOT = 182  # bool
    SPARED_ASTIGMATISM = 183  # bool
    SPARED_MADJICK = 184  # bool
    SPARED_FINALKNIGHT = 185  # bool
    SPARED_ENDOGENY = 186  # bool
    CONVERSATION_TORIEL_PACIFIST = 221  # counter
    CONVERSATION_SANS_PACIFIST = 222  # counter
    CONVERSATION_UNDYNE_PACIFIST = 223  # counter
    UNLOCK_NAPSTA_PACIFIST = 224  # bool
    CONVERSATION_PAPYRUS_PACIFIST = 225  # counter
    CONVERSATION_ALPHYS_PACIFIST = 226  # counter
    CONVERSATION_ASGORE_PACIFIST = 227  # counter
    CONVERSATION_METTATON_PACIFIST = 228  # counter
    CONVERSATION_NAPSTABLOOK_PACIFIST = 229  # counter
    KILLS_AREA_POINTER = 230  # range
    KILLS_OTHER = 231  # counter idk what the difference to Flags.KILLS is
    KILLS_RUINS = 232  # counter
    KILLS_TUNDRA = 233  # counter
    KILLS_WATER = 234  # counter
    KILLS_HOTLAND = 235  # counter
    GENOCIDE_RUINS = 251  # bool
    GENOCIDE_TUNDRA = 252  # bool
    GENOCIDE_WATER = 253  # bool
    GENOCIDE_HOTLAND = 254  # bool
    GENOCIDE_CORE = 255  # bool
    NICECREAM_BUSINESS2 = 280  # volatile range
    KILLED_UNDYNE_EX = 281  # bool
    KILLED_GLAD_DUMMY = 282  # bool
    KILLED_SNOWMAN = 283  # counter
    INTERACTED_CROSSWORDS = 284  # bool
    ROBBED_SNOWDIN = 285  # bool
    ROBBED_CORE = 286  # bool
    USED_RECOVERY_ITEM = 290  # bool
    INTERACTED_FAKEDOG = 291  # bool
    DELIVERED_SEATEA = 292  # bool
    DELIVERED_CINNABUN = 293  # bool
    DELIVERED_HOTDOG = 294  # bool
    TEM_SELL_PARAMETER1 = 295  # range
    TEM_SELL_PARAMETER2 = 296  # range
    STATUS_HOTEL = 297  # range
    ALLERGY_TEM_TALKED = 299  # bool
    GLOWSHROOMS_ON = 300  # bool
    FIGHTING_SANS = 301  # volatile bool
    GEEETTTTTTT_DUNKED_ON = 302  # volatile bool
    TUNDRA_STICK_BROKEN = 305  # range
    TEMMIE_COLLEGE_PAID = 306  # bool
    FUN_CALL_OCCURRED = 307  # bool
    COMPLETED_TILE_PUZZLE = 308  # bool
    INTERACTED_CLAMGIRL = 309  # bool
    CONVERSATION_ELDERPUZZLES = 310  # counter
    STATUS_SOSORRY = 311  # range
    ENCOUNTERED_GLYDE = 312  # bool
    CHECK_PAPYRUS_KITCHEN_AGAIN = 313  # bool
    UNDYNE_SPEARS_ANGER = 314  # bool
    CONVERSATION_TORIEL_SMS = 316  # counter
    CONVERSATION_SMS_PARAMETERS = 317  # volatile range
    FAILED_DEFUSING = 318  # bool
    STEPPED_GREEN_TILE = 319  # bool
    
    DIMENSIONAL_BOX_A_0 = 331  # range
    DIMENSIONAL_BOX_A_1 = 332  # range
    DIMENSIONAL_BOX_A_2 = 333  # range
    DIMENSIONAL_BOX_A_3 = 334  # range
    DIMENSIONAL_BOX_A_4 = 335  # range
    DIMENSIONAL_BOX_A_5 = 336  # range
    DIMENSIONAL_BOX_A_6 = 337  # range
    DIMENSIONAL_BOX_A_7 = 338  # range
    DIMENSIONAL_BOX_A_8 = 339  # range
    DIMENSIONAL_BOX_A_9 = 340  # range
    
    DIMENSIONAL_BOX_B_0 = 342  # range
    DIMENSIONAL_BOX_B_1 = 343  # range
    DIMENSIONAL_BOX_B_2 = 344  # range
    DIMENSIONAL_BOX_B_3 = 345  # range
    DIMENSIONAL_BOX_B_4 = 346  # range
    DIMENSIONAL_BOX_B_5 = 347  # range
    DIMENSIONAL_BOX_B_6 = 348  # range
    DIMENSIONAL_BOX_B_7 = 349  # range
    DIMENSIONAL_BOX_B_8 = 350  # range
    DIMENSIONAL_BOX_B_9 = 351  # range
    
    STATUS_UNDYNE = 380  # range
    UNDYNE_HP_LEFT = 381  # range
    FOUGHT_UNDYNE = 382  # bool
    POURED_WATER_GROUND = 383  # counter
    CONVERSATION_PAPYRUS_CALLS = 384  # counter
    CHOICE_MADDUMMY = 385  # range
    COMPLETED_PIANO_PUZZLE = 386  # bool
    PROGRESS_WATER_BATTLES = 387  # counter
    PROGRESS_WATER2_BATTLES = 388  # counter
    RAIN_PARAMETERS_0 = 390  # volatile range
    RAIN_PARAMETERS_1 = 391  # volatile range
    RAIN_PARAMETERS_2 = 392  # volatile range
    RAIN_PARAMETERS_3 = 393  # volatile range
    RAIN_PARAMETERS_4 = 394  # volatile range
    HAVE_WATER = 396  # volatile bool
    DISABLE_ALPHYS_CALLS = 397  # bool
    DISABLE_ALPHYS_STATUSES = 398  # bool
    CONVERSATION_ALPHYS_STATUSES = 399  # counter
    QUICK_BATTLE = 400  # bool
    LASER1_OFF = 401  # bool
    LASER2_ON = 402  # bool
    LASER2_OFF = 403  # bool
    COMPLETED_SHOOT_PUZZLE1 = 404  # bool
    COMPLETED_SHOOT_PUZZLE2 = 405  # bool
    CONVEYOR_PUZZLE_VARIABLE = 406  # volatile range
    FAILED_JETPACK_SEGMENT = 407  # bool
    HOT_DOGS_MONEY_SPENT = 408  # range
    CONVERSATION_HOTDOGS = 409  # counter
    HEADDOGS = 410  # counter
    REACHED_HEADDOGS_LIMIT = 411  # bool
    MUFFET_BRIBE_PRICE = 412  # range
    MUFFET_BRIBE_MONEY_SPENT = 413  # range
    STATUS_YELLOW_BUTTON = 415  # range
    RESET_BRIDGESEED_PUZZLE = 416  # range
    WON_BALL_GAME = 417  # bool
    FALL_ANIMATION_PARAMETERS = 418  # range
    DATED_UNDYNE = 419  # range
    UNDYNE_EXPRESSION = 420  # volatile range
    CHOICE_MEAL_GRILLBY = 421  # range
    BOMBS_DEFUSED = 425  # counter
    FOUGHT_MUFFET = 426  # bool
    KILLED_MUFFET = 427  # bool
    CURRENT_ELEVATOR_FLOOR = 428  # range
    COMPLETED_SHOOT_PUZZLE3 = 429  # bool
    COMPLETED_SHOOT_PUZZLE4 = 430  # bool
    ASKED_PAPYRUS_RG = 431  # bool
    KILLED_RG = 432  # bool
    SPIDER_SALE_BIG_SPENDINGS = 433  # bool
    LASER3_OFF = 434  # bool
    CONVERSATION_WARES = 435  # counter
    CONVERSATION_METTATON = 436  # counter
    CONVERSATION_ALPHYS = 437  # counter
    PROGRESS_HOTLAND_BATTLES = 438  # counter
    GOT_NAPSTABLOOK_FRIEND_REQ = 439  # bool
    DATED_SANS2 = 443  # range
    GOT_ALPHYS_ADVICE1 = 444  # bool
    GOT_ALPHYS_ADVICE2 = 445  # bool
    GOT_ALPHYS_ADVICE3 = 446  # bool
    GOT_ALPHYS_ADVICE4 = 447  # bool
    PROGRESS_CORE_BATTLES = 453  # counter
    TURN_METTATON = 454  # range
    KILLED_METTATON = 455  # bool
    PROGRESS_CORE_BATTLES2 = 456  # counter
    ALPHYS_EXPRESSION = 460  # volatile range
    CURRENT_FINAL_FLOOR = 461  # bool
    RODE_LONG_ELEVATOR = 462  # bool
    UNLOCKED_METTATON_HOUSE = 463  # bool
    CHOICE_FLAMEY_CHALLENGE = 464  # range
    STATUS_BPANTS = 465  # range
    CONVERSATION_MTT = 466  # counter
    CONVERSATION_GIRLS = 467  # counter
    WATER_TAKEN_AMOUNT = 470  # counter
    WATER_WASTED_AMOUNT = 471  # counter
    GOT_GUN = 472  # bool
    GOT_COWBOY_HAT = 473  # bool
    GOT_MYSTERY_KEY = 474  # bool
    GOT_FACE_STEAK = 475  # bool
    PROGRESS_EARLY_STORY = 480  # counter
    HAVE_CASTLE_KEY1 = 482  # bool
    HAVE_CASTLE_KEY2 = 483  # bool
    UNLOCKED_LATCHKEY = 484  # bool
    EARLY_STORY_PARAMETER1 = 485  # range
    EARLY_STORY_PARAMETER2 = 486  # range
    TOLD_ASGORE_READY = 487  # bool
    EXPERIENCE_COSMIC_GARBAGE = 488  # bool
    RIVERMAN_DESTINATION = 489  # volatile range
    GOT_TEM_VILLAGE_HINT = 490  # bool
    TEM_BOAT_VERSION = 491  # volatile bool
    CALLED_ALREADY = 492  # range
    PAPYRUS_AND_UNDYNE = 495  # bool
    CONVERSATION_UNDYNE_MAD = 500  # bool
    KILLED_FLOWEY = 505  # bool
    KILLED_ASGORE = 506  # bool
    COMPLETED_TRUELAB = 510  # bool
    TRUELAB_EVENTS_0 = 511  # range
    TRUELAB_EVENTS_1 = 512  # range
    TRUELAB_EVENTS_2 = 513  # range
    TRUELAB_EVENTS_3 = 514  # range
    TRUELAB_EVENTS_4 = 515  # range
    TRUELAB_EVENTS_5 = 516  # range
    TRUELAB_EVENTS_6 = 517  # range
    TRUELAB_EVENTS_7 = 518  # range
    TRUELAB_EVENTS_8 = 519  # range
    TRUELAB_EVENTS_9 = 520  # range
    TRUELAB_EVENTS_10 = 521  # range
    TRUELAB_EVENTS_11 = 522  # range
    DATED_ALPHYS = 523  # range
    STATUS_UNDYNE_LETTER = 524  # range
    POPATO_CHISPS_BOUGHT = 525  # counter
    CONVERSATION_ONIONSAN = 526  # counter
    GOT_SANS_ROOM_KEY = 527  # bool
    SEEN_CAST = 529  # bool
    FIGHTING_ASRIEL = 530  # volatile bool
    CONVERSATION_ASRIEL_FIGHT = 531  # counter
    BUT_IT_REFUSED = 532  # volatile bool
    DREAMED_ASRIEL_FIGHT = 533  # volatile bool
    SAVED_LOST_SOUL_0 = 535  # bool
    SAVED_LOST_SOUL_1 = 536  # bool
    SAVED_LOST_SOUL_2 = 537  # bool
    SAVED_LOST_SOUL_3 = 538  # bool
    TOGGLE_FINAL_BEAM = 539  # volatile bool
    PLOT_OVER = 540  # range
    CONVERSATION_ASRIEL2 = 541  # counter
    CHOICE_LEFT_TORIEL = 542  # bool
    PLOT = 543
    MENUCHOICE_0 = 544
    MENUCHOICE_1 = 545
    MENUCHOICE_2 = 546
    SONG = 547
    ROOM = 548
    GAME_TIME = 549


class IniFlags(enum.Enum):
    """
    An enum containing all keys for undertale.ini
    """
    GENERAL_NAME = "Name"
    GENERAL_TIME = "Time"
    GENERAL_ROOM = "Room"
    GENERAL_GAMEOVER = "Gameover"
    GENERAL_KILLS = "Kills"
    GENERAL_LOVE = "Love"
    GENERAL_FUN = "fun"
    GENERAL_CAPITAL_FUN = "Fun"
    GENERAL_TALE = "Tale"
    GENERAL_WON = "Won"
    GENERAL_BW = "BW"
    GENERAL_BC = "BC"
    GENERAL_CP = "CP"
    GENERAL_BP = "BP"
    GENERAL_CH = "CH"
    GENERAL_BH = "BH"
    RESET_RESET = "reset/reset"
    RESET_S_KEY = "reset/s_key"
    FLOWEY_MET1 = "Flowey/Met1"
    FLOWEY_K = "Flowey/K"
    FLOWEY_NK = "Flowey/NK"
    FLOWEY_IK = "Flowey/IK"
    FLOWEY_SK = "Flowey/SK"
    FLOWEY_FLOWEYEXPLAIN1 = "Flowey/FloweyExplain1"
    FLOWEY_EX = "Flowey/EX"
    FLOWEY_CHANGE = "Flowey/CHANGE"
    FLOWEY_AK = "Flowey/AK"
    FLOWEY_AF = "Flowey/AF"
    FLOWEY_ALTER = "Flowey/Alter"
    FLOWEY_ALTER2 = "Flowey/alter2"
    FLOWEY_TRUENAME = "Flowey/truename"
    FLOWEY_SPECIALK = "Flowey/SPECIALK"
    TORIEL_BSCOTCH = "Toriel/Bscotch"
    TORIEL_TS = "Toriel/TS"
    TORIEL_TK = "Toriel/TK"
    SANS_M1 = "Sans/M1"
    SANS_ENDMET = "Sans/EndMet"
    SANS_MEETLV1 = "Sans/MeetLv1"
    SANS_MEETLV2 = "Sans/MeetLv2"
    SANS_MEETLV = "Sans/MeetLv"
    SANS_PASS = "Sans/Pass"
    SANS_INTRO = "Sans/Intro"
    SANS_F = "Sans/F"
    SANS_MP = "Sans/MP"
    SANS_SK = "Sans/SK"
    SANS_SS = "Sans/SS"
    SANS_SS2 = "Sans/SS2"
    PAPYRUS_M1 = "Papyrus/M1"
    PAPYRUS_PS = "Papyrus/PS"
    PAPYRUS_PD = "Papyrus/PD"
    PAPYRUS_PK = "Papyrus/PK"
    FFFFF_F = "FFFFF/F"
    FFFFF_D = "FFFFF/D"
    FFFFF_P = "FFFFF/P"
    FFFFF_E = "FFFFF/E"
    UNDYNE_UD = "Undyne/UD"
    METTATON_BOSSMET = "Mettaton/BossMet"
    METT_O = "Mett/O"
    MTT_ESSAYNO = "MTT/EssayNo"
    ASGORE_KILLYOU = "Asgore/KillYou"
    ALPHYS_AD = "Alphys/AD"
    F7_F7 = "F7/F7"
    ENDF_ENDF = "EndF/EndF"
