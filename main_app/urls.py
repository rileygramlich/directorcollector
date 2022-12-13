from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('directors/', views.directors_index, name='index'),
    path('directors/<int:director_id>', views.directors_detail, name='detail'),
    path('directors/create/', views.DirectorCreate.as_view(), name='directors_create'),
    path('directors/<int:pk>/update/', views.DirectorUpdate.as_view(), name='directors_update'),
    path('directors/<int:pk>/delete/', views.DirectorDelete.as_view(), name='directors_delete')
]