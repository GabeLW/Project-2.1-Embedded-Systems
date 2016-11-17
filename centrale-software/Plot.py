from tkinter import *
import time

class Plot:
    def __init__(self, frameNumber, columnNumber, rowNumber):

        self.canvas = Canvas(frameNumber, width=300, height=300, bg='white')
        self.canvas.grid(column = columnNumber, row = rowNumber)

        self.canvas.create_line(25, 275, 275, 275, width = 1)
        self.canvas.create_line(25, 275, 25, 25, width = 1)

        self.s = 1
        self.x2 = 50
        self.y2 = 300

        # x-axis
        for i in range(11):
            x = 25 + (i * 25)
            self.canvas.create_line(x, 275, x, 25, width = 1, dash = (2, 5))
            self.canvas.create_text(x, 275, text = '%d'% (10 * i), anchor = N)
    
        # y-axis
        for i in range(11):
            y = 275 - (i * 25)
            self.canvas.create_line(25, y, 275, y, width = 1, dash = (2, 5))
            self.canvas.create_text(20, y, text='%d'% (10 * i), anchor=E)

    def step(self, value):
        value = (1 - value/255) * 550 + value/255 * 50
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
