import numpy as np
import csv
import cv2
import cv
import math
import decimal
import re
#from pie_demo import *
import sys
import cv2
import numpy as np
import os
import csv
import glob
#import labeling as lb
#from label_f import *
from write_frame import *

class Final:
	def __init__(self):
		self.happy_f_g=0.0
		self.angry_f_g=0.0
		self.sup_f_g=0.0
		self.sad_f_g=0.0
		#self.pe = open(path+"/_emotion.txt","w")
	def getResult(self):
		result=[self.happy_f_g,self.angry_f_g,self.sup_f_g,self.sad_f_g]
		return result

	def final1(self,l):
	
	
		
		""" extraction using vector value"""
		fearful=['0.05','0.02','0.03','0.04','0.06','0.07','0.54','0.53','0.69','0.33','0.27','0.45','0.41','0.20','0.33','0.38','0.44','0.77','0.32']
		happy=['0.33','0.54','0.27','0.29','0.66','0.64','0.44','0.55','0.27','0.41','0.40','0.25','0.37','0.07','0.01','0.10','0.92','0.08','0.88','0.98','0.91','0.94','0.95','0.13','0.09','0.99','0.14','0.12','0.11','0.28','0.30']
		joyful=['0.54','0,45','0.58','0.55','0.44','0.38','0.56','0.43','0.47']
		upset=['0.29','0.25','0.55','0.33','0.20','0.38','0.4','0.28','0.21','0.22','0.23','0.26','0.24','0.50','0.52']
		angry=['0.29','0.41','0.58','0.45','0.66','0.35','0.33','0.25','0.34','0.67','0.65']
		surprised=['0.59','0.29','0.33','0.58','0.35','0.45','0.77','0.79','0.38','0.25','0.63','0.66','0.37','0.61','0.36','0.86','0.87','0.82','0.57','0.83','0.68']
		depressed=['0.37','0.70','0.58','0.71','0.72','0.5','0.60','0.68','0.67','0.25','0.55','0.51','0.33','0.32','0.44','0.74','0.71','0.','0.75','0.76','0.72','0.73','0.78','0.55','0.38','0.45','0.54','0.27','0.62','0.16','0.15','0.19','0.46','0.48','0.39']
		sad=['0.45','0.44','0.20','0.41','0.17','0.19','0.42','0.18',]
		listing=[]
		for i in l:
			a=float(i)
			listing.append("{0:.2f}".format(round(a,2)))
		print len(listing)
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
		#fear=re.search(r'(0*\.0[0-9]+|0*\.5[0-9]+)')
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
		print fear+joy+happy+upset+angry+suprise+depress+sad+love
		happy=happy+joy+love
		anger=upset+angry+depress
		sad=sad+fear
		print "Happy :",happy
		print "anger :",anger
		print "sad :",sad
		print "suprise :",suprise
		self.happy_f_g+=happy
		self.angry_f_g+=anger
		self.sup_f_g+=suprise
		self.sad_f_g+=sad
		frame_emotion =max([happy,anger,suprise,sad])
		#return ([happy,anger,suprise,sad])
		"""if frame_emotion==happy:
			print "happy"
			#return(":HAPPY\n")
		elif frame_emotion==angry:
			print "Angry"
			#return(":ANGER\n")
		elif frame_emotion==sad:
			print "sad"
			#return(":SAD\n")
		elif frame_emotion==surprise:
			print "surp"
			#return(":SURPRISE\n")
		"""
		
		
	

#path="/home/ordellugo/Desktop/Test/part3.mp4"
#final(path)
