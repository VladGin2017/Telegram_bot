import requests
import re
import sqlite3
from bs4 import BeautifulSoup as BS


def find_price_lukoil():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.79 Safari/537.36'}

    reg2 = r'\d{2},\d{2}'

    r = requests.get('https://lukoilazs.ru/category/stoimost-benzina-na-segodnya/', headers=headers)
    soup = BS(r.content, 'html.parser')

    res = soup.find('div', class_='main-content-page').find_all(text=re.compile(reg2))
    global price
    price = res

    i = 11
    while i != 17:
        i += 1
        print(price[i])


def update_reg_92():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'reg_92'
    res = price[12].replace(',', '.')
    id = 'brand'
    record_id = 'Лукойл'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def update_reg_95():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'reg_95'
    res = price[14].replace(',', '.')
    id = 'brand'
    record_id = 'Лукойл'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def update_diesel():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'diesel'
    res = price[17].replace(',', '.')
    id = 'brand'
    record_id = 'Лукойл'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def run_lukoil():
    find_price_lukoil()
    update_reg_92()
    update_reg_95()
    update_diesel()
