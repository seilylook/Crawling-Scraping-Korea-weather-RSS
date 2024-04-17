#!/usr/bin/env python3
import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:
	print("usage: download-forecast-argv < region number: ")
	sys.exit()

# region number 저장
regionNumber = sys.argv[1]

# Root URL 주소
api_address = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# dict 타입으로 stnId 저장
values = {
	'stnId': regionNumber
}

params = parse.urlencode(values)

url = api_address + "?" + params

print("URL= ", url)

data = req.urlopen(url).read()

text = data.decode("utf-8")

print(text)
