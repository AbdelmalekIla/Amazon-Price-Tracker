import requests
from bs4 import BeautifulSoup
import lxml

product_url = ("https://www.amazon.com/Logitech-Gaming-Headset-Oculus-Quest-PC/dp/B08DCSBD1P/ref=sr_1_4?crid=2ESAOU40OOSUL&keywords=oculus+headset+only&qid=1699980879&sr=8-4")
http_head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.6",
    "referer": "https://www.amazon.com/"
}

res = requests.get(url=product_url, headers=http_head)

html_data = res.content

# html_data = amazon_req.page_source
soup = BeautifulSoup(html_data, 'lxml')
product_price = float((soup.find(class_="a-offscreen")).get_text().split('$')[1])
print(product_price)





