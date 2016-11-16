#for Python 3
import tkinter as tk
from tkinter import ttk
import serial
import serial.tools.list_ports
from ctypes import c_uint8
from time import sleep
from Plot import Plot

deviceInfo = {
    'tab1' : {'mode' : 'manual', 'status' : 'up'},
    'tab2' : {'mode' : 'manual', 'status' : 'up'},
    'tab3' : {'mode' : 'manual', 'status' : 'up'},
    'tab4' : {'mode' : 'manual', 'status' : 'up'},
    'tab5' : {'mode' : 'manual', 'status' : 'up'}
    }
connectedDevices = []
amountOfArduinos = 0
ser = 0
    
def checkDevices():
    global connectedDevices
    global amountOfArduinos
    global ser
    
    arduino_ports = [p.device for p in serial.tools.list_ports.comports()
                     if 'Arduino' in p.description
                     ]
    
    if not arduino_ports:
        tkLabelTop['text'] = 'No Arduino found!'
        for x in range(5):
            if (notebook.tab(x, option='state') == 'normal'):
                toggleTab(x)
                connectedDevices[:] = []

    if len(arduino_ports) < amountOfArduinos:
        temp = connectedDevices
        toggleTab(len(arduino_ports))
        [connectedDevices.remove(i) for i in arduino_ports if i in temp]
        amountOfArduinos -= 1
        
    if len(arduino_ports) > amountOfArduinos:
        tkLabelTop['text'] = ''
        for x in range(len(arduino_ports)):
            if not (arduino_ports[x] in connectedDevices):
                toggleTab(x)
                connectedDevices.append(arduino_ports[x])
                amountOfArduinos += 1
                ser = serial.Serial(connectedDevices[0], 9600)

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
    global ser
    if(ser.isOpen() == False):
        ser = serial.Serial(connectedDevices[0], 9600)
    if (deviceInfo[tabName]['status'] == 'up'):
        ser.write(c_uint8(int('0x0b', 16))) #0b = rood lampje aan
        deviceInfo[tabName]['status'] = 'down'
    else:
        ser.write(c_uint8(int('0x0a', 16)))
        deviceInfo[tabName]['status'] = 'up'

def toggleMode(tabName, labelNumber):
    if(DeviceInfo[tabName]['mode'] == 'manual'):
        DeviceInfo[tabName]['mode'] = 'automatic'
        labelNumber['text'] = 'Modus: %s' % (DeviceInfo[tabName]['mode'])
    else:
        DeviceInfo[tabName]['mode'] = 'manual'
        labelNumber['text'] = 'Modus: %s' % (DeviceInfo[tabName]['mode'])

def fillTab(frameNumber, tabName, labelNumber):

    tkToggleScreenButton = tk.Button(
        frameNumber,
        text='Toggle Screen',
        command=lambda: toggleScreen(tabName))
    tkToggleScreenButton.grid(column=0, row=1, sticky='W')

    tkToggleModeButton = tk.Button(
        frameNumber,
        text='Toggle mode',
        command=lambda: toggleMode(tabName, labelNumber))
    tkToggleModeButton.grid(column=0, row=2, sticky='W')

    Graph = Plot(frameNumber, 0, 5)
    Graph2 = Plot(frameNumber, 1, 5)
    
    #tkgui.after(300, Graph.step(90))
    #tkgui.root.update()
    
    labelNumber = tk.Label(frameNumber, text='Modus: %s' % (deviceInfo[tabName]['mode']))
    labelNumber.grid(column=0, row=3, sticky='W')

def gatherData():
    pass
    tkgui.after(2000, gatherData)

#Make a window 
tkgui = tk.Tk()
#set window size
tkgui.geometry('600x500')
#set window title
tkgui.title('Besturingscentrale')

#make label
tkLabelTop = tk.Label(tkgui, text='')
#pack the label
tkLabelTop.pack()

#create a notebook
notebook = ttk.Notebook(tkgui, width=675)
frame1 = ttk.Frame(notebook)
frame1.grid()
frame2 = ttk.Frame(notebook)
frame2.grid()
frame3 = ttk.Frame(notebook)
frame3.grid()
frame4 = ttk.Frame(notebook)
frame4.grid()
frame5 = ttk.Frame(notebook)
frame5.grid()
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
#tkgui.after(2000, gatherData)
tkgui.mainloop()
