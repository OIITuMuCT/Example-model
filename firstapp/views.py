from django.shortcuts import render, redirect
from .forms import UserForm

from .models import Person

def index(request):
    my_text = "Изучаем модели Django"
    people_kol = Person.object_person.count()
    context = {'my_text': my_text, "people_kol": people_kol}
    return render(request, "firstapp/index.html", context)