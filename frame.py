import cv2
import os
import glob
from time import sleep
from Tkinter import *
import sys

#class frame(Frame):

#	def __init__(self, master,time, path):
#		Frame.__init__(self, master)

def frame(time,path):
	print "------------creating frmaes-----------------"
	global Aframe
	Aframe=time * 29
	Aframe+=1

	split1=path.split("/");
	lenght=len(split1)
	split2=split1[lenght-1].split(".")

	global chpath,chpath1,files,frame
	chpath="";chpath1="";files=[];frame=[]

	global fgbg,smooth,smoothresult#,frame
	smooth=[];smoothresult=[];
	fgbg = cv2.BackgroundSubtractorMOG()


	for i in range(1,lenght-1):
		att="/"+split1[i]
		chpath=chpath + att
		#print(chpath)

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
	if("frame" in dirs1):
		directory='./frame'
		os.chdir(directory)
		files=glob.glob('*.jpg')
		#print len(files),type(files)
		parent=os.path.abspath('..')
		os.chdir(parent)

		if(len(files)<100):
			for filename in files:
				os.remove("./frame/"+filename)
				try:
					os.remove("./frame_smooth/"+filename)
				except Exception as e:
					pass
	
		
	else:
		os.mkdir("frame")
		os.mkdir("frame_smooth")
	

	if(len(files)>=100):
		frame.append(len(files))
		frame.append(" frames allready generated ")
		return frame
	else:	
		try:
			vid=cv2.VideoCapture(path)
			success,image=vid.read()
	
			#root=Tk()
			root=Toplevel()
			root.title('Video to frame conversion process')
			root.maxsize(300,100)
			root.geometry("300x100+30+30")

			global total,fp
			total=Aframe
			point =total/100
			increment = total / 20
			Label(root,textvariable="hi this",justify=LEFT).pack()
			title="\n Emotion Detection based on posture analysis\n"+"step 1: frame generation process\n"
			var=StringVar()
			var.set(title)
			l=Label(root,textvariable=var,justify=LEFT)#,anchor=NW,justify=LEFT)#,wraplength=398)
			l.pack()

	
			for fp in xrange(Aframe):
				try:
					if( fp % (5 * point) ==0):
						var.set(title+("\r[" + "=" *(fp / increment) +"" *((total-fp)/increment) +"]"+str(fp / point)+"%"))
						root.update_idletasks()

					success,image=vid.read()
					cv2.imwrite("frame/frame%d.jpg" % fp,image)	
					fgmask=fgbg.apply(image)
					median=cv2.medianBlur(fgmask,5)
					#cv2.imshow("frame",median)
					print "frame%d"%fp
					cv2.imwrite("frame_smooth/frame%d.jpg" % fp ,median)
					k = cv2.waitKey(1)
					if k == 2:
						break
						
				except Exception :
					continue
	
			directory='./frame'
			os.chdir(directory)
			files=glob.glob('*.jpg')
			print len(files),type(files)
			parent=os.path.abspath('..')
			os.chdir(parent)
			frame.append(len(files))
			frame.append(" frames allready generated ")
		
			root.destroy()
			#root.mainloop()
			
			#cv2.destroyWindow("frame")
			print "step 1 : finished"
			return frame
	
		except Exception :
			pass 	

#path="/home/ordellugo/Desktop/out.mp4"
#size=90
#print frame(size,path)
