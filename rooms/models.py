from django.db import models

from users.models import User


class Room(models.Model):
    number = models.CharField(max_length=50)
    price = models.IntegerField()
    beds = models.IntegerField()

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"
