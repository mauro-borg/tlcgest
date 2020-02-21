from django.contrib import admin

# Register your models here.

from .models import Sim, SimProfile, MobileDevice, MobileDeviceModel, \
     MobileDeviceStatus, MobileDeviceOwner, MobileDeviceAssignment, MobileUser

admin.site.register(Sim)
admin.site.register(SimProfile)
admin.site.register(MobileDevice)
admin.site.register(MobileDeviceModel)
admin.site.register(MobileDeviceStatus)
admin.site.register(MobileDeviceOwner)
admin.site.register(MobileDeviceAssignment)
admin.site.register(MobileUser)

