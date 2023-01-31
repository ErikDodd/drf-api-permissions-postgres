from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Shoe(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    laces = models.BooleanField(default=True, null=False, blank=False)
    brand = models.TextField()
    color = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
