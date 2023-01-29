from django.db import models

class CiscoSwitch(models.Model):
    device_type = models.CharField(max_length=255)
    host = models.GenericIPAddressField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
