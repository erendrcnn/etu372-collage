from django.db import models
from django.contrib.auth.models import AbstractUser

class Aktif_Ogrenci(models.Model):
    OgrenciID = models.AutoField(primary_key=True)
    Ad = models.CharField(max_length=255)
    Soyad = models.CharField(max_length=255)
    Numara = models.CharField(max_length=9)
    Tel = models.CharField(max_length=12)
    Email = models.EmailField()
    Adres = models.TextField()
    GPA = models.FloatField()

class Mezun_Ogrenci(models.Model):
    OgrenciID = models.AutoField(primary_key=True)
    Ad = models.CharField(max_length=255)
    Soyad = models.CharField(max_length=255)
    Numara = models.CharField(max_length=9)
    Tel = models.CharField(max_length=12)
    Email = models.EmailField()
    Adres = models.TextField()
    MezuniyetGPA = models.FloatField()
    MezuniyetTarihi = models.DateField()

class Veli(models.Model): # bunda ikili anahtar olcak
    VeliID = models.AutoField(primary_key=True)
    OgrenciID = models.ForeignKey("Aktif_Ogrenci", on_delete=models.CASCADE, db_column="OgrenciID")
    VeliAdi = models.CharField(max_length=255)
    VeliSoyadi = models.CharField(max_length=255)
    VeliTel = models.CharField(max_length=12)
    VeliEmail = models.EmailField()

class Idari_Personel(models.Model):
    CalisanID = models.AutoField(primary_key=True)
    Ad = models.CharField(max_length=255)
    Soyad = models.CharField(max_length=255)
    Adres = models.TextField()
    Tel = models.CharField(max_length=12)
    Email = models.EmailField()
    Maas = models.FloatField()
    BaslangicTarihi = models.DateField()
    DeneyimSuresi = models.FloatField()
    Unvan = models.TextField(max_length=50, null=True)  # Değişebilir

class Temizlik_Gorevlisi(models.Model):
    CalisanID = models.AutoField(primary_key=True)
    Ad = models.CharField(max_length=255)
    Soyad = models.CharField(max_length=255)
    Adres = models.TextField()
    Tel = models.CharField(max_length=12)
    Email = models.EmailField()
    Maas = models.FloatField()
    BaslangicTarihi = models.DateField()
    DeneyimSuresi = models.FloatField()
    CalismaYeri = models.TextField(max_length=200, null=True)

class Ogretmen(models.Model):
    CalisanID = models.AutoField(primary_key=True, unique=True)
    Ad = models.CharField(max_length=255)
    Soyad = models.CharField(max_length=255)
    Adres = models.TextField()
    Tel = models.CharField(max_length=12)
    Email = models.EmailField()
    Maas = models.FloatField()
    BaslangicTarihi = models.DateField()
    DeneyimSuresi = models.FloatField()

class Full_Time_Ogretmen(models.Model):
    CalisanID = models.OneToOneField("Ogretmen", on_delete=models.CASCADE, db_column='CalisanID', primary_key=True)

class Part_Time_Ogretmen(models.Model):
    CalisanID = models.OneToOneField("Ogretmen", on_delete=models.CASCADE, db_column='CalisanID', primary_key=True)
class Ders(models.Model):
    DersID = models.AutoField(primary_key=True)
    DersAdi = models.CharField(max_length=255)
    DersKodu = models.TextField(max_length=255)
    CalisanID = models.ForeignKey("Ogretmen", on_delete=models.CASCADE, db_column='CalisanID')

class Acilan_Ders(models.Model):
    AcilanDersID = models.AutoField(primary_key=True)
    DersID = models.ForeignKey("Ders", on_delete=models.CASCADE, default=1, db_column='DersID')
    DersAdi = models.CharField(max_length=255)
    Syllabus = models.TextField()
    DersSaati1 = models.TimeField(null=True)  # ?
    DersSaati2 = models.TimeField(null=True)  # ?
    DersGunu = models.CharField(max_length=15, null=True)
    DersKodu = models.TextField(max_length=255)
    CalisanID = models.ForeignKey("Ogretmen", on_delete=models.CASCADE, db_column='CalisanID')

class Malzeme(models.Model):
    MalzemeID = models.AutoField(primary_key=True)
    GiderID = models.ForeignKey("Ek_Gider", on_delete=models.CASCADE, default=1, db_column='GiderID', null=True)
    MalzemeMiktari = models.IntegerField()
    MalzemeFiyat = models.FloatField()
    MalzemeTuru = models.TextField()

class Ek_Gider(models.Model):
    GiderID = models.AutoField(primary_key=True)
    GiderAciklamasi = models.TextField()
    GiderMiktari = models.IntegerField()
    GiderTarihi = models.DateField()

class Sabit_Gider(models.Model):
    GiderID = models.AutoField(primary_key=True)
    GiderAciklamasi = models.TextField()
    GiderMiktari = models.IntegerField()

class Haftanin_Saatleri(models.Model):
    SaatGunID = models.AutoField(primary_key=True)
    BaslangicVakti = models.TimeField()
    BitisVakti = models.TimeField()
    Gun = models.TextField()

class Aktif_Ogrenci_Acilan_Ders_Alir(models.Model):
    AktifOgrenciAcilanDersID = models.AutoField(primary_key=True)
    AcilanDersID = models.ForeignKey("Acilan_Ders", on_delete=models.CASCADE, default=1, db_column='AcilanDersID')
    OgrenciID = models.ForeignKey("Aktif_Ogrenci", on_delete=models.CASCADE, default=1, db_column='OgrenciID')

class Aktif_Ogrenci_Mesguliyet(models.Model): # İkili anahtar olacak
    AktifOgrenciMesguliyetID = models.AutoField(primary_key=True)
    OgrenciID = models.ForeignKey("Aktif_Ogrenci", on_delete=models.CASCADE, default=1, db_column='OgrenciID')
    SaatGunID = models.ForeignKey("Haftanin_Saatleri", on_delete=models.CASCADE, db_column='SaatGunID')
    Sebep = models.TextField()

class Part_Time_Ogretmen_Mesguliyet(models.Model): # İkili anahtar olacak
    PartTimeOgretmenMesguliyetID = models.AutoField(primary_key=True)
    CalisanID= models.ForeignKey("Part_Time_Ogretmen", on_delete=models.CASCADE, db_column='CalisanID')
    SaatGunID = models.ForeignKey("Haftanin_Saatleri", on_delete=models.CASCADE, db_column='SaatGunID')
    Sebep = models.TextField()

class Malzeme_Ders(models.Model):
    MalzemeDersID = models.AutoField(primary_key=True)
    AcilanDersID = models.ForeignKey("Acilan_Ders", on_delete=models.CASCADE, default=1, db_column='AcilanDersID')
    MalzemeID = models.ForeignKey("Malzeme", on_delete=models.CASCADE, default=1, db_column='MalzemeID')

class Aktif_Ogrenci_Ders_Talep(models.Model):
    AktifOgrenciDersID = models.AutoField(primary_key=True)
    DersID = models.ForeignKey("Ders", on_delete=models.CASCADE, db_column='DersID')
    OgrenciID = models.ForeignKey("Aktif_Ogrenci", on_delete=models.CASCADE, db_column='OgrenciID')
