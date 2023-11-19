import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret, computer_webcam = camera.read()

    hsv = cv2.cvtColor(computer_webcam, cv2.COLOR_BGR2HSV)

    lover_red = np.array([0, 100, 100])
    up_red = np.array([10, 255, 255])

    lower_red2 = np.array([160, 100, 100])
    up_red2= np.array([179, 255, 255])

    maske1 = cv2.inRange(hsv, lover_red, up_red)
    maske2 = cv2.inRange(hsv, lower_red2, up_red2)

    maske = maske1 + maske2

    maskeli_goruntu = cv2.bitwise_and(computer_webcam, computer_webcam, mask=maske)

    cv2.imshow('Orjinal Goruntu (computer_webcam)', computer_webcam)
    cv2.imshow('Maskelenmiş Goruntu (computer_webcam)', maskeli_goruntu)

    if cv2.waitKey(1) & 0xFF == ord('z'):
        break

camera.release()
cv2.destroyAllWindows()