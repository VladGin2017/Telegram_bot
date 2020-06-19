import config
import telebot
import sqlite3
from emoji import emojize
from geopy.distance import geodesic
from telebot import types
from datetime import datetime
from image_creator import png_1, png_2, png_3, png_4

con = sqlite3.connect('data_base.db')
cor = con.cursor()

query = 'SELECT latitude FROM map'
cor.execute(query)
latitude = cor.fetchall()
lat = []
for element in latitude:
    lat.append(element[0])
latitude = lat
del lat

query_2 = 'SELECT longitude FROM map'
cor.execute(query_2)
longitude = cor.fetchall()
lon = []
for element in longitude:
    lon.append(element[0])
longitude = lon
del lon

query_3 = 'SELECT adress FROM map'
cor.execute(query_3)
adress = cor.fetchall()
adresses = []
for elements in adress:
    adresses.append(elements[0])
adress = adresses
del adresses

query_4 = 'SELECT brand FROM map'
cor.execute(query_4)
brand = cor.fetchall()
brands = []
for elements in brand:
    brands.append(elements[0])
brand = brands
del brands

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
    if element is not None:
        reg_2.append(element[0])
reg_98 = reg_2
del reg_2,

loc = None
global keyboard
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, text="Привет!" + (emojize(':hand:', use_aliases=True)) + "\n" +
                                           "На данный момент бот умеет: \n" +
                                           (emojize(':white_check_mark:', use_aliases=True) +
                                            " Находить ближайщую к тебе АЗС \n" +
                                            (emojize(':white_check_mark:', use_aliases=True) +
                                             " Выводить информацию о ценах на топливо каждого бренда \n" +
                                             (emojize(':white_check_mark:', use_aliases=True) +
                                              " Находить ближайшую АЗС с самым дешевым топливом в радиусе 1.5км \n" +
                                              (emojize(':white_check_mark:', use_aliases=True) +
                                               " Вывод графика динамики цен \n\n\n"  +
                                                "Теперь введи /menu и опробуй бота " +
                                                (emojize(':grinning:', use_aliases=True)))))))


@bot.message_handler(commands=['help'])
def help_(message):
    bot.send_message(message.chat.id, text="/menu - меню\n"
                                           "/geo - отправить свою геопозицию\n"
                                           "/start - информация о боте\n"
                                           "/help - помощь в командах бота")


@bot.message_handler(commands=["geo"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение" + emojize(':earth_africa:', use_aliases=True),
                                      request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, text="Для дальнейшей работы с ботом Вы должны отправить ему свою геопозицию.",
                     reply_markup=keyboard)


@bot.message_handler(commands=["menu"])
def keyboard_(message):
    global keyboard2
    keyboard2 = types.InlineKeyboardMarkup(row_width=1)
    button_1 = types.InlineKeyboardButton(text="Узнать цены" + (emojize(':mag_right:', use_aliases=True)),
                                          callback_data="price")
    button_2 = types.InlineKeyboardButton(text="Найти ближайшую АЗС" + (emojize(':round_pushpin:', use_aliases=True)),
                                          callback_data="find_near")
    button_3 = types.InlineKeyboardButton(text="Найти дешевое топливо" +
                                               (emojize(':arrow_lower_right:', use_aliases=True)),
                                          callback_data="low_price")
    button_4 = types.InlineKeyboardButton(text="Динамика цен" + (emojize(':bar_chart:', use_aliases=True)),
                                          callback_data="graph")
    keyboard2.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, text="Что хотите узнать?", reply_markup=keyboard2)


@bot.message_handler(content_types=["location"])
def location(message):
    global loc
    loc = (message.location.latitude, message.location.longitude)
    bot.send_message(message.chat.id, text="/menu")
    print('\n ------------------------------------------')
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2})".format(message.from_user.first_name,
                                                    message.from_user.last_name,
                                                    str(message.from_user.id)))
    print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
    print('------------------------------------------')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.reply_to(message, text="Извини, я тебя не понял" + emojize(':cry:', use_aliases=True) +
                               "\nПопробуй команду /help")


@bot.callback_query_handler(func=lambda call: True)
def main_menu(call):
    if call.data == "price":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Прайм", callback_data="prime")
        button_2 = types.InlineKeyboardButton(text="Беркут", callback_data="berkut")
        button_3 = types.InlineKeyboardButton(text="Газпром (ак)", callback_data="gasprom_1")
        button_4 = types.InlineKeyboardButton(text="Газпром", callback_data="gasprom_2")
        button_5 = types.InlineKeyboardButton(text="Лукойл", callback_data="lukoil")
        button_6 = types.InlineKeyboardButton(text="Тайм", callback_data="time")
        button_7 = types.InlineKeyboardButton(text="Энергия", callback_data="energia")
        keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7)

        bot.send_message(call.message.chat.id, text="Выберите бренд", reply_markup=keyboard)
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == "prime":
        bot.send_message(call.message.chat.id, text=str(brand[64]) + ": " + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-92: " + str(reg_92[64]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-95: " + str(reg_95[64]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "ДТ: " + str(diesel[64]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-98: " + str(reg_98[64]))
        print(f'Вызван callback: {call.data} \n')
        print('------------------------------------------')
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == "berkut":
        bot.send_message(call.message.chat.id, text=str(brand[87]) + ": " + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-92: " + str(reg_92[87]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-95: " + str(reg_95[87]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "ДТ: " + str(diesel[87]))
        print(f'Вызван callback: {call.data} \n')
        print('------------------------------------------')
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == "gasprom_1":
        bot.send_message(call.message.chat.id, text=str(brand[19]) + ": " + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-92: " + str(reg_92[19]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-95: " + str(reg_95[19]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "ДТ: " + str(diesel[19]))
        print(f'Вызван callback: {call.data} \n')
        print('------------------------------------------')
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == "gasprom_2":
        bot.send_message(call.message.chat.id, text=str(brand[30]) + ": " + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-92: " + str(reg_92[30]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-95: " + str(reg_95[30]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "ДТ: " + str(diesel[30]))
        print(f'Вызван callback: {call.data} \n')
        print('------------------------------------------')
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == "lukoil":
        bot.send_message(call.message.chat.id, text=str(brand[0]) + ": " + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-92: " + str(reg_92[0]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-95: " + str(reg_95[0]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "ДТ: " + str(diesel[0]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-98: " + str(reg_98[0]))
        print(f'Вызван callback: {call.data} \n')
        print('------------------------------------------')
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == "time":
        bot.send_message(call.message.chat.id, text=str(brand[91]) + ": " + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-92: " + str(reg_92[91]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-95: " + str(reg_95[91]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "ДТ: " + str(diesel[91]))
        print(f'Вызван callback: {call.data} \n')
        print('------------------------------------------')
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == "energia":
        bot.send_message(call.message.chat.id, text=str(brand[95]) + ": " + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-92: " + str(reg_92[95]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-95: " + str(reg_95[95]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "ДТ: " + str(diesel[95]) + "\n" +
                                                    (emojize(':fuelpump:', use_aliases=True)) +
                                                    "АИ-98: " + str(reg_98[95]))
        print(f'Вызван callback: {call.data} \n')
        print('------------------------------------------')
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == "find_near":
        if loc is not None:
            res = []
            for i in range(len(adress)):
                coords = (latitude[i], longitude[i])
                result = (geodesic(loc, coords)).kilometers
                res.append(result)
            index = res.index(min(res))

            bot.send_message(call.message.chat.id,
                                text="АЗС: " + (brand[index]) +
                                    "\nАдрес: " + (adress[index]) +
                                    "\nРасстояние: " + str("%.3f" % min(res)) + " км." +
                                    "\nЦена за литр топлива: \n" +
                                    (emojize(':fuelpump:', use_aliases=True)) + "АИ-92 - " + str(
                                    reg_92[index]) + " руб.\n" +
                                    (emojize(':fuelpump:', use_aliases=True)) + "АИ-95 - " + str(
                                    reg_95[index]) + " руб.\n" +
                                    (emojize(':fuelpump:', use_aliases=True)) + "ДТ - " + str(diesel[index]) + " руб.")

            bot.send_venue(call.message.chat.id, title=brand[index], address=adress[index],
                            longitude=longitude[index], latitude=latitude[index])
            print(f'Вызван callback: {call.data} \n'
                  f'Расстояние от А до Б: {min(res)} \n '
                  f'Адрес: {adress[index]} \n'
                  f'АЗС: {brand[index]} \n'
                  f'Номер элемента в списке: {index} \n'
                  f'Аи-92: {reg_92[index]}, Аи-95: {reg_95[index]}, ДТ: {diesel[index]}'
                  )
            print('------------------------------------------')
            bot.answer_callback_query(callback_query_id=call.id)

        else:
            bot.send_message(call.message.chat.id,
                                text="Сначала отправьте свою геопозицию! /geo")
            bot.answer_callback_query(callback_query_id=call.id)

    if call.data == "low_price":
        global keyboard_1
        if loc is not None:
            keyboard_1 = types.InlineKeyboardMarkup(row_width=2)
            button_1 = types.InlineKeyboardButton(text=(emojize(':fuelpump:', use_aliases=True)) +
                                                       "АИ-92", callback_data="regular_92")
            button_2 = types.InlineKeyboardButton(text=(emojize(':fuelpump:', use_aliases=True)) +
                                                       "АИ-95", callback_data="regular_95")
            button_3 = types.InlineKeyboardButton(text=(emojize(':fuelpump:', use_aliases=True)) +
                                                       "ДТ", callback_data="diesel")
            button_4 = types.InlineKeyboardButton(text=(emojize(':fuelpump:', use_aliases=True)) +
                                                       "АИ-98", callback_data="regular_98")
            keyboard_1.add(button_1, button_2, button_3, button_4)

            bot.send_message(call.message.chat.id, text="В радиусе 1,5км бот найдет для Вас самое дешевое топливо: ",
                             reply_markup=keyboard_1)
            print(f'Вызван callback: {call.data} \n')
            print('------------------------------------------')
            bot.answer_callback_query(callback_query_id=call.id)

        else:
            bot.send_message(call.message.chat.id,
                             text="Сначала отправьте свою геопозицию! /geo")
            bot.answer_callback_query(callback_query_id=call.id)

    if call.data == "regular_92":
        res = []
        br = []
        adr = []
        petrol = []
        latit = []
        longit =[]
        for i in range(len(reg_92)):
            coords = (latitude[i], longitude[i])
            result = (geodesic(loc, coords)).kilometers
            if result <= 1.5:
                res.append(result)
                br.append(brand[i])
                adr.append(adress[i])
                petrol.append(reg_92[i])
                latit.append(latitude[i])
                longit.append(longitude[i])
        index = petrol.index(min(petrol))
        bot.send_venue(call.message.chat.id, title=br[index], address=adr[index],
                       longitude=longit[index], latitude=latit[index])
        bot.send_message(call.message.chat.id,
                         text=f"АЗС: {br[index]}" "\n"
                              f"Адрес: {adr[index]}" "\n"
                              f"Цена за литр АИ-92 здесь составляет: {petrol[index]} руб.", reply_markup=keyboard_1)
        bot.answer_callback_query(callback_query_id=call.id)
        del res, br, adr, petrol, latit, longit

    if call.data == "regular_95":
        res = []
        br = []
        adr = []
        petrol = []
        latit = []
        longit = []
        for i in range(len(reg_95)):
            coords = (latitude[i], longitude[i])
            result = (geodesic(loc, coords)).kilometers
            if result <= 1.5:
                res.append(result)
                br.append(brand[i])
                adr.append(adress[i])
                petrol.append(reg_95[i])
                latit.append(latitude[i])
                longit.append(longitude[i])
        index = petrol.index(min(petrol))
        bot.send_venue(call.message.chat.id, title=br[index], address=adr[index],
                       longitude=longit[index], latitude=latit[index])
        bot.send_message(call.message.chat.id,
                         text=f"АЗС: {br[index]}" "\n"
                              f"Адрес: {adr[index]}" "\n"
                              f"Цена за литр АИ-95 здесь составляет: {petrol[index]} руб.", reply_markup=keyboard_1)
        print(f'Вызван callback: {call.data} \n'
              f'Адрес: {adr[index]} \n'
              f'АЗС: {br[index]} \n'
              f'Номер элемента в списке: {index} \n'
              f'Аи-95: {petrol[index]}')
        print('------------------------------------------')
        bot.answer_callback_query(callback_query_id=call.id)
        del res, br, adr, petrol, latit, longit

    if call.data == "diesel":
        res = []
        br = []
        adr = []
        dis = []
        latit = []
        longit = []
        for i in range(len(diesel)):
            coords = (latitude[i], longitude[i])
            result = (geodesic(loc, coords)).kilometers
            if result <= 1.5:
                res.append(result)
                br.append(brand[i])
                adr.append(adress[i])
                dis.append(diesel[i])
                latit.append(latitude[i])
                longit.append(longitude[i])
        index = dis.index(min(dis))
        bot.send_venue(call.message.chat.id, title=br[index], address=adr[index],
                       longitude=longit[index], latitude=latit[index])
        bot.send_message(call.message.chat.id,
                         text=f"АЗС: {br[index]}" "\n"
                              f"Адрес: {adr[index]}" "\n"
                              f"Цена за литр ДТ здесь составляет: {dis[index]} руб.", reply_markup=keyboard_1)
        print(f'Вызван callback: {call.data} \n'
              f'Адрес: {adr[index]} \n'
              f'АЗС: {br[index]} \n'
              f'Номер элемента в списке: {index} \n'
              f'ДТ: {dis[index]}')
        print('------------------------------------------')
        bot.answer_callback_query(callback_query_id=call.id)
        del res, br, adr, dis, latit, longit

    if call.data == "regular_98":
        res = []
        br = []
        adr = []
        petrol = []
        latit = []
        longit = []
        for i in range(len(reg_98)):
            coords = (latitude[i], longitude[i])
            result = (geodesic(loc, coords)).kilometers
            if result <= 1.5:
                res.append(result)
                br.append(brand[i])
                adr.append(adress[i])
                petrol.append(reg_98[i])
                latit.append(latitude[i])
                longit.append(longitude[i])
                if reg_98[i] is None:
                    petrol.remove(reg_98[i])
        index = petrol.index(min(petrol))
        bot.send_venue(call.message.chat.id, title=br[index], address=adr[index],
                       longitude=longit[index], latitude=latit[index])
        bot.send_message(call.message.chat.id,
                            text=f"АЗС: {br[index]}" "\n"
                            f"Адрес: {adr[index]}" "\n"
                            f"Цена за литр АИ-98 здесь составляет: {petrol[index]} руб.", reply_markup=keyboard_1)
        bot.answer_callback_query(callback_query_id=call.id)
        del res, br, adr, petrol, latit, longit

    if call.data == "graph":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="АИ-92", callback_data='png_92')
        button_2 = types.InlineKeyboardButton(text="АИ-95", callback_data='png_95')
        button_3 = types.InlineKeyboardButton(text="ДТ", callback_data='png_diesel')
        button_4 = types.InlineKeyboardButton(text="АИ-98", callback_data='png_98')
        keyboard.add(button_1, button_2, button_3, button_4)

        bot.send_message(call.message.chat.id, text="Выберите топливо", reply_markup=keyboard)
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == 'png_92':
        png_1()
        bot.send_photo(call.message.chat.id, open('regular_92.png', 'rb'))
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == 'png_95':
        png_2()
        bot.send_photo(call.message.chat.id, open('regular_95.png', 'rb'))
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == 'png_diesel':
        png_3()
        bot.send_photo(call.message.chat.id, open('diesel.png', 'rb'))
        bot.answer_callback_query(callback_query_id=call.id)

    if call.data == 'png_98':
        png_4()
        bot.send_photo(call.message.chat.id, open('regular_98.png', 'rb'))
        bot.answer_callback_query(callback_query_id=call.id)


if __name__ == '__main__':
    bot.polling(none_stop=True)
