from django.db import models

# Create your models here.
class Booking(models.Model):
    # user = ...
    email = models.EmailField()
    date = models.DateField()
    timeslot = models.SmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking by {self.email} for {self.date} at {self.timeslot} o\'clock'