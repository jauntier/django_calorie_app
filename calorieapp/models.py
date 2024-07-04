from django.db import models

# Create your models here.


# Create your models here.

from django.utils import timezone

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    added_on = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name