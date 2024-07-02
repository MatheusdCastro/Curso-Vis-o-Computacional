import cv2 as cv
import numpy as np

vazio = np.zeros((400, 400), dtype = 'uint8')
#retângulo cheio
retangulo = cv.rectangle(vazio.copy(),(30, 30), (370, 370), 255, -1)
circulo = cv.circle(vazio.copy(), (200, 200), 200, 255, -1)
cv.imshow('retangulo', retangulo)
cv.imshow('circulo', circulo)

#OR - Ou
or_ = cv.bitwise_or(retangulo, circulo)
cv.imshow('OR', or_)
#AND - E
and_ = cv.bitwise_and(retangulo, circulo)
cv.imshow('AND', and_)
#XOR - Ou exclusivo
xor = cv.bitwise_xor(retangulo, circulo)
cv.imshow('XOR', xor)
#NOT - Não
not_ = cv.bitwise_not(circulo)
cv.imshow('NOT', not_)

cv.waitKey(0)
cv.destroyAllWindows()