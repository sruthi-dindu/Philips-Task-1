import os

from PIL import Image

def convert_png_to_jpeg(input_path, output_path):
    image = Image.open(input_path)
    image = image.convert("RGB")
    image.save(output_path, "JPEG")


output_path = 'C:/Users/320220529/OneDrive - Philips/Documents/vinu.jpg'  # Replace with the desired output path for the JPEG file




def check_file_type(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.pdf':
        print(f"{file_path} is a PDF file.")
    elif file_extension in ('.jpg', '.jpeg'):
        print(f"{file_path} is an image file.")
    elif file_extension in ('.png'):
        convert_png_to_jpeg(file_path, output_path)
        print('file converted')
    else:
        print(f"{file_path} is neither a PDF nor an image file.")

# Example usage
#file_path = 'C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/Data/images/Sruthi_consent.jpg'
file_path = 'C:/Users/320220529/OneDrive - Philips/Documents/vinu.png'
check_file_type(file_path)
