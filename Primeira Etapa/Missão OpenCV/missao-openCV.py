# Importação das bibliotecas
import cv2 

# Leitura da imagem com a função imread()
imagem = cv2.imread('shooky.png')

print('Largura em pixels: ', end='')
print(imagem.shape[1]) # Largura da Imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) # Altura da imagem
print('Qtde de canais: ', end='') 
print(imagem.shape[2])

# Mostra a imagem com a função imshow
cv2.imshow("Imagem", imagem)
cv2.waitKey(0) # Espera esperar qualquer tecla

# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.png", imagem)