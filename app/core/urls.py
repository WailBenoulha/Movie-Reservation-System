from django.urls import path
from .views import ActorView

urlpatterns = [
    path('actors',ActorView.as_view(),name='actors'),
    path('actors/<int:pk>/',ActorView.as_view(),name='actors')
]