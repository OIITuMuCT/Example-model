from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя клиента")
    age = models.IntegerField(verbose_name="Возраст клиента")
    object_person = models.Manager()
    DoesNotExist = models.Manager