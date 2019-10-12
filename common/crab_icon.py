# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import requests
from bs4 import BeautifulSoup

url = 'http://www.fontawesome.com.cn/faicons/'
html = requests.get(url)

soup = BeautifulSoup(html.content, 'lxml')
# print(soup)
icon = soup.find('section', id='web-application').find_all('div')
icon_list = []

for item in icon:
    icon_list.append([item.find('a').find('i')['class'][1], str(item.find('a').find('i'))])
print(icon_list)
