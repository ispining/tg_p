import datetime
import os
import random
import threading
import time

from pyrogram import Client, enums
import pickle


def unpick(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


def pick(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


g = {"@ruworkis": {"next_post": None,
                             "message": [
                             """H&M
        
<u>Описание:</u> Работа простая, не физическая.
Упаковка и сбор одежды для заказов.

Подходит как мужчинам, так и женщинам.
Любой возраст.
<u>Время работы:</u>
• 7:00 - 17:30 (41/час)
<u>Город:</u> Холон
<u>Подвозка:</u> ✅
<u>Еда:</u> ❌
<u>Машина от работы:</u> По договоренности

+972504834744""",
                             """Работа в Sano
        
<u>Описание:</u> Работа физическая, но хорошо оплачивается.
• Бонусы
• Обеды (-8 шек)
• Длинные смены (11-12 часов)
<u>Время работы:</u>
• 6:00 - 18:30 (40/час)
• 19:00 - 5:00 (42/час)
<u>Требования:</u> 
Только от 23 до 40 лет.
Только мужчины.
<u>Город:</u> Од-ашарон
<u>Еда:</u> ✅
<u>Подвозка:</u> ✅
<u>Машина от работы:</u> По договоренности

+972504834744"""],
                             "interval": [61, 80]},
          "@batyam_live": {"next_post": None,
                            "message": [
                            """Ребят, кому нужна работа в центре - обращайтесь!

Хорошие условия:
• Есть вакансии с бонусами
• Подходит как мужчинам, так и женщинам
• Подходит любому возрасту
• Машина от работы по договоренности
• Бонусы

<b><u>Контакты:</u></b> 
Связаться по WhatsApp: +972504834744
Оставить заявку в боте: @MorLogisticsBot""",
                            """<b>Привет всем! Если ищете работу в центре, обращайтесь!</b>

<b><u>Условия отличные:</u></b> 
• Есть позиции с бонусной системой 
• Подойдет как для мужчин, так и для женщин 
• Возраст значения не имеет 
• Рабочий автомобиль возможен по договоренности 
• Приятные бонусы и поощрения
• Приятный коллектив

<b><u>Контакты:</u></b> 
WhatsApp: +972504834744
Бот: @MorLogisticsBot
"""
                            ],
                            "interval": [60*2, 60*4]}}
# pick("data", groups)
groups = unpick("data")


api_id = 21194050
api_hash = "ef8c398ae656ae51e585e405d3e83ff2"

tg = Client("Main", api_id, api_hash)
tg.start()

while True:
    try:
        for group_id in groups.keys():
            group_data = groups[group_id]
            if group_data["next_post"] == None:
                try:
                    tg.send_message(group_id, random.choice(group_data["message"]), parse_mode=enums.ParseMode.HTML)
                    groups[group_id]["next_post"] = datetime.datetime.now() + datetime.timedelta(
                        minutes=random.randint(group_data["interval"][0], group_data["interval"][1]))
                    pick("data", groups)
                    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(time_now)
                    print("[+] Posted to " + group_id)
                    print("[+] Next post at " + groups[group_id]["next_post"].strftime("%Y-%m-%d %H:%M:%S"))
                except:
                    pass

            elif datetime.datetime.now() > group_data["next_post"]:
                try:
                    tg.send_message(group_id, random.choice(group_data["message"]), parse_mode=enums.ParseMode.HTML)
                    groups[group_id]["next_post"] = datetime.datetime.now() + datetime.timedelta(
                        minutes=random.randint(group_data["interval"][0], group_data["interval"][1]))
                    pick("data", groups)
                    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(time_now)
                    print("[+] Posted to " + group_id)
                    print("[+] Next post at " + groups[group_id]["next_post"].strftime("%Y-%m-%d %H:%M:%S"))

                except:
                    pass
            time.sleep(random.randint(1, 10))
        print("[+] Sleeping 60 seconds...")
        time.sleep(60)
        print("[+] Waking up...")
    except KeyboardInterrupt:
        break

exit(0)

