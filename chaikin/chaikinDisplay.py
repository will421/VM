# -*- coding: utf-8 -*-

from graphics import *
from libPoint import Point_C



def  main():
	
	data = list()
	
	# stockage des points 
	fichier = open ("herisson.txt",'r')

	for line in fichier:
		pt = line.split(" ") 
		p = Point_C(pt[0],pt[1])
		data.append(p)

	fichier.close

	
	win = GraphWin('Chaikin',500,500)

	for elt in data:
		pt = Point(elt.x,elt.y)
		pt.draw(win)
	
	win.getMouse()
	win.close()

main()