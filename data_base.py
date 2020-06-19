import sqlite3


def db_create():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    cor.execute('CREATE TABLE IF NOT EXISTS map (latitude FLOAT, longitude FLOAT, adress TEXT, brand TEXT, '
                'reg_92 TEXT, reg_95 FLOAT, diesel FLOAT, reg_98 FLOAT)')
    data = [latitude, longitude, adress, brand, reg_92, reg_95, diesel, reg_98]
    cor.execute('INSERT INTO map VALUES (?, ?, ?, ?, ?, ?, ?, ?)', data)
    con.commit()


def add_column():
    con = sqlite3.connect('data_base.db')
    cor = con.cursor()
    cor.execute('ALTER TABLE map ADD {column_name} FLOAT')


while True:
    latitude = str(input('Широта:'))
    longitude = str(input('Долгота:'))
    adress = str(input('Адрес:'))
    brand = str(input('Компания:'))
    reg_92 = str(input('АИ-92:'))
    reg_95 = str(input('АИ-95:'))
    diesel = str(input('Дизель:'))
    reg_98 = str(input('АИ-98: '))

    db_create()
