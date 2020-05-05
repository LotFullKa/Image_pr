from django.db import models


class Image(models.Model):
    img = models.ImageField


class chr_class(models.Model):
    name = models.CharField(max_length=100, null=False)
    characters_cls = models.ForeignKey(
        to='models.Image',
        on_delete=models.SET_NULL
    )


class chr_race(models.Model):
    name = models.CharField(
        max_length=100,
        choices=enum_to_choices(),
        null=False
    )
