#!/usr/bin/python2
# ECE 2524 Final Project - Tetris

import random

class Shape:
	_layout = { \
	'O':{ \
	1:[[0,0,0,0],[0,2,2,0],[0,2,2,0],[0,0,0,0]], \
	2:[[0,0,0,0],[0,2,2,0],[0,2,2,0],[0,0,0,0]], \
	3:[[0,0,0,0],[0,2,2,0],[0,2,2,0],[0,0,0,0]], \
	4:[[0,0,0,0],[0,2,2,0],[0,2,2,0],[0,0,0,0]] \
	}, \
	'I':{ \
	1:[[0,0,0,0],[2,2,2,2],[0,0,0,0],[0,0,0,0]], \
	2:[[0,0,2,0],[0,0,2,0],[0,0,2,0],[0,0,2,0]], \
	3:[[0,0,0,0],[2,2,2,2],[0,0,0,0],[0,0,0,0]], \
	4:[[0,0,2,0],[0,0,2,0],[0,0,2,0],[0,0,2,0]] \
	}, \
	'S':{ \
	1:[[0,0,0,0],[0,0,2,2],[0,2,2,0],[0,0,0,0]], \
	2:[[0,0,2,0],[0,0,2,2],[0,0,0,2],[0,0,0,0]], \
	3:[[0,0,0,0],[0,0,2,2],[0,2,2,0],[0,0,0,0]], \
	4:[[0,0,2,0],[0,0,2,2],[0,0,0,2],[0,0,0,0]] \
	}, \
	'Z':{ \
	1:[[0,0,0,0],[0,2,2,0],[0,0,2,2],[0,0,0,0]], \
	2:[[0,0,0,2],[0,0,2,2],[0,0,2,0],[0,0,0,0]], \
	3:[[0,0,0,0],[0,2,2,0],[0,0,2,2],[0,0,0,0]], \
	4:[[0,0,0,2],[0,0,2,2],[0,0,2,0],[0,0,0,0]] \
	}, \
	'L':{ \
	1:[[0,0,0,0],[0,2,2,2],[0,2,0,0],[0,0,0,0]], \
	2:[[0,0,2,0],[0,0,2,0],[0,0,2,2],[0,0,0,0]], \
	3:[[0,0,0,2],[0,2,2,2],[0,0,0,0],[0,0,0,0]], \
	4:[[0,2,2,0],[0,0,2,0],[0,0,2,0],[0,0,0,0]] \
	}, \
	'J':{ \
	1:[[0,0,0,0],[0,2,2,2],[0,0,0,2],[0,0,0,0]], \
	2:[[0,0,2,2],[0,0,2,0],[0,0,2,0],[0,0,0,0]], \
	3:[[0,2,0,0],[0,2,2,2],[0,0,0,0],[0,0,0,0]], \
	4:[[0,0,2,0],[0,0,2,0],[0,2,2,0],[0,0,0,0]] \
	}, \
	'T':{ \
	1:[[0,0,0,0],[0,2,2,2],[0,0,2,0],[0,0,0,0]], \
	2:[[0,0,2,0],[0,0,2,2],[0,0,2,0],[0,0,0,0]], \
	3:[[0,0,2,0],[0,2,2,2],[0,0,0,0],[0,0,0,0]], \
	4:[[0,0,2,0],[0,2,2,0],[0,0,2,0],[0,0,0,0]] \
	}}
	
	def __init__(self):
		self.selectType()
		# initialize piece position
		if self._type=='I' and (self._orient==2 or self._orient==4):
			self._position_row = -2
			self._position_col = 6
		else:
			self._position_row = -1
			self._position_col = 6
		
	def getType(self):
		return self._type
		
	def selectType(self):
		type_dict = {1:'Z', 2:'S', 3:'L', 4:'I', 5:'O', 6:'J', 7:'T'}
		type_int = random.randint(1,7)
		self._type = type_dict[type_int]
		self._orient = random.randint(1,4)
	
	def getRow(self):
		return self._position_row
		
	def getCol(self):
		return self._position_col
	
	def moveUp(self):
		self._position_row = self._position_row - 1
	
	def moveDown(self):
		self._position_row = self._position_row + 1
		
	def moveRight(self):
		self._position_col = self._position_col + 1
		
	def moveLeft(self):
		self._position_col = self._position_col - 1
		
	def moveTo(self, newRow, newCol):
		if isinstance(newRow, int) and isinstance(newCol, int):
			self._position_row = newRow
			self._position_col = newCol
	
	def rotateCW(self):
		self._orient = self._orient - 1
		if self._orient == 0:
			self._orient = 4
	
	def rotateCC(self):
		self._orient = self._orient + 1
		if self._orient == 5:
			self._orient = 1
			
	def getLayout(self):
		return self._layout[self._type][self._orient]
			

		
