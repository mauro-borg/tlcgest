from django.contrib import admin

# Register your models here.

from .models import Sim, SimProfile, MobileDevice, MobileDeviceModel, \
     MobileDeviceStatus, MobileOwner, MobileDeviceAssignment, MobileUser, \
     MobilePhoneNumber, MobilePhoneNumberEvent

admin.site.register(Sim)
admin.site.register(SimProfile)
admin.site.register(MobileDevice)
admin.site.register(MobileDeviceModel)
admin.site.register(MobileDeviceStatus)
admin.site.register(MobileOwner)
admin.site.register(MobileDeviceAssignment)
admin.site.register(MobileUser)
admin.site.register(MobilePhoneNumber)
admin.site.register(MobilePhoneNumberEvent)

