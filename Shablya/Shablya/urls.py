from django.contrib import admin
from django.urls import path
from MainApp import views
from MainApp.views import index_page, cabinet_page, searching_page, about_us_page, t84bmoplot_page, m113_page, \
    su25_page, archer_page, bmp1_page, mech_page, spys_page, kulemet_maksima_page, pirach_page, shablya_page, \
    leopard1_page, bmp2_page, ak47_page, t54_page, sau_bogdana_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='mainpage'),
    path('cabinet', cabinet_page, name='cabinet'),
    path('searching', searching_page, name='search'),
    path('aboutus', about_us_page, name='aboutus'),
    path('t84bmoplot/<int:id_>/', views.t84bmoplot_page, name='t84bmoplot'),
    path('m113/<int:id_>/', views.m113_page, name='m113'),
    path('su25/<int:id_>/', views.su25_page, name='su25'),
    path('archer/<int:id_>/', views.archer_page, name='archer'),
    path('bmp1/<int:id_>/', views.bmp1_page, name='bmp1'),
    path('mech/<int:id_>/', views.mech_page, name='mech'),
    path('spys/<int:id_>/', views.spys_page, name='spys'),
    path('kulemet_maksima/<int:id_>/', views.kulemet_maksima_page, name='kulemet_maksima'),
    path('pirach/<int:id_>/', views.pirach_page, name='pirach'),
    path('shablya/<int:id_>/', views.shablya_page, name='shablya'),
    path('leopard1/<int:id_>/', views.leopard1_page, name='leopard1'),
    path('bmp2/<int:id_>/', views.bmp2_page, name='bmp2'),
    path('ak47/<int:id_>/', views.ak47_page, name='ak47'),
    path('t54/<int:id_>/', views.t54_page, name='t54'),
    path('sau_bogdana/<int:id_>/', views.sau_bogdana_page, name='sau_bogdana'),
    path('get_card_count_by_periods/', views.get_card_count, name='get_card_count_by_periods'),
]
