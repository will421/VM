# -*- coding: utf-8 -*-
from __future__ import division
import random
from math import *


class Point(object):
	'''
	rage
	'''
	def __init__(self,x,y):
		self.x=x
		self.y=y
 
	def __neg__(self):
		return Point(-self.x,-self.y)
 
	def __repr__(self):
		return '('+str(self.x)+';'+str(self.y)+')'
		
	def __mul__(self,val):
		if type(val) is int or type(val) is float :
			return Point(self.x*val,self.y*val)
		else:
			raise NotImplementedError
			
 
	def __add__(self,val):
		if type(val) is Point :
			return Point(self.x+val.x,self.y+val.y)
		else:
			raise TypeError
			
 
	def __sub__(self,val):
		if type(val) is Point :
			return Point(self.x-val.x,self.y-val.y)
		else:
			raise TypeError
			
 
 
	def milieu(self,p):
		return Point((self.x+p.x)/2,(self.y+p.y)/2)
 
	def vecteur(self,p):
		return Vecteur(p.x-self.x,p.y-self.y)
 
	def distance(self,p):
		return self.vecteur(p).norme()
		

		
		
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
	data.append(Point(i,i))

x,y = allDecomposition(data)
print("{} ||| {}".format(x,y))

def processRecon(m1,m2,e1,e2):
	x1 = (m1+e1)*3/4 + x2-e2)*1/4
	x2 = (m1+e1)*1/4 + x2-e2)*3/4
	return x1,x2
	
def reconstruction(m,e):
	nbI = len(m)*2
	i = 0
	res = list()
	while i < nbI:
		
		i++

