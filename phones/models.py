import datetime
from django.db import models


class Phone(models.Model):
    phone = models.CharField(verbose_name='Телефон', max_length=16)


class Code(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    code = models.CharField(max_length=5, verbose_name='Код')
    end = models.DateTimeField(default=datetime.datetime.now)
