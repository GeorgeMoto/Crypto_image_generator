from PIL import ImageDraw
from PIL import ImageFont
from project.base import*
from project.generator_of_percent import*
import os


def create_image(donut_number):

    # Задний фон изображения
    background = choice(RGB_BASE)

    # Создаем объект изображения в памяти
    img = Image.new("RGB", (WIDTH, HEIGHT), background)

    # Генерация уникального цифрового номера изображения
    def generate_text():

        # Подбирает цвет надписи отличный от основного фона
        def get_color_id_number():
            while True:
                color = choice(RGB_BASE)
                if color == background:
                    continue
                else:
                    return color

        id_number = Image.new("RGBA", (64, 50), color=(0, 0, 0, 0))
        dr = ImageDraw.Draw(id_number)
        fnt = ImageFont.truetype('DATA/Ubuntu-Bold.ttf', size=9)
        text = str(randint(100, 999)).encode("utf-8").hex()
        dr.text(
            (33, -1),
            f"{text}",
            font=fnt,
            # Цвет номера индентификатора
            fill=(get_color_id_number()),
        )
        return id_number

    # Изменить цвет слоя, третий параметр прменяется только если
    # функция применяется для создания теней
    def change_color(layer_image, name_of_layer_image, value_to_create_shadows=None):

        # Извлекаем пиксели
        layer_pixels = layer_image.load()

        # Генерируем диапазон смещения байта RGBA из диапозонов заданых в RANGE_COLORS
        r_byte = randint(*RANGE_COLORS.get(name_of_layer_image, (0, 0)))
        g_byte = randint(*RANGE_COLORS.get(name_of_layer_image, (0, 0)))
        b_byte = randint(*RANGE_COLORS.get(name_of_layer_image, (0, 0)))

        # Редактируем пиксели слоя
        for w in range(WIDTH):
            for h in range(HEIGHT):
                # Получаем текущий цвет пикселя и кортеж RGBA
                pixel = layer_pixels[w, h]
                # Меняем цвет на рандомный диапазон
                # Красим только сам объект
                if pixel != (0, 0, 0, 0):

                    if value_to_create_shadows is None:
                        layer_pixels[w, h] = (
                            pixel[0] + r_byte,
                            pixel[1] + g_byte,
                            pixel[2] + b_byte,
                            255
                        )
                    else:
                        layer_pixels[w, h] = (
                            value_to_create_shadows[0] + r_byte,
                            value_to_create_shadows[1] + g_byte,
                            value_to_create_shadows[2] + b_byte,
                            255
                        )

    # Нахождение первое вхождение rgb в изображении, используется
    # для создания теней на основе цветов основных слоев изображения
    def find_color(image, *, the_path_to_layer):
        name_of_image = image
        image = Image.open(f"{the_path_to_layer}/{image}")
        image = image.load()
        default_color = 0
        for w in range(WIDTH):
            for h in range(HEIGHT):
                # Как только в слое найден первый окрашенный пиксель, функция
                # возвращает его RGBA значение и прекращает работу

                if image[w, h] != (0, 0, 0, 0):
                    default_color = image[w, h]

                if default_color != 0:
                    return name_of_image, default_color

    # Основные слои изображения
    main_layers = os.listdir("png parts/main parts")

    # На основе списка main_layers формируется словарь где ключ - это имя слоя,
    # а значение его rgba в виде кортежа (0, 0, 0, 0)
    main_layers_colors = [find_color(img, the_path_to_layer="png parts/main parts") for img in main_layers]

    main_layers_colors = {value[0]: value[1] for value in main_layers_colors}

    # Изменение текущего слоя и наложение его на основной
    def get_modified_layer(layers, *, the_path_to_layer):

        for layer in layers:
            name_of_layer_image = layer.replace(".png", "")

            # Если в пути к файлу со слоем встречается имя слоя на основе которого генерировались тени,
            # то мы используем его rgba
            if layer in the_path_to_layer:

                data = Image.open(f"{the_path_to_layer}/{layer}").convert("RGBA")
                change_color(data, name_of_layer_image,
                             main_layers_colors.get(layer, None))
                # Накладываем получившийся слой на основное изображение
                img.paste(data, (0, 0), data)

            else:

                # Если такого имени слоя нет то применяется стандартный способ генерации
                data = Image.open(f"{the_path_to_layer}/{layer}").convert("RGBA")
                change_color(data, name_of_layer_image)

                img.paste(data, (0, 0), data)

    # Объединяем основные слои нашего изображения
    get_modified_layer(main_layers, the_path_to_layer="png parts/main parts")

    # Список png объектов из соответсвующей директории
    down_part_layers = os.listdir("png parts/sub parts/down_part")

    # Меняем цвет и накладываем объекты друг на друга
    get_modified_layer(down_part_layers, the_path_to_layer="png parts/sub parts/down_part")

    # Список png объектов из соответсвующей директории
    glaze_layers = os.listdir("png parts/sub parts/glaze")

    # Меняем цвет и накладываем объекты друг на друга
    get_modified_layer(glaze_layers, the_path_to_layer="png parts/sub parts/glaze")

    # Добавляем топпинг
    topping = add_topping()
    if topping is not None:
        change_color(topping[0], topping[2])
        img.paste(topping[0], (0, 0), topping[0])
    else:
        topping = 100

    # Добавляем глаза
    eyes = add_eyes()
    if eyes is not None:
        change_color(eyes[0], eyes[2])
        img.paste(eyes[0], (0, 0), eyes[0])
    else:
        eyes = 100

    # Добавляем к изображению уникальный id
    id_number = generate_text()
    img.paste(id_number, (0, 0), id_number)

    # Сохраняем результат в отдельную папку
    if not os.path.exists(f"result/{donut_number}"):
        os.mkdir(f"result/{donut_number}")
    img.save(f"result/{donut_number}/donut #{donut_number}.png")

    # Добавляем текстовые характеристики каждого доната
    with open(f"result/{donut_number}/specifications.txt", "w", encoding='utf-8') as file:
        # Вероятность получить такого же персонажа в %
        eyes_percent = eyes[1] if isinstance(eyes, list) else eyes
        topping_percent = topping[1] if isinstance(topping, list) else topping
        character_rarity = int(((eyes_percent * 0.01) * (topping_percent * 0.01)) * 100)

        characteristics = "Редкость предметов (шанс получить предмет в процентном соотношении)\n\n" \
            f"Глаза: {eyes_percent}%\n" \
            f"Топпинг: {topping_percent}%\n" \
            f"Вероятность получения персонажа {character_rarity}%"
        file.write(characteristics)

    # Сохраняем результат в общую папку
    if not os.path.exists("result/all_donuts"):
        os.mkdir("result/all_donuts")
    img.save(f"result/all_donuts/{donut_number} ({str(character_rarity).replace('.', ',')}%).png")

    # Сохраняем результат на ПК
    img.save(f"C:/Users/Георгий/Desktop/donuts/result/donut# {donut_number}.png")
