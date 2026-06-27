from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)

    def __str__(self):
        return self.degree