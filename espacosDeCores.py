import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Fotos/dogs.jpg')
cv.imshow('dogs', img)

#RGB
# plt.imshow(img)
# plt.show()

#escala de cinza
cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('cinza', cinza)

#BGR para HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#BGR para L * A * B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

#BGR para RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

#Cinza para BGR
cinza_bgr = cv.cvtColor(cinza, cv.COLOR_GRAY2BGR)#falsa escala de cinza 
cv.imshow('cinza_bgr', cinza_bgr)

cv.waitKey(0)
cv.destroyAllWindows()