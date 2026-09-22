import cv2, numpy as np

def _bottom_x(line,yb):
    x1,y1,x2,y2=line
    if y2==y1:return None
    return x1+(yb-y1)*(x2-x1)/(y2-y1)

def detect_lane(frame):
    h,w=frame.shape[:2]; roi=frame[int(h*.50):int(h*.95),:]
    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(cv2.GaussianBlur(gray,(5,5),0),50,150)
    lines=cv2.HoughLinesP(edges,1,np.pi/180,25,minLineLength=25,maxLineGap=50)
    groups=[[],[]]
    if lines is not None:
        for line in lines[:,0]:
            x1,y1,x2,y2=line; dx=x2-x1
            if abs(dx)<5: continue
            s=(y2-y1)/dx
            if -2.5<s<-.35: groups[0].append(line)
            elif .35<s<2.5: groups[1].append(line)
    pts=[]; yb=roi.shape[0]-1
    for g in groups:
        xs=[_bottom_x(l,yb) for l in g]; xs=[x for x in xs if x is not None and -w<=x<=2*w]
        if xs: pts.append(sum(xs)/len(xs))
    if len(pts)==2: center=sum(pts)/2; conf=1.0
    elif len(pts)==1:
        center=pts[0]+(w*.22 if pts[0]<w/2 else -w*.22); conf=.5
    else: center=w/2; conf=0.0
    return float(np.clip((center-w/2)/(w/2),-1,1)),conf,roi
