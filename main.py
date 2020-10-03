import matplotlib.pyplot as plt
from pearson_correlation import pearson_correlation as pc

# Load the scene image
file_name = 'Ig.tif' #input('Insira o nome da imagem cena com extensão: ')
img = plt.imread(file_name)

# Load the template image
file_name = 'Io.tif' #input('Insira o nome da imagem template com extensão: ')
tempt = plt.imread(file_name)

# Call Pearson Function and show the result
result = pc(img, tempt)
plt.imshow(result, cmap = 'gray')
