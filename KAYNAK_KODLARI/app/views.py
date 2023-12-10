from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from django.db import connection


def home(request):
    return render(request, 'home/home.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def aboutus(request):
    return render(request, 'home/about_us.html', {})

def gallery(request):
    return render(request, 'home/gallery.html', {})

def blog(request):
    return render(request, 'home/blog.html', {})

def map(request):
    return render(request, 'home/map.html', {})

def login_user(request):
    #cursor eklemesi
    cursor = connection.cursor()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            print("asdasdasdasdasdasdasdasd")
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # aktif_ogrenci = Aktif_Ogrenci.objects.filter(Email=email).first()
            # mezun_ogrenci = Mezun_Ogrenci.objects.filter(Email=email).first()
            # idari_personel = Idari_Personel.objects.filter(Email=email).first()
            # ogretmen = Ogretmen.objects.filter(Email=email).first()
            cursor.execute("SELECT * FROM app_aktif_ogrenci AO WHERE AO.Email = %s;", [email])
            aktif_ogrenci = cursor.fetchone()

            cursor.execute("SELECT * FROM app_mezun_ogrenci MO WHERE MO.Email = %s;", [email])
            mezun_ogrenci = cursor.fetchone()

            cursor.execute("SELECT * FROM app_idari_personel IP WHERE IP.Email = %s;", [email])
            idari_personel = cursor.fetchone()

            cursor.execute("SELECT * FROM app_ogretmen O WHERE O.Email = %s;", [email])
            ogretmen = cursor.fetchone()


            print(aktif_ogrenci)
            print(mezun_ogrenci)
            print(idari_personel)
            print(ogretmen)

            if aktif_ogrenci is not None:
                user = aktif_ogrenci
            elif mezun_ogrenci is not None:
                user = mezun_ogrenci
            elif ogretmen is not None:
                user = ogretmen
            elif idari_personel is not None:
                user = idari_personel
            else:
                print("Wrong password or email. Please try again.")
                return redirect('login_user')

            em = user[5]
            pw = em[:4]

            if pw == password:
                if aktif_ogrenci is not None:
                    request.session['user_type'] = 1
                    print("hi aktif ogrenci")
                elif mezun_ogrenci is not None:
                    request.session['user_type'] = 2
                    print("hi mezun ogrenci")
                elif ogretmen is not None:
                    print("hi ogretmen")
                    request.session['user_type'] = 3
                elif idari_personel is not None:
                    print("hi idari_personel")
                    request.session['user_type'] = 4

                request.session['user_id'] = user[0]
                print("email", email)
                print("password", password)

                # messages.success(request, "You have been logged in!")
                return dashboard(request)
            else:
                print("Wrong password or email. Please try again.")
                return render(request, 'home/login_page.html', {})
        else:
            print("There was an error logging in. Please try again.")
            # messages.error(request, "There was an error logging in. Please try again.")
            return render(request, 'home/login_page.html', {})
    else:
        form = LoginForm()
        print("login get method")
        return render(request, 'home/login_page.html', {'form': form})

def dashboard(request):
    cursor = connection.cursor()
    print("dashboarda girdim")
    user_type = request.session['user_type']
    user_id = request.session['user_id']

    if user_id is not None:
        if user_type == 1:
            #user = Aktif_Ogrenci.objects.get(OgrenciID=user_id)
            # cursor.execute("SELECT * FROM app_aktif_ogrenci AO WHERE AO.OgrenciID = %s;", [user_id])
            # user = cursor.fetchone()
            return redirect('ogrenci_dashboard')
        elif user_type == 2:
            #user = Mezun_Ogrenci.objects.get(OgrenciID=user_id)
            # cursor.execute("SELECT * FROM app_mezun_ogrenci MO WHERE MO.OgrenciID = %s;", [user_id])
            # user = cursor.fetchone()
            return redirect('ogrenci_dashboard')
        elif user_type == 3:
            #user = Ogretmen.objects.get(CalisanID=user_id)
            # cursor.execute("SELECT * FROM app_ogretmen O WHERE O.CalisanID = %s;", [user_id])
            # user = cursor.fetchone()
            return redirect('ogretmen_dashboard')
        elif user_type == 4:
            #user = Idari_Personel.objects.get(CalisanID=user_id)
            # cursor.execute("SELECT * FROM app_idari_personel IP WHERE IP.CalisanID = %s;", [user_id])
            # user = cursor.fetchone()
            return redirect('idare_dashboard')

        return redirect('login_user')
        # return render(request, 'dashboard.html', {'email': email, 'firstname': firstname})
    else:
        return redirect('login_user')

def logout_user(request):
    print("logout_user")
    request.session.clear()
    messages.success(request, "You Have Been Logged Out...")
    return redirect('login_user')
