from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Director, Nomination
from .forms import ShowingForm

class DirectorCreate(CreateView):
    model = Director
    fields = '__all__'

    def form_valid(self, form):
      # Assign the logged in user (self.request.user)
      form.instance.user = self.request.user  # form.instance is the cat
      # Let the CreateView do its job as usual
      return super().form_valid(form)

class DirectorUpdate(LoginRequiredMixin, UpdateView):
    model = Director
    fields = ['nationality', 'description', 'age']

class DirectorDelete(LoginRequiredMixin, DeleteView):
    model = Director
    success_url = '/directors/'


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def directors_index(request):
    directors = Director.objects.filter(user=request.user)
    return render(request, 'directors/index.html', { 'directors': directors})

@login_required
def directors_detail(request, director_id):
  director = Director.objects.get(id=director_id)
  showing_form = ShowingForm()
  nominations_director_doesnt_have = Nomination.objects.exclude(id__in = director.nominations.all().values_list('id'))
  return render(request, 'directors/detail.html', {
    'director': director,
    'showing_form': showing_form,
    'nominations_director_doesnt_have': nominations_director_doesnt_have
    })

@login_required
def add_showing(request, director_id):
  form = ShowingForm(request.POST)
  if form.is_valid():
    new_showing = form.save(commit=False)
    new_showing.director_id = director_id
    new_showing.save()
  return redirect('detail', director_id=director_id)

@login_required
def assoc_nomination(request, director_id, nomination_id):
  Director.objects.get(id=director_id).nominations.add(nomination_id)
  return redirect('detail', director_id=director_id)

@login_required
def unassoc_nomination(request, director_id, nomination_id):
  Director.objects.get(id=director_id).nominations.remove(nomination_id)
  return redirect('detail', director_id=director_id)


class NominationList(LoginRequiredMixin, ListView):
  model = Nomination

class NominationDetail(LoginRequiredMixin, DetailView):
  model = Nomination

class NominationCreate(LoginRequiredMixin, CreateView):
  model = Nomination
  fields = '__all__'

class NominationUpdate(LoginRequiredMixin, UpdateView):
  model = Nomination
  fields = ['type', 'won']

class NominationDelete(LoginRequiredMixin, DeleteView):
  model = Nomination
  success_url = '/nominations/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



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