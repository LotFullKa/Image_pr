from django.shortcuts import render

from main.models import Image


def index(request):
    last_minks = Image.objects.order_by()
    return render(request, 'minky/minks.html', {'last_minks': last_minks})
