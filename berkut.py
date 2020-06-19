import requests
import re
import sqlite3
from bs4 import BeautifulSoup as BS


def find_price_berkut():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.79 Safari/537.36'}
    reg = r'\d{2}.\d{2}'
    r = requests.get('http://azs-berkut.ru/price', headers=headers)
    if r.status_code == 200:
        soup = BS(r.content, 'html.parser')
        res = soup.find('div', class_='container center')
        global price
        price = res.find_all(text=re.compile(reg))
        global name
        name = ['АИ-92', 'Эко-плюс 92', 'АИ-95', 'Эко-плюс 95', 'ДТ', 'ДТз']

        i = -1
        while i != 5:
            i += 1
            print(name[i] + ': ' + price[i])
    else:
        print(f"Ошибка {r.status_code}")



def update_reg_92():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'reg_92'
    res = price[0]
    id = 'brand'
    record_id = 'Беркут'
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
    record_id = 'Беркут'
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
    record_id = 'Беркут'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def run_berkut():
    find_price_berkut()
    update_reg_92()
    update_reg_95()
    update_diesel()

find_price_berkut()