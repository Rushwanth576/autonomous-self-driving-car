import cv2, numpy as np
def detect_traffic_signal(frame):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    masks={
      'RED':cv2.bitwise_or(cv2.inRange(hsv,np.array([0,100,100]),np.array([10,255,255])),cv2.inRange(hsv,np.array([170,100,100]),np.array([179,255,255]))),
      'YELLOW':cv2.inRange(hsv,np.array([15,90,90]),np.array([40,255,255])),
      'GREEN':cv2.inRange(hsv,np.array([35,70,70]),np.array([90,255,255]))}
    label,area=max(((k,cv2.countNonZero(v)) for k,v in masks.items()),key=lambda x:x[1])
    return label if area>=180 else 'UNKNOWN'
