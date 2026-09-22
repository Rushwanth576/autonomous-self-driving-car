import cv2
def detect_circular_sign(frame):
    gray=cv2.GaussianBlur(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),(5,5),0)
    c=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,35,param1=100,param2=35,minRadius=8,maxRadius=80)
    return c is not None
