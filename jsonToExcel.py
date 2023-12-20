import pandas as pd
import json

def jsonToExcel():
    # JSON veri setini dosyadan oku
    with open('updated_data.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # JSON veri setini pandas DataFrame'e dönüştür
    df = pd.DataFrame(json_data)

    # DataFrame'i Excel dosyasına yazma
    df.to_excel('data.xlsx', index=False)
