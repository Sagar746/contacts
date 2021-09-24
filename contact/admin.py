from django.contrib import admin

from .models import Contact,Email

# Register your models here.

admin.site.register(Email)
admin.site.register(Contact)