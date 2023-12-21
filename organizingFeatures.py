import json
import pandas as pd



def organize():
    # uzun verileri düzenle
    abbreviator()
    # garip içerik düzenleme fonksiyonu
    last_words('updated_data.json')
    # tekrar eden verileri sil
    remove_duplicate_values('updated_data.json', 'updated_data.json')


def abbreviator():
# JSON veri setini dosyadan oku
    with open('data.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # bilgilerin karakter sayısını kontrol et ve 30 karakterden fazla ise boş olarak değiştir
    for item in json_data:
        if "taban" in item and item["taban"] is not None and len(item["taban"]) > 30:
            item["taban"] = None

    for item in json_data:
        if "dış materyal" in item and item["dış materyal"] is not None and len(item["dış materyal"]) > 30:
            item["dış materyal"] = None



    # Değiştirilmiş JSON veri setini başka bir dosyaya yaz
    with open('updated_data.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)





#son kelimeleri al ve duzenle
def last_words(dosya_adi):
    with open(dosya_adi, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    for item in json_data:
        if "taban" in item and item["taban"]:
            item["taban"] = item["taban"].split()[-1] if len(item["taban"].split()) > 0 else ""

        if "dış materyal" in item and item["dış materyal"]:
            item["dış materyal"] = item["dış materyal"].split()[-1] if len(item["dış materyal"].split()) > 0 else ""

        if "menşei" in item and item["menşei"]:
            item["menşei"] = item["menşei"].split()[-1] if len(item["menşei"].split()) > 0 else ""

    with open(dosya_adi, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)




def remove_duplicate_values(input_file, output_file):
    data = pd.read_json(input_file)  # CSV dosyasını oku
    data.drop_duplicates(inplace=True)  # Aynı değerleri sil
    data.to_json(output_file,  indent=4)  # Güncellenmiş veriyi CSV dosyasına yaz

    #json içerik düzenleme
    with open(input_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)



