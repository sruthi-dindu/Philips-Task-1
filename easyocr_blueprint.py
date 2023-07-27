import os
import io
from PIL import Image
import easyocr
from centroid import *
from draw_boundary import *
from mongo_blueprint import *

reader = easyocr.Reader(['en'])
link = "C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/image_data/Sophia_consent_forms.jpg"

def easyocr_blueprint(link):
    import easyocr
    img = Image.open(link)
    reader = easyocr.Reader(['en'])
    img.detect_horizontal = True
    results = reader.readtext(img)
    for i in results:
        print(i)
    #results = reader.readtext(img)
    li=[]
    bi=['Participant\'s name', 'Investigator name', 'Date', 'Relationship t0 the participant', 'Relationship to the participant','Investigalor name']
    box=[]
    for i in range(len(results)):
        if(results[i][1] in bi):
            box.append(results[i][1])
    add_blueprint(box,1)


    
    
            
#easyocr_blueprint(link)
            
            
    
        



      
