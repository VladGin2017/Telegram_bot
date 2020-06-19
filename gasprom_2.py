import requests
import re
import sqlite3
from bs4 import BeautifulSoup as BS


def find_price_gasprom_2():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.79 Safari/537.36'}

    reg = r'\d{2}.\d{2}₽'

    r = requests.get('https://www.gpnbonus.ru/our_azs/?region_id=137&region_name=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8'
                     '%D0%B1%D0%B8%D1%80%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C&CenterLon'
                     '=79.770236&CenterLat=55.276272&city=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1'
                     '%81%D0%BA&FUEL%5B%5D=176&FUEL%5B%5D=177&PARAM_AZS%5B%5D=181&PARAM_AZS%5B%5D=182&PARAM_AZS%5B%5D'
                     '=192', headers=headers)
    if r.status_code == 200:
        soup = BS(r.content, 'html.parser')

        res = soup.find('div', class_='oh pt10')
        global price
        price = res.find_all(text=re.compile(reg))
        name = ['G-100', 'G-95', 'АИ-95', 'АИ-92', 'ДТ']

        newprice = [x[:-2] for x in price]
        price = newprice

        i = -1
        while i != 4:
            i += 1
            print(name[i] + ': ' + price[i])

    else:
        print(f"Ошибка {r.status_code}")


def update_reg_92():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'reg_92'
    res = price[3]
    id = 'brand'
    record_id = 'Газпром'
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
    record_id = 'Газпром'
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
    record_id = 'Газпром'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def run_gasprom_2():
    find_price_gasprom_2()
    update_reg_92()
    update_reg_95()
    update_diesel()
