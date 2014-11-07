# -*- coding: utf-8 -*-

from __future__ import division
from libPoint import Point3D_C


class Grille:

	
	def __init__(self,w,h,points):
		'''
		w*h == len(points) avec w>0 et h>0
		'''
		self.points= points
		self.width = w
		self.heigth = h

	def __getitem__(self,i,j):
		return points[i+w*j]



if __name__ == "__main__":
	listPoints = [Point3D_C(i,i,i) for i in range(0,10) ]
	print listPoints



