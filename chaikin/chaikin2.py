# -*- coding: utf-8 -*-

<<<<<<< HEAD
from graphics import *


class Point_C:
=======
import random
from math import *

class Point:
>>>>>>> origin/master
    def __init__(self,x,y):
        self.x=x
        self.y=y
 
<<<<<<< HEAD
    def __repr__(self):
=======
    def affichage(self):
>>>>>>> origin/master
        return '('+str(self.x)+';'+str(self.y)+')'
 
    def milieu(self,p):
        return Point((self.x+p.x)/2,(self.y+p.y)/2)
 
    def vecteur(self,p):
        return Vecteur(p.x-self.x,p.y-self.y)
 
    def distance(self,p):
        return self.vecteur(p).norme()
<<<<<<< HEAD



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

=======
		
>>>>>>> origin/master

