# -*- coding: utf-8 -*-

from __future__ import division
import random
from math import *
from libPoint import Point_C


def processDecomp(point1,point2,point3,point4):
	""" retourne la moyenne est l'erreur """
	x = (-point1+point2*3+point3*3-point4)*(1/4)
	y = (point1-point2*3+point3*3-point4)*(1/4)
	return x,y
	
def decomposition(lPoint):
	"""lPoint de longueur puissance de 2
	"""
	l = len(lPoint)
	nbI = l/2
	x = list()
	y =list()
	i = 0
	while i<nbI:
		m,e = processDecomp(lPoint[(2*i-2)%l],lPoint[(2*i-1)%l],lPoint[(2*i)%l],lPoint[(2*i+1)%l])
		x.append(m)
		y.append(e)
		i+=1
	
	return x,y

def allDecomposition(lPoint):
	"""lPoint de longueur puissance 2"""
	x = lPoint
	y = list()
	
	while len(x)>2 :
		x,y2 = decomposition(x)
		y = y + y2
	return x,y

data = list()
for i in range(0,2**3):
	data.append(Point_C(i,i))

x,y = allDecomposition(data)
print("{} ||| {}".format(x,y))

def processRecon(m1,m2,e1,e2):
	x1 = (m1+e1)*3/4 + (x2-e2)*1/4
	x2 = (m1+e1)*1/4 + (x2-e2)*3/4
	return x1,x2
	
def reconstruction(m,e):
	nbI = len(m)*2
	i = 0
	res = list()
	while i < nbI:
		
		i+=1



