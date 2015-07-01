import cv2
import cv
import numpy as np
import os
import glob
from matplotlib import pyplot as plt
from time import sleep
from Tkinter import *
import sys


"""def sort(x):
	m=x[5:]
	m=m[:-4]
	m=int(m)
	return m
"""
def posture(path):
	print "-------------------finding posture-------------------"

	global count,count1,cntlist,cntlist1,avg,total,l,l2,posture,diff,result,framediff
	count=0;count1=0;avg=400;total=0;
	cntlist=[];cntlist=[];result=[];posture=[];#framediff=[]
	
	split1=path.split("/");
	lenght=len(split1)
	split2=split1[lenght-1].split(".")
	
	global chpath,chpath1
	chpath="";chpath1=""
	
	for i in range(1,lenght-1):
		att="/"+split1[i]
		chpath=chpath + att
			
	os.chdir(chpath)
	dirs = [d for d in os.listdir('.') if os.path.isdir(os.path.join('.', d))]
	
	if(split2[0] in dirs):
		chpath1=chpath+"/"+split2[0]
		os.chdir(chpath1)
	else:
		os.mkdir(split2[0])
		chpath1=chpath+"/"+split2[0]
		os.chdir(chpath1)	
	

	dirs1 = [d for d in os.listdir('.') if os.path.isdir(os.path.join('.', d))]
	if("frame_diff" in dirs1):
		os.chdir("./frame_diff")
		framediff=glob.glob('*.jpg')
		parent=os.path.abspath('..')
		os.chdir(parent)
	def sort(x):
		m=x[5:]
		m=m[:-4]
		m,n=m.split("_")
		m=int(m)
		return m
	#framediff=sorted(framediff,key=sort)
	#print framediff
		
	if("posture" in dirs1):
		directory='./posture'
		os.chdir(directory)
		posture=glob.glob('*.jpg')
		
		if(len(posture)<50):
			for filename in posture:
				#print filename
		    		#os.unlink(filename)
				os.remove(filename)
		parent=os.path.abspath('..')
		os.chdir(parent)
	else:
		os.mkdir("posture")
	
		
	if(len(posture)>=50):
		result.append(len(posture))
		result.append("This video allready processed" + str(len(framediff)) +" frames generated")
		return result
	else:	
		try:
			root=Toplevel()
			root.title('Posture Extracting')
			root.maxsize(300,100)
			root.geometry("300x100+30+30")
		
			global NoFrame
			NoFrame=len(framediff)-1
			point =NoFrame/100
			increment = NoFrame / 20
			title="\n Emotion Detection based on posture analysis\n"+"3 step:posture extraction.\n"+""
			var=StringVar()
			var.set(title)
			l=Label(root,textvariable=var,justify=LEFT)#,anchor=NW,justify=LEFT)#,wraplength=398)
			l.pack()
		
			global j,k
			j=0;k=1
			def sort(x):
				m=x[5:]
				m=m[:-4]
				m,n=m.split("_")
				m=int(m)
				return m
			framediff=sorted(framediff,key=sort)
			print framediff
			for i in framediff:
				try:
					if( k % (5 * point) ==0):
						var.set(title+("\r[" + "=" *(k / increment) +"" *((NoFrame-k)/increment) +"]"+str(k / point)+"%"))
						root.update_idletasks()
					k=k+1
					
					if(j>=len(framediff)):
						break
					j=j+1
					l=i.split("_")
					l2=l[1].split(".")
			
					img1="frame_diff/"+i     
					#print img1		
					img11=cv2.imread(img1)
				    	gray = cv2.cvtColor(img11,cv2.COLOR_BGR2GRAY)
				    	contours,hierarchy = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
					  
					for cnt in contours:
						if(len(cnt)>=count):
							cntlist=cnt
							count=len(cnt)
							total+=1

							avg=int((avg+count)/total)
	
					#print (img1,len(cntlist),avg)
					if(len(cntlist)>400):                                                                               
						x,y,w,h = cv2.boundingRect(cntlist)
						x=x-5;
						w=w+10
						y=y-15;
						h=h+20;
						#print x,y,w,h
						roi=img11[y:y+h,x:x+w]

						img2="frame/frame"+l2[0]+".jpg"
						img22 = cv2.imread(img2)
				
						crop_img = img22[y:y+h,x:x+w] #img2[200:400, 100:300] # Crop from x, y, w, h -> 100, 200, 300, 400
						# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
						#cv2.imshow("cropped", crop_img)
			
						cv2.rectangle(img11,(x,y),(x+w,y+h),(200,0,0),2)
						

			
						gray1=cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
						edge = cv2.Canny(gray1,100,120)
						contours1,hierarchy = cv2.findContours(edge,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
						for cnt1 in contours1:
							if(len(cnt1)>count1):
								cntlist1=cnt1
								count1=len(cnt1)
						x1,y1,w1,h1 = cv2.boundingRect(cntlist1)
						#print x1,y1,w1,h1
				
						ret,thresh1 = cv2.threshold(edge,127,255,cv2.THRESH_BINARY)
						roi=thresh1[y1:y1+h1,x1:x1+w1]
						cv2.rectangle(edge,(x1,y1),(x1+w1,y1+h1),(0,0,0),2)
						#cv2.imshow("posture",thresh1)
						print "--------posture:"+"posture/frame"+str(l2[0])+ '.jpg'
						cv2.imwrite("posture/frame"+str(l2[0])+ '.jpg',roi)
					
						k = cv2.waitKey(20)
						if k == 27:
							break
			
				except Exception as e:
					continue
				
			directory='./posture'
			os.chdir(directory)
			files=glob.glob('*.jpg')
			parent=os.path.abspath('..')
			os.chdir(parent)
			result.append(len(framediff))
			result.append(str(len(files))+" Defferent frames generated out of "+str(len(framediff)))
				
		
			#root.mainloop()
			root.destroy()
			#cv2.destroyWindow("posture")
			return result
		except Exception:
			pass

		
		
#path="/home/ordellugo/Desktop/out.mp4"
#print posture(path)
