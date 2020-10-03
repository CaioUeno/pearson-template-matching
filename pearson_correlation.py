import numpy as np
import matplotlib.pyplot as plt

def pearson_correlation(img, obj):

    num_rows, num_cols = img.shape
    num_rows_obj, num_cols_obj = obj.shape   
    half_num_rows_obj = num_rows_obj//2        
    half_num_cols_obj = num_cols_obj//2

    img_padded = np.pad(img, ((half_num_rows_obj,half_num_rows_obj),
                             (half_num_cols_obj,half_num_cols_obj)), 
                             mode='constant')
    
    img_result = np.zeros((num_rows, num_cols))
    mean_obj = np.mean(obj) #media de intensidade do objeto buscado (é o mesmo para toda função)
    std_obj = np.std(obj) #desvio padrão de intensidade do objeto buscado (é o mesmo para toda função)
    
    for row in range(num_rows):
        for col in range(num_cols):
            #região da imagem que será analisada
            patch = img_padded[row:row+num_rows_obj, col:col+num_cols_obj]
            #media e desvio padrão da região
            mean_patch = np.mean(patch)
            std_patch = np.std(patch)
            
            result_region = ((patch-mean_patch)*(obj-mean_obj))/np.sqrt(((std_patch**2)*(std_obj**2)))
            
            img_result[row, col] = np.sum(result_region)
            
    return img_result
