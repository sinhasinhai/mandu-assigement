import uuid

from django.db import models

# Create your models here.


class Contact(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, serialize=False)
    usn = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    semester = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=50, default="1")

    def __str__(self):
        return self.name
