import os
import io
from PIL import Image
import easyocr
from centroid import *
from draw_boundary import *
from mongo_blueprint import *
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["consent_forms"]
bp_database = db["blueprint"]
#cf_database = db["template"]

reader = easyocr.Reader(['en'])
link = "C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/pngs/page0.jpg"

def easyocr_template(link):
    img = Image.open(link)
    results = reader.readtext(img)
    li=[]
    bi=['Participant\'s name', 'Investigator name', 'Date', 'Relationship t0 the participant']
    keys=['participant_name', 'investigator_name','date', 'relationship']
    k=0
    for i in range(len(results)):
        if(results[i][1] in bi):
            search = bp_database.find({keys[k]: str(results[i][0])})
            k+=1
            for i in search:
                print(i)
            search = search[0]
            
            print(search['participant_name'])
            print(search['investigator_name'])
            print(search['Date'])
            print(search['relationship'])
            break

easyocr_template(link)        
        
        

        
    
    
            
easyocr_template(link)
            
            
    
        



      
