from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

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


@login_required
@require_POST
def like_link_post(request, link_post_id):
    link_post = get_object_or_404(LinkPost, id=link_post_id)
    link_post.total_likes += 1
    link_post.liked_by.add(request.user)
    link_post.save()
    return redirect('home:homepage')
