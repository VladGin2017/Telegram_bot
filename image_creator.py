import matplotlib.pyplot as plt
import sqlite3


con = sqlite3.connect('data_base.db')
cor = con.cursor()

query_5 = 'SELECT reg_92 FROM map'
cor.execute(query_5)
reg_92 = cor.fetchall()
reg = []
for element in reg_92:
    reg.append(element[0])
reg_92 = reg
del (reg)

query_6 = 'SELECT reg_95 FROM map'
cor.execute(query_6)
reg_95 = cor.fetchall()
reg_1 = []
for element in reg_95:
    reg_1.append(element[0])
reg_95 = reg_1
del (reg_1)

query_7 = 'SELECT diesel FROM map'
cor.execute(query_7)
diesel = cor.fetchall()
dt = []
for element in diesel:
    dt.append(element[0])
diesel = dt
del (dt)


def png_1():
    names = ['Лукойл', 'Прайм', 'Газпром(ак)', 'Газпром', 'Беркут', 'Роснефть', 'Тайм']
    values = [reg_92[0], reg_92[64], reg_92[19], reg_92[30], reg_92[87], reg_92[80], reg_92[98]]
    plt.figure(figsize=(10, 7))
    plt.subplot()
    plt.bar(names, values)
    plt.text(0.1, reg_92[0] - 2, reg_92[0], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(1.1, reg_92[64] - 2, reg_92[64], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(2.1, reg_92[19] - 2, reg_92[19], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(3.1, reg_92[30] - 2, reg_92[30], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(4.1, reg_92[87] - 2, reg_92[87], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(5.1, reg_92[80] - 2, reg_92[80], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(6.1, reg_92[98] - 2, reg_92[98], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.ylabel('Цена (в руб)')
    plt.xlabel('Бренд')
    plt.suptitle('График зависимости цен АИ-92')
    plt.savefig('regular_92.png')


def png_2():
    names = ['Лукойл', 'Прайм', 'Газпром(ак)', 'Газпром', 'Беркут', 'Роснефть', 'Тайм']
    values = [reg_95[0], reg_95[64], reg_95[19], reg_95[30], reg_95[87], reg_95[80], reg_95[98]]
    plt.figure(figsize=(10, 7))
    plt.subplot()
    plt.bar(names, values)
    plt.text(0.1, reg_95[0] - 2, reg_95[0], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(1.1, reg_95[64] - 2, reg_95[64], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(2.1, reg_95[19] - 2, reg_95[19], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(3.1, reg_95[30] - 2, reg_95[30], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(4.1, reg_95[87] - 2, reg_95[87], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(5.1, reg_95[80] - 2, reg_95[80], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(6.1, reg_95[98] - 2, reg_95[98], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.ylabel('Цена (в руб)')
    plt.xlabel('Бренд')
    plt.suptitle('График зависимости цен АИ-95')
    plt.savefig('regular_95.png')


def png_3():
    names = ['Лукойл', 'Прайм', 'Газпром(ак)', 'Газпром', 'Беркут', 'Роснефть', 'Тайм']
    values = [diesel[0], diesel[64], diesel[19], diesel[30], diesel[87], diesel[80], diesel[98]]
    plt.figure(figsize=(10, 7))
    plt.subplot()
    plt.bar(names, values)
    plt.text(0.1, diesel[0] - 2, diesel[0], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(1.1, diesel[64] - 2, diesel[64], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(2.1, diesel[19] - 2, diesel[19], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(3.1, diesel[30] - 2, diesel[30], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(4.1, diesel[87] - 2, diesel[87], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(5.1, diesel[80] - 2, diesel[80], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(6.1, diesel[98] - 2, diesel[98], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.ylabel('Цена (в руб)')
    plt.xlabel('Бренд')
    plt.suptitle('График зависимости цен ДТ')
    plt.savefig('diesel.png')
