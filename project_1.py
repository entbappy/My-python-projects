#Virtual Paint

import cv2
import numpy as np


#Reading Webcam
cap = cv2.VideoCapture(0) #for default
cap.set(3,640) #Set width
cap.set(4,480) #Set height

#Blue,Red,Green
myColors = [[40,60,113,162,251,243],[0,167,54,90,232,255],[29,72,87,53,184,172]]

#blue , green ,red
color_values = [[255,0,0],[0,0,255],[0,255,0]]

myPoints = [] #[x,y,colorID]

#color detection
def findColors(img,myColors,color_values):
    img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints =[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(img_HSV,lower,upper)
        x,y= getContours(mask)  #function calling
        cv2.circle(img_result,(x,y),10,color_values[count],cv2.FILLED)

        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
        # cv2.imshow(str(color[0]),mask)
    
    return newPoints


#Contours and shape detection
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
     
    x,y,w,h = 0,0,0,0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area>500:
            # cv2.drawContours(img_result,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)

    return x+w//2,y



def drawOnCanvas(myPoints,color_values):
    for point in myPoints:
        cv2.circle(img_result,(point[0],point[1]),10,color_values[point[2]],cv2.FILLED)




while True:
    success, img = cap.read()
    img_result = img.copy()

    newPoints = findColors(img,myColors,color_values)
    if len(newPoints)!=0:
        for nPoint in newPoints:
            myPoints.append(nPoint)
    
    if len(newPoints)!=0:
        drawOnCanvas(myPoints,color_values)

    cv2.imshow("Result",img_result)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


print("Code executed!")