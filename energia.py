import requests
import re
import sqlite3
from bs4 import BeautifulSoup as BS


def find_price_energia():
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/79.0.3945.79 Safari/537.36'}

    reg = r'\d{2}.\d{2}'

    r = requests.get('https://azsenergia.ru/', headers=headers)
    if r.status_code == 200:
        soup = BS(r.content, 'html.parser')
        global price
        price = soup.find('div', class_='stella').find_all(text=re.compile(reg))
        name = ['АИ-98', 'АИ-95', 'АИ-92', 'ДТевро', 'ДТ']

        i = -1
        while i != 4:
            i += 1
            print(name[i] + ": " + price[i])

    else:
        print(f"Ошибка {r.status_code}")

def update_reg_92():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'reg_92'
    res = price[2]
    id = 'brand'
    record_id = 'Энергия'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def update_reg_95():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'reg_95'
    res = price[1]
    id = 'brand'
    record_id = 'Энергия'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def update_diesel():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'diesel'
    res = price[3]
    id = 'brand'
    record_id = 'Энергия'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def update_reg_98():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'reg_98'
    res = price[0]
    id = 'brand'
    record_id = 'Энергия'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def run_energia():
    find_price_energia()
    update_reg_92()
    update_reg_95()
    update_diesel()
    update_reg_98()
