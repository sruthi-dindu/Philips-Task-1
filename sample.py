from pdf2image import convert_from_bytes
from werkzeug.utils import secure_filename
from flask import *
import fitz
import codecs
import io
import os
from convert_to_jpg import *
from easyocr_blueprint import *
from easyocr_consent_form import *
from find_item import *
from io import BytesIO
from PyPDF2 import PdfReader
import re
import base64

import numpy
import cv2

app = Flask(__name__)

def convert(f):
    return convert_to_jpg(f)

@app.route('/')  
def upload():  
    return render_template("webpage.html")

@app.route('/search', methods = ['POST'])  
def search():
    return render_template("search_consent.html")

@app.route('/participant_name', methods = ['POST'])  
def upload_success():
    return render_template("upload_success.html")

@app.route('/searching', methods = ['POST'])  
def search_consent_form():
    textbox_value = request.form['textbox']
    image_path = find_item(textbox_value)
    encoded_image = base64.b64encode(image_path).decode('utf-8')
    return render_template('display_search.html', image_path=encoded_image)
    

if __name__ == '__main__':  
    app.run(host= '0.0.0.0', debug = True)
