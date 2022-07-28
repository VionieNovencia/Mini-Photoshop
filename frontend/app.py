from tkinter import image_names
from cv2 import blur
from flask import Flask,render_template,redirect,request, url_for
import sys
sys.path.append('../')
import numpy as np
from PIL import Image
import os
from werkzeug.utils import secure_filename
from backend.milestone1 import *
from backend.milestone2 import *
from backend.milestone3 import *
from backend.helper import *

app = Flask(__name__)
app.config["Folder_upload"] = os.getcwd()+ "\\static\\"
app.config["Image_upload"] = os.getcwd() + "\\..\\test\\"
app.config["Image_download"] = os.getcwd() + "\\..\\test\\"

@app.route('/', methods=['GET', 'POST'])
def home():
    print("home")
    return render_template("home.html", filename = None)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print("upload")
    if request.method == 'POST':
        image_input = request.files["image"]
        filename = secure_filename(image_input.filename)
        # filename = get_filename(image_input.filename, "Before")
        # image.save(os.path.join(app.config['Image_upload'], filename))
        filename = get_filename(filename,"0")
        image_input.save(os.path.join(app.config["Folder_upload"], filename))
        print(filename)
    return render_template("edit.html", filename =  filename)

@app.route('/<command>', methods=['GET', 'POST'])
def editImage(command):
    if request.method == 'POST':
        filename = request.form["image"]
        filename = secure_filename(filename)
        image_input = readImage(os.path.join(app.config["Folder_upload"], filename))
        image_input = np.asarray(image_input)
        if image_input == "File tidak ditemukan.":
            return render_template("edit.html", filename = None, currentImg = None)
        else:
            if command == "negative":
                print("negative")
                result = negative(image_input)
            elif command == "grayscale":
                print("grayscale")
                result = grayscale(image_input)
            elif command == "complement":
                print("complement")
                result = complement(image_input)
            elif command == "flipv":
                print("flipv")
                result = flip_vertical(image_input)
            elif command == "fliph":
                print("fliph")
                result = flip_horizontal(image_input)
            elif command == "rotateccw":
                print("rotateccw")
                result = rotate90CCW(image_input)
            elif command == "rotatecw":
                print("rotatecw")
                result = rotate90CW(image_input)
            elif command == "zoomout":
                result = zoom_out(image_input)
            # elif command == "zoomin":
            #     result = zoom_in(image_input)
            elif command == "brightening":
                result = brightening(image_input)
            elif command == "contrast":
                result = contrast(image_input)
            elif command == "ltransformation":
                result = logTransformation(image_input)
            elif command == "ptransformation":
                result = powerTransformation(image_input)
            elif command == "blur":
                result = gaussianblur(image_input)
            elif command == "sharp":
                result = gaussianHighpass(image_input)
            elif command == "noise":
                result = noise(image_input)
            result = Image.fromarray(result)
            filename = new_filename(filename)
            print(filename)
            result.save(os.path.join(app.config["Folder_upload"], filename))
            return render_template("edit.html", filename = filename )
    return render_template("edit.html", filename = None)
    

if __name__ == "__main__":
    app.run(debug=True)