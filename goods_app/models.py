from django.db import models
from django.utils import timezone


class Suppliers(models.Model):
    """Поставщики товаров"""
    name = models.CharField(verbose_name='имя поставщика', max_length=64,
                            unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['name']


class Goods(models.Model):
    """Товары"""
    MEASURE_UNIT_CHOICES = (
        ('RUB', 'рубль'),
        ('CNY', 'юань'),
        ('USD', 'доллар'),
        ('EUR', 'евро'),
    )
    name = models.CharField(verbose_name='название', max_length=64)
    date_receipt = models.DateField(
        max_length=8, verbose_name='дата поступления', blank=True, null=True,
        default=timezone.now)
    date_upd = models.DateTimeField(
        verbose_name='дата обновления', auto_now=True, auto_created=True)
    price = models.PositiveIntegerField(verbose_name='цена')

    measure_unit = models.CharField(
        verbose_name='единица измерения', max_length=3,
        choices=MEASURE_UNIT_CHOICES)

    supplier = models.ForeignKey(
        Suppliers, verbose_name='поставщик', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name, self.supplier.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-date_upd', 'name']
        unique_together = (('name', 'supplier'),)
