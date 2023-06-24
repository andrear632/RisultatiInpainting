import shutil

for i in range(1, 9):
    #path_from = '/Users/andrearodriguez/Downloads/output/'+str(i)+'_output_0.wav'
    path_from = '/Users/andrearodriguez/Downloads/output/'+str(i)+'_original.wav'

    path_to = '/Users/andrearodriguez/rep/RisultatiInpainting/clip'+str(i)+'/original.wav'

    shutil.move(path_from, path_to)