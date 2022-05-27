
import cv2
import pickle
import cvzone
import numpy as np

width,height =107,48



#video process

cap = cv2.VideoCapture('carPark.mp4')

def parkingSpace(imgPro):

    spaceCounter = 0

   

    for pos in posList:
        x,y= pos

        imgcrop= imgPro[y:y+height,x:x+width]
        #cv2.imshow(str(x+y),imgcrop)
        count = cv2.countNonZero(imgcrop)
        cvzone.putTextRect(img,str(count),(x,y+height-3),scale=1,thickness=2,offset=0)

        if count < 700:
            color = (0,255,0)
            thickness = 3
            spaceCounter +=1
        else:
            color = (0,0,255)
            thickness = 2

        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(color),thickness)

    cvzone.putTextRect(img,f'FREE: {spaceCounter}/{len(posList)}',(100,50),scale=5,thickness=5,colorR=(0,200,0))

         
   


with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    success, img =cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    imgTreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)  
    
  
  
    parkingSpace(imgTreshold)
    #for pos in posList:
        
    cv2.imshow("Image",img)
    #cv2.imshow("ImageGRAY",imgGray)
    #cv2.imshow("ImageBLUR",imgBlur)
    #cv2.imshow("ImageMediumBLur",imgTreshold)
    cv2.waitKey(10)