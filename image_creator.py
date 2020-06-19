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
del reg


query_6 = 'SELECT reg_95 FROM map'
cor.execute(query_6)
reg_95 = cor.fetchall()
reg_1 = []
for element in reg_95:
    reg_1.append(element[0])
reg_95 = reg_1
del reg_1


query_7 = 'SELECT diesel FROM map'
cor.execute(query_7)
diesel = cor.fetchall()
dt = []
for element in diesel:
    dt.append(element[0])
diesel = dt
del dt


query_8 = 'SELECT reg_98 FROM map'
cor.execute(query_8)
reg_98 = cor.fetchall()
reg_2 = []
for element in reg_98:
    reg_2.append(element[0])
reg_98 = reg_2
del reg_2


def png_1():
    names = ['Лукойл', 'Прайм', 'Газпром(ак)', 'Газпром', 'Тайм', 'Энергия', 'Беркут']
    values = [reg_92[0], reg_92[64], reg_92[19], reg_92[29], reg_92[91], reg_92[94], reg_92[80]]
    plt.figure(figsize=(10, 8))
    plt.subplot()
    plt.bar(names, values)
    plt.text(0.1, reg_92[0] - 2, reg_92[0], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(1.1, reg_92[64] - 2, reg_92[64], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(2.1, reg_92[19] - 2, reg_92[19], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(3.1, reg_92[29] - 2, reg_92[29], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(4.1, reg_92[91] - 2, reg_92[91], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(5.1, reg_92[94] - 2, reg_92[94], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(6.1, reg_92[80] - 2, reg_92[80], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.ylabel('Цена (в руб)')
    plt.xlabel('Бренд')
    plt.suptitle('График цен АИ-92')
    plt.savefig('regular_92.png')


def png_2():
    names = ['Лукойл', 'Прайм', 'Газпром(ак)', 'Газпром','Тайм', 'Энергия']
    values = [reg_95[0], reg_95[64], reg_95[19], reg_95[30], reg_95[98], reg_95[101]]
    plt.figure(figsize=(10, 8))
    plt.subplot()
    plt.bar(names, values)
    plt.text(0.1, reg_95[0] - 2, reg_95[0], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(1.1, reg_95[64] - 2, reg_95[64], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(2.1, reg_95[19] - 2, reg_95[19], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(3.1, reg_95[30] - 2, reg_95[30], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(4.1, reg_95[98] - 2, reg_95[98], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(5.1, reg_95[101] - 2, reg_95[101], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.ylabel('Цена (в руб)')
    plt.xlabel('Бренд')
    plt.suptitle('График цен АИ-95')
    plt.savefig('regular_95.png')


def png_3():
    names = ['Лукойл', 'Прайм', 'Газпром(ак)', 'Газпром', 'Тайм', 'Энергия']
    values = [diesel[0], diesel[64], diesel[19], diesel[30], diesel[98], diesel[101]]
    plt.figure(figsize=(10, 8))
    plt.subplot()
    plt.bar(names, values)
    plt.text(0.1, diesel[0] - 2, diesel[0], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(1.1, diesel[64] - 2, diesel[64], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(2.1, diesel[19] - 2, diesel[19], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(3.1, diesel[30] - 2, diesel[30], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(4.1, diesel[98] - 2, diesel[98], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(5.1, diesel[101] - 2, diesel[101], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.ylabel('Цена (в руб)')
    plt.xlabel('Бренд')
    plt.suptitle('График цен ДТ')
    plt.savefig('diesel.png')


def png_4():
    names = ['Лукойл', 'Прайм', 'Энергия']
    values = [reg_98[0], reg_98[64], reg_98[101]]
    plt.figure(figsize=(10, 4))
    plt.subplot()
    plt.bar(names, values)
    plt.text(0.1, reg_98[0] - 2, reg_98[0], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(1.1, reg_98[64] - 2, reg_98[64], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.text(2.1, reg_98[101] - 2, reg_98[101], rotation=0, horizontalalignment='right', verticalalignment='center')
    plt.ylabel('Цена (в руб)')
    plt.xlabel('Бренд')
    plt.suptitle('График цен АИ-98')
    plt.savefig('regular_98.png')