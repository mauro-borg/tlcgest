from django.db import models

# Create your models here.

class MobileUser(models.Model):
    userid = models.CharField(max_length=20, primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    cod_fis = models.CharField(max_length=16, blank=True, null=True)
    vip = models.BooleanField(default=False)
    org_unit = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.userid, self.last_name, self.first_name)

# owner = company name, or 'personal'
class MobileOwner(models.Model):
    owner = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.owner)



class SimProfile(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.name)


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
    SIM_FORMAT_CHOICES = [
            ('F', 'Full-size'),
            ('M', 'Mini-SIM'),
            ('U', 'Micro-SIM'),
            ('N', 'Nano-SIM'),
            ('E', 'eSIM'),
            ]
    iccid = models.CharField(max_length=20)
    pin = models.CharField(max_length=5)
    puk = models.CharField(max_length=11)
    imsi = models.CharField(max_length=16, blank=True, null=True)
    profile = models.ForeignKey(SimProfile, on_delete=models.SET_NULL, null=True)
    usage = models.CharField(max_length=1, choices=USAGE_CHOICES, default='P')
    sim_type = models.CharField(max_length=1, choices=SIM_TYPE_CHOICES, default='V')
    sim_format = models.CharField(max_length=1, choices=SIM_FORMAT_CHOICES, default='N')
    active = models.BooleanField(default=False)
    invisible = models.BooleanField(default=False)

    user = models.ForeignKey(MobileUser, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.iccid)


class MobilePhoneNumber(models.Model):
    number = models.CharField(max_length=20, primary_key=True)
    sim = models.ForeignKey(Sim, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(MobileUser, on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField(default=True)
    ok_to_show = models.BooleanField(default=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(MobileOwner, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.number)

class MobilePhoneNumberEvent(models.Model):
    EVENT_CHOICES = [
            ('A', 'Activation'),
            ('C', 'Cessation'),
            ('T', 'Takeover'),
            ('K', 'Ok to takeover'),
            ('X', 'SIM change'),
            ('U', 'Transfer to other user'),
            ('O', 'Other'),
            ]
    number = models.ForeignKey(MobilePhoneNumber, on_delete=models.CASCADE)
    date = models.DateField()
    event = models.CharField(max_length=1, choices=EVENT_CHOICES)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return '%s %s %s' % (self.number, self.date, self.event)


class MobileDeviceModel(models.Model):
    name = models.CharField(max_length=50)
    variant = models.CharField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.manufacturer, self.name)


class MobileDeviceStatus(models.Model):
    status = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.status)


class MobileDevice(models.Model):
    imei = models.CharField(max_length=16, unique=True)
    model = models.ForeignKey(MobileDeviceModel, on_delete=models.CASCADE)
    serial_no = models.CharField(max_length=30, blank=True, null=True)
    owner = models.ForeignKey(MobileOwner, on_delete=models.CASCADE)
    status = models.ForeignKey(MobileDeviceStatus, on_delete=models.SET_NULL, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    date_purchased = models.DateField(blank=True, null=True)
    installed_sim = models.ForeignKey(Sim, on_delete=models.SET_NULL, blank=True, null=True)
    assignment = models.ManyToManyField(MobileUser, through='MobileDeviceAssignment')

    def __str__(self):
        return '%s' % (self.imei)


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
    date_stop = models.DateField(blank=True, null=True)
    docs_status = models.CharField(max_length=1, choices=DOCS_STATUS_CHOICES, default='U')
    mode = models.CharField(max_length=1, choices=MODE_CHOICES, default='P')

    def __str__(self):
        return '%s %s' % (self.device, self.user)

