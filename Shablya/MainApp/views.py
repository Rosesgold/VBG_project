from django.shortcuts import render


def index_page(request):
    return render(request, "index.html")


def cabinet_page(request):
    return render(request, "cabinet.html")


def searching_page(request):
    return render(request, "searching.html")


def about_us_page(request):
    return render(request, "aboutus.html")