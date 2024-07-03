import cv2 as cv

img = cv.imread("Fotos/ufcpici.png")
cv.imshow('ufc', img)
cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('cinza', cinza)

# thresholding simples
threshold, thresh = cv.threshold(cinza, 150, 255, cv.THRESH_BINARY)
cv.imshow('limiar', thresh)
print(threshold)

threshold, threshold_inv = cv.threshold(cinza, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('limiar inverso', threshold_inv)

#thresholding adaptativo
thresh_adaptativo1 = cv.adaptiveThreshold(cinza, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('limiar adaptativo1', thresh_adaptativo1)

thresh_adaptativo2 = cv.adaptiveThreshold(cinza, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 11)
cv.imshow('limiar adaptativo2', thresh_adaptativo2)

thresh_adaptativo3 = cv.adaptiveThreshold(cinza, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 15)
cv.imshow('limiar adaptativo3', thresh_adaptativo3)

cv.waitKey(0)
cv.destroyAllWindows()