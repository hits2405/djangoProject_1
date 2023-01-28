from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from users.models import User


class Ad(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey("users.User", related_name="ad", on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    description = models.TextField(null=False)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='logos/', null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Ad)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"
