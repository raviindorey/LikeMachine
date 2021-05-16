from django.shortcuts import render

from .models import LinkPost
from .forms import LinkPostForm


def home(request):
    links = LinkPost.objects.all()
    if request.method == 'POST':
        link_post_form = LinkPostForm(request.POST)
        if link_post_form.is_valid():
            link_post_obj = link_post_form.save(commit=False)
            link_post_obj.author = request.user
            link_post_obj.save()

    link_post_form = LinkPostForm()
    return render(request, 'home/homepage.html', {
        'links': links,
        'link_post_form': link_post_form,
    })
