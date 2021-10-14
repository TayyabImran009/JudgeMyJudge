from django.db import models

# Create your models here.


class judge (models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)
    general_district_court = models.CharField(
        max_length=100, null=True, blank=True)
    position1 = models.CharField(max_length=100, null=True, blank=True)
    juvenile_domestic_court = models.CharField(
        max_length=100, null=True, blank=True)
    position2 = models.CharField(max_length=100, null=True, blank=True)
    circuit_court = models.CharField(max_length=100, null=True, blank=True)
    position3 = models.CharField(max_length=100, null=True, blank=True)
