from tkinter import *
import time

class Plot:
    def __init__(self, frameNumber, columnNumber, rowNumber):

        canvas = Canvas(frameNumber, width=300, height=300, bg='white')
        canvas.grid(column = columnNumber, row = rowNumber)

        canvas.create_line(25, 275, 275, 275, width = 1)
        canvas.create_line(25, 275, 25, 25, width = 1)

        self.s = 1
        self.x2 = 50
        self.y2 = 300

        # x-axis
        for i in range(11):
            x = 25 + (i * 25)
            canvas.create_line(x, 275, x, 25, width = 1, dash = (2, 5))
            canvas.create_text(x, 275, text = '%d'% (10 * i), anchor = N)
    
        # y-axis
        for i in range(11):
            y = 275 - (i * 25)
            canvas.create_line(25, y, 275, y, width = 1, dash = (2, 5))
            canvas.create_text(20, y, text='%d'% (10 * i), anchor=E)

    def step(self, value):
        if self.s == 11:
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

#MyPlot = Plot()
#MyPlot.canvas.after(300, MyPlot.step(250)) # 250 is measurement value
#MyPlot.root.update() # loop these two statements
