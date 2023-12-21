from bs4 import BeautifulSoup
import requests
import json


def dataExtraction():
    base_link = "https://www.boyner.com.tr/search?q=ayakkab%C4%B1&page="
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    all_product_links = []

    for i in range(1, 2):
        link = base_link + str(i)
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")

        product_list_wrapper = soup.find("div", class_="product-list_productItemListWrapper__yKb6p")
        if product_list_wrapper:
            links = product_list_wrapper.find_all("a", href=True)
            all_product_links.extend([link['href'] for link in links])

    product_data = []

    for product_link in all_product_links:
        product_url = f"https://www.boyner.com.tr{product_link}"
        product_page = requests.get(product_url, headers=headers)
        product_soup = BeautifulSoup(product_page.content, "html.parser")

        brand = product_soup.find("span", class_="title_title__laaYP")
        brand = brand.text if brand else None

        price = product_soup.find('div', {'class': 'product-price_checkPrice__NMY9e'}).strong.text
        price = price.replace('TL', '').replace('.', '')  # fiyatta sadece rakamlar

        tech_specs = product_soup.find_all("span", class_="product-information-card_value__jGcTJ")
        tech_specs2 = product_soup.find_all("span", class_="title_subtitle__9USXk")

        taban = next((span.text for span in tech_specs if "taban" in span.text.lower()), None)
        dis_materyal = next((span.text for span in tech_specs if "dış materyal" in span.text.lower()), None)
        mensei = next((span.text for span in tech_specs if "menşei" in span.text.lower()), None)
        cinsiyet = next(("erkek" if "erkek" in span.text.lower() else "kadın" for span in tech_specs2 if "erkek" in span.text.lower() or "kadın" in span.text.lower()), None)
        tip = next((("terlik" if "terlik" in span.text.lower() else "ayakkabı" if "ayakkabı" in span.text.lower() else "bot" if "bot" in span.text.lower() else None)
                   for span in tech_specs2 if
                   "terlik" in span.text.lower() or "ayakkabı" in span.text.lower() or "bot" in span.text.lower()), None)

        product_data.append({
            "marka": brand,
            "taban": taban,
            "dış materyal": dis_materyal,
            "menşei": mensei,
            "cinsiyet": cinsiyet,
            "tip": tip,
            "fiyat": price
        })

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(product_data, f, ensure_ascii=False,indent=4)
