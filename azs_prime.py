import requests
import re
import sqlite3
from bs4 import BeautifulSoup as BS


def find_price_prime():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.79 Safari/537.36'}

    reg = r'\d{2}.\d{2}'
    reg_2 = r'[АPД]\w+'

    r = requests.get('https://azs-prime.ru/azs-maps', headers=headers)
    soup = BS(r.content, 'html.parser')
    res = soup.find(id='azsnet-list-price')

    global name
    name = res.find_all(text=re.compile(reg_2))

    global price
    price = res.find_all(text=re.compile(reg))

    i = -1

    while i != 5:
        i += 1
        print(name[i] + ' - ' + price[i])


def update_reg_92():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'reg_92'
    res = price[0]
    id = 'brand'
    record_id = 'Прайм'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def update_reg_95():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'reg_95'
    res = price[2]
    id = 'brand'
    record_id = 'Прайм'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def update_diesel():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'diesel'
    res = price[4]
    id = 'brand'
    record_id = 'Прайм'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def run_prime():
    find_price_prime()
    update_reg_92()
    update_reg_95()
    update_diesel()
