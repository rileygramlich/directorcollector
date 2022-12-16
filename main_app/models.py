from django.db import models
from django.urls import reverse
from datetime import date, timedelta
from django.contrib.auth.models import User

GENRES = (
    ('D', 'drama'),
    ('C', 'comedy'),
    ('R', 'romance'),
    ('A', 'action'),
)

RESULTS = (
    ('W', 'won'),
    ('L', 'lost')
)

class Nomination(models.Model):
    type = models.CharField(max_length=100)
    result = models.CharField(
    max_length=1,
    choices=RESULTS,
    default=RESULTS[0][0]
  )

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('nomination_detail', kwargs={'pk': self.id})

# Create your models here.
class Director(models.Model): 
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    nominations = models.ManyToManyField(Nomination)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'director_id': self.id})

    def film_within_4years(self):
        print(f'Printing showing set: {self.showing_set}')
        film_release = self.showing_set.filter(date.today() > date > timedelta(days=1461))
        return film_release

    def showing_a_film(self):
        isnt_showing = Showing.objects.exclude(id__in = self.showing_set.all().values_list('id'))
        return isnt_showing

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


