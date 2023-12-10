from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import RequestContext
from app.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth import get_user_model
from django.db import connection

def ogrenciMi(request):
    user_type = request.session['user_type']
    return user_type == 1

def ogrenci_dashboard(request):

    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('login_user')

    if not ogrenciMi(request):
        print("ogrenci olarak giriniz")
        # messages.success(request, "ogrenci olarak giriniz.")
        return redirect('login_user')

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM app_aktif_ogrenci AO WHERE AO.OgrenciID = %s;",[user_id])
    user = cursor.fetchone()

    context = {
        'user': user,
    }

    return render(request, 'ogrenci/ogrenci_dashboard.html', context)

def ogrenci_kisisel_bilgiler(request):

    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('login_user')

    if not ogrenciMi(request):
        print("ogrenci olarak giriniz")
        # messages.success(request, "ogrenci olarak giriniz.")
        return redirect('login_user')

    cursor = connection.cursor()
    # user = get_object_or_404(Aktif_Ogrenci, OgrenciID=user_id)
    cursor.execute("SELECT * FROM app_aktif_ogrenci AO WHERE AO.OgrenciID = %s;",[user_id])
    user = cursor.fetchone()
    # veli = get_object_or_404(Veli, OgrenciID=user_id)
    cursor.execute("SELECT * FROM app_veli V WHERE V.OgrenciID = %s;",[user_id])
    veli = cursor.fetchone()

    context = {
        'user': user,
        'veli': veli,
    }

    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        numara = request.POST.get('numara')
        telefon = request.POST.get('telefon')
        adres = request.POST.get('adres')
        veli_adi = request.POST.get('veli_adi')
        veli_soyadi = request.POST.get('veli_soyadi')
        veli_telefon = request.POST.get('veli_telefon')
        veli_email = request.POST.get('veli_email')

        # Öğrenci bilgilerini güncelle
        ogrenci_update_query = """
        UPDATE app_aktif_ogrenci
        SET Ad = %s, Soyad = %s, Numara = %s, Tel = %s, Adres = %s
        WHERE OgrenciID = %s
        """
        cursor.execute(ogrenci_update_query, [ad, soyad, numara, telefon, adres, user_id])

        # Veli bilgilerini güncelle
        veli_update_query = """
        UPDATE app_veli
        SET VeliAdi = %s, VeliSoyadi = %s, VeliTel = %s, VeliEmail = %s
        WHERE OgrenciID = %s
        """
        cursor.execute(veli_update_query, [veli_adi, veli_soyadi, veli_telefon, veli_email, user_id])

        # Kullanıcıya geri bildirim yap
        messages.success(request, "Bilgiler başarıyla güncellendi.")

        # Sayfayı yenile
        return redirect('ogrenci_kisiselBilgiler')

    return render(request, 'ogrenci/ogrenci_kisisel_bilgiler.html', context)

def ogrenci_ders_talebi(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('login_user')

    if not ogrenciMi(request):
        print("ogrenci olarak giriniz")
        # messages.success(request, "ogrenci olarak giriniz.")
        return redirect('login_user')

     # Sebebi Anlamadim Aktif_Ogrenci_Acilan_Ders_Alir
    cursor = connection.cursor()
    #dersler = Acilan_Ders.objects.all()
    cursor.execute("SELECT * FROM app_ders;")
    dersler = cursor.fetchall()

    oncedenSecilenler = oncedenSectiMi(request)
    # print(oncedenSecilenler)

    secili_dersler = []
    dersList = []

    if oncedenSecilenler is not None:
        for abbb in oncedenSecilenler:
            dersList.append(dersIDileKoduBul(abbb[1]))

        # print("dersList: ", dersList)
        secili_dersler = dersList

    # print("secili_dersler: ", secili_dersler)

    if request.method == 'POST':

        secili_dersler = request.POST.getlist('dersler')
        # print('Seçili Dersler:', secili_dersler)


        hepsi = Aktif_Ogrenci_Ders_Talep.objects.all()

        # denenmedi denencek
        # Tekrar tekrar ders ayni ders eklenebiliyor
        for ders in secili_dersler:
            # print("ders: ", ders)
            cursor.execute("SELECT DersID FROM app_Ders WHERE DersKodu = %s;", [ders])
            a = cursor.fetchone()

            ders_id = a[0]

            if check(hepsi, ders_id, user_id):
                continue

            # print("ders_id: ", ders_id)

            query = "INSERT INTO app_aktif_ogrenci_ders_talep (DersID, OgrenciID) " \
                    "VALUES  (%s, %s)"

            cursor.execute(query, [ders_id, user_id])


        return render(request, 'ogrenci/ogrenci_ders_talebi.html', {'dersler': dersler, 'secili_dersler': secili_dersler})
    else:
        # ders tablosundaki dersler ile acilan_ders tablosundaki derslerin kodları aynı olmadığından gözükmüyor baslangicta.
        # ustteki seyi dersIDileKoduBul fonksiyonda acilan_ders yerine dersten alarak duzelttim
        return render(request, 'ogrenci/ogrenci_ders_talebi.html', {'dersler': dersler, 'secili_dersler': secili_dersler})

def check(dersler, ders_id, user_id):

    for ders in dersler:
        if ders.DersID.DersID == ders_id and ders.OgrenciID.OgrenciID == user_id:
            # print("buldum")
            return True

    return False

def oncedenSectiMi(request):
    cursor = connection.cursor()
    user_id = request.session.get('user_id')
    cursor.execute("SELECT * FROM app_aktif_ogrenci_ders_talep WHERE OgrenciID = %s;",[user_id])
    ogrencininSectigiDersler = cursor.fetchall()

    return ogrencininSectigiDersler
    # for a in ogrencininSectigiDersler:
    #     print(a)

def dersIDileKoduBul(ders_id):
    # print("ders_id: ", ders_id)
    cursor = connection.cursor()
    cursor.execute("SELECT DersKodu FROM app_Ders WHERE DersID = %s;", [ders_id])
    asd = cursor.fetchone()

    # print("asd: ", asd[0])
    return asd[0]

def ogrenci_haftalik_program(request):
    #cursor eklemesi

    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('login_user')

    if not ogrenciMi(request):
        print("ogrenci olarak giriniz")
        # messages.success(request, "ogrenci olarak giriniz.")
        return redirect('login_user')

    cursor = connection.cursor()

    # denenmedi denencek
    cursor.execute("SELECT * FROM app_acilan_ders ad \
                     WHERE ad.DersID IN \
                     (SELECT aoada.AcilanDersID \
                     FROM app_aktif_ogrenci_acilan_ders_alir aoada \
                     WHERE aoada.OgrenciID=%s);", [user_id])

    haftalik_program = cursor.fetchall()

    program = []
    for a in haftalik_program:
        if a[2] == "Syllabus Ders":
            temp = [a[6], a[3].hour, a[5]]
            program.append(temp)
            temp = [a[6], a[3].hour + 1, a[5]]
            program.append(temp)

    cursor.execute("SELECT * FROM APP_HAFTANIN_SAATLERI;")
    hafta = cursor.fetchall()
    # ONEMLI!!! haftalik program = Aktif_Ogrenci_Acilan_Ders_Alir ile AKTIF_OGRENCI_MESGULIYET birlesiminden olusacak.
    gunler = []
    saatler = []

    for count in range(0,55):
        # print(hafta[count])
        if count % 11 == 0:
            gunler.append(hafta[count][3])
        if count < 11:
            saatler.append(hafta[count][1].hour)

    # secilen_alanlar = request.POST.getlist('secilen_alanlar')
    # print('secilen_alanlar:', secilen_alanlar)
    return render(request, 'ogrenci/ogrenci_haftalik_program.html',
                  {'gunler': gunler, 'saatler': saatler, 'program':program})
