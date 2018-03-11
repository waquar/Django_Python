from django.db import models

# Create your models here.
class College(models.Model):

    name = models.CharField(max_length=50, default=None)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=250, default= None)

    def __str__(self):
        return  self.name

    class Meta:
         db_table = "college"



class Student(models.Model):

    name = models.CharField(max_length=50, default=None)
    email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    pincode = models.CharField(max_length= 60)

    def __str__(self):
        return  self.name

    class Meta:
        db_table  = 'student'


