from django.urls import path
from .views import ActorView,MovieView,TheatreView

urlpatterns = [
    path('actors',ActorView.as_view(),name='actors'),
    path('actors/<int:pk>/',ActorView.as_view(),name='actor'),
    path('movies',MovieView.as_view(),name='movies'),
    path('movies/<int:pk>/',MovieView.as_view(),name='movie'),
    path('theatres',TheatreView.as_view(),name='theatres'),
    path('theatres/<int:pk>/',TheatreView.as_view(),name='theatre')
]