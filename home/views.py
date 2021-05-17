from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import DateField
from django.db.models.functions import Trunc

from common.decorators import ajax_required

from .models import LinkPost
from .forms import LinkPostForm


def home(request):
    """
    Homepage view loads all the LinkPosts
    and a form to create LinkPost
    """

    # linkposts are ordered by day then by total likes they have
    links = LinkPost.objects.annotate(
        day_created=Trunc('created', 'day', output_field=DateField()))\
        .order_by('-day_created', '-total_likes')

    # create a linkpost
    if request.method == 'POST':
        link_post_form = LinkPostForm(request.POST)
        if link_post_form.is_valid():
            link_post_obj = link_post_form.save(commit=False)
            link_post_obj.author = request.user
            link_post_obj.save()

    # linkpost form
    link_post_form = LinkPostForm()

    # get posts already liked by logged-in user
    user_likes = None
    if request.user.is_authenticated:
        user_likes = LinkPost.objects.filter(liked_by=request.user)

    return render(request, 'home/homepage.html', {
        'links': links,
        'link_post_form': link_post_form,
        'user_likes': user_likes,
    })


@ajax_required
@require_POST
@login_required
def like_link_post(request):
    """
    Ajax view to like/unlike a linkpost
    gets linkpost id and action from request data
    """
    link_post_id = request.POST.get('id')
    action = request.POST.get('action')
    if link_post_id and action:
        try:
            link_post = LinkPost.objects.get(id=link_post_id)
            if action == 'like':
                # Prevent multiple like requests
                if not LinkPost.objects.filter(liked_by=request.user):
                    link_post.total_likes += 1
                    link_post.liked_by.add(request.user)
            else:
                # Prevent multiple unlike requests
                if LinkPost.objects.filter(liked_by=request.user):
                    link_post.total_likes -= 1
                    link_post.liked_by.remove(request.user)
            link_post.save()

            return JsonResponse({
                'status': 'ok',
                'link_post_id': link_post_id
            })

        except LinkPost.DoesNotExist:
            return JsonResponse({'status': 'ko'})

    return JsonResponse({'status': 'ko'})


@ajax_required
@require_POST
@login_required
def delete_link_post(request):
    """
    Ajax view to delete a linkpost
    """
    link_post_id = request.POST.get('id')
    action = request.POST.get('action')
    if link_post_id and action:
        try:
            link_post = LinkPost.objects.get(id=link_post_id)
            if action == 'delete':
                # Only author should be able to delete its post
                if link_post.author == request.user:
                    link_post.delete()

            return JsonResponse({
                'status': 'ok',
                'link_post_id': link_post_id
            })

        except LinkPost.DoesNotExist:
            return JsonResponse({'status': 'ko'})

    return JsonResponse({'status': 'ko'})
