# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect, reverse
from audioop import reverse

from django.shortcuts import render, redirect
from MainApp.models import User
# from django.contrib.auth.models import User


def index_page(request):
    return render(request, "index.html")


def cabinet_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User(login=username, password=password)
        user.save()  # Зберігаємо користувача в базі даних
        return redirect('mainpage')

    return render(request, "cabinet.html")


# def cabinet_page(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         # Проверка наличия пользователя с указанным логином
#         if User.objects.filter(username=username).exists():
#             return render(request, "cabinet.html", {'error_message': 'Користувач з таким логіном вже існує'})
#
#         # Создание нового пользователя и сохранение его в базе данных
#         user = User.objects.create(login=username, password=password)
#         user.save()
#
#         return redirect('mainpage')
#
#     return render(request, "cabinet.html")


def searching_page(request):
    return render(request, "searching.html")


def about_us_page(request):
    return render(request, "aboutus.html")


def t84bmoplot_page(request):
    return render(request, "t84bmoplot.html")