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


class RaceHrefEnum(Enum):
    HUMAN = 'https://dungeon.su/articles/race/81-human/'
    ELF = 'https://dungeon.su/articles/race/79-elf/'
    HALF_ELF = 'https://dungeon.su/articles/race/84-half_elf/'
    GNOME = 'https://dungeon.su/articles/race/83-gnome/'
    HALFLING = 'https://dungeon.su/articles/race/80-halfling/'


class ClsHrefEnum(Enum):
    DRUID = 'https://dungeon.su/articles/class/90-druid/'
    WIZARD = 'https://dungeon.su/articles/class/105-wizard/'
    BARD = 'https://dungeon.su/articles/class/88-bard/'
    RANGER = 'https://dungeon.su/articles/class/97-ranger/'
