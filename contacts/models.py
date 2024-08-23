from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=150)
    car_id = models.IntegerField()
    car_title = models.CharField(max_length=150)
    user_city = models.CharField(max_length=20)
    user_state = models.CharField(max_length=20)
    email_id = models.EmailField()
    phone_number = models.IntegerField(default=True)
    message = models.TextField(blank=True,max_length=500)
    user_id = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email_id
