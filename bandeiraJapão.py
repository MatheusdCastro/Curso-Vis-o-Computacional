import cv2 as cv
import numpy as np

bandeira = np.zeros((400, 600, 3), dtype = 'uint8')

bandeira[:] = 255, 255, 255#pintando de branco
cv.circle(bandeira, (295, 200), 50, (0, 0, 255), -1)
cv.imshow('bandeira', bandeira)

cv.waitKey(0)
cv.destroyAllWindows()