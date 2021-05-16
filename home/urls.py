from django.urls import path

from .views import home, like_link_post

app_name = 'home'

urlpatterns = [
    path('<int:link_post_id>/like', like_link_post, name='like_link_post'),
    path('', home, name='homepage'),
]
