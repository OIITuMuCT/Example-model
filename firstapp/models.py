from django.db import models

from django.urls import reverse


# Типичный класс, определяющий модель, производный класса Model
class MyModelName(models.Model):
    # Поле (или множество полей)
    my_field_name = models.CharField(
        max_length=20, help_text="Не более 20 символов", verbose_name="Введите ФИО"
    )

    # Метаданные
    class Meta:
        ordering = ["-my_field_name"]

    # Методы
    def get_absolute_url(self):
        # возвращает url-адрес для доступа к экземпляру MyModelName
        return reverse("model_detail-view", args={str(self.id)})

    def __str__(self):
        # Строка для предоставления объекта MyModelName в Admin site
        return self.field_name


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя клиента")
    age = models.IntegerField(verbose_name="Возраст клиента")
    object_person = models.Manager()
    DoesNotExist = models.Manager


class Employee(models.Modle):
    name = models.CharField(max_length=20)
    salary = models.IntegerField()
    bonus = models.ImageField()