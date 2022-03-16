import os
from random import choice, randint
from PIL import Image


# Получаем рандомный редкий предмет в зависимости от уникальности
def get_item(folder_name, percent):
    item_list = os.listdir(f"png parts/rare items/{folder_name}/{percent}")
    if len(item_list) > 0:
        return [percent, choice(item_list)]


# Получить процент редкости предмета
# Используемая редкость предметов (20%)
def percent_checker(folder_name):
    rare_percent = randint(1, 100)
    if rare_percent <= 10:
        return get_item(folder_name, 10)
    elif rare_percent <= 20:
        return get_item(folder_name, 20)
    elif rare_percent <= 30:
        return get_item(folder_name, 30)
    else:
        return None


# В случае успеха, возвращает список с объектом изображения топпинга,
# процент редкости предмета, имя предмета
def add_topping():
    item = percent_checker("topping")
    if item is not None:
        return [
            Image.open(f"png parts/rare items/topping/{item[0]}/{item[1]}").convert("RGBA"),
            item[0], item[1].replace(".png", "")
            ]


# В случае успеха, возвращает список с объектом изображения глаз,
# процент редкости предмета, имя предмета
def add_eyes():
    item = percent_checker("eyes")
    if item is not None:
        return [
            Image.open(f"png parts/rare items/eyes/{item[0]}/{item[1]}").convert("RGBA"),
            item[0], item[1].replace(".png", "")
            ]
