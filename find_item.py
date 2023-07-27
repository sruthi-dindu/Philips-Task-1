import os
import io
from PIL import Image
import easyocr
from pymongo import MongoClient
import cv2
from bson.binary import Binary
import re

client = MongoClient("mongodb://localhost:27017/")
db = client["consent_forms"]
cf_database = db["Consentform"]



def find_item(data):
    try:
        # Define the regex pattern
        pattern = 'r"/*' + data + '*/ix"'
        cf_database.create_index([("$**", "text")])

        document = cf_database.find_one({'$text': {'$search': eval(pattern)}})
        image_data = document['image']
        return image_data
            
    except Exception as e:
        return("An error occurred:"+ str(e))

#print(find_item("Morgan"))
