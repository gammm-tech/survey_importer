# Survey Importer

## Proje Hakkında

Survey Importer, Excel veya Google Sheets üzerinden alınan anket verilerini Microsoft SQL Server veritabanına güvenli şekilde aktarmak için geliştirilmiş bir Python uygulamasıdır.

Uygulama, veri aktarımı sırasında:

- Veri doğrulama (Validation)
- Mükerrer kayıt (Duplicate) kontrolü
- Hata yönetimi
- İşlem loglama

işlemlerini gerçekleştirerek veritabanına yalnızca geçerli kayıtların eklenmesini sağlar.

---

## Kullanılan Teknolojiler

- Python 3.11
- Microsoft SQL Server
- SQL Server Management Studio (SSMS)
- pyodbc
- pandas
- openpyxl
- requests

---

## Proje Yapısı

```
survey_importer/
│
├── config.py          # Veritabanı ayarları
├── db.py              # SQL Server bağlantısı
├── sheets.py          # Excel / Google Sheets okuma
├── validator.py       # Veri doğrulama işlemleri
├── importer.py        # SQL'e veri aktarımı
├── logger.py          # Log yönetimi
├── main.py            # Uygulamanın başlangıç noktası
│
├── logs/
│   └── import_log.txt
│
├── requirements.txt
├── README.md
└── survey.xlsx
```

---

## Özellikler

### Veri Doğrulama

Aktarım öncesinde aşağıdaki kontroller yapılır:

- Zorunlu alan kontrolü
- Yaş doğrulaması
- Tarih doğrulaması
- Karakter uzunluğu kontrolü
- Boş veri kontrolü

---

### Duplicate Kontrolü

Her kayıt eklenmeden önce aşağıdaki alanlar kullanılarak veritabanında kontrol edilir:

- zaman_damgasi
- yas
- cinsiyet
- yasadiginiz_mahalle

Aynı kayıt bulunursa tekrar eklenmez.

---

### Loglama

Her işlem `logs/import_log.txt` dosyasına kaydedilir.

Log seviyeleri:

- INFO
- WARNING
- ERROR

Örnek:

```
[2026-07-19 20:15:31] [INFO] Yeni içe aktarma işlemi başlatıldı.
[2026-07-19 20:15:32] [WARNING] Satır 15 validation hatası.
[2026-07-19 20:15:34] [INFO] Satır 16 başarıyla veritabanına eklendi.
```

---

## Kurulum

### 1. Projeyi klonlayın

```
git clone <repo-url>
```

---

### 2. Gerekli paketleri yükleyin

```
pip install -r requirements.txt
```

---

### 3. Veritabanı bağlantısını yapılandırın

`config.py` dosyasını düzenleyin.

```
SERVER=
DATABASE=
USERNAME=
PASSWORD=
```

---

### 4. Excel dosyasını proje klasörüne ekleyin

Örnek:

```
anket.xlsx
```

---

### 5. Programı çalıştırın

```
py -3.11 main.py
```

---

## Çalışma Akışı

```
Excel / Google Sheets

        │
        ▼

Veri Okuma

        │
        ▼

Validation

        │
        ▼

Duplicate Kontrolü

        │
        ▼

Katilimcilar Tablosu

        │
        ▼

AnketCevaplari Tablosu

        │
        ▼

Commit

        │
        ▼

Log Oluşturma
```

---

## Hata Yönetimi

Uygulama `try-except-finally` yapısını kullanmaktadır.

- Beklenmeyen hatalarda `rollback()` uygulanır.
- İşlem sonunda bağlantı güvenli şekilde kapatılır.
- Hatalar log dosyasına kaydedilir.

---

## Geliştirilen Özellikler

- Excel / Google Sheets veri okuma
- SQL Server bağlantısı
- Veri doğrulama
- Duplicate kontrolü
- İki tabloya ilişkili veri aktarımı
- Transaction yönetimi
- Loglama sistemi
- Hata yönetimi
