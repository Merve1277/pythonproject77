import cv2
import numpy as np

def pirinc_tanesi_sayisi(pirinc_fotografi):

    image = cv2.imread(pirinc_fotografi)

    gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    connectivity = 8
    _, labels, stats, _ = cv2.connectedComponentsWithStats(binary, connectivity, cv2.CV_32S)

    pirinç_sayisi = len(stats)-1

    print("siyah veya koyu zemindeki pirinç tanelerinin sayısı",pirinç_sayisi)

    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

pirinc_fotografi ='pirinc.image.jpg'

pirinc_tanesi_sayisi(pirinc_fotografi)




