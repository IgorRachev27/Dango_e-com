from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название подкатегории')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название бренда')


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Группа брендов'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=False, default='')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория', null=False,
                                     default='')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='media/product', verbose_name='Изображение товара')
    name = models.CharField(max_length=100, verbose_name='Название товара')
    price = models.IntegerField( verbose_name='Цена')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Contact_us(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100, verbose_name='Email')
    subject = models.CharField(max_length=100, verbose_name='Тема')
    message = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Сообщение от клиентов'
        verbose_name_plural = 'Сообщения от клиентов'