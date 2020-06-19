import requests
import re
import sqlite3
from bs4 import BeautifulSoup as BS


def find_price_time():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.79 Safari/537.36'}

    reg = r'(\₽)'

    r = requests.get('https://vk.com/market-65011473', headers=headers)
    if r.status_code == 200:
        soup = BS(r.content, 'html.parser')
        global price
        price = soup.find('div', class_='market_list').find_all(text=re.compile(reg))

        name = ['Тайм-92', 'АИ-92', 'Тайм-95', 'ДТ']
        price.reverse()
        del price[0]

        newprice = [x[:-2] for x in price]
        price = newprice

        i = -1
        while i != 3:
            i += 1
            print(name[i] + ': ' + price[i])

    else:
        print(f"Ошибка {r.status_code}")


def update_reg_92():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'reg_92'
    res = price[1]
    id = 'brand'
    record_id = 'Тайм'
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
    record_id = 'Тайм'
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
    record_id = 'Тайм'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def run_time():
    find_price_time()
    update_reg_92()
    update_reg_95()
    update_diesel()
