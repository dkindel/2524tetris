#!/usr/bin/python2
# ece2524 final prokect - Tetris
# controller class 

import Shape
import Matrix
from Tkinter import *

class Application(Frame):
	_Matrix = Matrix.Matrix()
	_Shapes = []
	_row = 15
	_col = 10
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.boardHeight = 600
		self.boardWidth = 400
		self.sqSize = 25
		print("In init")
		master.minsize(height = self.boardHeight+5, width = self.boardWidth+5)
		master.maxsize(height = self.boardHeight+5, width = self.boardWidth+5)
		master.title("Tetris!")
		self.pack()
		self.initDraw()
		self._CurShape = Shape.Shape()
		self.board.delete("all")
		for row in range(self._row):
			for col in range(self._col):
				x1 = col*self.sqSize
				y1 = row*self.sqSize
				x2 = x1+self.sqSize
				y2 = y1 + self.sqSize
				self.board.create_rectangle(x1,y1,x2,y2, fill='orange')

		self.board.pack()
		self._job = self.after(2000, self.moveDown, 1)
	def initDraw(self):
		self.board = Canvas(self, bg = 'gray', height = self.boardHeight, width = self.boardWidth, bd = 0)
		self.scoreBox = Text(self, height=1)
		self.scoreBox.insert(INSERT, "Score: " + str(0))
		self.scoreBox.pack(side = BOTTOM)
		self.board.pack()
	def moveDown(self, timer):
		print("moving down")
		grid = self._CurShape.getLayout()
		row = self._CurShape.getRow()
		col = self._CurShape.getCol()
		for y in range(row - 1, row + 3):
			for x in range(col - 2, col + 2):
				if grid[y - (row - 1)][x - (col - 2)] == 2:
					self._Matrix.setValue(y, x, 0)
		self._CurShape.moveDown()
		grid = self._CurShape.getLayout()
		row = self._CurShape.getRow()
		col = self._CurShape.getCol()
		setDone = 0
		#since the refrence point in Shape is at 2,2 on a 0 based grid, we set that to be 0,0. The for loops go through each box in the 4X4 grid
		for y in range(row - 1, row + 3):
			for x in range(col - 2, col + 2):
#since grid is 0 based, we simply do some math. then check if the current coordinate has a 2 in it.
				if grid[y - (row - 1)][x - (col - 2)] == 2:
#if there is a 2 that means that peace will be moved, this next if statement checks if the value below our block is a stationary block or if the block is on the last block in the game field. If either is true, the block can not continue
					if (self._Matrix.getValue(y + 1, x) == 1) or y == 14:
						setDone = 1
#Next two clear the old blocks and update to the new postion
					self._Matrix.setValue(y, x, 1)
#If setDone is true, add the shape to a list so it can not be easily motified and call for a new piece to be generated in its spot
		if setDone == 1:
			self._Shapes.append(self._CurShape)
			self.addNextShape()
		self._job = self.after(2000, self.moveDown, 1)
		self.reDraw()
	def reDraw(self):
		self.board.delete("all")
		for row in range(self._row):
			for col in range(self._col):
				x1 = col*self.sqSize
				y1 = row *self.sqSize
				x2 = x1 + self.sqSize
				y2 = y1 + self.sqSize
				if(self._Matrix.getValue(row, col) == 1):
					self.board.create_rectangle(x1,y1,x2,y2, fill = 'blue')
				else:
					self.board.create_rectangle(x1,y1,x2,y2, fill='orange')
	def addNextShape(self):
		self._CurShape = Shape.Shape()
root = Tk()
app = Application(master = root)
app.mainloop()	
										