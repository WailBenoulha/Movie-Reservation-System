from django.urls import path
from .views import (ActorListView,ActorDetailView,
                    MovieListView,MovieDetailView,
                    TheatreView,MovieSheduleView,
                    get_seats)

urlpatterns = [
    path('actors',ActorListView.as_view(),name='actors'),
    path('actors/<int:pk>/',ActorDetailView.as_view(),name='actor'),
    path('movies',MovieListView.as_view(),name='movies'),
    path('movies/<int:pk>/',MovieDetailView.as_view(),name='movie'),
    path('theatres',TheatreView.as_view(),name='theatres'),
    path('theatres/<int:pk>/',TheatreView.as_view(),name='theatre'),
    path('shedules',MovieSheduleView.as_view(),name='shedules'),
    path('seats',get_seats,name='seats'),
    path('seats/<int:pk>/',get_seats,name='seats'),
]