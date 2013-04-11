#!/usr/bin/python2
# ECE 2524 Final project - Tetris
#Names can be I, L, T, S, 

class Shape:
	def __init__(self, Name, Grid):
		self.Name = Name, self.Grid = Grid
		self.Rotation = 1, self.OldGrid = Grid
	def setRotate(self, Grid):
		self.OldGrid = self.Grid
		self.Rotation += 1
		if (self.Rotation > 4):
			self.Rotation = 1
		self.Grid = Grid
	def getGrid(self):
		return self.Grid
	def undoRotation(self):
		self.Grid = self.OldGrid
		return self.Grid
	def getName(self):
		return self.Name
	def getRotate(self):
		return self.Rotation

	
