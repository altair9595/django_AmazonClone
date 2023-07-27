from django.contrib import admin
from .models import profile , Address , Phones

# Register your models here.
admin.site.register(profile)
admin.site.register(Address)
admin.site.register(Phones)