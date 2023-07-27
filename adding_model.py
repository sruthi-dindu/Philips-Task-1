
import os
import io
from PIL import Image
import easyocr
from pymongo import MongoClient
import cv2
from bson.binary import Binary

client = MongoClient("mongodb://localhost:27017/")
db = client["consent_forms"]
model_database = db["Models"]

def adding_model(link,function_name):
    with open(link, 'rb') as image_file:
        image_data = image_file.read()
    query={}
    query.update({'function' : Binary(image_data)})
    model_database.insert_one(query)
    return ("Added consent form successfully.")

form_1 = 'C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/medical-research-consent-form.jpg'
form_2 = 'C:/Users/320220529/Downloads/new_consent_form.jpg'
adding_model(form_1, 'medical_research_form')
adding_model(form_2, 'qualitative_research_consent_form')
