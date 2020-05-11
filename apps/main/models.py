from django.db import models
import os
from django.conf import settings

from apps.main.constants import ClassEnum, RaceEnum
from utils.enum_helpers import enum_to_choices


class Image(models.Model):
    img = models.ImageField()

    characters_cls = models.CharField(
        max_length=100,
        choices=enum_to_choices(ClassEnum),
        null=False,
        default=ClassEnum.NONE,
    )

    characters_race = models.CharField(
        max_length=100,
        choices=enum_to_choices(RaceEnum),
        null=False,
        default=RaceEnum.NONE,
    )

    def __str__(self):
        return self.characters_race.__str__() + ' - ' + self.characters_cls.__str__()

    def delete(self, *args, **kwargs):

        # try:
        #     os.remove(self.img.path)
        # except FileNotFoundError:
        #     pass
        if self.img.storage.exist():
            self.img.storage.delete(self.img.name)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
