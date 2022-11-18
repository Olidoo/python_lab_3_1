from django.db import models
import datetime


class CO2Sensors(models.Model):
    location = models.CharField(max_length=255, blank=False)
    measurement_date = models.DateField(default=datetime.date.today, blank=False)
    measurement_time = models.TimeField(default=datetime.time, blank=False)
    temperature = models.IntegerField(default=0, blank=False)
    name = models.CharField(max_length=50, blank=False)
    model = models.CharField(max_length=50, blank=False)
    group = models.CharField(max_length=50, blank=False)
