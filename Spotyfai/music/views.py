from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist, Song

#import models of the app users

from users.models import User
    
    #CREATE ARTIST
    
def create_artist(request):
    new_artist = Artist.objects.create(name_artist = "junior h",
                                       genero = "regional mexicano")
    
    return HttpResponse("new artist create")

def delete_artist(request):
    id_artist = 1
    rm_artist = Artist.objects.get(id = id_artist)
    name_rm_artist = rm_artist.name_artist
    rm_artist.delete()
    return HttpResponse(f"artist {name_rm_artist} to delete")

def reset_data_artist(request):
    new_name_artist = "natagod"
    new_genero = "corridos tumbados"
    reset_id_data_artist = 1
    try:
        data_reset_artist = Artist.objects.get(id = reset_data_artist)
    except Artist.DoesNotExist:
        return HttpResponse(f"user of id {reset_id_data_artist} not exist")
    data_reset_artist.name_artist = new_name_artist
    data_reset_artist.genero = new_genero
    return HttpResponse(f"modification of user for data name and genero for {new_name_artist} and {new_genero}")

def get_data_artist(request):
    id_get_artist = 1
    try:
        get_artist = Artist.objects.get(id = id_get_artist)
    except Artist.DoesNotExist:
        return HttpResponse("user do not exist")
    return render(request, "data_artist.html", {"list_data_artist":get_artist})

#functions of the model song

    #CREATE SONG

def create_song(request):
    try:
        artist_relation_foreignkey = Artist.objects.get(id = 4)
    except Artist.DoesNotExist:
        return HttpResponse("user do not exist")
    name_song = "el de la chevy"
    letter = """Viene en su Chevy silverado
Allá por Denver, Colorado lo miran
Siempre, trae gorra el muchacho
De buen estilo y muy buen porte al caminar
Tiene sangre de Zacatécas
Su padre y madre se lo vinieron a dar
Tiene la sangre entre sus venas
Es cailentito si lo hacen enojar
Allá por el freeway, la Chevy va bramando
O llanta va quemando
Siempre bien al tiro
Con corridos sonando
Al junior va sonando
Cuelga un San Júdas en el pecho
Es el déboto y el santito lo cuida
Tiene ya tiempo trabajando
Y los gustitos a él le gusta agarrar
Ruge el motor alterado
En varias de sus trocas ya lo han visto andar
Allá en los arrancones
Me han visto celebrando
Las trocas van sonando
Y la Chevy
De vista y caliente
Aquí traigo una plebita
Soy enamorado, ahí nomás pa terminar"""
    copyright_song = True
    new_song = Song.objects.create(artist = artist_relation_foreignkey,
                                   name_song = name_song,
                                   letter = letter,
                                   copyright_song = copyright_song,
                                   )
    return HttpResponse("song upload")

def delete_song(request):
    id_song = 1
    try:
        rm_song = Song.objects.get(id = id_song)
    except Song.DoesNotExist:
        return HttpResponse("Song not exist")
    name_rm_song = rm_song.name_song
    rm_song.delete()
    return HttpResponse(f"song {name_rm_song} to delete")

def get_data_song(request):
    id_song = 1
    try:    
        get_song = Song.objects.get(id = id_song)
    except Song.DoesNotExist:
        return HttpResponse("song not exist")
    data_song = {
        "name_artist" : get_song.artist.name_artist,
        "name_song" : get_song.name_song,
        "copyright_song" : get_song.copyright_song,
    }
    return render(request, "data_song.html", {"data_song_list" : data_song})
    

    
    
    
    
    
    
    
    