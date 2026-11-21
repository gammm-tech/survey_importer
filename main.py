from db import get_connection
from sheets import read_sheet
from validator import validate_row
from importer import (
    is_duplicate,
    insert_katilimci,
    insert_anket
)
from logger import write_log


def main():

    conn = get_connection()

    if not conn:
        print("Veritabanına bağlanılamadı.")
        write_log("ERROR", "Veritabanına bağlanılamadı.")
        return

    try:

        write_log("INFO", "===================================")
        write_log("INFO", "Yeni içe aktarma işlemi başlatıldı.")

        cursor = conn.cursor()

        df = read_sheet()

        successful = 0
        duplicates = 0
        invalid = 0

        print(f"\nToplam {len(df)} kayıt bulundu.\n")
        write_log("INFO", f"Toplam {len(df)} kayıt okundu.")

        for index, row in df.iterrows():

            # Validation
            errors = validate_row(row)

            if errors:

                invalid += 1

                print(f"\n{index + 2}. Excel satırı hatalı:")

                for error in errors:
                    print(f" - {error}")

                write_log(
                    "WARNING",
                    f"Satır {index + 2} validation hatası: {', '.join(errors)}"
                )

                continue

            # Duplicate kontrolü
            if is_duplicate(cursor, row):

                duplicates += 1

                print(f"{index + 2}. satır zaten veritabanında mevcut.")

                write_log(
                    "WARNING",
                    f"Satır {index + 2} duplicate kayıt bulundu."
                )

                continue

            # Katılımcıyı ekle
            katilimci_id = insert_katilimci(cursor, row)

            # Anket cevaplarını ekle
            insert_anket(cursor, row, katilimci_id)

            successful += 1

            write_log(
                "INFO",
                f"Satır {index + 2} başarıyla veritabanına eklendi."
            )

        conn.commit()

        print("\n===================================")
        print("İçe aktarma tamamlandı.")
        print("===================================")
        print(f"Toplam kayıt      : {len(df)}")
        print(f"Başarılı kayıt    : {successful}")
        print(f"Hatalı kayıt      : {invalid}")
        print(f"Duplicate kayıt   : {duplicates}")

        write_log("INFO", "===================================")
        write_log("INFO", "İçe aktarma tamamlandı.")
        write_log("INFO", f"Toplam kayıt: {len(df)}")
        write_log("INFO", f"Başarılı kayıt: {successful}")
        write_log("INFO", f"Hatalı kayıt: {invalid}")
        write_log("INFO", f"Duplicate kayıt: {duplicates}")

    except Exception as e:

        conn.rollback()

        print("\nİşlem sırasında hata oluştu!")
        print(e)

        write_log("ERROR", f"İşlem sırasında hata oluştu: {str(e)}")

    finally:

        conn.close()

        print("\nVeritabanı bağlantısı kapatıldı.")

        write_log("INFO", "Veritabanı bağlantısı kapatıldı.")
        write_log("INFO", "")


if __name__ == "__main__":
    main()