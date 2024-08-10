import webbrowser
from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
url_ = "mail.google.com"
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register(
    'chrome', None, webbrowser.BackgroundBrowser(chrome_path))

webbrowser.get('chrome').open_new_tab(url_)

url = "https://www.amazon.in/MuscleBlaze-CREAPRO-creatine-creapure-Unflavoured/dp/B08KPJRSGT?pd_rd_w=C4vZU" \
           "&content-id=amzn1.sym.c19c3264-ca5c-4c08-8eb5-3c9af541f7d2&pf_rd_p=c19c3264-ca5c-4c08-8eb5" \
           "-3c9af541f7d2&pf_rd_r=AK4HW9AVPQJ7V4RAFRX3&pd_rd_wg=vTJOg&pd_rd_r=2e1d9fab-d947-48d1-a6cd" \
           "-6b9f961301d1&pd_rd_i=B08KPJRSGT&psc=1&ref_=pd_bap_d_grid_rp_0_1_ec_pd_nav_hcs_rp_2_i"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

# practice_url = "https://appbrewery.github.io/instant_pot/"
# live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
responce = requests.get(url, headers=headers)

soup = BeautifulSoup(responce.content, "html.parser")

price = soup.find('span', class_='a-price-whole').text
print(price)
title = soup.find(id="productTitle").getText().strip()
print(title)

BUY_PRICE = 500

if price < str(BUY_PRICE):
    message = f"{title} is in sale for {price}!"
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )




# price_without_currency = price.split("$")[1]
# price_as_float = float(price_without_currency)
# print(price_as_float)

