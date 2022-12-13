from django.contrib import admin

# Register your models here.
from .models import Director, Showing

admin.site.register(Director)
admin.site.register(Showing)