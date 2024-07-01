import cv2 as cv
import numpy as np

img = cv.imread('Fotos/dog.webp')
cv.imshow('doguinho', img)

#transladar
def translada(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, x]])
    dimensoes = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensoes)
# x movimenta para a direita, o -x para a esuqerda
# y movimenta a imagem para baixo, -y para cima
transladado = translada(img, 100, 100)
cv.imshow('transladado', transladado)

transladado2 = translada(img, -100, 100)
cv.imshow('transladado2', transladado2)

#rotacionar
def rodar(img, teta, pontoRot = None): #none significa q a variável n tem valor algum
    (altura, largura) = img.shape[:2] #já pega as duas variáveis em toda a imagem
    if pontoRot == None:
        pontoRot = (largura//2, altura//2)
    rotMat = cv.getRotationMatrix2D(pontoRot, teta, 1.0)
    dimensoes = (largura, altura)
    return cv.warpAffine(img, rotMat, dimensoes)

rotacionada = rodar(img, -45, pontoRot = (10,10))
cv.imshow('rotacionada', rotacionada)

#mudança de escala/ resizing 
mudatamanho = cv.resize(img,(500, 500), interpolation = cv.INTER_AREA) 
cv.imshow('tamanho reduzido', mudatamanho)

#flipplig (inversão)
flip = cv.flip(img, -1) #0 modifica verticalmente; 1 modifica horizontalmente; -1 faz os dois; -0 não muda
cv.imshow('inversao', flip)

cv.waitKey(0) 
cv.destroyAllWindows()