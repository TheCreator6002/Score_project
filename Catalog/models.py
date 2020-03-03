from django.db import models
from datetime import date

class Category(models.Model):
    """Категория"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Manufacturer(models.Model):
    """Производитель товара"""
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=100, unique=True)


class Product(models.Model):
    """Товар"""
    title = models.CharField("Название товара", max_length=50)
    description = models.TextField("Описание")
    picture = models.ImageField("Изображение", upload_to='Product_picture')
    date_of_manufacture = models.DateTimeField("Дата производства")
    price = models.PositiveSmallIntegerField("Цена", help_text="Указывать сумму в рублях")
    manufacturer = models.ForeignKey(Manufacturer, verbose_name="Производитель", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Reviews(models.Model):
    """Отзыв на товар"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=50)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
