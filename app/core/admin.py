from django.contrib import admin
from .models import CustomUser,Actors,Movie,Theatre,Movie_shedules,Seats,Ticket

admin.site.register(CustomUser)
admin.site.register(Actors)
admin.site.register(Movie)
admin.site.register(Movie_shedules)
admin.site.register(Theatre)
admin.site.register(Seats)
admin.site.register(Ticket)