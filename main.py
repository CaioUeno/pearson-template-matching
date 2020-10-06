import matplotlib.pyplot as plt
import numpy as np
from pearson_correlation import pearson_correlation as pc, draw_rectangle

# Load the scene image
file_name = 'Ig.tif' #input('Insira o nome da imagem cena com extensão: ')
img = plt.imread(file_name)

# Load the template image
file_name = 'Io.tif' #input('Insira o nome da imagem template com extensão: ')
tempt = plt.imread(file_name)

# Call Pearson Function and show the result
result = pc(img, tempt)
plt.imshow(result, cmap = 'gray')

img_square = draw_rectangle(img, np.unravel_index(result.argmax(), result.shape), tempt.shape)
plt.imshow(img_square, 'gray')