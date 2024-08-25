from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from music.models import Artist, Song

def index(request):
    list_your_artist = Artist.objects.all()
    return render(request, "index.html", {"list_artist":list_your_artist})

def song(request, id):
    try:
        get_list_artist = Artist.objects.get(id = id)
    except Artist.DoesNotExist:
        return HttpResponse("song not exist")
    song_list = Song.objects.filter(artist = get_list_artist) 
    if not song_list.exists():
        return HttpResponse("artist not music upload")
    artist_data = {
        "song_list":song_list,
        "name_artist":get_list_artist.name_artist,
    }
    return render(request, "songlist.html", {"artist_data":artist_data})

def song_play(request, id):
    try:
        song_get = Song.objects.get(id = id)
    except Song.DoesNotExist:
        return HttpResponse(f"{id} not found")
    return render(request, "song.html", {"data_song":song_get})
