from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="songs"),
    path("artist",views.Artists,name="artist"),
    path("artist/<str:artist_name>",views.artist_songs,name="artist_songs"),
]