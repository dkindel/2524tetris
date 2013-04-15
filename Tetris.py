#!/usr/bin/python2
# ECE 2524 Final Project - Tetris

from Tkinter import *
from TestMatrix import *
import random

class Application(Frame):
 
  def initDraw(self):
    
    self.board = Canvas(self, bg = 'gray', height = self.boardHeight, width = self.boardWidth, bd = 0)
    self.scoreBox = Text(self, height = 1)
    self.scoreBox.insert(INSERT, "Score: " +  str(0))
    self.scoreBox.pack(side = BOTTOM)
    
    self.redrawBoard()
    self.board.pack()
    
  def __init__(self, master=None):
    root.bind_all('<Left>', self.keyleft)
    root.bind_all('<Right>', self.keyRight)
    root.bind_all('<Up>', self.keyUp)
    root.bind_all('<Down>', self.keyDown)
    root.bind_all('<Escape>', self.keyEscape)
    Frame.__init__(self, master)
    self.boardHeight = 400
    self.boardWidth = 250
    master.minsize(height = self.boardHeight+5, width = self.boardWidth +5)
    master.maxsize(height = self.boardHeight+5, width = self.boardWidth +5)
    self.sqSize = 25
    self.rows = 15
    self.cols = 10
    self.matrixNum = 0
    self.matrix = getNewMatrix(self.matrixNum)
    self.timer = 2000
    
    self.score = 0
    
    initScore()
    master.title("Tetris!")
    self.pack()
    self.initDraw()
    self._job = self.after(self.timer, self.moveDown, 1)
    
    
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
    
  def changeMatrix(self):
    self.matrixNum = (self.matrixNum + 1) % getNumMatrices()
    print self.matrixNum
    self.matrix = getNewMatrix(self.matrixNum)
    self.redrawBoard()
    
    
  def keyleft(self, event):
    print "left"
    
  def keyUp(self, event):
    
    self.changeMatrix()
    newScore = getScore()
    if(self.score != newScore):
      self.updateScore(newScore)
    
  def keyRight(self, event):
    print 'right'
    
  def keyEscape(self, event):
    root.quit()
    
  #timer = 1, called by the timer,
  #timer = 0, called by the key press
  def moveDown(self, timer):
    print "down"
    if not timer:
      self.cancel()
    self._job = self.after(self.timer, self.moveDown, 1)

  def keyDown(self, event):
    self.moveDown(0)
  
  def updateScore(self, score):
    self.score = score
    self.scoreBox.delete(1.0, END)
    self.scoreBox.insert(INSERT, "Score: " +  str(score))
    
  #cancels a current running "after" job
  def cancel(self):
    if self._job is not None:
      root.after_cancel(self._job)
      self._job = None
    
    
root = Tk()
app = Application(master = root)
app.mainloop()
root.destroy()
