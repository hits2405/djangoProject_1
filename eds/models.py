from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


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


"""    name = models.CharField(max_length=200)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, null=True)
    is_published = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="pic")"""
