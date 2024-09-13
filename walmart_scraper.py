from bs4 import BeautifulSoup
import requests
import json

walmart_url = "https://www.walmart.com/ip/POPSNAP-CAMERA-GREEN/5352547353?classType=VARIANT&athbdg=L1600&from=/search"
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

response = requests.get(walmart_url, headers=HEADERS)

soup = BeautifulSoup(response.text, "html.parser")

script_tag = soup.find("script", id="__NEXT_DATA__")

data = json.loads(script_tag.string)

print(data['props']['pageProps']['initialData']['data']['product']['priceInfo']['currentPrice']['price'])