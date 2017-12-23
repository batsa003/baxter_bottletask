import cv2
import numpy as np
import time

def detect_bottle(img):
    img = cv2.medianBlur(img,5)
#    img = cv2.GaussianBlur(img, (3,3), 0)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20.0,
                                param1=50,param2=55,minRadius=20,maxRadius=0)
    
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(255,255,0),3)
    numcircle = len(circles[0,:])
    print numcircle, ' number of circles detected for bottle'
    [x,y,z] = circles[0,0,:]
    return ((x,y),cimg)
	
if __name__ == "__main__":
    im = cv2.imread('camera_image.png',0)
    (bottle_pt, cimg) = detect_bottle(im)
    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

