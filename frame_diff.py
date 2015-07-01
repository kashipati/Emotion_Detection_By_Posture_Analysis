from os import *
import cv2
import cv
import time
import os
import glob
import numpy
from time import sleep
from Tkinter import *
import sys

def frame_diff(path):
	print "------------frame difference-----------"
		
	directory=path.split("/");
	lenght=len(directory)
	
	ext=directory[lenght-1].split(".")
	
	global chpath,chpath1,index,framediff,diffresult,diff_list
	chpath="";chpath1="";framediff=[];diffresult=[];diff_list=[]

	for i in range(1,lenght-1):
		att="/"+directory[i]
		chpath=chpath + att
		
	
	os.chdir(chpath)
	dirs = [d for d in os.listdir('.') if os.path.isdir(os.path.join('.', d))]
	
	if(ext[0] in dirs):
		chpath1=chpath+"/"+ext[0]
		os.chdir(chpath1)
	else:
		os.mkdir(ext[0])
		chpath1=chpath+"/"+ext[0]
		os.chdir(chpath1)	

	dirs1 = [d for d in os.listdir('.') if os.path.isdir(os.path.join('.', d))]
	if("frame_smooth" in dirs1):
		os.chdir("./frame_smooth")
		diff=glob.glob('*.jpg')
		frame=len(diff)
		parent=os.path.abspath('..')
		os.chdir(parent)

	if("frame_diff" in dirs1):
		directory='./frame_diff'
		os.chdir(directory)
		framediff=glob.glob('*.jpg')
		
		if(len(framediff)<500):
			for filename in framediff:
				os.remove(filename)
		parent=os.path.abspath('..')
		os.chdir(parent)
	else:
		os.mkdir("frame_diff")
		
	if(len(framediff)>=500):
		diffresult.append(len(framediff))
		diffresult.append("This video allready processed" + str(len(framediff)) +" frames generated")
		return diffresult
	else:
		try:
			files=[f for f in listdir('frame_smooth')]
			diff_list=[]
			index=0
		
			root=Toplevel()
			root.title('Finding the different frame')
			root.maxsize(300,100)
			root.geometry("300x100+30+30")			

			global total
			total=len(files)-1
			point =total/100
			increment = total / 20
			title="\n Emotion Detection based on posture analysis\n"+"step 2: Finding different posture\n"
			var=StringVar()
			var.set(title)
			l=Label(root,textvariable=var,justify=LEFT)#,anchor=NW,justify=LEFT)#,wraplength=398)
			l.pack()
	
		
			for i in xrange(0,len(files)-1):
				if( i % (5 * point) ==0):
					var.set(title+("\r[" + "=" *(i / increment) +"" *((total-i)/increment) +"]"+str(i / point)+"%"))
					root.update_idletasks()
				try:
					im1="frame_smooth/frame"+str(i)+".jpg"
					im2="frame_smooth/frame"+str(i+1)+".jpg"
				
					img1=cv2.imread(im1)
					img2=cv2.imread(im2)
					if(not(type(img1)=="NoneType" and type(img2)=="NoneType")):
						diff=cv2.absdiff(img1,img2)
						#ret,thresh1 = cv2.threshold(diff,127,255,cv2.THRESH_BINARY)
						#ret,thresh2 = cv2.threshold(thresh1,127,255,cv2.THRESH_TOZERO)
						#print("imaage diff %d:"%diff.sum())
						if(diff.sum()):
							imgw="frame_diff/frame"+str(index)+"_"+str(i+1)+".jpg"
							#cv2.imshow("frame_diff",diff)
							cv2.imwrite(imgw,diff)
							index=index+1
							diff_list.append(i)
						#else:
						#	diff_list.append(i)
					
				except Exception as e:
					continue
		
			directory='./frame_diff'
			os.chdir(directory)
			files=glob.glob('*.jpg')
			parent=os.path.abspath('..')
			os.chdir(parent)
			diffresult.append(len(files))
			diffresult.append(str(len(files))+" Defferent frames generated out of "+str(frame))
	
			root.destroy()
			#root.mainloop()
			#cv2.destroyWindow("frame_diff")
			return diffresult
		except Exception:
			pass
#path="/home/ordellugo/Desktop/out.mp4"

#print frame_diff(path)
