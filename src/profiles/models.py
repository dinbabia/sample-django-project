from django.db import models
from django.urls import reverse

# Create your models here.

class Profiles(models.Model):
    name = models.CharField(max_length=50)
    age  = models.IntegerField()
    job = models.CharField(max_length=50)
    favorite_sport = models.CharField(max_length=50)

    def get_absolute_url(self):
        # return f"/product/{self.id}/"
        return reverse("profiles:profile-detail", kwargs={
                          "id" : self.id
                      })
