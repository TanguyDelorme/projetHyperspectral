import cv2
import os
from spectral import *
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
img=[]

path = "../Dataset/"

liste = os.listdir(path)

selectionApprentissagePeau = ["0001", "0002", "0004", "0006", "0008", "0010", "0012", "0013", "0014", "0015", "0059", "0061", "0062", "0063", "0065", "0066", "0067", "0068", "0069", "0071"] #Numeros des dossiers (correspondant à des personnes
selectionApprentissageCheveux = ["0001", "0002", "0004", "0006", "0008", "0010", "0012", "0013", "0014", "0015", "0058", "0041", "0062", "0063", "0065", "0066", "0067", "0068", "0069", "0074"]
coordRectanglesPeau = [] #Coordonées des rectangles pour la zone correspondant à la peau pour chanque personne (doit etre de taille 4*len(selectionApprentissagePeau): 4 coordonées pour chaque personne dans l'ordre suivant: x1,y1,x2,y2
coordRectanglesCheveux = []

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
coordRectanglesCheveux.append([430,263,475,281])
coordRectanglesCheveux.append([404,201,462,225])
coordRectanglesCheveux.append([404,211,550,235])
coordRectanglesCheveux.append([370,127,486,177])
coordRectanglesCheveux.append([368,275,396,287])
coordRectanglesCheveux.append([358,223,472,299])
coordRectanglesCheveux.append([368,217,486,251])
coordRectanglesCheveux.append([394,233,464,247])
coordRectanglesCheveux.append([316,235,468,291])
coordRectanglesCheveux.append([490,383,538,417])
coordRectanglesCheveux.append([414,189,460,205])
coordRectanglesCheveux.append([416,153,506,191])
coordRectanglesCheveux.append([376,281,470,313])
coordRectanglesCheveux.append([504,351,544,377])
coordRectanglesCheveux.append([466,129,522,163])
coordRectanglesCheveux.append([452,135,512,171])
coordRectanglesCheveux.append([498,295,558,325])
coordRectanglesCheveux.append([388,191,450,235])
coordRectanglesCheveux.append([472,277,508,301])
coordRectanglesCheveux.append([374,67,402,117])


def getPixel( img, x, y, channel):
    return img[x, y, channel]

def mean_StdDev_rect( img, rect ): 
   return cv2.meanStdDev(img[rect[0]:rect[2],rect[1]:rect[3]])

def rect( img, rect ): #renvoie la sous-image définie par le rectangle construit à partir de x1, y1 (en haut a gauche) et x2,y2 (en bas a droite)
   imgRect=[]
   for i in range(rect[0],rect[2]):
       for j in range(rect[1],rect[3]):
           imgRect.append(img[i,j])
   return [imgRect]

def getPixel( img, x, y, channel):
    return img[x, y, channel]

moyenneLambdaPeau=np.zeros(33)
stdDevLambdaPeau=np.zeros(33)
moyenneLambdaCheveux=np.zeros(33)
stdDevLambdaCheveux=np.zeros(33)

for i in list(set(selectionApprentissagePeau).union(set(selectionApprentissageCheveux))):
   order_i_for_Peau=0
   order_i_for_Cheveux=0
   for x in range(1,34): #Jusqu'à 34 car on va jusqu'à n-1. On a reelement 33 images par dossier
      if x < 10:
         img.append(cv2.imread(path + i + "/F_0" + str(x) + ".png"))
      else:
         img.append(cv2.imread(path +i + "/F_" + str(x) + ".png"))
      if(i in selectionApprentissagePeau):   
      	 meanPeau,StdDevPeau=mean_StdDev_rect(img[x-1], coordRectanglesPeau[order_i_for_Peau])
      	 moyenneLambdaPeau[x-1]+= meanPeau[0]
      	 stdDevLambdaPeau[x-1]+= StdDevPeau[0]

      if(i in selectionApprentissageCheveux):   
      	 meanCheveux,StdDevCheveux=mean_StdDev_rect(img[x-1], coordRectanglesCheveux[order_i_for_Cheveux])
      	 moyenneLambdaCheveux[x-1]+= meanCheveux[0]
      	 stdDevLambdaCheveux[x-1]+= StdDevCheveux[0]           
   img.clear()
   if(i in selectionApprentissagePeau):
   	 moyenneLambdaPeau[order_i_for_Peau] = moyenneLambdaPeau[order_i_for_Peau]/len(selectionApprentissagePeau)
   	 stdDevLambdaPeau[order_i_for_Peau] = stdDevLambdaPeau[order_i_for_Peau]/len(selectionApprentissagePeau)
   	 order_i_for_Peau+=1
   if(i in selectionApprentissageCheveux):
   	 moyenneLambdaCheveux[order_i_for_Cheveux] = moyenneLambdaCheveux[order_i_for_Cheveux]/len(selectionApprentissageCheveux)
   	 stdDevLambdaCheveux[order_i_for_Cheveux] = stdDevLambdaCheveux[order_i_for_Cheveux]/len(selectionApprentissageCheveux)
   	 order_i_for_Cheveux+=1


#tableau moyenne
tabMoyenne = []
for i in range(0,len(moyenneLambdaPeau)):
  tabMoyenne.append([moyenneLambdaPeau[i],moyenneLambdaCheveux[i]])   
tabMoyenne = np.transpose(tabMoyenne)
#instanciation pour normaliser les données
sc = StandardScaler()
#transformation – centrage-réduction
tabMoyenne = sc.fit_transform(tabMoyenne)
print(tabMoyenne)
#instanciation pour la création de l'acp
acp = PCA(svd_solver='full')
print("==============")
print(acp.fit_transform(tabMoyenne))
print("==============")
print(acp.explained_variance_ratio_*100)

plt.figure(1)
ax1=plt.subplot(411)
plt.plot(range(1,34),moyenneLambdaPeau,label="moyenneLambdaPeau")
plt.ylabel('niveau de gris')
plt.xlabel('longueur d\'onde')
plt.ylim((0,2000))
plt.legend(loc='upper right')
plt.grid(True)

ax2=plt.subplot(412)
plt.plot(range(1,34),stdDevLambdaPeau,label="stdDevLambdaPeau")
plt.ylabel('niveau de gris')
plt.xlabel('longueur d\'onde')
plt.ylim((0,500))
plt.legend(loc='upper right')
plt.grid(True)

ax3=plt.subplot(413)
plt.plot(range(1,34),moyenneLambdaCheveux,label="moyenneLambdaCheveux")
plt.ylabel('niveau de gris')
plt.xlabel('longueur d\'onde')
plt.ylim((0,2000))
plt.legend(loc='upper right')
plt.grid(True)

ax4=plt.subplot(414)
plt.plot(range(1,34),stdDevLambdaCheveux,label="stdDevLambdaCheveux")
plt.ylabel('niveau de gris')
plt.xlabel('longueur d\'onde')
plt.ylim((0,500))
plt.legend(loc='upper right')
plt.grid(True)

plt.show() 
#x1 = [0,5,6,8,9,1,3,1,5,3,5,8,9,4,6,3,5,6,3,2]
#x2 = np.linspace(0, 3 * np.pi, 50)
#x3 = np.linspace(0, 4 * np.pi, 50)
#plt.figure(1)

#ax1 = plt.subplot(311)
#plt.plot(range(len(x1)), x1,label="line1")
#plt.plot(range(len(x2)), x2,label="line2")
#plt.ylabel('y_name') 
#plt.legend(loc='upper right')
#plt.grid(True)


#ax2 = plt.subplot(312)
#plt.plot(x2, np.sin(x2)) 

#ax3 = plt.subplot(313)
#plt.plot(x3, np.sin(x3)) 
#plt.xlabel('x_name')
#plt.show() 
