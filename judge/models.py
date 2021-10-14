from django.db import models
from django.contrib.auth.models import User

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


class judgeRateing (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ratedTo = models.ForeignKey(judge, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
