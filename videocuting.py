from moviepy.editor import *
import os
import sys
import glob

def videocuting(path):
	global chpath,chpath1,files,video,path3,videocuting
	chpath="";chpath1="";files=[];videocuting=[]
	ext=["3gp","avi"]
	myclip=VideoFileClip(path)
	LenInSec=myclip.duration
	l=(myclip.duration)/60#gets video length

	path1=path.split("/");
	lenght=len(path1)
	path2=path1[lenght-1].split(".")
	video=path1[lenght-1]
	#print video
	ext1=video.split(".")

	for i in range(1,lenght-1):
		att="/"+path1[i]
		chpath=chpath + att
			
	os.chdir(chpath)
	files=glob.glob('*')
	#video="_"+video
	try:
		if("_"+video in files):
			path3=chpath+"/_"+video
			videocuting.append(int(LenInSec))
			videocuting.append(path3)
			return videocuting
	
		elif(ext1[1] in ext):
			if(l>12):
			
				videocuting.append(12*60)
				videocuting.append(path)
				return videocuting
			else:
			
				videocuting.append(int(LenInSec))
				videocuting.append(path)
				return videocuting
		elif(l==12):
			videocuting.append(int(LenInSec))
			videocuting.append(path)
			return videocuting

		elif(l>12):
			part=l/4
			i=1
			myclip1=myclip.subclip((i,0),(i+3,0))
			myclip1.write_videofile("part1.mp4")
			i=i+part-1
			#print(myclip1)
			myclip2=myclip.subclip((i,0),(i+3,0))
			myclip2.write_videofile("part2.mp4")
			i=i+part
			myclip3=myclip.subclip((i,0),(i+3,0))
			myclip3.write_videofile("part3.mp4")
			i=i+part
			myclip4=myclip.subclip((i,0),(i+3,0))
			myclip4.write_videofile("part4.mp4")
			mainclip=concatenate([myclip1,myclip2,myclip3,myclip4])
			video="_"+video
			mainclip.write_videofile(video)
			os.remove("part1.mp4")
			os.remove("part2.mp4")
			os.remove("part3.mp4")
			os.remove("part4.mp4")
			path=chpath+"/"+video
			videocuting.append(int(LenInSec))
			videocuting.append(path)
			return videocuting
		
		else:
			videocuting.append(int(LenInSec))
			videocuting.append(path)
			return videocuting
	except Exception:
		pass
#path="/home/ordellugo/Desktop/out.mp4"
#print videocuting(path)

'''
myclip2=myclip.subclip(_from,_to)
myclip2.write_videofile("o.mp4")'''


