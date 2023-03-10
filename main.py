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

crop_values = [0, 0, 0, 0]
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('act1') == 'Head1':
            crop_values[0] = 0
        elif request.form.get('act1') == 'Head2':
            crop_values[0] = 1
        elif request.form.get('act1') == 'Head3':
            crop_values[0] = 2
        elif request.form.get('act1') == 'Head4':
            crop_values[0] = 3

        if request.form.get('act1') == 'Body1':
            crop_values[1] = 0
        elif request.form.get('act1') == 'Body2':
            crop_values[1] = 1
        elif request.form.get('act1') == 'Body3':
            crop_values[1] = 2
        elif request.form.get('act1') == 'Body4':
            crop_values[1] = 3

        if request.form.get('act1') == 'Border1':
            crop_values[2] = 0
        elif request.form.get('act1') == 'Border2':
            crop_values[2] = 1
        elif request.form.get('act1') == 'Border3':
            crop_values[2] = 2
        elif request.form.get('act1') == 'Border4':
            crop_values[2] = 3

        if request.form.get('act1') == 'Eyes1':
            crop_values[3] = 0
        elif request.form.get('act1') == 'Eyes2':
            crop_values[3] = 1
        elif request.form.get('act1') == 'Eyes3':
            crop_values[3] = 2
        elif request.form.get('act1') == 'Eyes4':
            crop_values[3] = 3
    elif request.method == 'GET':
        return render_template('index.html')
    make_image(crop_values)

    return render_template("index.html")

app.run()