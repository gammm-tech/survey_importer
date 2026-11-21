import pandas as pd


def validate_required(row):
    """
    Zorunlu alanların boş olup olmadığını kontrol eder.
    """

    required_fields = [
        "zaman_damgasi",
        "yas",
        "cinsiyet",
        "yasadiginiz_mahalle"
    ]

    errors = []

    for field in required_fields:
        if pd.isna(row[field]) or str(row[field]).strip() == "":
            errors.append(f"{field} boş.")

    return errors


def validate_age(row):
    """
    Yaş bilgisini kontrol eder.
    """

    errors = []

    try:
        age = int(row["yas"])

        if age < 0 or age > 120:
            errors.append("Yaş 0-120 arasında olmalıdır.")

    except:
        errors.append("Yaş sayısal değil.")

    return errors


def validate_datetime(row):
    """
    Tarih bilgisini kontrol eder.
    """

    errors = []

    try:
        pd.to_datetime(row["zaman_damgasi"])
    except:
        errors.append("Geçersiz zaman damgası.")

    return errors


def validate_lengths(row):
    """
    Metin alanlarının maksimum uzunluklarını kontrol eder.
    """

    limits = {
        "cinsiyet": 15,
        "egitim_durumu": 75,
        "calisma_durumu": 75,
        "yasadiginiz_mahalle": 100,
        "hanedeki_cocuk_sayisi": 50,
        "mahalledeki_cozulmesi_gereken_sorunlar": 500,
        "mahalledeki_parklarin_durumu": 100,
        "ilcede_duzenlenecek_cevre_etkinliklerine_katilim_durumu": 75,
        "cevre_doga_calismalarina_katilim": 350,
        "sokak_hayvanlari_calismalari": 100,
        "ilcedeki_oncelikli_toplumsal_calisma": 75,
        "ilcedeki_cocuklari_destekleme_calismalari": 500,
        "mahalledeki_kres_ihtiyaci": 100,
        "cocuklarin_dijital_bagimliliktan_uzaklasmasi_adimlari": 300,
        "ogrencilere_yonelik_destek_modeli": 100,
        "genclerin_gelisim_faaliyetleri": 500,
        "ilcedeki_genclerin_istihdam_engeli": 120,
        "ilcedeki_kulturel_miras_projesi": 100,
        "yetiskinlerin_spora_erisim_organizasyonlari": 500,
        "psikososyal_destek": 300,
        "gonullu_sorumlulugu_alma": 50,
        "topluluga_katki_saglama": 300,
        "toplulugun_temel_misyonu": 100,
        "acil_onemli_ozgun_proje_fikri": 350,
        "ilk_yapilacak_etkinlikler": 500,
        "ilk_yapilacak_etkinlik_kisisel": 500
    }

    errors = []

    for field, max_length in limits.items():

        if pd.isna(row[field]):
            continue

        if len(str(row[field])) > max_length:
            errors.append(
                f"{field} alanı {max_length} karakterden uzun."
            )

    return errors


def validate_row(row):
    """
    Tüm kontrolleri çalıştırır.
    """

    errors = []

    errors.extend(validate_required(row))
    errors.extend(validate_age(row))
    errors.extend(validate_datetime(row))
    errors.extend(validate_lengths(row))

    return errors