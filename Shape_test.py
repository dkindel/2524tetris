#!/usr/bin/python2

##### test case for Shape Class ######
import sys
import Shape

def printShape (s):
	print s.getLayout()[0]
	print s.getLayout()[1]
	print s.getLayout()[2]
	print s.getLayout()[3]
	print "row: " + str(s.getRow()) + "   column: " + str(s.getCol())
	return

print '\tr: rotateCW\n\tt: rotateCC\n\tw,s,a,d: movement\n\tn: new shape\n\te: exit'
s = Shape.Shape()
printShape(s)

for key in iter(sys.stdin.readline, ''):
	if key == 'r\n':
		s.rotateCW()
		printShape(s)
	elif key == 't\n':
		s.rotateCC()
		printShape(s)
	elif key == 'w\n':
		s.moveUp()
		printShape(s)
	elif key == 's\n':
		s.moveDown()
		printShape(s)
	elif key == 'a\n':
		s.moveLeft()
		printShape(s)
	elif key == 'd\n':
		s.moveRight()
		printShape(s)
	elif key == 'n\n':
		s.resetShape()
		printShape(s)
	elif key == 'e\n':
		sys.exit(0)
