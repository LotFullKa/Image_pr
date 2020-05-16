from django.db import models
import os
from django.conf import settings

from apps.main.constants import ClassEnum, RaceEnum, ClsHrefEnum, RaceHrefEnum
from utils.enum_helpers import enum_to_choices


class Image(models.Model):
    img = models.ImageField()

    characters_race = models.CharField(
        max_length=100,
        choices=enum_to_choices(RaceEnum),
    )

    characters_cls = models.CharField(
        max_length=100,
        choices=enum_to_choices(ClassEnum),
    )

    def __str__(self):
        return self.characters_race.__str__() + ' - ' + self.characters_cls.__str__()

    def delete(self, *args, **kwargs):
        if self.img.storage.exist():
            self.img.storage.delete(self.img.name)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'


class Hrefs(models.Model):

    race = models.CharField(
        max_length=200,
        choices=enum_to_choices(RaceEnum),
        default=''
    )

    cls = models.CharField(
        max_length=200,
        choices=enum_to_choices(ClassEnum),
        default=''
    )

    @property
    def race_href(self):
        for k in enum_to_choices(RaceHrefEnum):
            if self.race == k[0]:
                return k[1]

    @property
    def cls_href(self):
        for k in enum_to_choices(ClsHrefEnum):
            if self.cls == k[0]:
                return k[1]

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
