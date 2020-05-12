from django.shortcuts import render

from main.models import Image
from main.form import ImageForm
from main import constants


def index(request):
    form = ImageForm(request.GET)
    if form.is_valid() and 'find' in request.GET:
        last_minks = Image.objects.filter(
            characters_race=form.instance.characters_race,
            characters_cls=form.instance.characters_cls,
        )
    else:
        last_minks = Image.objects.all()

    form.fields['characters_cls'].widget.attrs = {'class': 'custom-select'}
    form.fields['characters_race'].widget.attrs = {'class': 'custom-select'}
    return render(request, 'minky/cartoons.html',
                  {'last_minks': last_minks,
                   'form': form,
                   })
