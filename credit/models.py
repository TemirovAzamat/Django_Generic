from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО')
    citizenship = models.CharField(max_length=20, verbose_name='Гражданство')
    birth_year = models.DateField(verbose_name='Дата рождения')
    work_place = models.CharField(max_length=30, verbose_name='Место работы')

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.CharField(max_length=16, verbose_name='Номер аккаунта')
    account_type = models.IntegerField(verbose_name='Тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='accounts')

    def __str__(self):
        return self.number


class Credit(models.Model):
    sum = models.IntegerField(verbose_name='Сумма кредита')
    date = models.DateField(auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credits')

    def __str__(self):
        return self.sum
