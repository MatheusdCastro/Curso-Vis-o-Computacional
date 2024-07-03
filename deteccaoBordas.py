import cv2 as cv
import numpy as np

img = cv.imread("Fotos/ufc.jpg")
dog = cv.imread('Fotos/dogs.jpg')
cinza = cv.cvtColor(dog, cv.COLOR_BGR2GRAY)

#Laplaciano
lap = cv.Laplacian(cinza, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplace", lap)

#Sobel(gradiente)
sobelx = cv.Sobel(cinza, cv.CV_64F, 1, 0)
cv.imshow("sobelx", sobelx)
sobely = cv.Sobel(cinza, cv.CV_64F, 0, 1)
cv.imshow("sobely", sobely)

sobel_combinado = cv.bitwise_or(sobelx, sobely)
cv.imshow("sobel combinado", sobel_combinado)

#canny
canny = cv.Canny(cinza, 150, 175)
cv.imshow("canny", canny)


cv.waitKey()
cv.destroyAllWindows()