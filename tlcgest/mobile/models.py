from django.db import models

# Create your models here.

class MobileUser(models.Model):
    userid = models.CharField(max_length=20, primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    cod_fis = models.CharField(max_length=16)
    vip = models.BooleanField(default=False)
    org_unit = models.CharField(max_length=20)


class SimProfile(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)



class Sim(models.Model):
    USAGE_CHOICES = [
            ('P', 'Telephony'),
            ('I', 'Internet Key'),
            ('W', 'Twin Card'),
            ('R', 'Router'),
            ('T', 'Tablet'),
            ('H', 'Hybrid'),
            ('O', 'Other'),
            ]
    SIM_TYPE_CHOICES = [
            ('D', 'DATA'),
            ('V', 'VOICE'),
            ]

    iccid = models.CharField(max_length=20)
    pin = models.CharField(max_length=5)
    puk = models.CharField(max_length=11)
    profile = models.ForeignKey(SimProfile, on_delete=models.SET_NULL, null=True)
    usage = models.CharField(max_length=1, choices=USAGE_CHOICES)
    sim_type = models.CharField(max_length=1, choices=SIM_TYPE_CHOICES)
    active = models.BooleanField(default=False)
    invisible = models.BooleanField(default=False)

    user = models.ForeignKey(MobileUser, on_delete=models.SET_NULL, null=True)

class MobileDeviceModel(models.Model):
    name = models.CharField(max_length=50)
    variant = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)

class MobileDeviceOwner(models.Model):
    owner = models.CharField(max_length=50)

class MobileDeviceStatus(models.Model):
    status = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

class MobileDevice(models.Model):
    imei = models.CharField(max_length=16, unique=True)
    model = models.ForeignKey(MobileDeviceModel, on_delete=models.CASCADE)
    serial_no = models.CharField(max_length=30)
    owner = models.ForeignKey(MobileDeviceOwner, on_delete=models.CASCADE)
    status = models.ForeignKey(MobileDeviceStatus, on_delete=models.SET_NULL, null=True)
    notes = models.TextField()
    date_purchased = models.DateField()
    installed_sim = models.ForeignKey(Sim, on_delete=models.SET_NULL, null=True)
    assignment = models.ManyToManyField(MobileUser, through='MobileDeviceAssignment')

class MobileDeviceAssignment(models.Model):
    DOCS_STATUS_CHOICES = [
            ('S', 'Sent'),
            ('R', 'Received'),
            ('C', 'Completed'),
            ('U', 'Unknown'),
            ]
    MODE_CHOICES = [
            ('T', 'Temporary'),
            ('P', 'Permanent'),
            ]
    device = models.ForeignKey(MobileDevice, on_delete=models.CASCADE)
    user = models.ForeignKey(MobileUser, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_stop = models.DateField()
    docs_status = models.CharField(max_length=1, choices=DOCS_STATUS_CHOICES)
    mode = models.CharField(max_length=1, choices=MODE_CHOICES)



