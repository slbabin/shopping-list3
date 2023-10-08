from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    complete = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return self.name
