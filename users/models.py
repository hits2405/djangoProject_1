from django.utils.translation import gettext_lazy as _
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=8, max_length=6, null=True, decimal_places=2)
    lng = models.DecimalField(max_digits=8, max_length=6, null=True, decimal_places=2)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return self.name

class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')
    ADMIN = 'admin', _('admin')


class User(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=10, choices=UserRoles.choices)
    age = models.PositiveSmallIntegerField()
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
