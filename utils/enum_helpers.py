
from enum import Enum
import random
from typing import Tuple, List, Type


def enum_to_choices(enum: Type[Enum]) -> List[Tuple]:
    """Convert enum to django choices."""

    return [(item.name, str(item.value)) for item in enum]


def enum_to_key_list(enum: Type[Enum]) -> List[str]:
    """Convert enum to list of keys."""

    return [item.name for item in enum]


def random_enum_key(enum: Type[Enum]) -> str:
    """Return random enum key."""

    return random.choice(enum_to_key_list(enum))


def random_enum_choice(enum: Type[Enum]) -> Tuple:
    """Return random enum tuple"""

    return random.choice(enum_to_choices(enum))
