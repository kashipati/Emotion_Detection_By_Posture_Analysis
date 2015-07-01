# A more realistic GUI programming example
import Tkinter
from Tkinter import *
from Dialog import Dialog
from FileDialog import LoadFileDialog
from ScrolledText import ScrolledText
from tkFileDialog import askopenfilename
import sys

import videocutting as cut
import frame as image
#from frame_smooth import *
import frame_diff as diff
import posture as post 
import vector as vect 
import labeling as label1
#import final as fnl

class FilenameEntry(Frame):
	global f,path,filename
	f=["mp4","py","3gp","avi","txt"]
	def __init__(self, master, text):
		Frame.__init__(self, master)
		Label(self, text=text).pack(side=LEFT)
		self.filename = StringVar()
		Entry(self, textvariable=self.filename,width=47).pack(side=LEFT, fill=X)
		Button(self, text="Browse...", command=self.browse,width=15).pack(side=RIGHT)

	def browse(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		file = askopenfilename() # show an "Open" dialog box and return the path to the selected file
		#print(file)
		#file = LoadFileDialog(self).go(pattern='*')
		#if file:
		#	self.filename.set(file)
		split1=file.split("/");
		lenght=len(split1)
		split2=split1[lenght-1].split(".")
		if(split2[1] in f):
			if file:
				self.filename.set(file)
			
		else:
			FormatNotFound(self, split1[lenght-1])	
		

	def get(self):
		return self.filename.get()

class ButtonBar(Frame):

	def __init__(self, master, left_button_list, right_button_list):
		Frame.__init__(self, master, bd=2, relief=SUNKEN)
		for button, action in left_button_list:
			Button(self, text=button, command=action,width=15).pack(side=LEFT)
		for button, action in right_button_list:
			Button(self, text=button, command=action,width=15).pack(side=RIGHT)

class FileNotFoundMessage(Dialog):
	def __init__(self, master, filename):
		Dialog.__init__(self, master, title = 'File not found',
			text = 'File ' + filename + ' does not exist',
			bitmap = 'warning', default = 0,
			strings = ('Cancel',))

class FormatNotFound(Dialog):
	def __init__(self, master, filename):
		Dialog.__init__(self, master, title = 'File Format change',
			text = 'File ' + filename + 'Not Video Format',
			bitmap = 'warning', default = 0,
			strings = ('Cancel',))

class FileNotSelected(Dialog):
	def __init__(self, master):
		Dialog.__init__(self, master, title = 'File not Selected',
			text = 'File not seletecd',
			bitmap = 'warning', default = 0,
			strings = ('Cancel',))

class TextWindow(Frame):

	def __init__(self, master, text):
		Frame.__init__(self, master)
		text_field = ScrolledText(self)
		text_field.insert(At(0,0), text)
		text_field.pack(side=TOP)
		text_field.config(state=DISABLED)
		ButtonBar(self, [],
			[('Close', self.master.destroy)]).pack(side=BOTTOM, fill=X)

class FormatNotFound(Dialog):

	def __init__(self, master, filename):
		Dialog.__init__(self, master, title = 'File Format change',
			text = 'File ' + filename + 'Not Video Format',
			bitmap = 'warning', default = 0,
			strings = ('Cancel',))


class MainWindow(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.grid()
		self.maxsize(600,400)#Welcome to Emotion Detection Based on Posture Analysis
		self.geometry("600x400+30+30")#Emotion detection of cohort through

		Label(self, text="\nEMOTION DETECTION AND ANALYSIS OF COHORT TUTOR \nTHROUGH GEUSTER AND POSTURE ANALYSIS IN A CLASSROOM CONTEXT.\n").pack(side=TOP)
		ButtonBar(self, [],
			[('Help', self.help),('About', self.about)]).pack(fill=X)

		self.filename_field = FilenameEntry(self, "Filename: ")
		self.filename_field.pack( fill=X)

		self.filename_field.place(y =320)		
	
		ButtonBar(self, [('Process', self.process)],
			[('Quit', self.quit)]).pack(side=BOTTOM, fill=X)
	
	def about(self):
		text = open("./about.txt").read()
		new_window = Toplevel()
		new_window.title("About")
		TextWindow(new_window, "\n\n"+text).pack()
	
	def help(self):
		text = open("./help.txt").read()
		new_window = Toplevel()
		new_window.title("Help")
		TextWindow(new_window, text).pack()
		
	def process(self):
		filename = self.filename_field.get()
		if(filename==""):
			FileNotSelected(self)
		else:
			try:	
				text0=cut.videocuting(filename)
				size=int(text0[0])
				text1=image.frame(size,text0[1])
				text=text0[1]
				text2=diff.frame_diff(text0[1])
				text=text+"\n"+text2[1]
				text3=post.posture(text0[1])
				text=text+"\n"+text3[1]
				vect.vector(text0[1])
				#vect.destroy()
				label1.read_file(text0[1])
				label1.result(text0[1])
				label1.write_frame(text0[1])
				label1.plot(text0[1])
				sys.exit()
				#fnl.final(text0[1])
				#print(text3)
				#text = open(filename).read()
				self.filename.set("")
			except IOError:
				FileNotFoundMessage(self, filename)
			#else:
				#new_window = Toplevel()
				#new_window.title(filename)
				#TextWindow(new_window, text).pack()
				#TextWindow(new_window, text1).pack()
				#TextWindow(new_window, text2).pack()
				
		
	def lpr(self):
		filename = self.filename_field.get()
		import os
		os.system('lpr ' + '"' + filename + '"')

if __name__ == "__main__":
    app = MainWindow(None)
    app.title('Emotion Detection')
    app.mainloop()
