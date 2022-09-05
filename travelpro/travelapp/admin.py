from django.contrib import admin

# Register your models here.
from .models import Place, People

admin.site.register(Place)
admin.site.register(People)