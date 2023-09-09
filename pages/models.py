from django.db import models
from django.utils.timezone import now

# Create your models here.


class tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    start = models.DateField(default=now)
    finish = models.DateField()

    class Meta:
        db_table = 'todo'
        ordering = ['-start']

    def __str__(self):
        return f'{self.title}'
