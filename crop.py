from PIL import Image

for i in range(1, 5):
    im = Image.open('/Users/andrearodriguez/Downloads/output_ddnm_20_1s/'+str(i)+'_mel-spectrograms.png')

    # third
    #left = 756
    #top = 32
    #right = 1088
    #bottom = 293

    # first
    #left = 98
    #top = 32
    #right = 430
    #bottom = 293

    # second
    left = 427
    top = 32
    right = 759
    bottom = 293
    
    im1 = im.crop((left, top, right, bottom))
    
    #im1.show()
    im1.save("/Users/andrearodriguez/rep/RisultatiInpainting/denoising/clip"+str(i)+"/noisy_20_gap_1.png")