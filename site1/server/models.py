from django.db import models
class Recipient(models.Model):
    cities =[
        ('Mumbai','Mumbai'),
        ('Delhi','Delhi'),
        ('Chennai','Chennai'),
        ('Banglore','Banglore'),
        ('Kolkata','Kolkata')
    ]
    name = models.CharField(max_length=255)
    mail = models.EmailField(max_length=355)
    city = models.CharField(max_length=400,choices=cities)
    time_stamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

