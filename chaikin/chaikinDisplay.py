# -*- coding: utf-8 -*-

from graphics import *
from libPoint import Point_C
import chaikin as ch
import random
import math as m


def randomColor():
	r = random.randrange(256)
	b = random.randrange(256)
	g = random.randrange(256)
	return color_rgb(r,g,b)

def draw(win,data,color='black',width=1):
	oldPt = None
	for elt in data:
		pt = Point(elt.x,elt.y)
		pt.draw(win)

		if not oldPt is None :
			line = Line(oldPt,pt)
			line.setOutline(color)
			line.draw(win)

		oldPt = pt
	pt = Point(data[0].x,data[0].y)
	line = Line(oldPt,pt)
	line.setOutline(color)
	line.draw(win)

def main(argv):
	
	file = "crocodile512.d.txt"
	if len(argv)>=1:
		file = argv[0]

	dataOriginal = list()
	
	# stockage des points 
	fichier = open (file,'r')


	for line in fichier:
		pt = line.split(" ") 
		i=0
		while(True):
			try:
				float(pt[i])
				break
			except ValueError:
				i+=1

		i2=i+1
		while(True):
			try:
				float(pt[i2])
				break
			except ValueError:
				i2+=1

		p = Point_C(float(pt[i]),float(pt[i2]))
		dataOriginal.append(p)

	fichier.close
	
	x = list()
	y = list()
	for elt in dataOriginal :
		x.append(elt.x)
		y.append(elt.y)
	minX = min(x)
	minY = min(y)
	maxX = max(x)
	maxY = max(y)


	win = GraphWin('ChaikinDecomposition',500,500)

	win.setCoords(minX,minY,maxX,maxY)


	#Herisson initial
	draw(win,dataOriginal)

	gen = ch.genDecomposition(dataOriginal)
	
	

	while True:
		try:
			data,e = gen.next()
			color = randomColor()
			draw(win,data,color=color)
		except StopIteration:
			break

	# win.getMouse()
	
	win = GraphWin('ChaikinReconstruction',500,500)
	win.setCoords(minX,minY,maxX,maxY)

	dataFinal = list(data)
	eFinal = list(e)

	draw(win,data)

	gen = ch.genReconstruction(data,e)

	while True:
		try:
			data = gen.next()
			color = randomColor()
			draw(win,data,color=color)
		except StopIteration:
			break

	win = GraphWin('ChaikinReconstruction',500,500)
	win.setCoords(minX,minY,maxX,maxY)

	epsilon = 0.30
	newError = [Point_C(0,0) if m.sqrt(error.x**2+error.y**2)<epsilon else error for error in eFinal]

	draw(win,dataFinal)
	gen = ch.genReconstruction(dataFinal,newError)

	while True:
		try:
			data = gen.next()
			color = randomColor()
			draw(win,data,color=color)
		except StopIteration:
			break

	win.getMouse()
	win.close()

if __name__ == '__main__':
	main(main(sys.argv[1:]))