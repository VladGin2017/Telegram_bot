import sqlite3


def db_create():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    cor.execute('CREATE TABLE IF NOT EXISTS map (latitude FLOAT, longitude FLOAT, adress TEXT, '
                'brand TEXT, reg_92 TEXT, reg_95 FLOAT, diesel FLOAT)')
    data = [latitude, longitude, adress, brand, reg_92, reg_95, diesel]
    cor.execute('INSERT INTO map VALUES (?, ?, ?, ?, ?, ?, ?)', data)

    con.commit()


while True:
    latitude = str(input('Широта:'))
    longitude = str(input('Долгота:'))
    adress = str(input('Адрес:'))
    brand = str(input('Компания:'))
    reg_92 = str(input('АИ-92:'))
    reg_95 = str(input('АИ-95:'))
    diesel = str(input('Дизель:'))

    db_create()
