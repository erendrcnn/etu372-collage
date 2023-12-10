DROP DATABASE IF EXISTS proje;
CREATE DATABASE IF NOT EXISTS proje;
USE proje;

-- IDARI_PERSONEL tablosunu oluşturma
CREATE TABLE IDARI_PERSONEL (
    CalisanID INT NOT NULL PRIMARY KEY,
    Ad VARCHAR(255),
    Soyad VARCHAR(255),
    Adres VARCHAR(255),
    Tel VARCHAR(255),
    Email VARCHAR(255),
    Maas DECIMAL(10, 2),
    BaslangicTarihi DATE,
    DeneyimSuresi INT,
    Unvan VARCHAR(255)
);

-- TEMIZLIK_GOREVLISI tablosunu oluşturma
CREATE TABLE TEMIZLIK_GOREVLISI (
    CalisanID INT NOT NULL PRIMARY KEY,
    Ad VARCHAR(255),
    Soyad VARCHAR(255),
    Adres VARCHAR(255),
    Tel VARCHAR(255),
    Email VARCHAR(255),
    Maas DECIMAL(10, 2),
    BaslangicTarihi DATE,
    DeneyimSuresi INT,
    CalismaYeri VARCHAR(255)
);

-- Genel OGRETMEN tablosunu oluşturma
CREATE TABLE OGRETMEN (
    CalisanID INT NOT NULL PRIMARY KEY,
    Ad VARCHAR(255),
    Soyad VARCHAR(255),
    Adres VARCHAR(255),
    Tel VARCHAR(255),
    Email VARCHAR(255),
    Maas DECIMAL(10, 2),
    BaslangicTarihi DATE,
    DeneyimSuresi INT
);

-- PART_TIME_OGRETMEN tablosunu oluşturma, OGRETMEN'den türetilmiş
CREATE TABLE PART_TIME_OGRETMEN (
    CalisanID INT NOT NULL PRIMARY KEY,
    FOREIGN KEY (CalisanID) REFERENCES OGRETMEN(CalisanID)
);

-- FULL_TIME_OGRETMEN tablosunu oluşturma, OGRETMEN'den türetilmiş
CREATE TABLE FULL_TIME_OGRETMEN (
    CalisanID INT NOT NULL PRIMARY KEY,
    FOREIGN KEY (CalisanID) REFERENCES OGRETMEN(CalisanID)
);

-- HAFTANIN_SAATLERI tablosunu oluşturma
CREATE TABLE HAFTANIN_SAATLERI (
    SaatGunID INT NOT NULL PRIMARY KEY,
    BaslangicVakti TIME,
    BitisVakti TIME,
    Gun VARCHAR(255)
);

-- PART_TIME_OGRETMEN_MESGULIYET tablosunu oluşturma
CREATE TABLE PART_TIME_OGRETMEN_MESGULIYET (
    PartTimeOgretmenMesguliyetID INTEGER NOT NULL,
    CalisanID INT,
    SaatGunID INT,
    Sebep VARCHAR(255),
    PRIMARY KEY (PartTimeOgretmenMesguliyetID),
    FOREIGN KEY (CalisanID) REFERENCES PART_TIME_OGRETMEN(CalisanID),
    FOREIGN KEY (SaatGunID) REFERENCES HAFTANIN_SAATLERI(SaatGunID)
);

-- AKTIF_OGRENCI tablosunu oluşturma
CREATE TABLE AKTIF_OGRENCI (
    OgrenciID INT NOT NULL PRIMARY KEY,
    Ad VARCHAR(255),
    Soyad VARCHAR(255),
    Numara VARCHAR(255),
    Tel VARCHAR(255),
    Email VARCHAR(255),
    Adres VARCHAR(255),
    GPA DECIMAL(3, 2)
);

-- MEZUN_OGRENCI tablosunu oluşturma
CREATE TABLE MEZUN_OGRENCI (
    OgrenciID INT NOT NULL PRIMARY KEY,
    Ad VARCHAR(255),
    Soyad VARCHAR(255),
    Numara VARCHAR(255),
    Tel VARCHAR(255),
    Email VARCHAR(255),
    Adres VARCHAR(255),
    MezuniyetGPA DECIMAL(3, 2),
    MezuniyetTarihi DATE
);

-- VELI tablosunu oluşturma
CREATE TABLE VELI (
    VeliID INT NOT NULL,
    OgrenciID INT,
    VeliAdi VARCHAR(255),
    VeliSoyadi VARCHAR(255),
    VeliTel VARCHAR(255),
    VeliEmail VARCHAR(255),
    PRIMARY KEY (VeliID),
    FOREIGN KEY (OgrenciID) REFERENCES AKTIF_OGRENCI(OgrenciID)
);

-- AKTIF_OGRENCI_MESGULIYET tablosunu oluşturma
CREATE TABLE AKTIF_OGRENCI_MESGULIYET (
    AktifOgrenciMesguliyetID INT NOT NULL,
    OgrenciID INT,
    SaatGunID INT,
    Sebep VARCHAR(255),
    PRIMARY KEY (AktifOgrenciMesguliyetID),
    FOREIGN KEY (OgrenciID) REFERENCES AKTIF_OGRENCI(OgrenciID),
    FOREIGN KEY (SaatGunID) REFERENCES HAFTANIN_SAATLERI(SaatGunID)
);

-- DERS tablosunu oluşturma
CREATE TABLE DERS (
    DersID INT NOT NULL PRIMARY KEY,
    CalisanID INT,
    DersAdi VARCHAR(255),
    DersKodu VARCHAR(10),
    FOREIGN KEY (CalisanID) REFERENCES OGRETMEN(CalisanID)
);

-- ACILAN_DERS tablosunu oluşturma
CREATE TABLE ACILAN_DERS (
    AcilanDersID INT NOT NULL,
    CalisanID INT,    
    DersID INT,
    DersAdi VARCHAR(255),
    DersKodu VARCHAR(10),
    Syllabus TEXT,
    DersGunu VARCHAR(10),
    DersSaati1 TIME,
    DersSaati2 TIME,
    PRIMARY KEY (AcilanDersID),
    FOREIGN KEY (CalisanID) REFERENCES OGRETMEN(CalisanID),
    FOREIGN KEY (DersID) REFERENCES DERS(DersID)
);

-- AKTIF_OGRENCI_ACILAN_DERS_ALIR tablosunu oluşturma
CREATE TABLE AKTIF_OGRENCI_ACILAN_DERS_ALIR (
    AktifOgrenciAcilanDersID INT NOT NULL,
    AcilanDersID INT,
    OgrenciID INT,
    PRIMARY KEY (AktifOgrenciAcilanDersID),
    FOREIGN KEY (AcilanDersID) REFERENCES ACILAN_DERS(AcilanDersID),
    FOREIGN KEY (OgrenciID) REFERENCES AKTIF_OGRENCI(OgrenciID)
);

-- AKTIF_OGRENCI_DERS_TALEP tablosunu oluşturma
CREATE TABLE AKTIF_OGRENCI_DERS_TALEP (
    AktifOgrenciDersID INT NOT NULL,
    DersID INT,
    OgrenciID INT,
    PRIMARY KEY (AktifOgrenciDersID),
    FOREIGN KEY (DersID) REFERENCES DERS(DersID),
    FOREIGN KEY (OgrenciID) REFERENCES AKTIF_OGRENCI(OgrenciID)
);

-- EK_GIDER tablosunu oluşturma
CREATE TABLE EK_GIDER (
    GiderID INT NOT NULL PRIMARY KEY,
    GiderAciklamasi VARCHAR(255),
    GiderMiktari DECIMAL(10, 2),
    GiderTarihi DATE
);

-- MALZEME tablosunu oluşturma
CREATE TABLE MALZEME (
    MalzemeID INT NOT NULL PRIMARY KEY,
    MalzemeMiktari INT,
    MalzemeFiyat DECIMAL(10, 2),
    MalzemeTuru VARCHAR(255),
    GiderID INT,
    FOREIGN KEY (GiderID) REFERENCES EK_GIDER(GiderID)
);

-- MALZEMEDERS tablosunu oluşturma
CREATE TABLE MALZEME_DERS (
    MalzemeDersID INT NOT NULL,
    AcilanDersID INT,
    MalzemeID INT,
    PRIMARY KEY (MalzemeDersID),
    FOREIGN KEY (AcilanDersID) REFERENCES ACILAN_DERS(AcilanDersID),
    FOREIGN KEY (MalzemeID) REFERENCES MALZEME(MalzemeID)
);

-- SABIT_GIDER tablosunu oluşturma
CREATE TABLE SABIT_GIDER (
    GiderID INT NOT NULL PRIMARY KEY,
    GiderAciklamasi VARCHAR(255),
    GiderMiktari DECIMAL(10, 2)
);

-- TRIGGER icin ek bir tablo (ER modelinde yok)
CREATE TABLE ContactInfo (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(255),
    Type ENUM('Teacher', 'Student')
);

SET GLOBAL event_scheduler = ON;

-- Aylık Rapor Etkinliği
CREATE EVENT monthly_expense_report
ON SCHEDULE EVERY 1 MONTH STARTS '2023-12-01 00:00:00'
DO
    INSERT INTO MonthlyExpenseReports (report_date, report_content)
    SELECT NOW(), CONCAT_WS(' ', giderAciklamasi, giderMiktari)
    FROM (
        SELECT giderAciklamasi, giderMiktari FROM SABIT_GIDER
        UNION ALL
        SELECT giderAciklamasi, giderMiktari FROM EK_GIDER
    ) AS combined_expenses;

-- Haftalık Rapor Etkinliği
CREATE EVENT weekly_expense_report
ON SCHEDULE EVERY 1 WEEK STARTS '2023-12-01 00:00:00'
DO
    INSERT INTO WeeklyExpenseReports (report_date, report_content)
    SELECT NOW(), CONCAT_WS(' ', giderAciklamasi, giderMiktari)
    FROM (
        SELECT giderAciklamasi, giderMiktari FROM SABIT_GIDER
        UNION ALL
        SELECT giderAciklamasi, giderMiktari FROM EK_GIDER
    ) AS combined_expenses;


DELIMITER //

CREATE TRIGGER AfterMalzemeInsert
AFTER INSERT ON MALZEME
FOR EACH ROW
BEGIN
    IF NEW.MalzemeMiktari = 0 THEN
        INSERT INTO EK_GIDER (GiderAciklamasi, GiderMiktari, GiderTarihi)
        VALUES ('Ek Malzeme Gerekiyor', NEW.MalzemeMiktari * NEW.MalzemeFiyat, CURRENT_DATE());
    END IF;
END; //

CREATE TRIGGER CheckSalaryHierarchy
BEFORE UPDATE ON IDARI_PERSONEL
FOR EACH ROW
BEGIN
    DECLARE full_time_salary DECIMAL(10,2);
    DECLARE part_time_salary DECIMAL(10,2);
    DECLARE cleaning_staff_salary DECIMAL(10,2);
    
    SELECT Maas INTO full_time_salary FROM FULL_TIME_OGRETMEN WHERE CalisanID = NEW.CalisanID;
    SELECT Maas INTO part_time_salary FROM PART_TIME_OGRETMEN WHERE CalisanID = NEW.CalisanID;
    SELECT Maas INTO cleaning_staff_salary FROM TEMIZLIK_GOREVLISI WHERE CalisanID = NEW.CalisanID;

    IF NEW.Maas <= full_time_salary OR full_time_salary <= part_time_salary OR part_time_salary <= cleaning_staff_salary THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Salary hierarchy violation.';
    END IF;
END; //

CREATE TRIGGER after_acilanders_insert
AFTER INSERT ON ACILAN_DERS
FOR EACH ROW
BEGIN
    -- Öğretmenin iletişim bilgilerini ekle
    INSERT INTO ContactInfo (Name, Email, Phone, Type)
    SELECT CONCAT(o.Ad, ' ', o.Soyad), o.Email, o.Tel, 'Teacher'
    FROM OGRETMEN o
    WHERE o.CalisanID = NEW.CalisanID;

    -- Dersi alan öğrencilerin iletişim bilgilerini ekle
    INSERT INTO ContactInfo (Name, Email, Phone, Type)
    SELECT CONCAT(ao.Ad, ' ', ao.Soyad), ao.Email, ao.Tel, 'Student'
    FROM AKTIF_OGRENCI ao
    JOIN AKTIF_OGRENCI_ACILAN_DERS_ALIR aoda ON ao.OgrenciID = aoda.OgrenciID
    WHERE aoda.AcilanDersID = NEW.AcilanDersID;
END;

DELIMITER ;

-- Bu tablolar ve ilişkileri, görseldeki şemaya dayanmaktadır.
-- Her bir tablonun oluşturulması için ilgili sütunlar ve kısıtlamalar eklendi.
-- Yabancı anahtar kısıtlamaları, ilişkili tabloların sütunlarına referans verir şekilde ayarlandı.