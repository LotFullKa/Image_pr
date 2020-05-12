from django import forms

from main.models import Image


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('characters_cls',
                  'characters_race',)
