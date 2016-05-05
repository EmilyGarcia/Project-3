from tkinter import *
import requests
import json
from functools import partial

###################################################################################################################################
##############################################           FUNCTIONS           ######################################################
###################################################################################################################################



"""
def b1Callback( job ):
	result = makeRequest
	partial(openDescription( job ))
def b2Callback( job ):
	partial(openDescription( job ))
def b3Callback( job ):
	partial(openDescription( job ))
def b4Callback( job ):
	partial(openDescription( job ))
def b5Callback( job ):
	partial(openDescription( job ))
"""
def openDescription( job ):
	#tkinter.messagebox.showinfo(job['title'], job['description'])
	descWindow = Tk()
	jobDesc = job['description']
	msg = Message(descWindow, text= jobDesc)
	msg.config(bg='lightgray', font=('times', 12))
	msg.pack()
def makeRequest( entry ):
	# gets city location entered
	city = entry.get()
	
	# makes request
	payload = {'location': city}
	ourRequest = requests.get('http://jobs.github.com/positions.json?', params=payload)
	result = ourRequest.json()
	return result
def displayJobs( entry, master ):
	result = makeRequest(entry)
	
	#take first five jobs results
	job1 = result[0]
	job2 = result[1]
	job3 = result[2]
	job4 = result[3]
	job5 = result[4]
	
	# buttons for further info
	desc1 = partial(openDescription,job1)
	b1 = Button(master, command= desc1, text= job1['title'], width= 40)
	b1.grid(row=4, column=0, sticky=W, pady=4)
	
	desc2 = partial(openDescription,job2)
	b2 = Button(master, command= desc2, text= job2['title'], width= 40)
	b2.grid(row=5, column=0, sticky=W, pady=4)
	
	desc3 = partial(openDescription,job3)
	b3 = Button(master, text= job3['title'], command= desc3, width= 40)
	b3.grid(row=6, column=0, sticky=W, pady=4)
	
	desc4 = partial(openDescription,job4)
	b4 = Button(master, text= job4['title'], command= desc4, width= 40)
	b4.grid(row=7, column=0, sticky=W, pady=4)
	
	desc5 = partial(openDescription,job5)
	b5 = Button(master, text= job5['title'], command= desc5, width= 40)
	b5.grid(row=8, column=0, sticky=W, pady=4)
