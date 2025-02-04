from django.urls import path
from .views import ActorView,MovieView

urlpatterns = [
    path('actors',ActorView.as_view(),name='actors'),
    path('actors/<int:pk>/',ActorView.as_view(),name='actor'),
    path('movies',MovieView.as_view(),name='movies'),
    path('movies/<int:pk>/',MovieView.as_view(),name='movie')
]