def insert_katilimci(cursor, row):
    """
    Katilimcilar tablosuna kayıt ekler.
    Oluşan katilimci_id'yi geri döndürür.
    """

    query = """
    INSERT INTO Katilimcilar (
        zaman_damgasi,
        yas,
        cinsiyet,
        egitim_durumu,
        calisma_durumu,
        yasadiginiz_mahalle,
        hanedeki_cocuk_sayisi
    )
    OUTPUT INSERTED.katilimci_id
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    cursor.execute(
        query,
        row["zaman_damgasi"],
        row["yas"],
        row["cinsiyet"],
        row["egitim_durumu"],
        row["calisma_durumu"],
        row["yasadiginiz_mahalle"],
        row["hanedeki_cocuk_sayisi"]
    )

    katilimci_id = cursor.fetchone()[0]

    return katilimci_id
def insert_anket(cursor, row, katilimci_id):

    query = """
    INSERT INTO AnketCevaplari (

        katilimci_id,
        mahalledeki_cozulmesi_gereken_sorunlar,
        mahalledeki_parklarin_durumu,
        ilcede_duzenlenecek_cevre_etkinliklerine_katilim_durumu,
        cevre_doga_calismalarina_katilim,
        sokak_hayvanlari_calismalari,
        ilcedeki_oncelikli_toplumsal_calisma,
        ilcedeki_cocuklari_destekleme_calismalari,
        mahalledeki_kres_ihtiyaci,
        cocuklarin_dijital_bagimliliktan_uzaklasmasi_adimlari,
        ogrencilere_yonelik_destek_modeli,
        genclerin_gelisim_faliyetleri,
        ilcedeki_genclerin_istihdam_engeli,
        ilcedeki_kulturel_miras_projesi,
        yetiskinlerin_spora_erisim_organizasyonlari,
        psikososyal_destek,
        gonullu_sorumlulugu_alma,
        topluluga_katki_saglama,
        toplulugun_temel_misyonu,
        acil_onemli_ozgun_proje_fikri,
        ilk_yapilacak_etkinlikler,
        ilk_yapilacak_etkinlik_kisisel

    )

    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """

    cursor.execute(
        query,

        katilimci_id,
        row["mahalledeki_cozulmesi_gereken_sorunlar"],
        row["mahalledeki_parklarin_durumu"],
        row["ilcede_duzenlenecek_cevre_etkinliklerine_katilim_durumu"],
        row["cevre_doga_calismalarina_katilim"],
        row["sokak_hayvanlari_calismalari"],
        row["ilcedeki_oncelikli_toplumsal_calisma"],
        row["ilcedeki_cocuklari_destekleme_calismalari"],
        row["mahalledeki_kres_ihtiyaci"],
        row["cocuklarin_dijital_bagimliliktan_uzaklasmasi_adimlari"],
        row["ogrencilere_yonelik_destek_modeli"],

        # Excel'deki isim
        row["genclerin_gelisim_faaliyetleri"],

        row["ilcedeki_genclerin_istihdam_engeli"],
        row["ilcedeki_kulturel_miras_projesi"],
        row["yetiskinlerin_spora_erisim_organizasyonlari"],
        row["psikososyal_destek"],
        row["gonullu_sorumlulugu_alma"],
        row["topluluga_katki_saglama"],
        row["toplulugun_temel_misyonu"],
        row["acil_onemli_ozgun_proje_fikri"],
        row["ilk_yapilacak_etkinlikler"],
        row["ilk_yapilacak_etkinlik_kisisel"]
    )
def is_duplicate(cursor, row):
        """
        Aynı katılımcı daha önce eklenmiş mi kontrol eder.
        """

        query = """
        SELECT COUNT(*)
        FROM Katilimcilar
        WHERE
            zaman_damgasi = ?
            AND yas = ?
            AND cinsiyet = ?
            AND yasadiginiz_mahalle = ?
        """

        cursor.execute(
            query,
            row["zaman_damgasi"],
            row["yas"],
            row["cinsiyet"],
            row["yasadiginiz_mahalle"]
        )

        count = cursor.fetchone()[0]

        return count > 0