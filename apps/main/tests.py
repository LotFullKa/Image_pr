from django.test import TestCase
from main.constants import ClsHrefEnum, ClassEnum, RaceHrefEnum, RaceEnum
from main.models import Image, Hrefs
from utils.enum_helpers import random_enum_choice, enum_to_choices


class HrefsTestCase(TestCase):

    def test_race_href(self):
        subject = Hrefs()
        subject.race = random_enum_choice(RaceEnum)
        for k in enum_to_choices(RaceHrefEnum):
            if k[1] == subject.race_href:
                self.assertEqual(k[0], subject.race)

    def test_cls_href(self):
        subject = Hrefs()
        subject.cls = random_enum_choice(ClassEnum)
        for k in enum_to_choices(ClsHrefEnum):
            if k[1] == subject.cls_href:
                self.assertEqual(k[0], subject.cls)


class ImageTestCase(TestCase):

    def test_str(self):
        subject = Image()
        subject.characters_cls = enum_to_choices(ClassEnum)[0]
        subject.characters_race = enum_to_choices(RaceEnum)[0]
        self.assertEqual(subject.__str__(),
                enum_to_choices(RaceEnum)[0].__str__() + ' - ' + enum_to_choices(ClassEnum)[0].__str__())
