from django.shortcuts import render, redirect

from main.models import Image
from main.form import ImageForm, HrefsFrom, ImageForUploadForm


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


def upload_img(request):
    if request.method == "POST":
        form_for_upload = ImageForUploadForm(request.POST, request.FILES)

        if form_for_upload.is_valid():
            form_for_upload.save()
            return redirect('index')
    else:
        form_for_upload = ImageForUploadForm()
    return render(request, 'minky/upload.html', {
        'form_for_upload': form_for_upload,
    })


def home(request):
    form = HrefsFrom(request.GET)
    if form.is_valid():
        race_href = form.instance.race_href
        cls_href = form.instance.cls_href
    else:
        race_href = None
        cls_href = None

    return render(request, 'home.html',
                  {'form': form,
                   'race_href': race_href,
                   'cls_href': cls_href
                   })
