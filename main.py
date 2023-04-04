"""Этот модуль реализует функционал работы с сайтом"""
from flask import Flask, render_template, request
from random import randint
import webbrowser
from ImageForge import *

webbrowser.open('http://127.0.0.1:5000')

# Инициализация
character_stats = [0, 0, 0, 0]
make_image(character_stats)
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    """Эта функция реализует главную страницу"""
    if request.method == 'POST':
        for act_number in range(4):
            # Кнопки ротации составляющих
            if request.form.get(f'act{act_number}') == '>':
                character_stats[act_number] = rotate_value(character_stats[act_number], 4)
            elif request.form.get(f'act{act_number}') == '<':
                character_stats[act_number] = rotate_value(character_stats[act_number], 4, -1)
            elif request.form.get(f'act{act_number}') == '?':
                character_stats[act_number] = randint(0, 3)
    elif request.method == 'GET':
        return render_template('index.html')
    make_image(character_stats)

    return render_template("index.html")


app.run()
