from django.urls import path

from .views import home, like_link_post, delete_link_post

app_name = 'home'

urlpatterns = [
    path('like/', like_link_post, name='like_link_post'),
    path('delete/', delete_link_post, name='delete_link_post'),
    path('', home, name='homepage'),
]
