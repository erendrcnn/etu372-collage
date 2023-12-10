import random
import datetime

# Olusturulacak kayit sayisi.
NUM_OF_RECORDS = 20
DATABASE_NAME = "school_management_system"

# Tablo isimleri ve sutun isimlerini tutan dictionary.
tables = {
    "app_IDARI_PERSONEL": ["CalisanID", "Ad", "Soyad", "Adres", "Tel", "Email", "Maas", "BaslangicTarihi", "DeneyimSuresi", "Unvan"],
    "app_TEMIZLIK_GOREVLISI": ["CalisanID", "Ad", "Soyad", "Adres", "Tel", "Email", "Maas", "BaslangicTarihi", "DeneyimSuresi", "CalismaYeri"],
    "app_OGRETMEN": ["CalisanID", "Ad", "Soyad", "Adres", "Tel", "Email", "Maas", "BaslangicTarihi", "DeneyimSuresi"],
    "app_FULL_TIME_OGRETMEN": ["CalisanID"],
    "app_PART_TIME_OGRETMEN": ["CalisanID"],
    "app_HAFTANIN_SAATLERI": ["SaatGunID", "BaslangicVakti", "BitisVakti", "Gun"],
    "app_PART_TIME_OGRETMEN_MESGULIYET": ["PartTimeOgretmenMesguliyetID", "CalisanID", "SaatGunID", "Sebep"],
    "app_AKTIF_OGRENCI": ["OgrenciID", "Ad", "Soyad", "Numara", "Tel", "Email", "Adres", "GPA"],
    "app_MEZUN_OGRENCI": ["OgrenciID", "Ad", "Soyad", "Numara", "Tel", "Email", "Adres", "MezuniyetGPA", "MezuniyetTarihi"],
    "app_VELI": ["VeliID", "OgrenciID", "VeliAdi", "VeliSoyadi", "VeliTel", "VeliEmail"],
    "app_AKTIF_OGRENCI_MESGULIYET": ["AktifOgrenciMesguliyetID", "OgrenciID", "SaatGunID", "Sebep"],
    "app_DERS": ["DersID", "DersAdi", "DersKodu", "CalisanID"],
    "app_ACILAN_DERS": ["AcilanDersID", "DersID", "CalisanID", "DersKodu", "DersAdi", "Syllabus", "DersGunu", "DersSaati1", "DersSaati2"],
    "app_AKTIF_OGRENCI_ACILAN_DERS_ALIR": ["AktifOgrenciAcilanDersID", "AcilanDersID", "OgrenciID"],
    "app_AKTIF_OGRENCI_DERS_TALEP" : ["AktifOgrenciDersID", "DersID", "OgrenciID"],
    "app_EK_GIDER": ["GiderID", "GiderAciklamasi", "GiderMiktari", "GiderTarihi"],
    "app_MALZEME": ["MalzemeID", "GiderID", "MalzemeMiktari", "MalzemeFiyat", "MalzemeTuru"],
    "app_MALZEME_DERS": ["MalzemeDersID", "AcilanDersID", "MalzemeID"],
    "app_SABIT_GIDER": ["GiderID", "GiderAciklamasi", "GiderMiktari"]
}

# ID counters
id_counters = {
    "CalisanID": 1, "OgrenciID": 1, "VeliID": 1, "GiderID": 1, "DersID": 1, "SaatGunID": 1, "MalzemeID": 1
}

# Specific ID counters
acilan_ders_id_counter = 1
acilan_ders_ogr_counter = NUM_OF_RECORDS * 2 + 1
ders_id_counter = 1
saat_gun_id_counter = 1
malzeme_id_counter = 1
malzemeders_id_counter = 1
ogrenci_id_counter = 1
mezun_ogrenci_id_counter = 501
aktif_ogr_ders_id_counter = 1
aktif_ogr_talep_id_counter = 1
aktif_ogr_mesguliyet_id_counter = 1
part_time_ogretmen_mesguliyet_id_counter = 1
malzeme_ders_id_counter = 1
part_time_ogretmen_id = []
part_time_ogretmen_m_id = []
full_time_ogretmen_id = []
ogrenci_soyad_list = []
ogr_email_list = []
ogrt_email_list = []
idari_email_list = []
veli_email_list = []
temizlik_email_list = []
gunler = ["Pazartesi", "Sali", "Carsamba", "Persembe", "Cuma"]
saat_araliklari = ["'07:00:00', '08:00:00'", "'08:00:00', '09:00:00'", "'09:00:00', '10:00:00'", "'10:00:00', '11:00:00'", "'11:00:00', '12:00:00'", "'12:00:00', '13:00:00'", "'13:00:00', '14:00:00'", "'14:00:00', '15:00:00'", "'15:00:00', '16:00:00'", "'16:00:00', '17:00:00'", "'17:00:00', '18:00:00'"]

def create_insert_statements(table_name, column_names, num_records):
    insert_statements = []
    # Ad ve Soyad değerlerini saklamak için listeler
    first_names = []
    last_names = []
    global id_counters, acilan_ders_id_counter, acilan_ders_ogr_counter, ders_id_counter, saat_gun_id_counter, malzeme_id_counter, part_time_ogretmen_id, part_time_ogretmen_m_id, full_time_ogretmen_id, ogrenci_id_counter, mezun_ogrenci_id_counter, malzemeders_id_counter, aktif_ogr_ders_id_counter, aktif_ogr_mesguliyet_id_counter, part_time_ogretmen_mesguliyet_id_counter, malzeme_ders_id_counter, ogrenci_soyad_list, aktif_ogr_talep_id_counter, ogr_email_list, ogrt_email_list, idari_email_list, veli_email_list, temizlik_email_list
    
    # PART_TIME ve FULL_TIME app_OGRETMEN tablolarina kayit eklerken, app_OGRETMEN tablosuna da kayit eklememiz gerekiyor.
    if table_name == "app_OGRETMEN":
        num_records *= 2

    for i in range(num_records):
        values = []
        half_size = num_records // 2
        for col in column_names:
            if col == "AcilanDersID":
                if table_name == "app_ACILAN_DERS":
                    values.append(str(acilan_ders_id_counter))
                    acilan_ders_id_counter += 1
                else:
                    values.append(str(random.randint(1, acilan_ders_id_counter - 1)))
            elif col == "DersID":
                if table_name == "app_DERS":
                    values.append(str(ders_id_counter))
                    ders_id_counter += 1
                else:
                    values.append(str(random.randint(1, ders_id_counter - 1)))
            elif col == "SaatGunID":
                values.append(str(random.randint(1, gunler.__len__() * saat_araliklari.__len__())))
            elif col == "MalzemeID":
                if table_name == "app_MALZEME":
                    values.append(str(malzeme_id_counter))
                    malzeme_id_counter += 1
                elif table_name == "app_MALZEME_DERS":
                    values.append(str(malzemeders_id_counter))
                    malzemeders_id_counter += 1
                else:
                    values.append(str(random.randint(1, malzeme_id_counter - 1)))
            elif col == "CalisanID":
                if table_name == "app_OGRETMEN":
                    if i < half_size:
                        values.append(str(id_counters[col]))
                        part_time_ogretmen_id.append(str(id_counters[col]))
                        part_time_ogretmen_m_id.append(str(id_counters[col]))
                        id_counters[col] += 1
                    else:
                        values.append(str(id_counters[col]))
                        full_time_ogretmen_id.append(str(id_counters[col]))
                        id_counters[col] += 1
                elif table_name == "app_FULL_TIME_OGRETMEN":
                    if len(full_time_ogretmen_id) > 0:
                        values.append(full_time_ogretmen_id.pop(0))
                elif table_name == "app_PART_TIME_OGRETMEN":
                    if len(part_time_ogretmen_id) > 0:
                        values.append(part_time_ogretmen_id.pop(0))
                elif table_name == "app_PART_TIME_OGRETMEN_MESGULIYET":
                    if len(part_time_ogretmen_m_id) > 0:
                        values.append(part_time_ogretmen_m_id.pop(0))
                elif table_name == "app_ACILAN_DERS" or table_name == "app_DERS":
                    values.append(str(acilan_ders_ogr_counter))
                    acilan_ders_ogr_counter += 1
                elif col in id_counters:
                    values.append(str(id_counters[col]))
                    id_counters[col] += 1
                else:
                    values.append("NULL")
            elif col == "OgrenciID":
                if table_name == "app_AKTIF_OGRENCI":
                    values.append(str(id_counters[col]))
                    id_counters[col] += 1
                elif table_name == "app_MEZUN_OGRENCI":
                    values.append(str(mezun_ogrenci_id_counter))
                    mezun_ogrenci_id_counter += 1
                else:
                    if ogrenci_id_counter != num_records + 1:
                        values.append(str(ogrenci_id_counter))
                        ogrenci_id_counter += 1
                    else:
                        ogrenci_id_counter = 1
                        values.append(str(ogrenci_id_counter))
                        ogrenci_id_counter += 1
            elif col == "AktifOgrenciDersID":
                if table_name == "app_AKTIF_OGRENCI_DERS_TALEP":
                    values.append(str(aktif_ogr_talep_id_counter))
                    aktif_ogr_talep_id_counter += 1
                else:
                    values.append(str(random.randint(1, aktif_ogr_talep_id_counter - 1)))
            elif col == "GiderID":
                if table_name == "app_EK_GIDER":
                    values.append(str(id_counters[col]))
                    id_counters[col] += 1
                elif table_name == "app_SABIT_GIDER":
                    values.append(str(id_counters[col]))
                    id_counters[col] += 1
                else:
                    values.append("NULL")
            elif col == "VeliID":
                if table_name == "app_VELI":
                    values.append(str(id_counters[col]))
                    id_counters[col] += 1
                else:
                    values.append(str(random.randint(1, id_counters[col] - 1)))
            elif col == "AktifOgrenciAcilanDersID":
                if table_name == "app_AKTIF_OGRENCI_ACILAN_DERS_ALIR":
                    values.append(str(aktif_ogr_ders_id_counter))
                    aktif_ogr_ders_id_counter += 1
                else:
                    values.append(str(random.randint(1, aktif_ogr_ders_id_counter - 1)))
            elif col == "AktifOgrenciMesguliyetID":
                if table_name == "app_AKTIF_OGRENCI_MESGULIYET":
                    values.append(str(aktif_ogr_mesguliyet_id_counter))
                    aktif_ogr_mesguliyet_id_counter += 1
                else:
                    values.append(str(random.randint(1, aktif_ogr_mesguliyet_id_counter - 1)))
            elif col == "PartTimeOgretmenMesguliyetID":
                if table_name == "app_PART_TIME_OGRETMEN_MESGULIYET":
                    values.append(str(part_time_ogretmen_mesguliyet_id_counter))
                    part_time_ogretmen_mesguliyet_id_counter += 1
                else:
                    values.append(str(random.randint(1, part_time_ogretmen_mesguliyet_id_counter - 1)))
            elif col == "MalzemeDersID":
                if table_name == "app_MALZEME_DERS":
                    values.append(str(malzeme_ders_id_counter))
                    malzeme_ders_id_counter += 1
                else:
                    values.append(str(random.randint(1, malzeme_ders_id_counter - 1)))
            # Handle other columns as before
            elif col in ["Ad", "VeliAdi"]:
                firstname = random.choice([
                                    "JALE", "ALI", "MAHMUT", "MANSUR", "KURSAD", "GAMZE", "MIRAC", "YUCEL", "KUBILAY",
                                    "HAYATI", "BEDRIYE MUGE", "BIRSEN", "SERDAL", "BUNYAMIN", "OZGUR", "FERDI", "REYHAN",
                                    "ILHAN", "GULSAH", "NALAN", "SEMIH", "ERGUN", "FATIH", "SENAY", "SERKAN", "EMRE",
                                    "BAHATTIN", "IRAZCA", "HATICE", "BARIS", "REZAN", "FATIH", "FUAT", "GOKHAN", "ORHAN",
                                    "MEHMET", "EVREN", "OKTAY", "HARUN", "YAVUZ", "PINAR", "MEHMET", "UMUT", "MESUDE",
                                    "HUSEYIN CAHIT", "HASIM ONUR", "EYYUP SABRI", "MUSTAFA", "UFUK", "AHMET ALI",
                                    "MEDIHA", "HASAN", "KAMIL", "NEBI", "OZCAN", "NAGIHAN", "CEREN", "SERKAN", "HASAN",
                                    "YUSUF KENAN", "CETIN", "TARKAN", "MERAL LEMAN", "ERGUN", "KENAN AHMET", "METIN", "YAHYA",
                                    "BENGU", "FATIH NAZMI", "DILEK", "MEHMET", "TUFAN AKIN", "MEHMET", "TURGAY YILMAZ", "GULDEHEN",
                                    "GOKMEN", "BULENT", "EROL", "BAHRI", "OZEN OZLEM", "SELMA", "TUGSEM", "TESLIME NAZLI", "GULCIN",
                                    "ISMAIL", "MURAT", "EBRU", "TUMAY", "AHMET", "EBRU", "HUSEYIN YAVUZ", "BASAK", "AYSEGUL",
                                    "EVRIM", "YASER", "ULKU", "OZHAN", "UFUK", "AKSEL", "FULYA", "BURCU", "TAYLAN", "YILMAZ",
                                    "ZEYNEP", "BAYRAM", "GULAY", "RABIA", "SEVDA", "SERHAT", "ENGIN", "ASLI", "TUBA", "BARIS",
                                    "SEVGI", "KALENDER", "HALIL", "BILGE", "FERDA", "EZGI", "AYSUN", "SEDA", "OZLEM", "OZDEN",
                                    "KORAY", "SENEM", "LATIFE", "EMEL", "BATURAY KANSU", "NURAY", "EREN", "OZLEM", "DENIZ",
                                    "ILKNUR", "TEVFIK OZGUN", "HASAN SERKAN", "KURSAT", "SEYFI", "SEYMA", "OZLEM", "ERSAGUN",
                                    "DILBER", "MESUT", "ELIF", "MUHAMMET FATIH", "OZGUR SINAN", "MEHMET OZGUR", "MAHPERI", "ONUR",
                                    "IBRAHIM", "FATIH", "CAN ATA", "SUHEYLA", "VOLKAN", "ILKAY", "ILKNUR", "ZUMRUT ELA", "HALE",
                                    "YENER", "SEDEF", "FADIL", "SERPIL", "ZULFIYE", "SULTAN", "MUAMMER HAYRI", "DERVIS", "YASAR GOKHAN",
                                    "TUBA HANIM", "MEHRI", "MUSTAFA FERHAT", "SERDAR", "MUSTAFA EMRE", "ONAT", "SUKRU", "OLCAY BASAK",
                                    "SERDAR", "YILDIZ", "AYDIN", "ALI HALUK", "NIHAT BERKAY", "ISMAIL"])
                values.append("'" + firstname + "'")     # Adı verilere kaydet.
                first_names.append(firstname.strip("'").lower())            # Adı listeye kaydet
            elif col in ["Soyad"]:
                random_soyad = random.choice([
                        "SEN", "KANDEMiR", "CEViK", "ERKURAN", "TUTEN", "OZTURK", "YUZBASIOGLU", "VURAL", "YUCEL", "SONMEZ", "ERTEKiN",
                        "DEDE", "UYANIK", "ASLAN", "AKBULUT", "ORHON", "UZ", "YAVUZ", "ERDEM", "KULAC", "KAYA", "SELVi", "AKPINAR",
                        "ABACIOGLU", "CAY", "ISIK", "OZER", "OZDEMiR", "OZTURK", "TAHTACI", "BUYUKCAM", "KULAKSIZ", "AKSEL", "EROGLU",
                        "KARAKUM", "DAL", "OCAL", "AYHAN", "YiGiT", "YARBiL", "CANACANKATAN", "GUMUSAY", "MURT", "HALHALLI", "ULUOZ",
                        "SEYHANLI", "CALISKANTURK", "YILMAZ", "SARACOGLU", "SEZER", "DOGAN", "DEMiR", "KAYAYURT", "SURUM", "YAVASi",
                        "TURGUT", "TANRIKULU", "BARBAROS", "ALDiNC", "TEKiN", "GULSAN", "KUFECiLER", "ALMACIOGLU", "CINDEMIR",
                        "TURKDOGAN", "KAYA", "ONER", "SELiMAN", "YAMAN", "ATiK", "YiGiT", "GiRAY", "YALCINKAYA", "KILIC", "SENTURK",
                        "KARABAG", "DEGiRMENCi", "BODUROGLU", "YILDIZ", "GULER", "ERASLAN", "UZER", "PiSiRGEN", "ADANIR", "KOC",
                        "KORKMAZ", "YENiDOGAN", "AYDOGAN", "HACCACOGLU", "ERGE", "ERDOGAN", "OGUT AYDIN", "KUTLU", "KUCUR", "TULUBAS",
                        "PEKTAS", "KAYACAN", "GULEN", "DOGAN", "BADILLIOGLU", "GULEN", "AKKUCUK", "CANDAN", "TEMEL", "YENiGUN",
                        "YILDIRIM", "BEDER", "AKINCI", "OZDEMiR", "ONUK", "AYDOGAN", "YILMAZ", "AKCAN", "ATASOY", "SARACOGLU", "CEKiC",
                        "COMERT", "TOPAL", "KARAHAN", "SAHiN", "CETiN", "YILMAZ", "INAL", "AYTAC", "YILDIZ", "ALTUN", "KiSi", "GUNDUZ",
                        "OZKURT", "PURCU", "AK", "URFALI", "KARAMAN", "MEMETOGLU", "KAZBEK", "KiRECCi", "AKIN", "YADiGAROGLU", "YUKSEL",
                        "OZCELiK", "BABUS", "KAPLAN", "AKOZ", "KARTAL", "BiLGiC", "ERDEN", "TUGCUGiL", "KUMRAL", "ERBAS", "ORAL",
                        "DURUCAN", "CENGiZ", "YILDIRIM", "KUTLUCAN", "BAGCI", "BALABAN", "KAYA", "BALCI", "TUFEKCi", "ATAY", "YARAR", "SEVER"])

                last_names.append(random_soyad.strip("'").lower())  # Soyadı listeye kaydet

                if table_name == "app_AKTIF_OGRENCI":
                    ogrenci_soyad_list.append(random_soyad)

                values.append("'" + random_soyad + "'")
            elif col == "VeliSoyadi":
                curr_soyad = ogrenci_soyad_list.pop(0)
                values.append("'" + curr_soyad + "'")
                last_names.append(curr_soyad.strip("'").lower())    # Soyadı listeye kaydet
            elif col == "DersAdi":
                values.append("'" + random.choice(["Matematik", "Ingilizce", "Almanca", "Satranc" , "Web Tasarim", "Robotik Programlama", "Turkce", "Muzik", "Biyoloji", "Kimya", "Fizik", "Tarih", "Cografya"]) + "'")
            elif col in ["Adres"]:
                values.append("'" + random.choice(["Altindag", "Cankaya", "Etimesgut", "Kecioren", "Mamak", "Sincan", "Yenimahalle", "Akyurt", "Ayas", "Bala", "Beypazari", "Camlidere", "Cubuk", "Elmadag", "Evren", "Golbasi", "Gudul", "Haymana", "Kalecik", "Kazan", "Kizilcahamam", "Nallihan", "Polatli", "Sereflikochisar"]) + "'")
            elif col == "Numara":
                values.append("'201" + str(random.randint(100000, 999999)) + "'")
            elif col.endswith("Tel"):
                values.append("'05" + str(random.randint(100000000, 999999999)) + "'")
            elif col.endswith("Email"):
                # Adın ilk harfi ve soyadı birleştirerek email oluştur
                email = f"{first_names[-1][0]}{last_names[-1]}@etu372.edu.tr"
                values.append("'" + email + "'")

                if table_name == "app_OGRETMEN":
                    ogrt_email_list.append(email)
                elif table_name == "app_IDARI_PERSONEL":
                    idari_email_list.append(email)
                elif table_name == "app_VELI":
                    veli_email_list.append(email)
                elif table_name == "app_TEMIZLIK_GOREVLISI":
                    temizlik_email_list.append(email)
                else:
                    ogr_email_list.append(email)
            elif col == "Unvan":
                if i == 0:
                    values.append("'Mudur'")
                else:
                    values.append("'" + random.choice(["Mudur Yardimcisi", "Sekreter", "Muhasebeci", "Memur", "Bilisim Sorumlusu"]) + "'")
            elif col in ["Maas", "GiderMiktari", "MalzemeFiyat"]:
                values.append(str(random.uniform(2500.00, 35000.00).__format__(".2f")))
            elif col in ["BaslangicTarihi", "MezuniyetTarihi", "GiderTarihi"]:
                values.append("'" + str(datetime.date(random.randint(2000, 2023), random.randint(1, 12), random.randint(1, 28))) + "'")
            elif col == "DeneyimSuresi":
                values.append(str(random.randint(1, 30)))
            elif col == "GPA" or col == "MezuniyetGPA":
                values.append(str(random.uniform(2.00, 4.00)))
            elif col == "DersKodu":
                values.append("'D" + str(random.randint(100, 999)) + "'")
            elif col == "Syllabus":
                values.append("'Syllabus Content'")
            elif col == "Sebep":
                values.append("'" + random.choice(["Izinli", "Toplanti", "Egitim", "Hastalik", "Konferans", "Seminer"]) + "'")
            elif col == "MalzemeTuru":
                values.append("'" + random.choice(["Kitap", "Defter", "Kalem", "Laboratuvar Malzemesi", "Sanat Malzemesi", "Silgi", "Tahta Kalemi", "Kagit"]) + "'")
            elif col == "GiderAciklamasi":
                values.append("'" + random.choice(["Elektrik Faturasi", "Su Faturasi", "Dogalgaz Faturasi", "Bakim Giderleri", "Yazilim Lisansi", "Kirtasiye Gideri"]) + "'")
            elif col == "DersSaati1" or col == "DersSaati2":
                values.append("NULL")
            elif col in ["BaslangicVakti", "BitisVakti", "Gun"]:
                values.append("") # Sonra doldurulacak.
                #values.append("'" + str(random.randint(7, 18)) + ":00:00'")
            elif col == "MalzemeMiktari":
                values.append(str(random.randint(1, 100)))
            else:
                values.append("NULL")


        insert_statements.append(f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(values)});")
    return insert_statements

# Dosyaya database olusturmak icin gerekli kodlari yazdiralim.
output_file = open("DBGenerator.sql", "w")

print("-- USE DBNAME;")
print("USE " + DATABASE_NAME + ";\n")
output_file.write("USE " + DATABASE_NAME + ";\n")

# Define the table dependencies (child tables depend on parent tables)
table_dependencies = {
    "app_IDARI_PERSONEL": [],
    "app_TEMIZLIK_GOREVLISI": [],
    "app_OGRETMEN": [],
    "app_PART_TIME_OGRETMEN": ["app_OGRETMEN"],
    "app_FULL_TIME_OGRETMEN": ["app_OGRETMEN"],
    "app_HAFTANIN_SAATLERI": [],
    "app_PART_TIME_OGRETMEN_MESGULIYET": ["app_PART_TIME_OGRETMEN", "app_HAFTANIN_SAATLERI"],
    "app_MEZUN_OGRENCI": [],
    "app_AKTIF_OGRENCI": [],
    "app_VELI": ["app_AKTIF_OGRENCI"],
    "app_AKTIF_OGRENCI_MESGULIYET": ["app_AKTIF_OGRENCI", "app_HAFTANIN_SAATLERI"],
    "app_DERS": ["app_OGRETMEN"],
    "app_ACILAN_DERS": ["app_OGRETMEN", "app_DERS"],
    "app_AKTIF_OGRENCI_ACILAN_DERS_ALIR": ["app_ACILAN_DERS", "app_AKTIF_OGRENCI"],
    "app_AKTIF_OGRENCI_DERS_TALEP" : ["app_DERS", "app_AKTIF_OGRENCI"],
    "app_EK_GIDER": [],
    "app_MALZEME": ["app_EK_GIDER"],
    "app_MALZEME_DERS": ["app_ACILAN_DERS", "app_MALZEME"],
    "app_SABIT_GIDER": [],
}

# Function to perform topological sort
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                dfs(neighbor)
            stack.append(node)

    for node in graph.keys():
        dfs(node)

    return stack[::-1]

# Get the sorted table names
sorted_tables = topological_sort(table_dependencies)

# Generate DELETE statements based on the sorted order
print("-- Delete statements for all tables")
for table_name in sorted_tables:
    print(f"DELETE FROM {table_name};")
    output_file.write("DELETE FROM " + table_name + ";\n")
print()
output_file.write("\n")

# Sonrasinda app_HAFTANIN_SAATLERI tablosu icin INSERT kodlarini yazdiralim.
print("-- Insert statements for app_HAFTANIN_SAATLERI")
for gun in gunler:
    for saat_araligi in saat_araliklari:
        print(f"INSERT INTO app_HAFTANIN_SAATLERI (SaatGunID, BaslangicVakti, BitisVakti, Gun) VALUES ({saat_gun_id_counter}, {saat_araligi}, '{gun}');")
        output_file.write("INSERT INTO app_HAFTANIN_SAATLERI (SaatGunID, BaslangicVakti, BitisVakti, Gun) VALUES (" + str(saat_gun_id_counter) + ", " + saat_araligi + ", '" + gun + "');\n")
        saat_gun_id_counter += 1
print()
output_file.write("\n")

# Sonrasinda tum tablolar icin INSERT kodlarini yazdiralim.
for table_name, column_names in tables.items():
    insert_statements = create_insert_statements(table_name, column_names, NUM_OF_RECORDS)
    if table_name != "app_HAFTANIN_SAATLERI":
        print(f"-- Insert statements for {table_name}")
        for statement in insert_statements:
            print(statement)
            output_file.write(statement)
    print()
    output_file.write("\n")

# VERİTABANI İÇİN PART-TIME ÖĞRETMENLERİN MEŞGUL OLMADIĞI VE
# ÖĞRENCİLERİN MEŞGUL OLMADIĞI YERLERE app_DERS SAATLERİNİN DEĞERLERİNİ ATAYACAK ŞEKİLDE BİR QUERY YAZ.
print("-- Update statements for app_ACILAN_DERS")
print("UPDATE app_ACILAN_DERS ad\n" +
      "SET ad.DersSaati1 = (\n" +
      "    SELECT h.BaslangicVakti\n" +
      "    FROM app_HAFTANIN_SAATLERI h\n" +
      "    LEFT JOIN app_PART_TIME_OGRETMEN_MESGULIYET ptm ON h.SaatGunID = ptm.SaatGunID\n" +
      "    LEFT JOIN app_AKTIF_OGRENCI_MESGULIYET aom ON h.SaatGunID = aom.SaatGunID\n" +
      "    WHERE ptm.CalisanID IS NULL AND aom.OgrenciID IS NULL\n" +
      "    ORDER BY RAND()\n" +
      "    LIMIT 1\n" +
      ");")
output_file.write("UPDATE app_ACILAN_DERS ad SET ad.DersSaati1 = (SELECT h.BaslangicVakti FROM app_HAFTANIN_SAATLERI h LEFT JOIN app_PART_TIME_OGRETMEN_MESGULIYET ptm ON h.SaatGunID = ptm.SaatGunID LEFT JOIN app_AKTIF_OGRENCI_MESGULIYET aom ON h.SaatGunID = aom.SaatGunID WHERE ptm.CalisanID IS NULL AND aom.OgrenciID IS NULL ORDER BY RAND() LIMIT 1);" + "\n")

# Dosyayi kapat.
output_file.close()

# Mailleri ayrı ayrı dosyalara kaydet.
ogr_email_file = open("ogr_email_list.txt", "w")
ogrt_email_file = open("ogrt_email_list.txt", "w")
idari_email_file = open("idari_email_list.txt", "w")
veli_email_file = open("veli_email_list.txt", "w")
temizlik_email_file = open("temizlik_email_list.txt", "w")

for email in ogr_email_list:
    ogr_email_file.write(email + "\n")
for email in ogrt_email_list:
    ogrt_email_file.write(email + "\n")
for email in idari_email_list:
    idari_email_file.write(email + "\n")
for email in veli_email_list:
    veli_email_file.write(email + "\n")
for email in temizlik_email_list:
    temizlik_email_file.write(email + "\n")

ogr_email_file.close()
ogrt_email_file.close()
idari_email_file.close()
veli_email_file.close()
temizlik_email_file.close()