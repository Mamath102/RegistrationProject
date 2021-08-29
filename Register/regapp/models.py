from django.db import models
from django.urls import reverse
# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    mobile_Number=models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail')
