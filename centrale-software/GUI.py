#for Python 3
import tkinter as tk
from tkinter import ttk
import serial
import serial.tools.list_ports
from ctypes import c_uint8
from time import sleep

DeviceInfo = {
    'tab1' : {'mode' : 'manual', 'status' : 'up'},
    'tab2' : {'mode' : 'manual', 'status' : 'up'},
    'tab3' : {'mode' : 'manual', 'status' : 'up'},
    'tab4' : {'mode' : 'manual', 'status' : 'up'},
    'tab5' : {'mode' : 'manual', 'status' : 'up'}
    }
ConnectedDevices = []
    
arduino_ports = []
def checkDevices():
    
    arduino_ports = [p.device for p in serial.tools.list_ports.comports()
                     if 'Arduino' in p.description
                     ]
    if not arduino_ports:
        tkLabelTop['text'] = 'No Arduino found!'
        for x in range(5):
            if (notebook.tab(x, option='state') == 'normal'):
                toggleTab(x)
                ConnectedDevices[:] = []
    if len(arduino_ports) >= 1:
        tkLabelTop['text'] = ''
        for x in range(len(arduino_ports)):
            if not (arduino_ports[x] in ConnectedDevices):
                toggleTab(x)
                ConnectedDevices.append(arduino_ports[x])
                print(ConnectedDevices)
    tkgui.after(5000, checkDevices)

def quit():
    global tkgui
    tkgui.destroy()

def toggleTab(deviceID):
    if(notebook.tab(deviceID, option='state') == 'normal'):
        notebook.tab(deviceID, state='disabled')
    else:
        notebook.tab(deviceID, state='normal')
        
def toggleScreen(tabName):
    ser = serial.Serial('COM4', 9600)
    sleep(3)
    if (deviceInfo[tabName]['status'] == 'up'):
        ser.write(c_uint8(int(255)))
    else:
        ser.write(c_uint8(int(0)))
        
def createPlot():
    pass

def toggleMode(tabName, labelNumber):
    if(DeviceInfo[tabName]['mode'] == 'manual'):
        DeviceInfo[tabName]['mode'] = 'automatic'
        labelNumber['text'] = DeviceInfo[tabName]['mode']
    else:
        DeviceInfo[tabName]['mode'] = 'manual'
        labelNumber['text'] = DeviceInfo[tabName]['mode']

def fillTab(frameNumber, tabName, labelNumber):
    
    tkToggleTabButton = tk.Button(
        frameNumber,
        text='Toggle tab 2',
        command= lambda: toggleTab(1))
    tkToggleTabButton.grid(column=0,row=0)

    tkToggleScreenButton = tk.Button(
        frameNumber,
        text='Toggle Screen',
        command=lambda: toggleScreen(tabName))
    tkToggleScreenButton.grid(column=0,row=1)

    tkToggleModeButton = tk.Button(
        frameNumber,
        text='Toggle mode',
        command=lambda: toggleMode(tabName, labelNumber))
    tkToggleModeButton.grid(column=0,row=2)
    
    tkModeLabel1 = tk.Label(frameNumber, text='Modus: ')
    tkModeLabel1.grid(column=1,row=2)
   
    labelNumber = tk.Label(frameNumber, text=DeviceInfo['tab1']['mode'])
    labelNumber.grid(column=2,row=2)

#Make a window 
tkgui = tk.Tk()
#set window size
tkgui.geometry('500x330')
#set window title
tkgui.title('Besturingscentrale')

#make label
tkLabelTop = tk.Label(tkgui, text='')
#pack the label
tkLabelTop.pack()

#create a notebook
notebook = ttk.Notebook(tkgui, width=500)
frame1 = ttk.Frame(notebook)
frame1.grid()
frame2 = ttk.Frame(notebook)
frame2.grid()
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)
notebook.add(frame1, text='Tab 1', sticky='EW', state='disabled')
notebook.add(frame2, text='Tab 2', sticky='EW', state='disabled')
notebook.add(frame3, text='Tab 3', sticky='EW', state='disabled')
notebook.add(frame4, text='Tab 4', sticky='EW', state='disabled')
notebook.add(frame5, text='Tab 5', sticky='EW', state='disabled')
notebook.pack()

fillTab(frame1, 'tab1', 'label1')
fillTab(frame2, 'tab2', 'label2')
fillTab(frame3, 'tab3', 'label3')
fillTab(frame4, 'tab4', 'label4')
fillTab(frame5, 'tab5', 'label5')

tkButtonCheckDevices = tk.Button(
    tkgui,
    text='Check for devices',
    command=checkDevices)
tkButtonCheckDevices.pack()

tkButtonQuit = tk.Button(
    tkgui,
    text='Quit',
    command=quit)
tkButtonQuit.pack()

checkDevices()
tkgui.after(3000, checkDevices)
tkgui.mainloop()
