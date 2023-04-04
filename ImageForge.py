"""Этот модуль реализует функционал работы с изображениями"""
from PIL import Image


def make_image(crop_values):
    """Эта функция принимает массив параметров персонажа и сохраняет изображение
    готового персонажа в файл static/img/image.png

    Она использует файл static/img/Parts.png и вырезает из него выбранные части персонажа"""
    img = Image.open("static/img/Parts.png")
    paste_img = img.crop((crop_values[0] * 15, 0, (crop_values[0] + 1) * 15, 20))
    for i in range(1, len(crop_values)):
        cropped_img = img.crop((crop_values[i] * 15, i * 20, (crop_values[i] + 1) * 15, (i + 1) * 20))
        paste_img.paste(cropped_img, (0, 0), mask=cropped_img.split()[3])
    paste_img.save("static/img/image.png")
    img.close()


def rotate_value(current, maximum, bump=1):
    """Эта функция возвращает увеличенное значение, имитируя цикличность: 0->1->2->3->0"""
    return (current + bump) % maximum
