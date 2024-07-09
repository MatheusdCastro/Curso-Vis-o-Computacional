import cv2 as cv

#fazendo o recohecimento em vídeos
cap = cv.VideoCapture(0)
cap.set(3, 640)#setand o tamanho da janela
cap.set(4, 480)
while True:
    sucesso, img = cap.read()
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(cinza, 1.1, minNeighbors = 4)
    for(x, y, w, h) in face:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
    cv.putText(img, 'Matheus', (x, y-1), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2) 
    cv.imshow('face', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv.waitKey(0)
cv.destroyAllWindows()