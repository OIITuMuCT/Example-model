from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('my-form/', views.my_form, name="my_form"),
    path('about/', views.about, name='about'),
    
]
