from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # first_kana = models.CharField(max_length=30)
    # last_kana = models.CharField(max_length=30)



    def __str__(self):
        return self.first_name

class Contact(models.Model):
    email = models.EmailField()
    massage = models.TextField()

    def __str__(self):
        return self.email