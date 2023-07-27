import easyocr
import cv2
import os
import io
from PIL import Image


link = 'C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/Data/images/Alejandro_cancer_consent_form.jpg'
#C:\Users\320220529\OneDrive - Philips\Desktop\Consent_forms\1. Basic\pngs

from PIL import Image, ImageEnhance

def enhance_image(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Enhance the sharpness of the image
    enhancer_sharpness = ImageEnhance.Sharpness(image)
    sharpened = enhancer_sharpness.enhance(2.5)  # Increase the sharpness
    
    # Enhance the brightness of the image
    enhancer_brightness = ImageEnhance.Brightness(sharpened)
    brightened = enhancer_brightness.enhance(1.0)  # Increase the brightness
    
    # Enhance the contrast of the image
    enhancer_contrast = ImageEnhance.Contrast(brightened)
    contrasted = enhancer_contrast.enhance(1.2)  # Increase the contrast
    
    # Display the original and enhanced images
    #image.show(title="Original Image")
    #contrasted.show(title="Enhanced Image")
    contrasted.save('C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/normalized_image.jpg')
    return 

# Example usage

'''enhance_image(link)
link = 'C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/normalized_image.jpg'
img = Image.open(link)
reader = easyocr.Reader(['en'])
img.detect_horizontal = True
#image = cv2.imread(link)
#results = reader.readtext(link, detail=0, paragraph=False, horizontal=True)
results = reader.readtext(img)

link = 'C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/Data/images/Alejandro_cancer_consent_form.jpg'

img = Image.open(link)
reader = easyocr.Reader(['en'])
img.detect_horizontal = True
image = cv2.imread(link)
#results = reader.readtext(link, detail=0, paragraph=False, horizontal=True)
results1 = reader.readtext(img)
k = '    |     '
en = 'ENHANCED IMAGE '
nm = '                NORMAL IMAGE '
for i in range(len(results)):
    #print(en,results[i][2],nm, results1[i][2])
    print(results[i])
print(123)'''



link = 'C:/Users/320220529/OneDrive - Philips/Pictures/econsent/handwritten.jpg'
enhance_image(link)
link = 'C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/normalized_image.jpg'
img = Image.open(link)
reader = easyocr.Reader(['en'])
img.detect_horizontal = True
#image = cv2.imread(link)
#results = reader.readtext(link, detail=0, paragraph=False, horizontal=True)
results = reader.readtext(img)
yes = 0
no = 0 
for i in range(len(results)):
    if(results[i][2]>0.5):
        yes+=1
    else:
        no+=1
print("enhanced image")
if(yes>no):
    print("the confidence is less than 0.5")
else:
    print("the confidence is less than 0.5")
    

