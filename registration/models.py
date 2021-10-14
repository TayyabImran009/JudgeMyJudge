from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=500)
    case_number = models.IntegerField(blank=True, null=True)
    picture_id = models.ImageField(blank=True, null=True,
                                   upload_to='user_image/', default="default.jpg")
    membership = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
