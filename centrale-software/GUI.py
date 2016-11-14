#for Python 2
import tkinter as tk
from tkinter import ttk
#for Python 3
#import tkinter as tk
#from tkinter import ttk
 
import platform

def quit():
    global tkgui
    tkgui.destroy()

def toggleTab(deviceID):
    if(notebook.tab(deviceID, option='state') == 'normal'):
        notebook.tab(deviceID, state='disabled')
    else:
        notebook.tab(deviceID, state='normal')
    
    
#Make a window 
tkgui = tk.Tk()
#set window size
tkgui.geometry('500x300')
#set window title
tkgui.title('Besturingscentrale')

#make label
tkLabelTop = tk.Label(tkgui, text="Hier kan ook nog tekst")
#pack the label
tkLabelTop.pack()

#create a notebook
notebook = ttk.Notebook(tkgui, width=500)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)
notebook.add(frame1, text='Tab 1', sticky='EW')
notebook.add(frame2, text='Tab 2', sticky='EW')
notebook.add(frame3, text='Tab 3', sticky='EW')
notebook.add(frame4, text='Tab 4', sticky='EW')
notebook.add(frame5, text='Tab 5', sticky='EW')
notebook.pack()

tkButtonQuit = tk.Button(
    tkgui,
    text="Quit",
    command=quit)
tkButtonQuit.pack()

tkToggleTab2Button = tk.Button(
    frame1,
    text="enable Tab 2",
    command= lambda: toggleTab(1))
tkToggleTab2Button.pack()
   
tkLabel = tk.Label(frame1, text="Zet tekst hier neer...")
tkLabel.pack()
 
strVersion = "running Python version " + platform.python_version()
tkLabelVersion = tk.Label(frame2, text=strVersion)
tkLabelVersion.pack()
strPlatform = "Platform: " + platform.platform()
tkLabelPlatform = tk.Label(frame2, text=strPlatform)
tkLabelPlatform.pack()
 
tkgui.mainloop()
