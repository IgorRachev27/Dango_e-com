from django.db import models
from app.models import Product
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    image = models.ImageField(upload_to='media/order/image', verbose_name = 'Изображение')
    product = models.CharField(max_length=1000,default='', verbose_name = 'Товар')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Клент')
    quantity = models.IntegerField(verbose_name = 'Количество')
    price = models.IntegerField(verbose_name = 'Цена')
    address = models.TextField(verbose_name = 'Адрес')
    phone = models.CharField(max_length=16, verbose_name = 'Телефон')
    pincode = models.CharField(max_length=10, verbose_name = 'Код')
    total = models.CharField(max_length=50, default="", verbose_name = 'Общая сумма заказа')
    date = models.DateField(default=datetime.today, verbose_name = 'Дата заказа')


    def __str__(self):
        return self.product
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
