from django.shortcuts import render, redirect, reverse
from .models import User


def index_page(request):
    return render(request, "index.html")


def cabinet_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User(login=username, password=password)
        user.save()  # Зберігаємо користувача в базі даних
        return redirect(reverse('mainpage'))  # Перенаправляємо на іншу сторінку

    return render(request, "cabinet.html")


def searching_page(request):
    return render(request, "searching.html")


def about_us_page(request):
    return render(request, "aboutus.html")