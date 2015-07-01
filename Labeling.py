import numpy as np
import csv
import cv2
import cv
import math
import decimal
from pylab import *
import re

import os
import glob


global happy_f_g,angry_f_g,sup_f_g,sad_f_g,f_result,frame_list
f_result=[];frame_list=[]

def write_frame(path):
	print "writing emotions to the frames"
	directory=path.split("/");
	lenght=len(directory)
	split2=directory[lenght-1].split(".")
	
	directory1=path.split(".");

		
	global chpath,chpath1
	chpath="";chpath1=""

	for i in range(1,lenght-1):
		att="/"+directory[i]
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
	print(dirs1)
	"""if("frame_emotion" in dirs1):
		os.chdir("./frame_emotion")
		diff=glob.glob('*.jpg')
		frame=len(diff)
		parent=os.path.abspath('..')
		os.chdir(parent)
	"""
	if("frame_emotion" in dirs1):
		directory='./frame_emotion'
		os.chdir(directory)
		framediff=glob.glob('*.jpg')
		
		if(len(framediff)<50):
			for filename in framediff:
				os.remove(filename)
		parent=os.path.abspath('..')
		os.chdir(parent)
	else:
		os.mkdir("frame_emotion")	


	
	emo_dir=chpath1+'/frame_Emotion'
	#os.mkdir(emo_dir)
	print frame_list
	for i in frame_list:
		file_name,emotion=i.split(":")
		print file_name+":"+emotion
		img=cv2.imread(chpath1+'/posture/'+file_name)
		
		cv2.putText(img, emotion, (0, 250),cv2.FONT_HERSHEY_SIMPLEX, 1.0,(255,255,255))
		#print flag
		#cv2.imshow("ouput",img)
	#	if flag:
		#print "success "
		s=emo_dir+"/"+file_name
		#print s
		cv2.imwrite(s,img)
		
		
		

def plot(path):
	try:	
		print "-----------ploting pie chart------------------"
		directory=path.split("/");
		lenght=len(directory)
		split2=directory[lenght-1].split(".")
	
		directory1=path.split(".");

		
		global chpath,chpath1
		chpath="";chpath1=""

		for i in range(1,lenght-1):
			att="/"+directory[i]
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

	
		w1=chpath1+"/"+split2[0]+"_emotion.txt"
		print w1
		print "all frames completeed"
	
		r = open(w1,"r")
		plot1=r.read()
		#print plot1
		e_list=plot1.split("\n")
		#print e_list
		emotion=e_list[0]
		values=e_list[1]
		emotion=emotion.split(",")
		values=values.split(",")
		#print emotion, values
		values=[float(x) for x in values]
		r.close()

		#print "ploting results"
		figure(1, figsize=(10,10))
		ax = axes([0.1, 0.1, 0.8, 0.8])
		# The slices will be ordered and plotted counter-clockwise.
		labels = emotion
		fracs = values
		explode=(0.1, 0.15, 0.2, 0.1)
		pie(fracs, labels=labels,autopct='%1.1f%%', shadow=True, colors=('b', 'r', 'y','c'),startangle=90,explode=explode)
	
		        # The default startangle is 0, which would start
		        # the Frogs slice on the x-axis.  With startangle=90,
		        # everything is rotated counter-clockwise by 90 degrees,
		        # so the plotting starts on the positive y-axis.
		title('Overall Emotions', bbox={'facecolor':'0.8', 'pad':5})
		show()
		
		
	except Exception :
		pass

def read_file(path):

	try:
		global happy_f_g,angry_f_g,sup_f_g,sad_f_g,f_result,frame_list
		f_result=[];frame_list=[]
	
		angry_f_g=0;happy_f_g=0
		sup_f_g=0
		sad_f_g=0

		directory=path.split("/");
		lenght=len(directory)
		split2=directory[lenght-1].split(".")
		
		directory1=path.split(".");

			
		global chpath,chpath1
		chpath="";chpath1=""
	
		for i in range(1,lenght-1):
			att="/"+directory[i]
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
	
		text=chpath1+"/"+split2[0]+".txt"
		f=open(text,"r")
		data=f.read()
		data_list=data.split("\n")
		#print "len of data list",len(data_list)
		
		global e
		e=0
		for data_line in data_list:
			e+=1
	
			file_name,file_data=data_line.split(":")
			data_list=file_data.split(",")
			data_list=data_list[:-1]
			print file_name
			
			
	
	
		
			""" extraction using vector value"""
			fearful=['0.05','0.02','0.03','0.04','0.06','0.07','0.54','0.53','0.69','0.33','0.27','0.45','0.41','0.20','0.33','0.38','0.44','0.77','0.32']
			happy=['0.33','0.54','0.27','0.29','0.66','0.64','0.44','0.55','0.27','0.41','0.40','0.25','0.37','0.07','0.01','0.10','0.92','0.08','0.88','0.98','0.91','0.94','0.95','0.13','0.09','0.99','0.14','0.12','0.11','0.28','0.30']
			joyful=['0.54','0,45','0.58','0.55','0.44','0.38','0.56','0.43','0.47']
			upset=['0.29','0.25','0.55','0.33','0.20','0.38','0.4','0.28','0.21','0.22','0.23','0.26','0.24','0.50','0.52']
			angry=['0.29','0.41','0.58','0.45','0.66','0.35','0.33','0.25','0.34','0.67','0.65']
			surprised=['0.59','0.29','0.33','0.58','0.35','0.45','0.77','0.79','0.38','0.25','0.63','0.66','0.37','0.61','0.36','0.86','0.87','0.82','0.57','0.83','0.68']
			depressed=['0.37','0.70','0.58','0.71','0.72','0.5','0.60','0.68','0.67','0.25','0.55','0.51','0.33','0.32','0.44','0.74','0.71','0.','0.75','0.76','0.72','0.73','0.78','0.55','0.38','0.45','0.54','0.27','0.62','0.16','0.15','0.19','0.46','0.48','0.39']
			sad=['0.45','0.44','0.20','0.41','0.17','0.19','0.42','0.18']
			listing=[]
			for i in data_list:
				a=float(i)
				listing.append("{0:.2f}".format(round(a,2)))
			#print len(listing)
			countf=0
			f=[]
			h=[]
			j=[]
			u=[]
			a=[]
			su=[]
			d=[]
			s=[]
			o=[]
			countf=0
			counth=0
			countj=0
			countu=0
			counta=0
			countsu=0
			countd=0
			counts=0
			counto=0
			
			for i in listing:
				fear=re.search(r'(0*\.0[0-9]+|0*\.5[0-9]+)',i)
				if i in fearful:# or fear :
					f.append(i)
					countf+=1
				elif i in happy:
					h.append(i)
					counth+=1
				elif i in joyful:
					j.append(i)
					countj+=1
				elif i in upset:
					u.append(i)
					countu+=1
				elif i in angry:
					a.append(i)
					counta+=1
				elif i in surprised:
					su.append(i)
					countsu+=1
				elif i in depressed:
					d.append(i)
					countd+=1
				elif i in sad:
					s.append(i)
					counts+=1
				else:
					o.append(i)
					counto+=1
		
			
			print "fearful:",len(f) 
			print "joyful:", len(j)
			print "happy: ", len(h)
			print "upset:",len(u)
			print "angry:", len(a)
			print "suprised:", len(su)
			print "depressed:", len(d)
			print "sad:" ,len(s)
			print "love:", len(o)
		
	
			fear=(countf/float(len(listing)))*100.0
			joy=(countj/float(len(listing)))*100.0
			happy=(counth/float(len(listing)))*100.0
			upset=(countu/float(len(listing)))*100.0
			angry=(counta/float(len(listing)))*100.0
			suprise=(countsu/float(len(listing)))*100.0
			depress=(countd/float(len(listing)))*100.0
			sad=(counts/float(len(listing)))*100.0
			love=(counto/float(len(listing)))*100.0
			#print fear+joy+happy+upset+angry+suprise+depress+sad+love
			happy=happy+joy+love
			anger=upset+angry+depress
			sad=sad+fear
			print "Happy :",happy
			print "anger :",anger
			print "sad :",sad
			print "suprise :",suprise
			
			m=max(happy,anger,sad,suprise)
			if m == happy:
				frame_list.append(file_name+":HAPPY")	
				
			elif m == anger:	
				frame_list.append(file_name+":ANGER")
			
			elif m == sad:
				frame_list.append(file_name+":SAD")

			elif m == suprise:
				frame_list.append(file_name+":SUPRISE")
			
			happy_f_g+=happy
			angry_f_g+=anger
			sup_f_g+=suprise
			sad_f_g+=sad
							
			print ""
			print ""

		
	except Exception:
		pass



def result(path):
	print '--------calculating results-----------'
	directory=path.split("/");
	lenght=len(directory)
	split2=directory[lenght-1].split(".")
	
	directory1=path.split(".");

		
	global chpath,chpath1
	chpath="";chpath1=""

	for i in range(1,lenght-1):
		att="/"+directory[i]
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

	
	w=chpath1+"/"+split2[0]+"_emotion.txt"
	#print w
	#print "all frames completeed"
	
	r = open(w,"w")
	r.write("happy,angry,suprised,sad\n")
	r.write(str(happy_f_g)+","+str(angry_f_g)+","+str(sup_f_g)+","+str(sad_f_g)+"\n")
	r.close()

#path="/home/ordellugo/Desktop/kashi2.3gp"
#read_file(path)

#result(path)
#print frame_dict
#write_frame(path)
#plot(path)
	
