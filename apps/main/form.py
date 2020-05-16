from django import forms

from main.models import Image, Hrefs


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('characters_cls',
                  'characters_race',)


class ImageForUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('characters_cls',
                  'characters_race',
                  'img',)


class HrefsFrom(forms.ModelForm):

    class Meta:
        model = Hrefs
        fields = ('race',
                  'cls',
                  )
