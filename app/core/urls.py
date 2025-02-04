from django.urls import path
from .views import ActorListView,ActorDetailView,MovieListView,MovieDetailView,TheatreView

urlpatterns = [
    path('actors',ActorListView.as_view(),name='actors'),
    path('actors/<int:pk>/',ActorDetailView.as_view(),name='actor'),
    path('movies',MovieListView.as_view(),name='movies'),
    path('movies/<int:pk>/',MovieDetailView.as_view(),name='movie'),
    path('theatres',TheatreView.as_view(),name='theatres'),
    path('theatres/<int:pk>/',TheatreView.as_view(),name='theatre')
]