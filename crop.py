from PIL import Image

for i in range(1, 9):
    im = Image.open('/Users/andrearodriguez/Downloads/output/'+str(i)+'_mel-spectrograms.png')

    left = 756
    top = 32
    right = 1088
    bottom = 293

    # original
    #left = 98
    #top = 32
    #right = 430
    #bottom = 293

    # cut
    #left = 427
    #top = 32
    #right = 759
    #bottom = 293
    
    im1 = im.crop((left, top, right, bottom))
    
    #im1.show()
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/original.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/cut_1.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/cut_2.png")
    im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/audioldm_1.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/audioldm_2.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/tango_1.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/tango_2.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/ddnm_1.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/ddnm_2.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/ddnm+_1.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/ddnm+_2.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/repaint_1.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/repaint_2.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/repaintjump_1.png")
    #im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/clip"+str(i)+"/repaintjump_2.png")