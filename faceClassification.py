import cv2
import os
from spectral import *

img=[]

path = "../Dataset/"

liste = os.listdir(path)

selectionApprentissagePeau = ["0001", "0002", "0004", "0006", "0008", "0010", "0012", "0013", "0014", "0015", "0059", "0061", "0062", "0063", "0065", "0066", "0067", "0068", "0069", "0071"] #Numeros des dossiers (correspondant à des personnes

coordRectanglesPeau = [] #Coordonées des rectangles pour la zone correspondant à la peau pour chanque personne (doit etre de taille 4*len(selectionApprentissagePeau): 4 coordonées pour chaque personne dans l'ordre suivant: x1,y1,x2,y2

for i in range(0,80):
    if i%2==0:
        coordRectanglesPeau.append(0)
    else:        
        coordRectanglesPeau.append(100)
        
moyenneLambdaPeau=[] #Tableau de 33 longueurs d'onde moyennes correspondant à la peau (moyenne à la longueur d'onde 1,2,3,..,33)

def rect( img, x1, y1, x2, y2 ): #renvoie la sous-image définie par le rectangle construit à partir de x1, y1 (en haut a gauche) et x2,y2 (en bas a droite)
   imgRect=[]
   for i in range(x1, x2):
       for j in range(x2,y2):
           imgRect.append(img[i,j])
   return [imgRect]

def getPixel( img, x, y, channel):
    return img[x, y, channel]

def mean_rect( img, x1, y1, x2, y2 ): 
   return cv2.mean(img[x1:x2,y1:y2])[0]

for i in range(0,33):
    moyenneLambdaPeau.append(0)
    
for i in selectionApprentissagePeau:    
    for x in range(1,34): #Jusqu'à 34 car on va jusqu'à n-1. On a reelement 33 images par dossier
        if x < 10:
            img.append(cv2.imread(path + i + "/F_0" + str(x) + ".png"))
        else:
            img.append(cv2.imread(i + "/F_" + str(x) + ".png"))    
        #cv2.imshow('myImage', img[x-1])

for i in range(0,33):
    for j in range(0, len(selectionApprentissagePeau)):
        #TODO: iterer sur tableau correspondant à rectangle
        moyenneLambdaPeau[i] += mean_rect(img[i+(33*j)], coordRectanglesPeau[j*len(selectionApprentissagePeau)], coordRectanglesPeau[j*len(selectionApprentissagePeau)+1], coordRectanglesPeau[j*len(selectionApprentissagePeau)+2], coordRectanglesPeau[j*len(selectionApprentissagePeau)+3]) 
    moyenneLambdaPeau[i] = moyenneLambdaPeau[i]/len(selectionApprentissagePeau)
