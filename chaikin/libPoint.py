# -*- coding: utf-8 -*-

from __future__ import division

class Point_C(object):
	'''
	rage
	'''
	def __init__(self,x,y):
		self.x=x
		self.y=y
 
	def __neg__(self):
		return Point_C(-self.x,-self.y)
 
	def __repr__(self):
		return '('+str(self.x)+';'+str(self.y)+')'
		
	def __mul__(self,val):
		if type(val) is int or type(val) is float :
			return Point_C(self.x*val,self.y*val)
		else:
			raise NotImplementedError
			
	def __rmul__(self,val):
		return self.__mul__(val)
			
	def __div__(self,val):
		if type(val) is int or type(val) is float :
			return Point_C(self.x//val,self.y//val)
		else:
			raise NotImplementedError
	def __truediv__(self,val):
		if type(val) is int or type(val) is float :
			return Point_C(self.x/val,self.y/val)
		else:
			raise NotImplementedError

			
	def __add__(self,val):
		if type(val) is Point_C :
			return Point_C(self.x+val.x,self.y+val.y)
		else:
			raise TypeError
			
 
	def __sub__(self,val):
		if type(val) is Point_C :
			return Point_C(self.x-val.x,self.y-val.y)
		else:
			raise TypeError

	
	def milieu(self,p):
		return Point((self.x+p.x)/2,(self.y+p.y)/2)
 
	def vecteur(self,p):
		return Vecteur(p.x-self.x,p.y-self.y)
 
	def distance(self,p):
		return self.vecteur(p).norme()
