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
		self.boardHeight = 400
		self.boardWidth = 250
		self.difficulty = 1600
		self.sqSize = 25
		self.voidmove = 0
		self.score_count = 0
		self.increaseDiff = 1
		print("In init")
		master.minsize(height = self.boardHeight+5, width = self.boardWidth+5)
		master.maxsize(height = self.boardHeight+5, width = self.boardWidth+5)
		master.title("Tetris!")
		self.pack()
		self.menu()
		self._CurShape = Shape.Shape()
		
	
	def bindEvents(self):
		root.bind_all("<Left>", lambda event, arg = -1: self.moveLateral(event, arg))
		root.bind_all("<Right>", lambda event, arg = 1: self.moveLateral(event, arg))
		root.bind_all("<Up>", lambda event, arg = 0: self.moveLateral(event, arg))
		root.bind_all('r', lambda event, arg = 0: self.moveLateral(event, arg))
		root.bind_all('<Down>', self.moveDown)
		#root.bind_all('<Escape>', self.keyEscape)
		self._job = self.after(self.difficulty, self.moveDown, 1)
		
	def initDraw(self):
		print "1"
		self.board = Canvas(self, bg = 'gray', height = self.boardHeight, width = self.boardWidth, bd = 0)
		self.scoreBox = Entry(self)
		self.scoreBox.insert(0, "Score: " + str(self.score_count))
		self.scoreBox.pack(side = BOTTOM)
		for row in range(self._row):
			for col in range(self._col):
				x1 = col*self.sqSize
				y1 = row*self.sqSize
				x2 = x1+self.sqSize
				y2 = y1 + self.sqSize
				self.board.create_rectangle(x1,y1,x2,y2, fill='orange')
		self.board.pack()
	def moveDown(self, timer):
		print("moving down")
		print self.voidmove
		if self.voidmove == 1:
                        self._Shapes.append(self._CurShape)
                        self.turnOver()
			
		if self._job is not None:
			root.after_cancel(self._job)
			self._job = None
		self.removeCurrent()
		self._CurShape.moveDown()
		self.redrawAfter()
		print self.difficulty
#If setDone is true, add the shape to a list so it can not be easily motified and call for a new piece to be generated in its spot
		self._job = self.after(self.difficulty, self.moveDown, 1)

	def moveLateral(self, event, direction):
                print "moving left or right"
		print self.voidmove
		print direction
		self.removeCurrent()
		if direction == 0:
			self._CurShape.rotateCC()
                grid = self._CurShape.getLayout()
                row = self._CurShape.getRow()
                col = self._CurShape.getCol()


                for y in range(row - 1, row + 3):
                        for x in range(col - 2, col + 2):
                                if grid[y - (row - 1)][x - (col - 2)] == 2:
                                        if (self._Matrix.getValue(y, x + direction) == 1 or x + direction < 0 or x + direction >= 10 or y < 0):
						if direction == 0:
							self._CurShape.rotateCW()
						self.redrawAfter()
						return 0
		if direction == 1:
			self._CurShape.moveRight()
		elif direction == -1:
			self._CurShape.moveLeft()
                
		self.redrawAfter()
		
	
	def rotate(self, event):
		print "rotate"
		print self.voidmove
                if not self.voidmove:
                        self.removeCurrent()

		self.removeCurrent()
		self._CurShape.rotateCW()
		grid = self._CurShape.getLayout()
		row = self._CurShape.getRow()
		col = self._CurShape.getCol()
		for y in range(row - 1, row + 3):
			for x in range(col - 2, col + 2):
				if grid[y - (row - 1)][x - (col - 2)] == 2:
					if (self._Matrix.getValue(y, x) == 1 or x < 0 or x >= 10 or y < 0):
						self._CurShape.rotateCC()
						return 0 
		self.redrawAfter()

	#def moveBottom(self):
	def redrawAfter(self):
		print "redrawAfter"
		
		grid = self._CurShape.getLayout()
		row = self._CurShape.getRow()
		col = self._CurShape.getCol()
		self.voidmove = 0
		#since the refrence point in Shape is at 2,2 on a 0 based grid, we set that to be 0,0. The for loops go through each box in the 4X4 grid
		for y in range(row - 1, row + 3):
			for x in range(col - 2, col + 2):
#since grid is 0 based, we simply do some math. then check if the current coordinate has a 2 in it.
				if grid[y - (row - 1)][x - (col - 2)] == 2:
#if there is a 2 that means that peace will be moved, this next if statement checks if the value below our block is a stationary block or if the block is on the last block in the game field. If either is true, the block can not continue
					self._Matrix.setValue(y, x, 1)
					if (self._Matrix.getValue(y + 1, x) == 1) or y == 14:
						self.voidmove = 1

						

#Next two clear the old blocks and update to the new postion
		self.reDraw()
		
	def reDraw(self):
		print "reDraw"
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
	def turnOver(self):
		print "turn over"
		self.voidmove = 0
		self.checkBoardforScore()
		self._CurShape = Shape.Shape()

	def addNextShape(self):
		print "addNextShape"
		self.voidmove = 0
				
		self._CurShape = Shape.Shape()

	def checkBoardforScore(self):
		print "checkBoardforSchore"
		for row in range(self._row):
			col = 0
			while col < self._col and self._Matrix.getValue(row, col) == 1: 
				col = col +1
			if col == self._col and self._Matrix.getValue(row, col-1) == 1:
				self.score(row)


	def score(self, row_score):
		print "\nrow score"
		print row_score
		self.score_count = self.score_count + 10
		for row in range(row_score):
			for col in range(self._col):
				if row_score - row == 0:
					self._Matrix.setValue(0, col, 0)
				else:
					temp = self._Matrix.getValue(row_score - (row+1), col)
					self._Matrix.setValue(row_score - row, col, temp)
		
		self.reDraw()		
		self.updateScoreBox()
		self.updateDifficulty()
		
	def updateDifficulty(self):
		if(self.increaseDiff and self.difficulty > 400):
			self.difficulty = int(self.difficulty*.9)
			if(self.difficulty < 400):
				self.difficulty = 400
		



	def removeCurrent(self):
		print "remove Current"
		grid = self._CurShape.getLayout()
		row = self._CurShape.getRow()
		col = self._CurShape.getCol()
		for y in range(row - 1, row + 3):
			for x in range(col - 2, col + 2):
				if grid[y - (row - 1)][x - (col - 2)] == 2:
					self._Matrix.setValue(y, x, 0)
					
	def updateScoreBox(self):
		print "updating"
		self.scoreBox.delete(0, END)
		self.scoreBox.insert(0, "Score: " + str(self.score_count))
		self.scoreBox.pack(side = BOTTOM)
		
		
	def menu(self):
		self.startGameButton = Button(self, text="Start Game", bg = 'black', fg = 'white', command = self.startGame)
		self.quitButton = Button(self, text = "Quit", bg = 'black', fg = 'white', command = self.quit)
		self.startGameButton.pack()
		self.quitButton.pack()
		
	def startGame(self):
		self.startGameButton.destroy()
		self.quitButton.destroy()
		
		self.regButton = Button(self, text = "Increasing Difficulty", bg = 'black', fg = 'white', command = self.regPlay)
		self.constButton = Button(self, text = "Constant Difficulty", bg = 'black', fg = 'white', command = self.constantPlay)
		self.backToMainButton = Button(self, text = "<< Back", bg = 'black', fg = 'white', command = self.goBackToMain)
		self.regButton.pack()
		self.constButton.pack()
		
	def regPlay(self):
		self.regButton.destroy()
		self.constButton.destroy()
		self.initDraw()
		self.bindEvents()
		
	def constantPlay(self):
		self.regButton.destroy()
		self.constButton.destroy()
		self.easyButton = Button(self, text = "Easy", bg = 'black', fg = 'white', command = self.setEasyDiff)
		self.medButton = Button(self, text = "Medium", bg = 'black', fg = 'white', command = self.setMedDiff)
		self.hardButton = Button(self, text = "Hard", bg = 'black', fg = 'white', command = self.setHardDiff)
		self.backFromSetDiff = Button(self,text = "<< Back", bg = 'black', fg = 'white', command = self.goBackFromConst)
		self.easyButton.pack()
		self.medButton.pack()
		self.hardButton.pack()
		self.backFromSetDiff.pack()
	
	
	def goBackFromConst(self):
		self.easyButton.destroy()
		self.medButton.destroy()
		self.hardButton.destroy()
		self.backFromSetDiff.destroy()
		
		self.regButton = Button(self, text = "Increasing Difficulty", bg = 'black', fg = 'white', command = self.regPlay)
		self.constButton = Button(self, text = "Constant Difficulty", bg = 'black', fg = 'white', command = self.constantPlay)
		self.backToMainButton = Button(self, text = "<< Back", bg = 'black', fg = 'white', command = self.goBackToMain)
		self.regButton.pack()
		self.constButton.pack()
		self.backToMainButton.pack()
		
	def goBackToMain(self):
		self.regButton.destroy()
		self.constButton.destroy()
		self.backToMainButton.destroy()
		self.menu()
		
	def quit(self):
		root.quit()
		
	def setEasyDiff(self):
		self.difficulty = 1600
		self.startConst()
	def setMedDiff(self):
		self.difficulty = 1000
		self.startConst()
	def setHardDiff(self):
		self.difficulty = 400
		self.startConst()
		
	def startConst(self):
		self.easyButton.destroy()
		self.medButton.destroy()
		self.hardButton.destroy()
		self.backFromSetDiff.destroy()
		self.increaseDiff = 0
		self.initDraw()
		self.bindEvents()
		
root = Tk()
app = Application(master = root)
app.mainloop()	
										
