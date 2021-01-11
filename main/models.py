from django.db import models
from django.db.models import JSONField


class InputModel(models.Model):
    field = models.CharField(max_length=25)
    data = JSONField()

    def __str__(self):
        return f'Данные: {self.field} {self.data}'