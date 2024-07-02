import cv2 as cv

img = cv.imread('Fotos/ufc.jpg')
cv.imshow('ufc', img)

#testando o canny nas suavizações para saber a melhor
#media
media = cv.blur(img, (5, 5))
cv.imshow('media', media)
canny_media = cv.Canny(media, 125, 175)
cv.imshow('mediaCanny', canny_media)

#Gauss
gauss = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('gauss', gauss)
canny_gauss = cv.Canny(gauss, 125, 175)
cv.imshow('gaussCanny', canny_gauss)

#mediana
mediana = cv.medianBlur(img, 5)
cv.imshow('mediana', mediana)
canny_mediana = cv.Canny(mediana, 125, 175)
cv.imshow('medianaCanny', canny_mediana)

#bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)
canny_bilateral = cv.Canny(bilateral, 125, 175)
cv.imshow('bilateralCanny', canny_bilateral)

cv.waitKey(0)
cv.destroyAllWindows()