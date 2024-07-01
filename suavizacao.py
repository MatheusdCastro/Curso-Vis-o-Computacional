import cv2 as cv 

img = cv.imread("Fotos/ufc.jpg")
cv.imshow('img', img)

#media simples
media = cv.blur(img, (7, 7))
cv.imshow('media', media)

#gaussiana
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('gauss', gauss)

#mediana -> bom em reduzir ruído(plastico)
mediana = cv.medianBlur(img, 7)
cv.imshow('mediana', mediana)

# bilateral -> bom em identificar bordas
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)
cv.destroyAllWindows()