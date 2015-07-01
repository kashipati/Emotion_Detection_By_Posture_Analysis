import cv2
import os

def write_on_frame(path1,emption):
	print path1
	img=cv2.imread(path1)
	
	cv2.putText(img, text, (0, 250),cv2.FONT_HERSHEY_SIMPLEX, 1.0,(255,255,255))
	#cv2.imshow("ouput",img)
	cv2.imwrite(path,img)
	return img
#r=write_on_frame("./part1/posture/frame10.jpg","happy")

