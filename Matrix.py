#!/usr/bin/python2
# ECE 2524 Final Project - Tetris

class Matrix:
	# 15 x 10 int type matrix. int value can be 0, 1 and 2
	_matrix = [ [ 0 for i in range(10) ] for j in range(15) ]
	
	# return the value at the specified location. return -1 if x or y is invalid
	def getValue(self, row, col):
		if isinstance(row,int) and isinstance(col,int) and col >=0 and col <=9 and row>=0 and row<=14:
			return self._matrix[row][col]
		else:
			return -1
	
	# set the value at the specifed location. return a boolean. false if failed.		
	def setValue(self, row, col, value):
		if isinstance(row, int) and isinstance(col, int) and isinstance(value, int) \
		and col >=0 and col <=9 and row>=0 and row<=14 and value >=0 and value <=2:
			self._matrix[row][col] = value
			return True
		else:
			return False
			
	# return the whole matrix
	def getMatrix(self):
		return self._matrix
	
	# replace the entire matrix with the new matrix, return false if newMatrix is not valid	
	def setMatrix(self, newMatrix):
		if not isinstance(newMatrix,list):
			return False
		if len(newMatrix) != 15:
			return False
		for i in range(15):
			if len(newMatrix[i]) != 10:
				return False
			for j in range(10):
				if (not isinstance(newMatrix[i][j], int) ) or newMatrix[i][j] > 2 or newMatrix[i][j] < 0:
					return False
		self._matrix = newMatrix
		return True
	
	# set all 2's to value 1	
	def clear(self):
		for i in range(15):
			for j in range(10):
				self._matrix[i][j] = 0
		return
		
	def removeRow(self, location):
		print "trying to del" + str(location)
		for y in range(location, -1, -1):
			for x in range(10):
				if y == 0:
					self._matrix[y][x] = 0
				else:
					self._matrix[y][x] = self._matrix[y-1][x]
			
