from django.contrib import admin
from django.urls import path
from MainApp.views import index_page, cabinet_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='mainpage'),
    path('cabinet/', cabinet_page, name='cabinet')
]
