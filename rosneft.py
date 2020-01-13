import sqlite3
import re
from bs4 import BeautifulSoup as BS


def find_price_rosneft():
    reg = r'\d{2}.\d{2}'
    r = open('rosneft.html', encoding='utf-8').read()
    soup = BS(r, 'html.parser')

    res = soup.find('div', class_='b-info-nav').find_all(text=re.compile(reg))
    global price
    price = res
    names = ['АИ-92', 'АИ-95', 'АИ-98', 'ДТ', ]

    i = -1
    while i != 3:
        i += 1
        print((names[i]) + ' - ' + str(price[i]))


def update_reg_92():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    column = 'reg_92'
    res = price[0]
    id = 'brand'
    record_id = 'Роснефть'
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
    record_id = 'Роснефть'
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
    record_id = 'Роснефть'
    query = 'UPDATE map SET ' + column + '=' + str(res) + ' WHERE ' + id + " = '" + str(record_id) + "'"
    cor.execute(query)
    con.commit()
    cor.close()


def run_rosneft():
    find_price_rosneft()
    update_reg_92()
    update_reg_95()
    update_diesel()
