import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def getHtml(url):
    """Получение HTML"""
    r = requests.get(url).text
    return r

def getParametr():
    file_name = "C:\Renata\m.xlsx"
    df = pd.read_excel(file_name)
    links=df['Источник']
    name=[]
    for link in links:
        content = BeautifulSoup(getHtml(link))
        name.append(content.find('h1',id='pagetitle').text)


    df['Название'] = name
    df.to_excel("C:\Renata\m.xlsx", index=False)

getParametr()