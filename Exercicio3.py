import cv2 as cv
#aplicando deteção de bordas em vídeos

captura = cv.VideoCapture("Videos/cachorrinhofofo.mp4")
while True:
    isTrue, quadro = captura.read()
    cinza = cv.cvtColor(quadro, cv.COLOR_BGR2GRAY)
    # canny = cv.Canny(cinza, 120, 180)
    lap = cv.Laplacian(cinza, cv.CV_64F)
    # sobelx = cv.Sobel(cinza, cv.CV_64F, 1, 0)
    cv.imshow('video', lap)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

captura.release()

cv.waitKey(0)
cv.destroyAllWindows()
