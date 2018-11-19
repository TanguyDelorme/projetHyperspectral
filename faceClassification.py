import cv2
import os
from spectral import *

img=[]

path = "../Dataset/"

liste = os.listdir(path)

selectionApprentissagePeau = ["0001", "0002", "0004", "0006", "0008", "0010", "0012", "0013", "0014", "0015", "0059", "0061", "0062", "0063", "0065", "0066", "0067", "0068", "0069", "0071"] #Numeros des dossiers (correspondant à des personnes

coordRectanglesPeau = [] #Coordonées des rectangles pour la zone correspondant à la peau pour chanque personne (doit etre de taille 4*len(selectionApprentissagePeau): 4 coordonées pour chaque personne dans l'ordre suivant: x1,y1,x2,y2


coordRectanglesPeau.append([416,344,516,388])
coordRectanglesPeau.append([402,315,474,337])
coordRectanglesPeau.append([440,347,514,365])
coordRectanglesPeau.append([386,285,486,307])
coordRectanglesPeau.append([342,399,444,431])
coordRectanglesPeau.append([390,405,494,427])
coordRectanglesPeau.append([406,397,510,421])
coordRectanglesPeau.append([446,361,520,383])
coordRectanglesPeau.append([366,407,444,435])
coordRectanglesPeau.append([464,569,542,583])
coordRectanglesPeau.append([322,419,432,447])
coordRectanglesPeau.append([482,369,578,409])
coordRectanglesPeau.append([404,428,504,449])
coordRectanglesPeau.append([496,467,602,511])
coordRectanglesPeau.append([490,265,584,297])
coordRectanglesPeau.append([526,279,630,317])
coordRectanglesPeau.append([492,409,574,427])
coordRectanglesPeau.append([488,331,524,361])
coordRectanglesPeau.append([484,367,560,391])
coordRectanglesPeau.append([444,213,558,265])

moyenneLambdaPeau=[] #Tableau de 33 longueurs d'onde moyennes correspondant à la peau (moyenne à la longueur d'onde 1,2,3,..,33)

##def rect( img, rect ): #renvoie la sous-image définie par le rectangle construit à partir de x1, y1 (en haut a gauche) et x2,y2 (en bas a droite)
##   imgRect=[]
##   for i in range(rect[0]，rect[2]):
##       for j in range(rect[1]，rect[3]):
##           imgRect.append(img[i,j])
##   return [imgRect]

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
            img.append(cv2.imread(path + i + "/F_" + str(x) + ".png"))    
        #cv2.imshow('myImage', img[x-1])

for i in range(0,33):
    for j in range(0, len(selectionApprentissagePeau)):
        #TODO: iterer sur tableau correspondant à rectangle
        moyenneLambdaPeau[i] += mean_rect(img[i+(33*j)], coordRectanglesPeau[j][0], coordRectanglesPeau[j][1], coordRectanglesPeau[j][2], coordRectanglesPeau[j][3]) 
    moyenneLambdaPeau[i] = moyenneLambdaPeau[i]/len(selectionApprentissagePeau)
    print(moyenneLambdaPeau[i])
