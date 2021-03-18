from django.db import models

# Create your models here.

#creating models here and storing in  database acts a mysql

class Contact(models.Model):
    usn=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50,default="")
    semester=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name








