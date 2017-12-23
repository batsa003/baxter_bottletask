import cv2
import numpy as np

# Given an opencv image, find the cap and return the pixel coordinates of the cap along with the detected image.
def detect_cap(img):
    # Setup SimpleBlobDetector parameters.
    img = cv2.GaussianBlur(img,(5,5),0)
    #cv2.imshow('hi',img)
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 10
    params.maxThreshold = 200;
    params.minArea = 1000
    params.maxArea = 2300
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(img)
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    print len(keypoints), ' number of points detected for cap'
    if(len(keypoints) == 0):
        print('Failed to find the CAP!')
        return None
    return (keypoints[0].pt,im_with_keypoints)

if __name__ == "__main__":
    image = cv2.imread('camera_image.png')
    (cap_pt, im_with_cap) = detect_cap(image)
    cv2.imshow('Keypoints', im_with_cap)
    cv2.waitKey(0)
