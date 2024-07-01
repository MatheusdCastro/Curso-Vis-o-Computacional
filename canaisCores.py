import cv2 as cv 
import numpy as np

img = cv.imread("Fotos/ufc.jpg")
cv.imshow('ufc', img)
vazio = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('vazio', vazio)

#separanado os 3 canais de ecores
b, g, r = cv.split(img)
blue = cv.merge([b, vazio, vazio])
green = cv.merge([vazio, g, vazio])
red = cv.merge([vazio, vazio, r])
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(cinza.shape)

juntar = cv.merge([b, g, r])
cv.imshow('juntar', juntar)

cv.waitKey(0)
cv.destroyAllWindows()