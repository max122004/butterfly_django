from django.db import models


class Masters(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя мастера')
    services = models.CharField(max_length=100, verbose_name='Услуга')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return f'{self.name} - {self.services}'


class Clients(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    phone = models.CharField(verbose_name='Телефон клиента')
    data = models.DateField(verbose_name='Дата записи клиента')
    time = models.TimeField(verbose_name='Время записи клиента')
    service = models.ForeignKey(Masters, on_delete=models.CASCADE, null=True, verbose_name='Услуга клиента')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name} - {self.service}'

