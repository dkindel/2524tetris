# ece2524 final prokect - Tetris
# controller class 

import Shape
import Matrix

class Controller:
	_Matrix = Matrix.Matrix()
	_Shapes = []
	_CurShape

	def __init__(self):
		self._CurShape = Shape.Shape()
	def moveDown(self):
		self._CurShape.moveDown()
		grid = self._CurShape.getLayout()
		row = self._curShape.getRow()
		col = self._curShape.getCol()
		setDone = 0
		#since the refrence point in Shape is at 2,2 on a 0 based grid, we set that to be 0,0. The for loops go through each box in the 4X4 grid
		for y in range(row - 1, row + 2):
			for x in range(col - 2, col + 1):
#since grid is 0 based, we simply do some math. then check if the current coordinate has a 2 in it.
				if grid[y - (row + 1)][x - (col + 2)] == 2
:
#if there is a 2 that means that peace will be moved, this next if statement checks if the value below our block is a stationary block or if the block is on the last block in the game field. If either is true, the block can not continue
					if (self._Matrix.getValue(y + 1, x) == 1) or y == 14:
						setDone = 1
#Next two clear the old blocks and update to the new postion
					self._Matrix.setValue(y - 1, x, 0)
					self._Matrix.setValue(y, x, 1)
#If setDone is true, add the shape to a list so it can not be easily motified and call for a new piece to be generated in its spot
		if setDone == 1:
			self._Shapes.append(self._CurShape)
			addNextShape()
	def addNextShape(self):
		self._CurShape = Shape.Shape()
			
										
