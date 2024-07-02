import cv2 as cv

img = cv.imread('Fotos/ufc.jpg')
cv.imshow('ufc', img)

#cinza
cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('ufccinza', cinza)
#hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('ufchsv', hsv)
#L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('ufclab', lab)
#LUV
luv = cv.cvtColor(img, cv.COLOR_BGR2LUV)
cv.imshow('ufcluv', luv)

print(img.shape)
print(cinza.shape)
print(hsv.shape)
print(lab.shape)
print(luv.shape)

cv.waitKey(0)
cv.destroyAllWindows()