import pandas as pd
import json
# JSON dosyasını oku

def oneHotEncode():
    with open('updated_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # DataFrame oluştur
    df = pd.DataFrame(data)
    df.to_csv('updated_data.csv', index=False)

    df = pd.read_csv('updated_data.csv')

    # One-hot encoding yap
    df_encoded = pd.get_dummies(df, columns=['marka', 'taban', 'dış materyal', 'menşei', 'cinsiyet', 'tip'])

    df_encoded.to_csv('one_hot_encoded_data.csv', index=False)




