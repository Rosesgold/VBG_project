# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect, reverse
from audioop import reverse

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.models import User
# from django.contrib.auth.models import User
from .models import Card


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

#
# def my_view(request, card_id):
#     card = get_object_or_404(Card, pk=card_id)
#
#     return render(request, 'your_template.html', {'card': card})


def searching_page(request):
    return render(request, "searching.html")


def about_us_page(request):
    return render(request, "aboutus.html")


def t84bmoplot_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def m113_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def su25_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def archer_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def bmp1_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def mech_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def spys_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def kulemet_maksima_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def pirach_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def shablya_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def leopard1_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def bmp2_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def ak47_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def t54_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


def sau_bogdana_page(request, id_):
    data_from_db = get_object_or_404(Card, pk=id_)
    return render(request, "cards/cards.html", {'data_from_db': data_from_db})


# def get_card_count(request):
#     count = Card.objects.filter(history_period='Новітній час').count()
#     return JsonResponse({'count': count})

def get_card_count(request):
    selected_history_period = request.GET.get('timePeriod')  # Отримати значення обраного чекбокса 'timePeriod'

    if selected_history_period:
        count = Card.objects.filter(history_period=selected_history_period).count()
        return JsonResponse({'count': count})
    else:
        # Обробка, якщо чекбокс не обрано
        return JsonResponse({'error': 'No history period selected'})

