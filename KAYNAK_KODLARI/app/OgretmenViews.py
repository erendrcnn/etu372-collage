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

def ogretmenMi(request):
    user_type = request.session['user_type']
    return user_type == 3

def ogretmen_dashboard(request):
    if not ogretmenMi(request):
        print("ogretmen olarak giriniz")
        # messages.success(request, "ogrenci olarak giriniz.")
        return redirect('login_user')

    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('login_user')

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM app_ogretmen O WHERE O.CalisanID = %s;", [user_id])
    user = cursor.fetchone()

    context = {
        'user': user,
    }

    return render(request, 'ogretmen/ogretmen_dashboard.html', context)
def ogretmen_kisisel_bilgiler(request):
    #cursor eklemesi
    cursor = connection.cursor()

    if not ogretmenMi(request):
        print("ogretmen olarak giriniz")
        # messages.success(request, "ogretmen olarak giriniz.")
        return redirect('login_user')

    user_id = request.session.get('user_id')
    print("ogretmen_kisisel_bilgiler girdim")
    print("user_id: ", user_id)
    if user_id is None:
        return redirect('login_user')

    #user = get_object_or_404(Ogretmen, CalisanID=user_id)
    cursor.execute("SELECT * FROM app_ogretmen O WHERE  O.CalisanID = %s;",[user_id])
    user = cursor.fetchone()

    print(user)

    istekler = []
    malzemeler = []
    cursor.execute("SELECT * FROM app_Acilan_Ders AD WHERE AD.CalisanID = %s;",[user_id])
    dersler = cursor.fetchall()

    print(dersler)

    for ders in dersler:
        print(ders)
        if ders is not None:
            for i in range(0,8):
                print(ders[i])

            cursor.execute("SELECT * FROM app_malzeme_ders MD WHERE  MD.AcilanDersID = %s;",[ders[1]])
            malzemeler = cursor.fetchall()

            for malzeme in malzemeler:

                if malzeme is not None:
                    for j in range(0,3):
                        print(malzeme[0])
                else:
                    print("Kayitli malzeme yoktur")
        else:
            print("ders yok.")


    context = {
        'user': user,
        'dersler': dersler,
        'malzemeler': malzemeler,
        'istekler': istekler
    }

    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        adres = request.POST.get('adres')
        telefon = request.POST.get('telefon')
        email = request.POST.get('email')

        update_query = """
        UPDATE app_ogretmen
        SET Ad = %s, Soyad = %s, Adres = %s, Tel = %s, Email = %s
        WHERE CalisanID = %s
        """
        cursor.execute(update_query, [ad, soyad, adres, telefon, email,  user_id])
        # connection.commit()

        # Kullanıcıya geri bildirim yap
        messages.success(request, "Bilgiler başarıyla güncellendi.")

        # Sayfayı yenile
        return redirect('ogretmen_kisiselBilgiler')

    return render(request, 'ogretmen/ogretmen_kisisel_bilgiler.html', context)
def ogretmen_haftalik_program(request):
    #cursor eklemesi

    if not ogretmenMi(request):
        print("ogretmen olarak giriniz")
        # messages.success(request, "ogretmen olarak giriniz.")
        return redirect('login_user')
    #asd = Haftanin_Saatleri.objects.all()
    # user_id = request.session.get('user_id')
    # asd = cursor.execute("SELECT * Acilan_Ders AD WHERE AD.CalisanID='{0}';".format(user_id))

    user_id = request.session.get('user_id')
    print("ogretmen_kisisel_bilgiler girdim")
    # print("user_id: ", user_id)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM app_acilan_ders aoada \
                     WHERE aoada.CalisanID=%s;", [user_id])

    haftalik_program = cursor.fetchall()
    print("haftalik_program: ", haftalik_program)

    print()

    program = []
    for a in haftalik_program:
        if a[2] == "Syllabus Ders":
            temp = [a[6], a[3].hour, a[5]]
            program.append(temp)
            temp = [a[6], a[3].hour + 1, a[5]]
            program.append(temp)

    cursor.execute("SELECT * FROM APP_HAFTANIN_SAATLERI;")
    hafta = cursor.fetchall()

    # ONEMLI!!! haftalik program = PART_TIME_OGRETMEN_DERS ile PART_TIME_OGRETMEN_MESGULIYET birlesiminden veya sadece FULL_TIME_OGRETMEN_DERS olusacak.
    gunler = []
    saatler = []
    count = 0
    for count in range(0, 55):
        # print(hafta[count])
        if count % 11 == 0:
            gunler.append(hafta[count][3])
        if count < 11:
            saatler.append(hafta[count][1].hour)

    # secilen_alanlar = request.POST.getlist('secilen_alanlar')
    # print('secilen_alanlar:', secilen_alanlar)

    return render(request, 'ogretmen/ogretmen_haftalik_program.html',
                  {'gunler': gunler, 'saatler': saatler, 'program':program})
