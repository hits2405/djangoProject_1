from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, null=True)
    is_published = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="pic")

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
