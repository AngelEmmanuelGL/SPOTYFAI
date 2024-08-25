from django.urls import path, include
from . import views

urlpatterns = [
    path("create_user/", views.create_user, name = "create_user"),
    path("delete_user/", views.delete_user, name = "delete_user"),
    path("reset_data_user/", views.reset_data_user, name = "reset_data_user"),
    path("get_all_user/", views.get_all_user, name = "get_all_user"),
    path("music/", include("music.urls"))
]