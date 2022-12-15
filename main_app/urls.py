from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('directors/', views.directors_index, name='index'),
    path('directors/<int:director_id>', views.directors_detail, name='detail'),
    path('directors/create/', views.DirectorCreate.as_view(), name='directors_create'),
    path('directors/<int:pk>/update/', views.DirectorUpdate.as_view(), name='directors_update'),
    path('directors/<int:pk>/delete/', views.DirectorDelete.as_view(), name='directors_delete'),
    path('directors/<int:director_id>/add_showing/', views.add_showing, name='add_showing'),
    path('nominations/', views.NominationList.as_view(), name='nominations_index'),
    path('nominations/<int:pk>/', views.NominationDetail.as_view(), name='nominations_detail'),
    path('nominations/create/', views.NominationCreate.as_view(), name='nominations_create'),
    path('nominations/<int:pk>/update/', views.NominationUpdate.as_view(), name='nominations_update'),
    path('nominations/<int:pk>/delete/', views.NominationDelete.as_view(), name='nominations_delete'),
    path('director/<int:director_id>/assoc_nomination/<int:nomination_id>/', views.assoc_nomination, name='assoc_nomination'),
    path('director/<int:director_id>/unassoc_nomination/<int:nomination_id>/', views.unassoc_nomination, name='unassoc_nomination'),
]