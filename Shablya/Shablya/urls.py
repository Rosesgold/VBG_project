from django.contrib import admin
from django.urls import path
from MainApp.views import index_page, cabinet_page, searching_page, about_us_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='mainpage'),
    path('cabinet/', cabinet_page, name='cabinet'),
    path('searching/', searching_page, name='search'),
    path('aboutus/', about_us_page, name='aboutus')
]
