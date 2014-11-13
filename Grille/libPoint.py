# -*- coding: utf-8 -*-

from __future__ import division
import math as m
class Point3D_C(object):

	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z
 
	def __neg__(self):
		return Point3D_C(-self.x,-self.y,-self.z)
 
	def __repr__(self):
		return '('+str(self.x)+','+str(self.y)+","+str(self.z)+')'
		
	def __mul__(self,val):
		if type(val) is int or type(val) is float :
			return Point3D_C(self.x*val,self.y*val,self.z*val)
		else:
			raise NotImplementedError
			
	def __rmul__(self,val):
		return self.__mul__(val)
			
	def __div__(self,val):
		if type(val) is int or type(val) is float :
			return Point3D_C(self.x//val,self.y//val,self.z//val)
		else:
			raise NotImplementedError

	def __truediv__(self,val):
		if type(val) is int or type(val) is float :
			return Point3D_C(self.x/val,self.y/val,self.z/val)
		else:
			raise NotImplementedError

			
	def __add__(self,val):
		if type(val) is Point3D_C :
			return Point3D_C(self.x+val.x,self.y+val.y,self.z+val.z)
		else:
			raise TypeError
			
 
	def __sub__(self,val):
		if type(val) is Point3D_C :
			return Point3D_C(self.x-val.x,self.y-val.y,self.z-val.z)
		else:
			raise TypeError

	def norme(self):
		return m.sqrt(self.x**2+self.y**2+self.z**2)

	
	def milieu(self,p):
		return Point3D_C((self.x+p.x)/2,(self.y+p.y)/2,(self.z+p.z)/2)
 
 	def toVertex(self):
 		return str(self.x) + " " + str(self.y) + " " + str(self.z)
	# def vecteur(self,p):
		# return Vecteur(p.x-self.x,p.y-self.y)
 
	# def distance(self,p):
		# return self.vecteur(p).norme()
