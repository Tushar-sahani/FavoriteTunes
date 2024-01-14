from django.shortcuts import render

from .models import Song,Artist

def index(request):
    songs = Song.objects.all()
    # print(songs)
    return render(request,"TuneTracker/index.html",{"songs":songs, "i":1})

def Artists(request):
    artist = Artist.objects.all()
    return render(request,"TuneTracker/index.html",{"artists":artist})

def artist_songs(request,artist_name):
    songs = Song.objects.filter(artist = artist_name)
    return render(request,"TunerTracker/artist_Songs.html",{"name":artist_name,"songs":songs})
    