# -*- coding: utf-8 -*-

from __future__ import division
from libPoint import Point3D_C
import subdivision as sub

class Grille:

	
	def __init__(self,w,h,points):
		'''
		w*h == len(points) avec w>0 et h>0
		'''
		self.points= points
		self.width = w #nombre de colonne mais aussi nombre de point d'une ligne
		self.height = h #nombre de ligne mais aussi le nombre de point d'une colonne
		# print points
	def convertTo1D(self,i,j):
		res = i+self.width*j
		# print "self:{},{},{}  convertTo1D({},{}) = {}".format(self.width,self.height,len(self.points),i,j,res)
		return res

	def __getitem__(self,i,j):
		return self.points[self.convertTo1D(i,j)]

	def __setitem__(self,i,j,value):
		self.points[self.convertTo1D(i,j)] = value

	def getLinePoints(self,j):
		for i in range(0,self.width) :
			yield self.__getitem__(i,j)

	def getColumnPoints(self,i):
		for j in range(0,self.height):
			yield self.__getitem__(i,j)


	def __repr__(self):
		res = ""
		for j in range(0,self.height) : #Pour chaque ligne
			for i in range(0,self.width): #Pour chaque element d'une ligne
				res = res +" " + self.__getitem__(i,j).__repr__()
			res = res +"\n"
		return res


	def subdivisionLine(self):
		newData = list()
		for j in range(0,self.height): #parcours des lignes et subdivision
			line = list(self.getLinePoints(j))
			newLine = sub.subdivisionChaikinOneStep(line)
			newData = newData + newLine
		self.width = len(newLine) #On met à jour le nombre de colonne
		self.points = newData

	def subdivisionColumn(self):
		newData = list()
		for i in range(0,self.width): #parcours des colonnes et subdivision
			col = list(self.getColumnPoints(i))
			col = sub.subdivisionChaikinOneStep(col)
			newData = newData + col
		self.height = len(col) #On met à jour le nombre ligne

		newData2 = list() #Besoin d'une inversion pour être dans notre structure de donnée
		# print newData
		for j in range(0,self.height):
			for i in range(0,self.width):
				newData2.append(newData[(i*self.height)+j])
		self.points = newData2

	def subdivision(self):
		self.subdivisionLine()
		self.subdivisionColumn()

if __name__ == "__main__":
	listPoints = [Point3D_C(i,i,i) for i in range(0,10) ]
	print listPoints



