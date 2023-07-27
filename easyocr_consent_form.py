import os
import io
from PIL import Image
import easyocr
from centroid import *
from draw_boundary import *
from mongo_consent_form import *
from pymongo import MongoClient
import cv2


client = MongoClient("mongodb://localhost:27017/")
db = client["consent_forms"]
bp_database = db["blueprint"]

reader = easyocr.Reader(['en'])

#link = "C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/pngs/vinu.jpg"

class Template:
    def medical_research_consent(self, results,link):
        bi=['Participant\'s name', 'Investigator name', 'Date', 'Relationship t0 the participant', 'Relationship to the participant','Investigalor name']
        keys=['participant_name', 'investigator_name','date', 'relationship']
        k=0
        text_arr = []
        for i in range(len(results)):
            if(results[i][1] in bi):
                #print(results[i][1],results[i+1][1])
                text_arr.append(results[i+1][1])
        bi = ['participant_name', 'investigator_name','date', 'relationship']
        add_consentform(text_arr,link,bi)

    def drug_resistance_cancer_cells(self, results, link):
        text_arr = []
        text_arr.append(results[2][1])
        text_arr.append(results[-10][1])
        text_arr.append(results[-9][1])
        text_arr.append(results[-5][1])
        text_arr.append(results[-4][1])
        bi = ['Serial_Number','Name of the Participant', 'Start_data', 'Name of the Researcher', 'End Date']
        add_consentform(text_arr,link,bi)


def easyocr_consent_form(link,function):
    import easyocr
    img = Image.open(link)
    reader = easyocr.Reader(['en'])
    img.detect_horizontal = True
    image = cv2.imread(link)
    #results = reader.readtext(link, detail=0, paragraph=False, horizontal=True)
    results = reader.readtext(img)

    # Create an instance of the class
    my_object = Template()

    # Call the function using the variable
    getattr(my_object, function)(results,link)
    
    

#easyocr_consent_form(link)
            
            
    
        



      
