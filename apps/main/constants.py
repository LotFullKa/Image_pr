from enum import Enum


class RaceEnum(Enum):
    NONE = 'none'
    HUMAN = 'Human'
    ELF = 'Elf'
    HALF_ELF = 'Half_Elf'
    GNOME = 'Gnome'
    HALFLING = 'Halfling'


class ClassEnum(Enum):
    NONE = 'none'
    DRUID = 'Druid'
    WIZARD = 'Wizard'
    BARD = 'Bard'
    RANGER = 'Ranger'
