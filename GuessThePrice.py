import pandas as pd
import joblib

# Eğitilmiş modeli yükle
model = joblib.load("C:/Software/PyCharm/pythonProjects/mLDataExtraction/mlModells/GradientBoostingRegressor_model.pkl")

# Tahmin için girdi verisi oluştur
girdi_verisi = pd.DataFrame({
    "marka_Nike": [False],
    "marka_Skechers": [True],
    "marka_adidas": [False],
    "taban_EVA": [True],
    "taban_Kauçuk": [False],
    "taban_Poliüretan": [False],
    "taban_Termo": [False],
    "dış materyal_Deri": [False],
    "dış materyal_Sentetik": [True],
    "dış materyal_Tekstil": [False],
    "menşei_Endonezya": [False],
    "menşei_Hindistan": [False],
    "menşei_Türkiye": [False],
    "menşei_Vietnam": [True],
    "menşei_Çin": [False],
    "cinsiyet_erkek": [True],
    "cinsiyet_kadın": [False],
    "tip_ayakkabı": [True],
    "tip_bot": [False]
})

# Tahmin yap
tahmin = model.predict(girdi_verisi)
print("Tahmin edilen fiyat:", tahmin)
