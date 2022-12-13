from django.db import models
from django.urls import reverse
from datetime import date, timedelta

GENRES = (
    ('D', 'drama'),
    ('C', 'comedy'),
    ('R', 'romance'),
    ('A', 'action'),
)

# Create your models here.
class Director(models.Model): 
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'director_id': self.id})

    # def film_within_4years(self):
    #     four_years_from_now = (date.today() + timedelta(days=1461))
    #     print(four_years_from_now)
    #     film_within_4Years = self.showing_set.filter(date.today() > date > timedelta(days=1461)))
    #     return film_within_4Years

class Showing(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=1,
        choices=GENRES,
        default=GENRES[0][0]
        )
    # Because Django:
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        #get_genre_display() built in with django?
        return f"The {self.get_genre_display()} {self.name} is showing on {self.date}."