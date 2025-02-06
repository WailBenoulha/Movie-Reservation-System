from django.db import models
from django.db.models import F

class Actors(models.Model):
    name = models.CharField(max_length=255)    

    def __str__(self):
        return self.name

class Movie(models.Model):
    GENRE_CHOICES = [
        ("action", "Action"),
        ("adventure", "Adventure"),
        ("comedy", "Comedy"),
        ("war", "War"),
        ("family", "Family"),
    ]
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255,choices=GENRE_CHOICES)
    actors = models.ManyToManyField(Actors)

    def __str__(self):
        return self.name

class Theatre(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    num_vip_seats = models.IntegerField()
    num_normal_seats = models.IntegerField()

    def __str__(self):
        return self.name

class Movie_shedules(models.Model):
    datetime = models.DateTimeField()    
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre,on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        # vip_count = self.theatre.num_vip_seats
        # normal_count = self.theatre.num_normal_seats

        # for i in range(1,vip_count + 1):
        #     Seats.objects.create(number=i,movie_time_infos=self,seat_type="vip")

        # for i in range(1,normal_count + 1):
        #     Seats.objects.create(number=i,movie_time_infos=self,seat_type="normal") 
        Seats.objects.create(
            movie_time_infos=self,
            number_vip_seats=self.theatre.num_vip_seats,
            number_normal_seats=self.theatre.num_normal_seats,
            fix_vip_seats=self.theatre.num_vip_seats,
            fix_normal_seats=self.theatre.num_normal_seats,            
            ) 

    def __str__(self):
        return f"{self.movie.name} at {self.theatre.name} on {self.datetime}"  


class Seats(models.Model):
    movie_time_infos = models.OneToOneField(Movie_shedules,on_delete=models.CASCADE)
    number_vip_seats = models.IntegerField(editable=False)
    number_normal_seats = models.IntegerField(editable=False)
    fix_vip_seats = models.IntegerField(editable=False)
    fix_normal_seats = models.IntegerField(editable=False)

    
class Ticket(models.Model):
    SEAT_TYPE = [
        ("vip","Vip"),
        ("normal","Normal"),
    ]
    movie_shedule = models.ForeignKey(Movie_shedules,on_delete=models.CASCADE)
    seat_type = models.CharField(max_length=255,choices=SEAT_TYPE)
    username = models.CharField(max_length=255)
    ticket_number = models.IntegerField(editable=False)

    def save(self,*args,**kwargs):
        seat = Seats.objects.get(movie_time_infos=self.movie_shedule)
        
        if self.seat_type == "vip":
            Seats.objects.filter(movie_time_infos=self.movie_shedule).update(
                number_vip_seats=F('number_vip_seats') - 1
            )
            disponible_seats = seat.number_vip_seats
            total_seats = seat.fix_vip_seats
        elif self.seat_type == "normal":
            Seats.objects.filter(movie_schedule=self.movie_shedule).update(
                number_normal_seats=F('number_normal_seats') - 1
            )
            disponible_seats = seat.number_normal_seats
            total_seats = seat.fix_normal_seats

        self.ticket_number = total_seats - disponible_seats    
        super().save(*args,**kwargs)    

    def __str__(self):
        return f"Ticket for {self.username} ({self.seat_type} seat) - {self.movie_shedule.movie.name} at {self.movie_shedule.theatre.name}"