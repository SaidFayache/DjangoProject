from django.db import models


class Prof(models.Model):
    name = models.CharField(max_length=60)
    field = models.CharField(max_length=60)

    def __str__(self):
        return self.name
