from django.contrib import admin

# Register your models here.
from .models import User, Bunk

admin.site.register(User)
admin.site.register(Bunk)