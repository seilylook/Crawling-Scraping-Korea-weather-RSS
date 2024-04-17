from bs4 import BeautifulSoup
import urllib.request as req
import datetime

url = "https://finance.naver.com/marketindex/"

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

response = req.urlopen(url).read()

soup = BeautifulSoup(response, 'html.parser')

currency = soup.select_one("#exchangeList > li:nth-child(1) > a.head.usd > div > span.value")

print(f"Date: {now} | USD: {currency.string}")


