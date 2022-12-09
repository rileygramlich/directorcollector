from django.shortcuts import render
from django.http import HttpResponse


class Director: 
  def __init__(self, name, nationality, description, age):
    self.name = name
    self.nationality = nationality
    self.description = description
    self.age = age

directors = [
  Director('Martin Scorsese', 'American', 'Master of crime dramas', 80),
  Director('Christopher Nolan', 'British', 'Loves to use non-linear story-telling', 52),
  Director('Akira Kurosawa', 'Japanese', 'Legendary sammurai movie director', 0)
]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello welcome to the Director Collector</h1> ') # render homepage later

def about(request):
    return render(request, 'about.html')

def directors_index(request):
    return render(request, 'directors/index.html', { 'directors': directors})