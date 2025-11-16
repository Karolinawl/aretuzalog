import os                          # praca z folderami/ścieżkami
import pandas as pd                # praca z tabelami (DataFrame)
import numpy as np                 # operacje na tablicach i macierzach
from datetime import datetime      # biblioteka do obsługi dat i czasu

FILTER_DATE = datetime.today().date()   # np. 2025-11-03
print(f" Dziś jest: {FILTER_DATE}")
files = [
    "data/weeks/week1.csv", "data/weeks/week2.csv", "data/weeks/week3.csv",
    "data/weeks/week4.csv", "data/weeks/week5.csv", "data/weeks/week6.csv",
    "data/weeks/week7.csv", "data/weeks/week8.csv", "data/weeks/week9.csv",
    "data/weeks/week10.csv", "data/weeks/week11.csv", "data/weeks/week12.csv",
    "data/weeks/week13.csv", "data/weeks/week14.csv", "data/weeks/week15.csv",
    "data/weeks/week16.csv"
]# pd.concat() łączy wiele DataFrame w jeden
dataframes = [pd.read_csv(f) for f in files if os.path.exists(f)]
df = pd.concat(dataframes, ignore_index=True)
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)
else:
    print("⚠️ Brak kolumny 'date' w danych.")

# --- 5️⃣  Filtrujemy po dacie ----------------------------------------------
mask = df["date"] == pd.to_datetime(FILTER_DATE)
df_filtered = df[mask]

# --- 6️⃣  Wyświetlamy wynik -------------------------------------------------
podglad = [c for c in ["date", "session"] if c in df.columns]
print(f"\n🔎 zajecia {FILTER_DATE}:")
print(df_filtered[podglad])
