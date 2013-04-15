#!/usr/bin/python2
# ECE 2524 Final Project - Tetris

from Tkinter import *
import random

class Application(Frame):

  #//def redraw(self):
    #self.
 
  def initDraw(self):
    matrix2 = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], \
	      [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], \
	      [0,0,0,0,0,0,0,0,0,0],[2,0,0,1,0,1,0,2,0,0],[2,0,0,1,2,1,0,1,1,1],[1,0,1,1,0,1,0,1,0,1],[0,0,0,0,0,0,0,0,0,0]]


    self.board = Canvas(self, bg = 'gray', height = self.boardHeight, width = self.boardWidth, bd = 0)
    self.chcol = Button(self, bg = 'red')
    self.chcol["command"] = self.redrawBoard
    self.chcol["text"] = "Redraw"
    self.chcol.pack(side = BOTTOM)
    
    self.redrawBoard()
    self.board.pack()
    self.board.after(1000, self.changeMatrix, matrix2)
    
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.boardHeight = 600
    self.boardWidth = 400
    master.minsize(height = self.boardHeight+5, width = self.boardWidth +5)
    master.maxsize(height = self.boardHeight+5, width = self.boardWidth +5)
    self.sqSize = 25
    self.rows = 15
    self.cols = 10
    self.matrix = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], \
	      [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], \
	      [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

    master.title("Tetris!")
    self.pack()
    self.initDraw()
    
    
  def redrawBoard(self):
    self.board.delete("all")
    for row in range(self.rows):
      for col in range(self.cols):
	x1 = col*self.sqSize
	y1 = row * self.sqSize
	x2 = x1 + self.sqSize
	y2 = y1 + self.sqSize
	if(self.matrix[row][col] == 2):
	  self.board.create_rectangle(x1,y1,x2,y2, fill= 'green')
	elif(self.matrix[row][col]):
	  self.board.create_rectangle(x1,y1,x2,y2, fill= 'blue')
	else:
	  self.board.create_rectangle(x1,y1,x2,y2, fill= 'orange')
    
  def changeMatrix(self, matrix):
    self.matrix = matrix
    self.redrawBoard
    

root = Tk()
app = Application(master = root)
app.mainloop()
root.destroy()
