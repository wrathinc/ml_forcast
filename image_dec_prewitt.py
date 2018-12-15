import cv2
import numpy as np

img = cv2.imread('../satna.jpg')

dst = cv2.fastNlMeansDenoisingColored(img,10,10,7,21)

#cv2.imshow("orignial",img)
cv2.imshow("smoothed",dst)




