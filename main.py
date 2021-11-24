from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


URL = "https://www.amazon.co.uk/LEGO-75955-Hogwarts-Wizzarding-Building/dp/B07BLG43H2/ref=sr_1_28?crid=3AKVKJ9AKGI4K"

header = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

response = requests.get(URL, headers=header)
amazon_text = response.text
soup = BeautifulSoup(amazon_text, "lxml")

#price_currency = soup.find(id="priceblock_ourprice")
price_currency = soup.find(class_="a-offscreen")

print(price_currency)
price =float(price_currency.getText().split("£")[1])
print(price)

my_price = 65

if my_price >= price:
    my_email = "*****"
    password = "*****"
    # What is happening here is that Python is trying to interpret a string, and expects that the bytes in
    # that string are legal for the format it’s expecting. In this case, it’s expecting a string composed of ASCII bytes.
    # These bytes are in the range 0-127 (ie 8 bytes). £ is therefore out of range.
    text = f"Subject:WOW Amazon price alert!\n\nNow you can buy Lego only for £{price}:\n{URL}".encode('utf-8')


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="************",
                            msg=text)



