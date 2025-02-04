from django.db import models

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

        vip_count = self.theatre.num_vip_seats
        normal_count = self.theatre.num_normal_seats

        for i in range(1,vip_count + 1):
            Seats.objects.create(number=i,movie_time_infos=self,seat_type="vip")

        for i in range(1,normal_count + 1):
            Seats.objects.create(number=i,movie_time_infos=self,seat_type="normal")  

    def __str__(self):
        return f"{self.movie.name} at {self.theatre.name} on {self.datetime}"  


class Seats(models.Model):
    TYPE_CATEGORIE = [
        ("vip", "Vip"),
        ("normal", "Normal"),
    ]
    number = models.IntegerField()  
    movie_time_infos = models.ForeignKey(Movie_shedules,on_delete=models.CASCADE)
    seat_type = models.CharField(max_length=255,choices=TYPE_CATEGORIE)

    def __str__(self):
        return f"{self.movie_time_infos.movie} - {self.movie_time_infos.movie} - {self.movie_time_infos.datetime} - Seat {self.number} - {self.seat_type}"

class Ticket(models.Model):
    seat = models.ForeignKey(Seats,on_delete=models.CASCADE)
    username = models.CharField(max_length=255)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        self.seat.delete()

    def __str__(self):
        return f"Ticket for {self.username} - Seat {self.seat.number} ({self.seat.seat_type})"