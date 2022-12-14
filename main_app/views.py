from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Director
from .forms import ShowingForm

class DirectorCreate(CreateView):
    model = Director
    fields = '__all__'

class DirectorUpdate(UpdateView):
    model = Director
    fields = ['nationality', 'description', 'age']

class DirectorDelete(DeleteView):
    model = Director
    success_url = '/directors/'


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def directors_index(request):
    directors = Director.objects.all()
    return render(request, 'directors/index.html', { 'directors': directors})

def directors_detail(request, director_id):
  director = Director.objects.get(id=director_id)
  showing_form = ShowingForm()
  return render(request, 'directors/detail.html', {
    'director': director,
    'showing_form': showing_form
    })

def add_showing(request, director_id):
  form = ShowingForm(request.POST)
  if form.is_valid():
    new_showing = form.save(commit=False)
    new_showing.director_id = director_id
    new_showing.save()
  return redirect('detail', director_id=director_id)


#   Basic old way limited db:
# class Director: 
#   def __init__(self, name, nationality, description, age):
#     self.name = name
#     self.nationality = nationality
#     self.description = description
#     self.age = age

# directors = [
#   Director('Martin Scorsese', 'American', 'Master of crime dramas', 80),
#   Director('Christopher Nolan', 'British', 'Loves to use non-linear story-telling', 52),
#   Director('Akira Kurosawa', 'Japanese', 'Legendary sammurai movie director', 0)
# ]