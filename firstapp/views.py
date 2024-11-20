from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .forms import UserForm
from django.contrib.auth.models import User

from .models import Person


def index(request):
    my_text = "Изучаем модели Django"
    people_kol = Person.object_person.count()
    context = {"my_text": my_text, "people_kol": people_kol}
    return render(request, "firstapp/index.html", context)

def about(request):
    context = {"name": 'name = John'}
    return render(request, 'firstapp/about.html', context)

def my_form(request):

    if request.method == "POST":  # Пользователь отправил данные
        form = UserForm(request.POST)  # Создание экземпляра формы
        if form.is_valid():  # проверка валидности формы
            form.save()
            redirect('my_form3')
            
            # form.save()  # Запись данных в БД
        # Остаемся на той же странице, обновляем форму
    # Загрузить форму для вода клиентов
    my_text = "Сведения о клиентах"
    people = Person.object_person.all()
    form = UserForm()
    context = {"my_text": my_text, "people": people, "form": form}
    return render(request, "firstapp/my_form.html", context)


def edit_form(request, id):
    person = Person.object_person.get(id=id)
    # Если пользователь вернул отредактированные данные
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return redirect('my_form')
    # Если пользователь отправляет данные на редактирование
    data = {"person": person}
    return render(request, "firstapp/edit_form.html", context=data)

def delete(request, id):
    try:
        person = Person.object_person.get(id=id)
        person.delete()
        return redirect('my_form')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2> Object not found</h2>")

def user_create(request):
    # Создать пользователя и сохранить его в базе данных
    user = User.objects.create_user('myusername', 'myemail@example.com', 'mypassword')
    
    # Обновить поля и сохранить их снова
    user.first_name = 'Mike'
    user.last_name = 'Smit'
    # user.save()
    return user