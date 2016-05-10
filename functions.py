from Tkinter import *
import Tkinter
import requests
import json
from functools import partial
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
##################################################################################################################################
##############################################           FUNCTIONS          ######################################################
##################################################################################################################################
def parseDesc ( desc ):
	for word in desc:
		finalDesc = finalDesc + word
		"""if (word == "<"):
			finalDesc = finalDesc + (word + 3)
		else:
			finalDesc = finalDesc + word"""
	return finalDesc
def openDescription1( job1 ):
	descWindow1 = Tkinter.Tk()
	descWindow1.title(job1['title'])
	jobDesc1 = job1['description']
	msg1 = Message(descWindow1, text= jobDesc1, font=('times', 12), fg='MediumPurple4', bg='light cyan')
	msg1.pack()
def openDescription2( job2 ):
	descWindow2 = Tkinter.Tk()
	descWindow2.title(job2['title'])
	jobDesc2 = job2['description']
	msg2 = Message(descWindow2, text= jobDesc2, font=('times', 12), fg='MediumPurple4', bg='light cyan', relief = FLAT)
	msg2.pack()
def openDescription3( job3 ):
	descWindow3 = Tkinter.Tk()
	descWindow3.title(job3['title'])
	jobDesc3 = job3['description']
	msg3 = Message(descWindow3, text= jobDesc3, font=('times', 12), fg='MediumPurple4', bg='light cyan', relief = FLAT)
	msg3.pack()
def openDescription4( job4 ):
	descWindow4 = Tkinter.Tk()
	descWindow4.title(job2['title'])
	jobDesc4 = job4['description']
	msg4 = Message(descWindow4, text= jobDesc4, font=('times', 12), fg='MediumPurple4', bg='light cyan', relief = FLAT)
	msg4.pack()
def openDescription5( job5 ):
	descWindow5 = Tkinter.Tk()
	descWindow5.title(job2['title'])
	jobDesc5 = job5['description']
	msg5 = Message(descWindow5, text= jobDesc5, font=('times', 12), fg='MediumPurple4', bg='light cyan', relief = FLAT)
	msg5.pack()
def makeRequest( entry ):
	# Gets city location entered
	city = entry.get()
	
	# Makes request
	payload = {'location': city}
	ourRequest = requests.get('http://jobs.github.com/positions.json?', params=payload)
	result = ourRequest.json()
	return result
def displayJobs( entry, master ):
	result = makeRequest( entry )
	
	# Take first five jobs results
	global job1, job2, job3, job4, job5
	job1 = result[0]
	job2 = result[1]
	job3 = result[2]
	job4 = result[3]
	job5 = result[4]
	
	# Button 1
	desc1 = partial( openDescription1,job1 )
	
	b1 = Button( master, command= desc1, text= job1['title'], width= 40, fg='MediumPurple4', bg='DarkOliveGreen3', relief = FLAT)
	b1.grid( row=4, column=0, sticky=W, pady=4 )
	
	# Button 2
	desc2 = partial( openDescription2,job2 )
	
	b2 = Button( master, command= desc2, text= job2['title'], width= 40, fg='MediumPurple4', bg='DarkOliveGreen3', relief = FLAT )
	b2.grid( row=5, column=0, sticky=W, pady=4 )
	
	# Button 3
	desc3 = partial( openDescription3,job3 )
	
	b3 = Button( master, command= desc3, text= job3['title'], width= 40, fg='MediumPurple4', bg='DarkOliveGreen3', relief = FLAT )
	b3.grid( row=6, column=0, sticky=W, pady=4 )
	
	# Button 4
	desc4 = partial( openDescription4,job4 )
	
	b4 = Button( master, command= desc4, text= job4['title'], width= 40, fg='MediumPurple4', bg='DarkOliveGreen3', relief = FLAT )
	b4.grid( row=7, column=0, sticky=W, pady=4 )
	
	# Button 5
	desc5 = partial( openDescription5,job5 )
	
	b5 = Button( master, command= desc5, text= job5['title'], width= 40, fg='MediumPurple4', bg='DarkOliveGreen3', relief = FLAT )
	b5.grid( row=8, column=0, sticky=W, pady=4 )
"""def getLat():
	
def getLon():
"""	

def mapThat():
	# make sure the value of resolution is a lowercase L,
	#  for 'low', not a numeral 1
	mapp = Basemap(projection='mill', lat_0=36, lon_0=-119,
	    resolution = 'h', area_thresh = .1,
	    llcrnrlon=-130, llcrnrlat=31,
	    urcrnrlon=-109, urcrnrlat=43)
	 
	mapp.drawcoastlines()
	mapp.drawcountries()
	mapp.fillcontinents(color='coral')
	mapp.drawmapboundary()
	mapp.drawstates()
	 
	
	lons = [-120, -119, -110]
	lats = [32, 36, 40]
	x,y = mapp(lons, lats)
	mapp.plot(x, y, 'bo', markersize=10)
	
	labels = [job1['title'], job2['title'], job3['title']]
	for label, xpt, ypt in zip(labels, x, y):
    		plt.text(xpt+30000, ypt+6000, label)
	plt.show()
