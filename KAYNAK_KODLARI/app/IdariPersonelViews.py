from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import RequestContext
from app.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.db import connection

def IdariPersonelMi(request):
    user_type = request.session['user_type']
    return user_type == 4

def idare_dashboard(request):

    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('login_user')

    if not IdariPersonelMi(request):
        print("IdariPersonel olarak giriniz")
        # messages.success(request, "ogrenci olarak giriniz.")
        return redirect('login_user')



    cursor = connection.cursor()
    cursor.execute("SELECT * FROM app_idari_personel IP WHERE IP.CalisanID = %s;", [user_id])
    user = cursor.fetchone()

    context = {
        'user': user,
    }

    return render(request, 'idare/idare_dashboard.html', context)

def idare_kisisel_bilgiler(request):
    #cursor eklemesi

    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('login_user')

    if not IdariPersonelMi(request):
        print("IdariPersonel olarak giriniz")
        # messages.success(request, "IdariPersonel olarak giriniz.")
        return redirect('login_user')

    cursor = connection.cursor()

    #user = get_object_or_404(Idari_Personel, CalisanID=user_id)
    cursor.execute("SELECT * FROM app_idari_personel IP WHERE IP.CalisanID = %s;",[user_id])
    user = cursor.fetchone()

    context = {
        'user': user,
    }

    if request.method == 'POST':
        cursor.execute("UPDATE app_idari_personel SET Ad = %s, Soyad = %s, Tel = %s, Adres = %s, Unvan = %s WHERE CalisanID = %s;",
                       [request.POST['ad'], request.POST['soyad'], request.POST['telefon'], request.POST['adres'], request.POST['unvan'], user_id])
        cursor.fetchone()
        return redirect('idari_kisiselBilgiler')

    return render(request, 'idare/idare_kisisel_bilgiler.html', context)

def idare_okul_verileri(request):
    #cursor eklemesi


    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('login_user')

    if not IdariPersonelMi(request):
        print("IdariPersonel olarak giriniz")
        # messages.success(request, "IdariPersonel olarak giriniz.")
        return redirect('login_user')

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM app_aktif_ogrenci;")
    aktif_ogrenciler = cursor.fetchall()

    cursor.execute("SELECT * FROM app_mezun_ogrenci;")
    mezun_ogrenciler = cursor.fetchall()


    cursor.execute("SELECT * FROM app_veli;")
    veliler = cursor.fetchall()

    cursor.execute("SELECT * FROM app_ogretmen;")
    ogretmenler = cursor.fetchall()

    cursor.execute("SELECT * FROM app_sabit_gider;")
    sabit_gider = cursor.fetchall()

    cursor.execute("SELECT * FROM app_ek_gider;")
    ek_gider = cursor.fetchall()

    cursor.execute("SELECT * FROM app_idari_personel;")
    idari_personel = cursor.fetchall()

    cursor.execute("SELECT * FROM app_Temizlik_Gorevlisi;")
    temizlik_gorevlisi = cursor.fetchall()


    cursor.execute("SELECT SUM(maas) FROM app_ogretmen;")
    ogretmen_maaslari = cursor.fetchone();

    cursor.execute("SELECT SUM(maas) FROM app_idari_personel;")
    idari_personel_maaslari = cursor.fetchone();


    cursor.execute("SELECT SUM(maas) FROM app_temizlik_gorevlisi;")
    temizlik_gorevlisi_maaslari = cursor.fetchone();

    idare_ders_programlarini_ata(request)



    context = {
        'aktif_ogrenciler': aktif_ogrenciler,
        'mezun_ogrenciler': mezun_ogrenciler,
        'veliler': veliler,
        'ogretmenler': ogretmenler,
        'idari_personel': idari_personel,
        'temizlik_gorevlisi': temizlik_gorevlisi,
        'sabit_gider': sabit_gider,
        'ek_gider': ek_gider,
        'ogretmen_maaslari':ogretmen_maaslari,
        'idari_personel_maaslari':idari_personel_maaslari,
        'temizlik_gorevlisi_maaslari':temizlik_gorevlisi_maaslari
    }

    return render(request, 'idare/okul_verileri.html', context)


def idare_ders_programlarini_ata(request):
    # cursor eklemesi
    cursor = connection.cursor()

    if not IdariPersonelMi(request):
        # print("IdariPersonel olarak giriniz")
        # messages.success(request, "IdariPersonel olarak giriniz.")
        return redirect('login_user')

    cursor.execute("SELECT aodt.DersID \
                    FROM app_Aktif_Ogrenci_Ders_Talep aodt \
                    GROUP BY aodt.DersID HAVING COUNT(aodt.OgrenciID) > 1 ORDER BY COUNT(aodt.OgrenciID) DESC;")
    asd = cursor.fetchall()

    ogrenci_talepleri_azalanSira = []
    for a in asd:
        ogrenci_talepleri_azalanSira.append(a[0])

    # print("ogrenci_talepleri_azalanSira: ", ogrenci_talepleri_azalanSira)

    cursor.execute("SELECT hs.SaatGunID \
                    FROM app_haftanin_saatleri hs \
                    LEFT OUTER JOIN app_aktif_ogrenci_mesguliyet aom \
                    ON hs.SaatGunID=aom.SaatGunID \
                    GROUP BY hs.SaatGunID ORDER BY COUNT(aom.OgrenciID) ASC;")
    abb = cursor.fetchall()

    ogrenci_mesguliyetleri_artanSira = []
    for b in abb:
        ogrenci_mesguliyetleri_artanSira.append(b[0])

    # print("ogrenci_mesguliyetleri_artanSira: ", ogrenci_mesguliyetleri_artanSira)

    for ogrenci_talebi in ogrenci_talepleri_azalanSira:
        # print("ogrenci_talebi: ", ogrenci_talebi)
        for ogrenci_mesguliyet in ogrenci_mesguliyetleri_artanSira:
            # print("ogrenci_mesguliyet: ",ogrenci_mesguliyet)
            cursor.execute("SELECT * \
                            FROM app_part_time_ogretmen_mesguliyet ptom \
                            WHERE ptom.SaatGunID =%s;",[ogrenci_mesguliyet])
            ogretmen_mesguliyetle_cakisma = cursor.fetchone()

            # print("ogretmen_mesguliyetle_cakisma: ",ogretmen_mesguliyetle_cakisma)


            # bence burda insert into app_aktif_ogrenci_acilan_ders_alir yapcaz ama emin değilim burda bırakıyorum.
            # bu haliyle sürekli aynı id oluyor herkeste.
            if ogretmen_mesguliyetle_cakisma is None:
                cursor.execute("SELECT aodt.OgrenciID \
                                FROM app_Aktif_Ogrenci_Ders_Talep aodt \
                                WHERE aodt.DersID=%s;", [ogrenci_talebi])

                arr = cursor.fetchall()
                # print("arr: ",arr)

                talep_eden_ogrenciler = []

                for a in arr:
                    talep_eden_ogrenciler.append(a[0])

                # print("talep_eden_ogrenciler: ", talep_eden_ogrenciler)

                cursor.execute("SELECT CalisanID FROM app_Ders where DersID = %s", [ogrenci_talebi])
                asdasdasd = cursor.fetchone()

                hocaID = asdasdasd[0]
                # print("hocaID: ", hocaID)

                cursor.execute("INSERT INTO app_Part_Time_Ogretmen_Mesguliyet (CalisanID, SaatGunID, Sebep) \
                                VALUES (%s, %s, %s)", [hocaID, ogrenci_mesguliyet, "Ders"])
                cursor.fetchone()

                cursor.execute("INSERT INTO app_Part_Time_Ogretmen_Mesguliyet (CalisanID, SaatGunID, Sebep) \
                                                VALUES (%s, %s, %s)", [hocaID, ogrenci_mesguliyet+1, "Ders"])
                cursor.fetchone()

                cursor.execute("SELECT * FROM app_Ders where DersID = %s", [ogrenci_talebi])
                ders_bilgileri = cursor.fetchone()

                # print("ders_bilgileri: ",ders_bilgileri)

                cursor.execute("SELECT * FROM app_Haftanin_Saatleri where SaatGunID = %s", [ogrenci_mesguliyet])
                dersSaatiVeGunu = cursor.fetchone()

                # print("dersSaatiVeGunu: ", dersSaatiVeGunu)

                cursor.execute("INSERT INTO app_Acilan_Ders (DersID, DersAdi, Syllabus, DersSaati1, DersSaati2, DersGunu, DersKodu, CalisanID) \
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [ders_bilgileri[0], ders_bilgileri[1], "Syllabus Ders", dersSaatiVeGunu[1], dersSaatiVeGunu[2], dersSaatiVeGunu[3], ders_bilgileri[2], ders_bilgileri[3]])
                cursor.fetchone()


                for talep_eden_ogrenci in talep_eden_ogrenciler:

                    cursor.execute("INSERT INTO APP_Aktif_Ogrenci_Acilan_Ders_Alir (AcilanDersID, OgrenciID)"
                                   "VALUES (%s, %s)", [ders_bilgileri[0], talep_eden_ogrenci])
                    cursor.fetchone()

                    cursor.execute("INSERT INTO app_aktif_ogrenci_mesguliyet (OgrenciID, SaatGunID, Sebep) \
                                    VALUES (%s, %s, %s)", [talep_eden_ogrenci, ogrenci_mesguliyet, ders_bilgileri[2]])
                    cursor.fetchone()

                    cursor.execute("INSERT INTO app_aktif_ogrenci_mesguliyet (OgrenciID, SaatGunID, Sebep) \
                                    VALUES (%s, %s, %s)",
                                   [talep_eden_ogrenci, ogrenci_mesguliyet + 1, ders_bilgileri[2]])
                    cursor.fetchone()

                break

    return render(request, 'idare/okul_verileri.html')
