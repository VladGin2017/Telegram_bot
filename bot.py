import config
import telebot
import sqlite3

from geopy.distance import geodesic
from telebot import types
from datetime import datetime

con = sqlite3.connect('data_base.db')
cor = con.cursor()

query = 'SELECT latitude FROM map'
cor.execute(query)
latitude = cor.fetchall()
lat = []
for element in latitude:
    lat.append(element[0])
latitude = lat
del (lat)
# print(latitude)

query_2 = 'SELECT longitude FROM map'
cor.execute(query_2)
longitude = cor.fetchall()
lon = []
for element in longitude:
    lon.append(element[0])
longitude = lon
del (lon)

query_3 = 'SELECT adress FROM map'
cor.execute(query_3)
adress = cor.fetchall()
adresses = []
for elements in adress:
    adresses.append(elements[0])
adress = adresses
del (adresses)

query_4 = 'SELECT brand FROM map'
cor.execute(query_4)
brand = cor.fetchall()
brands = []
for elements in brand:
    brands.append(elements[0])
brand = brands
del (brands)

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

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, text="Привет, на данный момент бот умеет находить ближайщую к тебе АЗС,"
                                           " а так же выводить информацию о ценах на топливо каждого бренда\n"
                                           "В будущем появятся такие функции, как поиск ближайшей АЗС по бренду,"
                                           " поиск ближайшей АЗС с самым дешевым топливом по городу, "
                                           "вывод графика динамики цен за месячный период. \n"
                                           "А пока, что бы опробовать бота напиши в чат: \n"
                                           "/menu - узнать цену на топливо\n"
                                           "/geo - отправить боту свою геопозицию и узнать расположение ближайшей АЗС")


@bot.message_handler(commands=["geo"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, text="Для дальнейшей работы с ботом Вы должны отправить ему свою геопозицию.",
                     reply_markup=keyboard)


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        global loc
        loc = (message.location.latitude, message.location.longitude)
        bot.send_message(message.chat.id, text="Теперь напишите /menu и узнайте, как бот может Вам помочь.")
        print('\n ------------------------------------------')
        print(datetime.now())
        print("Сообщение от {0} {1}. (id = {2})".format(message.from_user.first_name,
                                                        message.from_user.last_name,
                                                        str(message.from_user.id)))
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))


@bot.message_handler(commands=["menu"])
def keyboard_(message):
    global keyboard_2
    keyboard_2 = types.InlineKeyboardMarkup(row_width=1)
    button_1 = types.InlineKeyboardButton(text="Узнать цены", callback_data="price")
    button_2 = types.InlineKeyboardButton(text="Найти ближайшую АЗС", callback_data="find_near")
    button_3 = types.InlineKeyboardButton(text="Найти дешевое топливо", callback_data="low_price")
    keyboard_2.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, text="Что хотите узнать?", reply_markup=keyboard_2)


@bot.callback_query_handler(func=lambda call: True)
def test(call):
    if call.data == "price":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Прайм", callback_data="prime")
        button_2 = types.InlineKeyboardButton(text="Беркут", callback_data="berkut")
        button_3 = types.InlineKeyboardButton(text="Газпром (ак)", callback_data="gasprom_1")
        button_4 = types.InlineKeyboardButton(text="Газпром", callback_data="gasprom_2")
        button_5 = types.InlineKeyboardButton(text="Лукойл", callback_data="lukoil")
        button_6 = types.InlineKeyboardButton(text="Роснефть", callback_data="rosneft")
        button_7 = types.InlineKeyboardButton(text="Тайм", callback_data="time")
        keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7)

        bot.send_message(call.message.chat.id, text="Выберите бренд", reply_markup=keyboard)

    if call.data == "prime":
        bot.send_message(call.message.chat.id, text=str(brand[64]) + ": " + "\n" +
                                                    "АИ-92: " + str(reg_92[64]) + "\n" +
                                                    "АИ-95: " + str(reg_95[64]) + "\n" +
                                                    "ДТ: " + str(diesel[64]))

    if call.data == "berkut":
        bot.send_message(call.message.chat.id, text=str(brand[87]) + ": " + "\n" +
                                                    "АИ-92: " + str(reg_92[87]) + "\n" +
                                                    "АИ-95: " + str(reg_95[87]) + "\n" +
                                                    "ДТ: " + str(diesel[87]))

    if call.data == "gasprom_1":
        bot.send_message(call.message.chat.id, text=str(brand[19]) + ": " + "\n" +
                                                    "АИ-92: " + str(reg_92[19]) + "\n" +
                                                    "АИ-95: " + str(reg_95[19]) + "\n" +
                                                    "ДТ: " + str(diesel[19]))
    if call.data == "gasprom_2":
        bot.send_message(call.message.chat.id, text=str(brand[30]) + ": " + "\n" +
                                                    "АИ-92: " + str(reg_92[30]) + "\n" +
                                                    "АИ-95: " + str(reg_95[30]) + "\n" +
                                                    "ДТ: " + str(diesel[30]))

    if call.data == "lukoil":
        bot.send_message(call.message.chat.id, text=str(brand[0]) + ": " + "\n" +
                                                    "АИ-92: " + str(reg_92[0]) + "\n" +
                                                    "АИ-95: " + str(reg_95[0]) + "\n" +
                                                    "ДТ: " + str(diesel[0]))

    if call.data == "rosneft":
        bot.send_message(call.message.chat.id, text=str(brand[80]) + ": " + "\n" +
                                                    "АИ-92: " + str(reg_92[80]) + "\n" +
                                                    "АИ-95: " + str(reg_95[80]) + "\n" +
                                                    "ДТ: " + str(diesel[80]))

    if call.data == "time":
        bot.send_message(call.message.chat.id, text=str(brand[98]) + ": " + "\n" +
                                                    "АИ-92: " + str(reg_92[98]) + "\n" +
                                                    "АИ-95: " + str(reg_95[98]) + "\n" +
                                                    "ДТ: " + str(diesel[98]))
    if call.data == "find_near":
        global coincidence
        your_dist = loc
        res = []
        i = -1
        while i != 100:
            i = i + 1
            coords = (latitude[i], longitude[i])
            result = (geodesic(your_dist, coords)).kilometers
            res.append(result)

        minimum = min(res)
        for i in range(len(res)):
            if minimum == res[i]:
                coincidence = i
                break
        bot.send_message(call.message.chat.id,
                             text="Ближайшая АЗС " + (brand[coincidence]) + " по адресу: " + (adress[coincidence]) +
                                  "\n Расстояние до нее составляет: " + str(
                                 "%.3f" % minimum) + " километра." + "\n Цена за литр топлива: " + "\nАИ-92 - " + str(
                                 reg_92[coincidence]) + " рублей" +
                                  "\n АИ-95 - " + str(reg_95[coincidence]) + " рублей" + "\nДТ - " + str(
                                 diesel[coincidence]) + " рублей")
        bot.send_venue(call.message.chat.id, title=brand[coincidence], address=adress[coincidence],
                       longitude=longitude[coincidence], latitude=latitude[coincidence], reply_markup=keyboard_2)

    if call.data == "low_price":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        button_1 = types.InlineKeyboardButton(text="АИ-92", callback_data="regular_92")
        button_2 = types.InlineKeyboardButton(text="АИ-95", callback_data="regular_95")
        button_3 = types.InlineKeyboardButton(text="ДТ", callback_data="diesel")
        keyboard.add(button_1, button_2, button_3)

        bot.send_message(call.message.chat.id, text="В радиусе 2км бот найдет для Вас самое дешевое топливо: ",
                         reply_markup=keyboard)

    if call.data == "regular_92":
        your_dist = loc
        res = []
        br = []
        adr = []
        r_92 = []
        i = -1
        while i != 100:
            i = i + 1
            coords = (latitude[i], longitude[i])
            result = (geodesic(your_dist, coords)).kilometers
            if result <= 2:
                res.append(result)
                br.append(brand[i])
                adr.append(adress[i])
                r_92.append(reg_92[i])
        print(res, br, adr, r_92)
        index = r_92.index(min(r_92))

        bot.send_message(call.message.chat.id,
                             text="АЗС: " + str(br[index]) + "\n"
                                  "Адрес: " + str(adr[index]) + "\n" 
                                  "Цена за литр АИ-92 здесь составляет: " + str(r_92[index]) + "руб.")

    if call.data == "regular_95":
        your_dist = loc
        res = []
        br = []
        adr = []
        r_95 = []
        i = -1
        while i != 100:
            i = i + 1
            coords = (latitude[i], longitude[i])
            result = (geodesic(your_dist, coords)).kilometers
            if result <= 2:
                res.append(result)
                br.append(brand[i])
                adr.append(adress[i])
                r_95.append(reg_95[i])
        index = r_95.index(min(r_95))

        bot.send_message(call.message.chat.id,
                             text="АЗС: " + str(br[index]) + "\n"
                                  "Адрес: " + str(adr[index]) + "\n" 
                                  "Цена за литр АИ-95 здесь составляет: " + str(r_95[index]) + "руб.")

    if call.data == "diesel":
        your_dist = loc
        res = []
        br = []
        adr = []
        dis = []
        i = -1
        while i != 100:
            i = i + 1
            coords = (latitude[i], longitude[i])
            result = (geodesic(your_dist, coords)).kilometers
            if result <= 2:
                res.append(result)
                br.append(brand[i])
                adr.append(adress[i])
                dis.append(diesel[i])
        index = dis.index(min(dis))

        bot.send_message(call.message.chat.id,
                             text="АЗС: " + str(br[index]) + "\n"
                                  "Адрес: " + str(adr[index]) + "\n" 
                                  "Цена за литр ДТ здесь составляет: " + str(dis[index]) + "руб.")





'''
@bot.message_handler(content_types=["location"])
def location(message):
    global coincidence
    if message.location is not None:
        your_dist = (message.location.latitude, message.location.longitude)
        i = -1
        res = []
        while i != 100:
            i = i + 1
            coords = (latitude[i], longitude[i])
            result = (geodesic(your_dist, coords)).kilometers
            # result = int(result)
            res.append(result)

        minimum = min(res)
        for i in range(len(res)):
            if minimum == res[i]:
                coincidence = i
                break
        bot.send_message(message.chat.id,
                         text="Ближайшая АЗС " + (brand[coincidence]) + " по адресу: " + (adress[coincidence]) +
                              "\n Расстояние до нее составляет: " + str(
                             "%.3f" % minimum) + " километра." + "\n Цена за литр топлива: " + "\nАИ-92 - " + str(
                             reg_92[coincidence]) + " рублей" +
                              "\n АИ-95 - " + str(reg_95[coincidence]) + " рублей" + "\nДТ - " + str(
                             diesel[coincidence]) + " рублей")
        print('\n ------------------------------------------')
        print(datetime.now())
        print("Сообщение от {0} {1}. (id = {2})".format(message.from_user.first_name,
                                                        message.from_user.last_name,
                                                        str(message.from_user.id)))
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
'''

if __name__ == '__main__':
    bot.polling(none_stop=True)

