import json

def features():
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







