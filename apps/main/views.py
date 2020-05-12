from django.shortcuts import render

from main.models import Image
from main.form import ImageForm


def index(request):
    form = ImageForm(request.GET)
    if form.is_valid() and form.instance.characters_race != '' and form.instance.characters_cls != '':
        last_minks = Image.objects.filter(
            characters_race=form.instance.characters_race,
            characters_cls=form.instance.characters_cls,
        )
    else:
        last_minks = Image.objects.all()

    return render(request, 'minky/cartoons.html',
                  {'last_minks': last_minks,
                   'form': form,
                   })
