# -*- coding: utf-8 -*-

from __future__ import division
import random
from math import *
from libPoint import Point_C

def processDecomp(point1,point2,point3,point4):
	""" retourne la moyenne est l'erreur """
	x = (1/4)*(-point1+3*point2+3*point3-point4)
	y = (1/4)*(point1-3*point2+3*point3-point4)
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

def processRecon(m1,m2,e1,e2):
	x1 = (m1+e1)*3/4 + (m2-e2)*1/4
	x2 = (m1+e1)*1/4 + (m2-e2)*3/4
	return x1,x2
	
def reconstruction(m,e):
	l = len(m)
	nbI = l
	i = 0
	res = list()
	while i < nbI:
		x1,x2 = processRecon(m[i%l],m[(i+1)%l],e[i%l],e[(i+1)%l])
		res.append(x1)
		res.append(x2)
		i+=1
	return res

	
def allDecomposition(lPoint,verbose=False):
	"""lPoint de longueur puissance 2"""
	if verbose:
		print("Decomposition:")
	
	x = lPoint
	y = list()
	
	if verbose:
		print("{} || {}".format(x,y))
	while len(x)>4 :
		x,y2 = decomposition(x)
		y = y2 + y
		if verbose:
			print("{} || {}".format(x,y))
	return x,y
	
def allReconstruction(m,e,verbose=False):
	if verbose:
		print("Reconstruction:")
	error = e
	moy = list(m)
	
	if verbose:
		print("{} || {}".format(moy,error))
	while len(error)>1 :
		oldL = len(moy)
		moy = reconstruction(moy,error[:len(moy)])
		del error[:oldL]
		if verbose:
			print("{} || {}".format(moy,error))
	return moy

def genDecomposition(lPoint):
	"""lPoint de longueur puissance 2"""
	x = lPoint
	y = list()
	
	while len(x)>4 :
		x,y2 = decomposition(x)
		y = y2 + y
		yield x,y

def genReconstruction(m,e):
	error = e
	moy = list(m)
	
	while len(error)>1 :
		oldL = len(moy)
		moy = reconstruction(moy,error[:len(moy)])
		del error[:oldL]
		yield moy


# data = list()
# for i in range(0,2**3):
# 	data.append(Point_C(i,i))
	
	
# x,y = allDecomposition(data,verbose=False)
# print("-----------")
# res = allReconstruction(x,y,verbose=True)

# gen = genDecomposition(data)


# while True:
# 	try:
# 		print gen.next()
# 	except StopIteration:
# 		break

# gen = genReconstruction(x,y)
# while True:
# 	try:
# 		print gen.next()
# 	except StopIteration:
# 		break


