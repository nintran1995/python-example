from django.db import models

class Boarding(models.Model):
    zip_code = models.CharField(max_length=200)
    start_date = models.DateTimeField('date started')
    end_date = models.DateTimeField('date ended')
    size = models.CharField(max_length=20)