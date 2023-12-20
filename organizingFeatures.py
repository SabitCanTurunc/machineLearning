import json

def abbreviator():
# JSON veri setini dosyadan oku
    with open('data.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # bilgilerin karakter sayısını kontrol et ve 30 karakterden fazla ise boş olarak değiştir
    for item in json_data:
        if "taban" in item and item["taban"] is not None and len(item["taban"]) > 30:
            item["taban"] = ""

    for item in json_data:
        if "dış materyal" in item and item["dış materyal"] is not None and len(item["dış materyal"]) > 30:
            item["dış materyal"] = ""



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





