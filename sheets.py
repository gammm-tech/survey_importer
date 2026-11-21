import pandas as pd


def read_sheet():
    df = pd.read_excel("anket1.xlsx")

    print(f"{len(df)} kayıt okundu.")

    return df