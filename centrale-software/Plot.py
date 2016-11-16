from tkinter import *
import time

class Plot:
    def __init__(self):
        
        self.root = Tk()
        self.root.title('Temperatuur')

        self.canvas = Canvas(self.root, width=1200, height=600, bg='white') # 0,0 is top left corner
        self.canvas.pack(expand=YES, fill=BOTH)

        self.canvas.create_line(50,550,1150,550, width=2) # x-axis
        self.canvas.create_line(50,550,50,50, width=2)    # y-axis

        self.s = 1
        self.x2 = 50
        self.y2 = 300

        # x-axis
        for i in range(23):
            x = 50 + (i * 50)
            self.canvas.create_line(x,550,x,50, width=1, dash=(2,5))
            self.canvas.create_text(x,550, text='%d'% (10*i), anchor=N)
    
        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            self.canvas.create_line(50,y,1150,y, width=1, dash=(2,5))
            self.canvas.create_text(40,y, text='%d'% (10*i), anchor=E)

    def step(self, value):
        if self.s == 23:
            # new frame
            self.s = 1
            self.x2 = 50
            self.canvas.delete('temp') # only delete items tagged as temp
        x1 = self.x2
        y1 = self.y2
        self.x2 = 50 + self.s * 50
        self.y2 = value
        self.canvas.create_line(x1, y1, self.x2, self.y2, fill='black', tags='temp')
        self.s += 1

if __name__ == '__main__':
    MyPlot = Plot()
    MyPlot.canvas.after(300, MyPlot.step(250)) # 250 is measurement value
    MyPlot.root.update() # loop these two statements
