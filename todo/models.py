from django.db import models

# Create your models here.
class ListofItems(models.Model):
    item = models.CharField(max_length=264,unique=True)
    note = models.CharField(max_length=265,unique=True)
    date = models.DateField()

    def __str__(self):
        return self.item
