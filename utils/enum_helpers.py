
from enum import Enum
from typing import Tuple, List, Type


def enum_to_choices(enum: Type[Enum]) -> List[Tuple]:
    """Convert enum to django choices."""

    return [(item.name, str(item.value)) for item in enum]
