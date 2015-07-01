import sys
import cv2
import numpy as np
import os
import csv
import glob

def vector(path):
	#try:	
		print "--------finding shape of posture--------------------"
		path1=path.split("/");
		lenght=len(path1)
		path2=path1[lenght-1].split(".")
	
		global chpath,chpath1,files,frame
		chpath="";chpath1="";files=[];frame=[]
	
		for i in range(1,lenght-1):
			att="/"+path1[i]
			chpath=chpath + att
		
	
		os.chdir(chpath)
		dirs = [d for d in os.listdir('.') if os.path.isdir(os.path.join('.', d))]
	
		if(path2[0] in dirs):
			chpath1=chpath+"/"+path2[0]
			os.chdir(chpath1)
		else:
			os.mkdir(path2[0])
			chpath1=chpath+"/"+path2[0]
			os.chdir(chpath1)

		dirs1 = [d for d in os.listdir('.') if os.path.isdir(os.path.join('.', d))]

		if("posture" in dirs1):
			directory='./posture'
			os.chdir(directory)
			files=glob.glob('*.jpg')
			#print len(files),type(files)
		
			if(len(files)<50):
				for filename in files:
					os.remove(filename)
			parent=os.path.abspath('..')
			os.chdir(parent)
		g = open(chpath1+"/"+path2[0]+".txt","w")
		diff_list=[]
		count=1	
	
		global posture
		files=[f for f in os.listdir('./posture')]
		def sort(x):
			m=x[5:]
			m=m[:-4]
			m=int(m)
			return m
		files=sorted(files,key=sort)
	
		for i_file in files:
			im="./posture/"+i_file
			print i_file
			img=cv2.imread(im)
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



			contours, hierarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
			drawing = np.zeros(img.shape,np.uint8)

			max_area=0
			try:	   
			    for i in range(len(contours)):
				    cnt=contours[i]
				    area = cv2.contourArea(cnt)
				   
				    if(area>max_area):
					max_area=area
					ci=i
			    cnt=contours[ci]
			    hull = cv2.convexHull(cnt)
			    moments = cv2.moments(cnt)
			    if moments['m00']!=0:
					cx = int(moments['m10']/moments['m00']) # cx = M10/M00
					cy = int(moments['m01']/moments['m00']) # cy = M01/M00
				      
			    centr=(cx,cy)       
			    cv2.circle(img,centr,5,[0,0,255],2)       
			    cv2.drawContours(drawing,[cnt],0,(0,255,0),2) 
			    cv2.drawContours(drawing,[hull],0,(0,0,255),2) 
				  
			    cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
			    hull = cv2.convexHull(cnt,returnPoints = False)
			    
			    if(1):
				
				       defects = cv2.convexityDefects(cnt,hull)
				       mind=0
				       maxd=0
				       if(defects.shape[0]):
					    g.write(str(i_file)+":")	
				       for i in range(defects.shape[0]):
					    s,e,f,d = defects[i,0]
					    start = tuple(cnt[s][0])
					    end = tuple(cnt[e][0])
					    far = tuple(cnt[f][0])
					    ratio=float(f)/(d)
					    re=ratio*100
					    #print re
					   	
					    g.write(str(re)+",")
					    	
					    dist = cv2.pointPolygonTest(cnt,centr,True)
					    cv2.line(img,start,end,[0,255,0],2)
					    #cv2.imshow("lablel",img)
				       g.write("\n")
					    
					     
				       #i=0
			    
			    			   
			    out="contour/con"+str(count)+".jpg"
			    count+=1
			    #cv2.imwrite("feature/bound%d.jpg" % count,img)	                
			    k = cv2.waitKey(1)
			    if k == 2:
				cv2.destroyWindow("label")
				break
			except Exception:
				continue
		#cv2.destroyWindow("label")
		g.close()
		
	#except Exception:
	#	pass
	
#path="/home/ordellugo/Desktop/part1.mp4"
#vector(path)

	


