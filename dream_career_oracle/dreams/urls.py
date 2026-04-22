from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dreams/", views.dream_list, name="dream_list"),
    path("dream/create/", views.create_dream, name="create_dream"),
    path("dream/<int:pk>/", views.dream_detail, name="dream_detail"),
    path("dream/<int:pk>/like/", views.like_dream, name="like_dream"),
    path("dream/<int:pk>/delete/", views.delete_dream, name="delete_dream"),
    path("dream/<int:dream_id>/add_step/", views.add_step, name="add_step"),
    path("step/<int:step_id>/edit/", views.edit_step, name="edit_step"),
    path("step/<int:step_id>/delete/", views.delete_step, name="delete_step"),
    path("dream/<int:pk>/edit/", views.edit_dream, name="edit_dream"),
]
