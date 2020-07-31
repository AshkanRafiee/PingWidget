# -*- coding: utf-8 -*-
#Coded By Ashkan Rafiee https://github.com/AshkanRafiee/PingWidget/
################Libraries################
import PySimpleGUI as sg
import webbrowser
import time
import threading
from pythonping import ping
################Libraries################


status = None
mypings1 = []
mypings2 = []
mypings3 = []
mypings4 = []

################GUI################
sg.theme('DarkGreen5')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('First IP',size=(32,1),pad=(20,1)),sg.Text('Second IP',size=(31,1),pad=(20,1)),sg.Text('Third IP',size=(32,1),pad=(20,1)),sg.Text('Fourth IP',pad=(20,1))],
          [sg.Input(size=(36,1), key='ip1',pad=(20,15)),sg.Input(size=(36,1), key='ip2',pad=(20,15)),sg.Input(size=(36,1), key='ip3',pad=(20,15)),sg.Input(size=(36,1), key='ip4',pad=(20,15))],
          [sg.Listbox(values='',size=(34, 10),pad=(20,1), key='list1'),sg.Listbox(values='',size=(34, 10),pad=(20,1), key='list2'),sg.Listbox(values='',size=(34, 10),pad=(20,1), key='list3'),sg.Listbox(values='',size=(34, 10),pad=(20,1), key='list4')],
          [sg.Button('Website',pad=(170,30),size=(15,3)), sg.Button('Start',pad=(2,30),size=(15,3)), sg.Button('Stop',pad=(5,30),size=(15,3)), sg.Button('Exit',pad=(170,30),size=(15,3))],
          [sg.Text('Made By Ashkan Rafiee')]]
# Create the Window
window = sg.Window('WarpRefer - Get Free Warp Plus Referrals!', layout)
# Event Loop to process "events" and get the "values" of the inputs
################GUI################


def disabler():
	window['ip1'].update(disabled=True)
	window['ip2'].update(disabled=True)
	window['ip3'].update(disabled=True)
	window['ip4'].update(disabled=True)

def enabler():
	window['ip1'].update(disabled=False)
	window['ip2'].update(disabled=False)
	window['ip3'].update(disabled=False)
	window['ip4'].update(disabled=False)

def valueinputer():
	global ip1,ip2,ip3,ip4
	ip1 = str(values['ip1'])
	ip2 = str(values['ip2'])
	ip3 = str(values['ip3'])
	ip4 = str(values['ip4'])

def autopinger1():
	global mypings1
	while status:
		if ip1 == "":
			result = ping("tehran.ir",count=1)
			mypings1.append(result)
			window.Element('list1').Update(values=mypings1)
			time.sleep(1)
		else:
			result = ping(ip1,count=1)
			mypings1.append(result)
			window.Element('list1').Update(values=mypings1)
			time.sleep(1)

def autopinger2():
	global mypings2
	while status:
		if ip2 == "":
			result = ping("192.168.68.1",count=1)
			mypings2.append(result)
			window.Element('list2').Update(values=mypings2)
			time.sleep(1)
		else:
			result = ping(ip2,count=1)
			mypings2.append(result)
			window.Element('list2').Update(values=mypings2)
			time.sleep(1)

def autopinger3():
	global mypings3
	while status:
		if ip3 == "":
			result = ping("4.2.2.4",count=1)
			mypings3.append(result)
			window.Element('list3').Update(values=mypings3)
			time.sleep(1)
		else:
			result = ping(ip3,count=1)
			mypings3.append(result)
			window.Element('list3').Update(values=mypings3)
			time.sleep(1)

def autopinger4():
	global mypings4
	while status:
		if ip4 == "":
			result = ping("8.8.8.8",count=1)
			mypings4.append(result)
			window.Element('list4').Update(values=mypings4)
			time.sleep(1)
		else:
			result = ping(ip4,count=1)
			mypings4.append(result)
			window.Element('list4').Update(values=mypings4)
			time.sleep(1)

def threadhandler():
	threading.Thread(target=autopinger1, daemon=True).start()
	threading.Thread(target=autopinger2, daemon=True).start()
	threading.Thread(target=autopinger3, daemon=True).start()
	threading.Thread(target=autopinger4, daemon=True).start()

while True:
    event, values = window.read()
    if event == 'Start':
    	status = True
    	disabler()
    	valueinputer()
    	threadhandler()
    if event == 'Stop':
    	status = False
    	enabler()
    if event == 'Website':
    	webbrowser.open_new('https://ashkanrafiee.ir/PingWidget')

    if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
        break