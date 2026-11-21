import pyodbc
from config import SERVER, DATABASE, USERNAME, PASSWORD, PORT


def get_connection():
    """
    SQL Server bağlantısını oluşturur ve döndürür.
    """

    conn_str = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={SERVER},{PORT};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
        "Encrypt=no;"
        "TrustServerCertificate=yes;"
    )

    try:
        conn = pyodbc.connect(conn_str)
        print("Veritabanına başarıyla bağlanıldı.")
        return conn

    except Exception as e:
        print(" Veritabanı bağlantı hatası:")
        print(e)
        return None