from django.shortcuts import render

from .models import LinkPost


def home(request):
    links = LinkPost.objects.all()
    return render(request, 'home/homepage.html', {
        'links': links
    })
