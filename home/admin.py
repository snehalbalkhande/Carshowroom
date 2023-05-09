from django.contrib import admin

# Register your models here.
from .models import Car, Contact

admin.site.register(Car)
admin.site.register(Contact)
