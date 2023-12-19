from bs4 import BeautifulSoup
import requests
import json

base_link = "https://www.boyner.com.tr/search?q=ayakkab%C4%B1&page="
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

all_product_links = []

for i in range(1):
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

    tech_specs = product_soup.find_all("span", class_="product-information-card_value__jGcTJ")

    taban = next((span.text for span in tech_specs if "taban" in span.text.lower()), None)
    ic_materyal = next((span.text for span in tech_specs if "iç materyal" in span.text.lower()), None)
    dis_materyal = next((span.text for span in tech_specs if "dış materyal" in span.text.lower()), None)
    mensi = next((span.text for span in tech_specs if "menşei" in span.text.lower()), None)

    product_data.append({
        "brand": brand,
        "taban": taban,
        "iç materyal": ic_materyal,
        "dış materyal": dis_materyal,
        "menşei": mensi
    })

with open('data.json', 'w', encoding='utf-8') as f:
  json.dump(product_data, f, ensure_ascii=False)

