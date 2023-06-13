# Importing Image class from PIL module
from PIL import Image

for i in range(1,9):
    # Opens a image in RGB mode
    im = Image.open('/Users/andrearodriguez/Downloads/Risultati/DDNM+_2sec/'+str(i)+'_mel-spectrograms.png')
    
    # Setting the points for cropped image
    left = 756
    top = 32
    right = 1088
    bottom = 293
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    
    # Shows the image in image viewer
    #im1.show()
    im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/ddnm+_2.png")