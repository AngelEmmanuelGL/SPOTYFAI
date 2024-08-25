from . import views
from django.urls import path
urlpatterns = [
    path("create_artist/", views.create_artist, name = "create_artist"),
    path("delete_artist/", views.delete_artist, name = "delete_artist"),
    path("reset_data_artist/", views.reset_data_artist, name = " reset_data_artist"),
    path("get_data_artist/", views.get_data_artist, name = "get_data_artist"),
    path("create_song/", views.create_song, name = "create_song"),
    path("delete_song/", views.delete_song, name = "delete_song"),
    path("get_data_song/", views.get_data_song, name = "get_data_song"),
]