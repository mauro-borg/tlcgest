from django.contrib import admin

# Register your models here.

from .models import Sim, MobileDevice

admin.site.register(Sim)
admin.site.register(MobileDevice)

