from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="posts-index"),
    path("about/", views.about, name="posts-about")
]
