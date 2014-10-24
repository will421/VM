# -*- coding: utf-8 -*-

from graphics import *
from libPoint import Point_C
from multiprocessing import Process
import chaikin as ch

import random
import math as m
import os


def randomColor():
	r = random.randrange(256)
	b = random.randrange(256)
	g = random.randrange(256)
	return color_rgb(r,g,b)

def draw(win,data,color='black',width=1):
	oldPt = None
	for elt in data:
		pt = Point(elt.x,elt.y)
		#pt.draw(win)

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


	win1 = GraphWin('ChaikinDecomposition',500,500)

	win1.setCoords(minX,minY,maxX,maxY)


	#Herisson initial
	draw(win1,dataOriginal)

	gen = ch.genDecomposition(dataOriginal)
	

	while True:
		try:
			data,e = gen.next()
			color = randomColor()
			draw(win1,data,color=color)
		except StopIteration:
			break

	win1.getKey()

	
	win2 = GraphWin('ChaikinReconstruction',500,500)
	win2.setCoords(minX,minY,maxX,maxY)

	dataFinal = list(data)
	eFinal = list(e)

	draw(win2,data)
	gen = ch.genReconstruction(data,e)

	while True:
		try:
			data = gen.next()
			color = randomColor()
			draw(win2,data,color=color)
		except StopIteration:
			break
	win2.getKey()


	epsilon = 0.30
	win3 = GraphWin('ChaikinReconstruction'+" epsilon="+str(epsilon),500,500)
	win3.setCoords(minX,minY,maxX,maxY)

	
	newError = [Point_C(0,0) if error.norme()<epsilon else error for error in eFinal]

	draw(win3,dataFinal)




	gen = ch.genReconstruction(dataFinal,newError)

	while True:
		try:
			data = gen.next()
			color = randomColor()
			draw(win3,data,color=color)
		except StopIteration:
			break
	win3.getKey()

	#formule de comparaison : Racine des sommes de la differene au carré des normes

	proc1 = Process(target=ch.errorGraphique,args=(dataOriginal,20,ch.getError))
	proc1.start()
	# ch.errorGraphique(dataOriginal,20,ch.getError)
	

	data_approx,coeffs = ch.allDecomposition(dataOriginal)
	proc2 = Process(target=ch.getHist,args=(coeffs,50))
	proc2.start()


	os.system('pause')
	win1.close()
	win2.close()
	win3.close()
	proc1.terminate()
	proc2.terminate()

	#win.getMouse()


if __name__ == '__main__':
	main(sys.argv[1:])