from enum import Enum


class RaceEnum(Enum):
    HUMAN = 'Human'
    ELF = 'Elf'
    HALF_ELF = 'Half_Elf'
    GNOME = 'Gnome'
    HALFLING = 'Halfling'


class ClassEnum(Enum):
    DRUID = 'Druid'
    WIZARD = 'Wizard'
    BARD = 'Bard'
    RANGER = 'Ranger'
