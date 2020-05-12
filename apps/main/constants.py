from enum import Enum


class RaceEnum(Enum):
    NONE = ''
    HUMAN = 'Human'
    ELF = 'Elf'
    HALF_ELF = 'Half_Elf'
    GNOME = 'Gnome'
    HALFLING = 'Halfling'


class ClassEnum(Enum):
    NONE = ''
    DRUID = 'Druid'
    WIZARD = 'Wizard'
    BARD = 'Bard'
    RANGER = 'Ranger'
