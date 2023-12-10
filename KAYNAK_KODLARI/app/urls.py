"""
URL configuration for school_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views, OgrenciViews, OgretmenViews, IdariPersonelViews


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about ,name='about'),
    path('aboutus', views.aboutus ,name='aboutus'),
    path('gallery', views.gallery ,name='gallery'),
    path('blog', views.blog ,name='blog'),
    path('map', views.map ,name='map'),
    path('home', views.home, name='home'),
    path('login/', views.login_user, name='login_user'),

    path('ogrenci/logout', views.logout_user, name='logout'),
    path('ogretmen/logout', views.logout_user, name='logout'),
    path('idare/logout', views.logout_user, name='logout'),

    path('ogrenci/dashboard', OgrenciViews.ogrenci_dashboard, name='ogrenci_dashboard'),
    path('ogretmen/dashboard', OgretmenViews.ogretmen_dashboard, name='ogretmen_dashboard'),
    path('idare/dashboard', IdariPersonelViews.idare_dashboard, name='idare_dashboard'),

    path('ogrenci/kisiselBilgiler', OgrenciViews.ogrenci_kisisel_bilgiler, name='ogrenci_kisiselBilgiler'),
    path('ogretmen/kisiselBilgiler', OgretmenViews.ogretmen_kisisel_bilgiler, name='ogretmen_kisiselBilgiler'),
    path('idare/kisiselBilgiler', IdariPersonelViews.idare_kisisel_bilgiler, name='idari_kisiselBilgiler'),

    path('ogrenci/dersTalebi', OgrenciViews.ogrenci_ders_talebi, name='ogrenci_ders_talebi'),
    path('ogrenci/haftalikProgram', OgrenciViews.ogrenci_haftalik_program, name='ogrenci_haftalik_program'),

    path('ogretmen/haftalikProgram', OgretmenViews.ogretmen_haftalik_program, name='ogretmen_haftalik_program'),
    # path('ogretmen/haftalikProgram', OgretmenViews.ogretmen_malzeme_ekle, name='ogretmen_malzeme_ekle'),

    path('idare/okulVerileri', IdariPersonelViews.idare_okul_verileri, name='idare_okul_verileri'),

    path('idare/okulVerileri', IdariPersonelViews.idare_ders_programlarini_ata, name='ders-programi-olustur')
]

