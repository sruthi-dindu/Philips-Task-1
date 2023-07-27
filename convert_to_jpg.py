import fitz
from PIL import Image
import os
import PIL
import os
import io
import os
from PyPDF2 import PdfReader
from PIL import Image
import cv2


        

def convert_to_jpg(pdf_path):
    file_extension = os.path.splitext(pdf_path)[1].lower()

    if file_extension == '.pdf':
        # import module
        from pdf2image import convert_from_path
        # Store Pdf with convert_from_path function
        images = convert_from_path(pdf_path)
        output_folder = 'pngs/'
        target =[]
 
        for i in range(len(images)):
            filename = os.path.join(output_folder, 'page' + str(i) + '.jpg')
            images[i].save(filename, 'JPEG')
            image = Image.open(filename)
            image.save(filename)
            target.append(filename)
    
        return target
    
    elif file_extension in ('.jpg', '.jpeg'):
        output_folder = 'pngs/'
        output_path = os.path.join(output_folder, 'page0' + '.jpg')
        image = Image.open(pdf_path)
        #image = image.convert("RGB")
        image.save(output_path, "JPEG")
        target =[]
        target.append(output_path)
        return target
    
    elif file_extension in ('.png'):
        output_folder = 'pngs/'
        output_path = os.path.join(output_folder, 'page0' + '.jpg')
        image = Image.open(pdf_path)
        image = image.convert("RGB")
        image.save(output_path, "JPEG")
        target =[]
        target.append(output_path)
        return target
        
    

#link = 'C:/Users/320220529/OneDrive - Philips/Documents/vinu.png'
#link = 'C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/Data/images/Sruthi_consent.jpg'
#print(convert_to_jpg(link))


