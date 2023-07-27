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
from select_blueprint import *
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

@app.route('/selectform', methods = ['POST'])  
def select_consent():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["consent_forms"]
    model_database = db["Models"]
    arr=[]
    # Retrieve all documents in the collection
    documents = model_database.find()
    # Iterate over the documents and print their contents
    for document in documents:
        print(document)
        image_data = document['function']
        arr.append(base64.b64encode(image_data).decode('utf-8'))
    return render_template("select_consent.html", form_1 = arr[0], form_2 = arr[1])
    
 
    

@app.route('/consentform', methods = ['POST'])  
def upload_consent():
    return render_template("upload_consent.html")

@app.route('/template', methods = ['POST'])  
def upload_template():
    return render_template("contact_custodian.html")
    #return render_template("upload_template.html")

@app.route('/search', methods = ['POST'])  
def search():
    
    return render_template("search_consent.html")


@app.route('/upload_success', methods = ['POST'])  
def upload_success():
    if request.method == 'POST':
        # Get the uploaded file
        #file = request.files['file'].read()
        file = request.files['file']
        function = request.form.get('secret')
        if 'file' not in request.files:
            return 'No file uploaded'
        
        # Save the file to a local directory
        file.save("uploads/" + file.filename)

        # Get the path of the uploaded file
        file_path = os.path.join("C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/uploads" , file.filename)

        array = convert_to_jpg(file_path)

        for i in array:
            path = os.path.join("C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic", i)
            k = easyocr_consent_form(path,function)
        return render_template("upload_success.html")
        
        
        
    



    

@app.route('/template_success', methods = ['POST'])  
def template_success():
    return render_template("contact_custodian.html")
    '''if request.method == 'POST':
        # Get the uploaded file
        #file = request.files['file'].read()
        function = request.form.get('function')
        file = request.files['file']
        if 'file' not in request.files:
            return 'No file uploaded'
        
        # Save the file to a local directory
        file.save("uploads/" + file.filename)

        # Get the path of the uploaded file
        file_path = os.path.join("C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/uploads" , file.filename)

        array = convert_to_png(file_path)

        for i in array:
            path = os.path.join("C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic", i)
            k = easyocr_blueprint(path)
        
        
        return render_template("template_success.html")'''

@app.route('/searching', methods = ['POST'])  
def search_consent_form():
    textbox_value = request.form['textbox']
    image_path = find_item(textbox_value)
    
    try:
        encoded_image = base64.b64encode(image_path).decode('utf-8')
        return render_template('display_search.html', image_path=encoded_image)
    except Exception as e:
        return render_template('no_data.html')

@app.route('/selecting', methods = ['POST'])  
def select_consent_form():
    selected_function = request.form['option']
    if(eval(selected_function) == 3):
        return render_template("contact_custodian.html")
    #return render_template("sample.html", function = eval(selected_function))
    function = select_blueprint(eval(selected_function))
    return render_template("upload_consent.html", function = function)

    

if __name__ == '__main__':  
    app.run(host= '0.0.0.0', debug = True)
