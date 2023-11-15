import requests
from bs4 import BeautifulSoup
import smtplib
# URL of the product page on Amazon
product_url = ("https://www.amazon.com/Logitech-Gaming-Headset-Oculus-Quest-PC/dp/B08DCSBD1P/ref=sr_1_4?crid"
               "=2ESAOU40OOSUL&keywords=oculus+headset+only&qid=1699980879&sr=8-4")
# HTTP headers to simulate a request from a web browser
http_head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.7",
    "referer": "https://www.amazon.com"
}

# Define the price at which you want to be notified
buy_price = 55

# Email configuration
my_email = "yourEmail@gmail.com"
password = "PASSWORD"
to_email = "yourEmail@gmail.com"

# Send a GET request to the product URL with the specified headers
res = requests.get(url=product_url, headers=http_head)

# Get the HTML content of the response
html_data = res.content

# Parse the HTML content using BeautifulSoup with the lxml parser
soup = BeautifulSoup(html_data, 'lxml')

# Extract the product price from the HTML and convert it to a float
product_price = float((soup.find(class_="a-offscreen")).get_text().split('$')[1])

# Extract the product title from the HTML
product_title = soup.find(id="productTitle").get_text()

# Check if the current price is less than or equal to the desired price
if product_price <= buy_price:
    # Use SMTP to send an email notification
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"subject:Amazon Price Alert!\n\n "
                                                                       f"{product_title}\n"
                                                                       f"Current price:{product_price}$\n\n"
                                                                       f"{product_url}".encode("utf-8"))






