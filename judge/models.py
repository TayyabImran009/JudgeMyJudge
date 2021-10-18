from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class judge (models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(
        max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    coat_name = models.CharField(
        max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class judgeRateing (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ratedTo = models.ForeignKey(judge, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    description = models.TextField(max_length=9999, null=True, blank=True)
    cannon1 = models.CharField(max_length=200, null=True, blank=True)
    cannon2 = models.CharField(max_length=200, null=True, blank=True)
    cannon3 = models.CharField(max_length=200, null=True, blank=True)
    cannon4 = models.CharField(max_length=200, null=True, blank=True)
    cannon5 = models.CharField(max_length=200, null=True, blank=True)
    political_perspective_of_judge = models.CharField(
        max_length=200, null=True, blank=True)
    family_connections_in_legal_community = models.CharField(
        max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username


class bestInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ratedTo = models.ForeignKey(judge, on_delete=models.CASCADE)
    child_age = models.IntegerField()
    child_physical_condition = models.CharField(max_length=200)
    child_mental_health = models.CharField(max_length=200)
    father_age = models.IntegerField()
    mother_age = models.IntegerField()
    father_physical_condition = models.CharField(max_length=200)
    father_mental_health = models.CharField(max_length=200)
    mother_physical_condition = models.CharField(max_length=200)
    mother_mental_health = models.CharField(max_length=200)
    relation_with_father = models.CharField(max_length=200)
    relation_with_mother = models.CharField(max_length=200)
    involvement_with_father = models.CharField(max_length=200)
    involvement_with_mother = models.CharField(max_length=200)
    child_needs = models.CharField(max_length=200)
    child_relation_with_siblings = models.CharField(max_length=200)
    child_relation_with_other_family = models.CharField(max_length=200)
    father_roll = models.CharField(max_length=200)
    mother_roll = models.CharField(max_length=200)
    father_support = models.CharField(max_length=200)
    mother_support = models.CharField(max_length=200)
    child_preference = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
