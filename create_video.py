import numpy as np
import cv2
import cv
import os
def sort(x):
	m=x[5:]
	m=m[:-4]
	m=int(m)
	return m
def create_v(frames,path):
	#fourcc = cv2.VideoWriter_fourcc(*'XVID')
	'''fourcc = cv.CV_FOURCC('i','Y', 'U', 'V')
	frame=cv.LoadImage(path+"/"+frames[2])
	frame_size = cv.GetSize(frame)
	print "Video size: ", frame_size  
	out=cv2.VideoWriter('output.avi',fourcc,1.0,frame_size)
	for i in frames:
		path1=path+i
		print path1
		img=cv2.imread(path1)
		s="./output/"+i[:-4]+".png"
		print s
		cv2.imwrite(s,img)
		out.write(img)
	out.release()'''
	
	
	
	frame=cv.LoadImage(path+"/"+frames[2])
	print dir(frame)
	fps = 1.0      # so we need to hardcode the FPS
	print "Recording at: ", fps, " fps"  

	frame_size = cv.GetSize(frame)
	print "Video size: ", frame_size  
	CODEC = cv.CV_FOURCC('D','I','V','3') # MPEG 4.3
	# CODEC = cv.CV_FOURCC('M','P','4','2') # MPEG 4.2
	# CODEC = cv.CV_FOURCC('M','J','P','G') # Motion Jpeg
	# CODEC = cv.CV_FOURCC('U','2','6','3') # H263
	# CODEC = cv.CV_FOURCC('I','2','6','3') # H263I
	# CODEC = cv.CV_FOURCC('F','L','V','1') # FLV
	CODEC = cv.CV_FOURCC('P','I','M','1') # MPEG-1
	CODEC = cv.CV_FOURCC('D','I','V','X') # MPEG-4 = MPEG-1

	writer = cv.CreateVideoWriter(path+"/out.avi", CODEC, fps, frame_size, True)
	for i in frames:
		
		path1=path+"/"+i	
		print path1
		img=cv.LoadImage(path1)
		cv.WriteFrame(writer, img)

def create_video(path):	
	
	l=os.listdir(path)
	l=sorted(l,key=sort)
	create_v(l,path)
create_video("/home/ordellugo/Desktop/Test/part3/posture")	

