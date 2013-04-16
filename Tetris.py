#!/usr/bin/python2
# ECE 2524 Final Project - Tetris

from Tkinter import *
from TestMatrix import *
import random

class Application(Frame):
 
  def initDraw(self):
    #initialize the board and the score text box
    self.board = Canvas(self, bg = 'gray', height = self.boardHeight, width = self.boardWidth, bd = 0)
    self.scoreBox = Text(self, height = 1)
    self.scoreBox.insert(INSERT, "Score: " +  str(0))
    self.scoreBox.pack(side = BOTTOM)
    
    self.redrawBoard()
    self.board.pack()
    
  #sets variables to be used
  def __init__(self, master=None):
    # bind all key presses
    root.bind_all('<Left>', self.keyleft)
    root.bind_all('<Right>', self.keyRight)
    root.bind_all('<Up>', self.keyUp)
    root.bind_all('<Down>', self.keyDown)
    root.bind_all('<Escape>', self.keyEscape)
    #call init on frame
    Frame.__init__(self, master)
    #sets the board height
    self.boardHeight = 400
    self.boardWidth = 250
    #make not resizeable
    master.minsize(height = self.boardHeight+5, width = self.boardWidth +5)
    master.maxsize(height = self.boardHeight+5, width = self.boardWidth +5)
    #set grid sizes
    self.sqSize = 25
    self.rows = 15
    self.cols = 10
    
    self.timer = 2000
    self.score = 0
    initScore()
    
    #sets temp matrix code for now.
    #will be updated by getting an init matrix
    self.matrixNum = 0
    self.matrix = getNewMatrix(self.matrixNum)
    
    master.title("Tetris!")
    self.pack()
    self.initDraw()
    
    #set timer to move piece down
    self._job = self.after(self.timer, self.moveDown, 1)
    
  
  def redrawBoard(self):
    #resets info in the board
    self.board.delete("all")
    
    #loops through each square in the matrix and display the color for each rectangle
    #corresponding to each number in the matrix
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
    
  #gets a new matrix to display
  def changeMatrix(self):
    #test code to get a new matrix - loops through matrices listed in "TestMatrix"
    self.matrixNum = (self.matrixNum + 1) % getNumMatrices()
    self.matrix = getNewMatrix(self.matrixNum)
    self.redrawBoard()
    
  #respond to left keypress
  def keyleft(self, event):
    print "left"
    
  #respond to up keypress
  def keyUp(self, event):
    self.changeMatrix()
    newScore = getScore()
    #only update if the score has changed
    if(self.score != newScore):
      self.updateScore(newScore)
    
  #respond to right keypress
  def keyRight(self, event):
    print 'right'
    
  #quits when given escape keypress
  def keyEscape(self, event):
    root.quit()
    
  #respond to down keypress
  def keyDown(self, event):
    self.moveDown(0)
    
  #timer = 1, called by the timer,
  #timer = 0, called by the key press
  def moveDown(self, timer):
    print "down"
    #if the key is pressed, we reset the timer to 0 again
    if not timer:
      self.cancel()
    self._job = self.after(self.timer, self.moveDown, 1)

  #updates the score using information provided by score
  def updateScore(self, score):
    self.score = score
    self.scoreBox.delete(1.0, END)
    self.scoreBox.insert(INSERT, "Score: " +  str(score))
    
  #cancels a current running "after" job
  def cancel(self):
    if self._job is not None:
      root.after_cancel(self._job)
      self._job = None
    
    
#build the app and run the mainloop until it's finished
root = Tk()
app = Application(master = root)
app.mainloop()
root.destroy()
