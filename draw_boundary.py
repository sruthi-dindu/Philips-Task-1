from PIL import Image, ImageDraw
import numpy as np

def convert(list_of_lists):

    # Convert the list of lists to a NumPy array
    numpy_array = np.array(list_of_lists)

    # Convert the NumPy array to an array of tuples
    array_of_tuples = np.asarray([tuple(row) for row in numpy_array])

    return(array_of_tuples)

def draw_boundary(box):
    # Load the image
    image_path = "C:/Users/320220529/OneDrive - Philips/Desktop/Consent_forms/1. Basic/pngs/page0.jpg"
    image = Image.open(image_path)
    
    for coords in box:
        coords = convert(coords)
        print(coords)
        draw = ImageDraw.Draw(image)
        draw.polygon(coords, outline="red")
        image.show()

    # Display or save the image with the bounding box
    



#[[200, 273], [401, 273], [401, 310], [200, 310]]
#[[[202, 344], [399, 344], [399, 376], [202, 376]]]

#[[[202, 344], [399, 344], [399, 376], [202, 376]]]
#draw_boundary([(201, 433), (398, 433), (398, 465), (201, 465)])
#draw_boundary([(202, 344), (399, 344), (399, 376), (202, 376)])

