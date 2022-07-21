from django.contrib import admin

# import your models here
from .models import Cultivation, Hoya

# Register your models here
admin.site.register(Hoya)
admin.site.register(Cultivation)