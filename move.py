import shutil

for i in range(1, 17):
    path_from = '/Users/andrearodriguez/Downloads/output/'+str(i)+'_inpainted.wav'

    i = i+8
    path_to = '/Users/andrearodriguez/rep/RisultatiInpainting/clip'+str(i)+'/ddnm_2.wav'

    shutil.move(path_from, path_to)