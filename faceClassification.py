import cv2
import os
from spectral import *

img=[]

path = "../Dataset/"

liste = os.listdir(path)
print(liste)

for i in liste:    
    for x in range(1,34): #Jusqu'à 34 car on va jusqu'à n-1. On a reelement 33 images par dossier
        if x < 10:
            img.append(cv2.imread(i + "/F_0" + str(x) + ".png"))
        else:
            img.append(cv2.imread(i + "/F_" + str(x) + ".png"))    
        #cv2.imshow('myImage', img[x-1])
