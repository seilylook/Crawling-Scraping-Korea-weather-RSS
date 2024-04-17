#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text)
    locations = soup.find_all('location')

    for location in locations:
        city = location.find('city').text
        date = location.find('data').find('tmef').text
        weather = location.find('data').find('wf').text

        print(f'City: {city} | Date: {date} | Weather: {weather}')  

if __name__ == "__main__":
    main()
	

