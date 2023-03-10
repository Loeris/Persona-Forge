from flask import Flask, render_template, request
from PIL import Image
from random import randint

img = Image.open("static/img/Parts.png")

def make_image(crop_values):
    paste_img = img.crop((crop_values[0] * 15, 0, (crop_values[0] + 1) * 15, 20))
    for i in range(1, len(crop_values)):
        cropped_img = img.crop((crop_values[i] * 15, i * 20, (crop_values[i] + 1) * 15, (i + 1) * 20))
        paste_img.paste(cropped_img, (0, 0), mask=cropped_img.split()[3])
    paste_img.save("static/img/image.png")


def rotate_value(current, maximum, bump=1):
    return (current + bump) % maximum


crop_values = [0, 0, 0, 0]
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        for act_number in range(4):
            if request.form.get(f'act{act_number}') == '>':
                crop_values[act_number] = rotate_value(crop_values[act_number], 4)
            elif request.form.get(f'act{act_number}') == '<':
                crop_values[act_number] = rotate_value(crop_values[act_number], 4, -1)
    elif request.method == 'GET':
        return render_template('index.html')
    make_image(crop_values)

    return render_template("index.html")

app.run()