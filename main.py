"""Этот модуль реализует функционал работы с сайтом."""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint
import webbrowser
from ImageForge import *
from ImageVault import *

# Инициализация
character_stats = [0, 0, 0, 0]
character_size = [6]
make_image(character_stats)
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/vault", methods=['GET', 'POST'])
def vault():
    """Эта функция реализует страницу хранилища."""
    return render_template("vault.html")
@app.route("/forge", methods=['GET', 'POST'])
def forge():
    """Эта функция реализует страницу создания."""
    context = {}
    context['size'] = str(character_size[0] * 65)
    if request.method == 'POST':
        for act_number in range(4):
            # Кнопки ротации составляющих
            if request.form.get(f'act{act_number}') == '>':
                character_stats[act_number] = rotate_value(character_stats[act_number], 4)
            elif request.form.get(f'act{act_number}') == '<':
                character_stats[act_number] = rotate_value(character_stats[act_number], 4, -1)
            elif request.form.get(f'act{act_number}') == '?':
                character_stats[act_number] = randint(0, 3)
        if request.form.get('size') == '-':
            if character_size[0] > 1:
                character_size[0] -= 1
        if request.form.get('size') == '+':
            character_size[0] += 1
        context['size'] = str(character_size[0] * 65)
    elif request.method == 'GET':
        return render_template('forge.html', context=context)
    make_image(character_stats)

    return render_template("forge.html", context=context)


def forge_start():
    """Эта функция запускает сервер и открывает сайт."""
    webbrowser.open('http://127.0.0.1:5000/forge')
    app.run()
