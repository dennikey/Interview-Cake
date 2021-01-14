from PIL import Image 

# Opens a image in RGB mode 
im = Image.open("1.jpg") 

# Size of the image in pixels (size of orginal image) 
# (This is not mandatory) 
width, height = im.size 

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((185, 779, 200, 1000)) 

# Shows the image in image viewer 
im1.show()



'''
from wand.image import Image as wi

def imagetaker(file_name):
    pdf = wi(file_name)
    pdfimage = pdf.convert("jpeg")
    i = 1
    links = []

    for img in pdfimage.sequence:
        page = wi(image=img)
        page.save(filename=str(i)+".jpg")
        links.append(str(i) + ".jpg")
        i += 1
    
    return links

for i in range(len(pages)):
    page = pages[i]
    page.save('output_{}.jpg'.format(i), 'png')
'''