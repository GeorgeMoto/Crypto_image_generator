WIDTH = 64
HEIGHT = 50

# Список мягких RGB цветов для создания фона
RGB_BASE = [
    (255, 228, 225), (206, 178, 229), (222, 247, 254),
    (181, 242, 234), (217, 191, 140), (246, 255, 248),
    (255, 250, 221)
]

# Название элемента в ключе, кортеж содержит диапозон изменяемости цветов
RANGE_COLORS = {
    "down_part": (-30, 30), "shadow border": (-20, 20),
    "inside of the shadow": (-20, 20), "glaze": (-200, 200),
    "shadow of glaze": (-30, 30), "main_contour": (-20, 20),
    "topping stars": (-10, 10), "stars": (-20, 20), "tetris":  (-50, 50),
    "eyes": (0, 0), "eyes1": (0, 0), "eyes2": (0, 0), "eyes3": (0, 0),
    "eyes4": (0, 0), "sunglasses1": (0, 0), "sunglasses2": (0, 0),
    "sunglasses3": (0, 0), "snow": (0, 0), "lines": (-30, 30),
    "pixels": (-20, 20)
}
