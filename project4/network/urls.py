
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("following_posts", views.following_posts, name='following_posts'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('user/<slug:user_slug>', views.user_page_view, name='user_page_view'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('like/<int:post_id>', views.like_post, name='like_post'),
]
