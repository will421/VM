# -*- coding: utf-8 -*-
from __future__ import division
from math import fabs,sqrt
import math
import sys

import numpy as np
import pylab as P
import random
import Image,ImageTk
import operator
import Tkinter as Tk


n = 10;
N = 2**n;
epsilon = 0.6;
print("N:{}".format(N));

#0 Extraction des données tel qu'image
random.seed(1)
#data = [random.uniform(0,10) for i in range(N)]
#data = range(1,N+1)
data = [math.sin(i) for i in np.linspace(0,np.pi*4,N)]



P.plot(range(0,len(data)),data, marker='o', color='r', ls='')
P.show()
# print("Data: {}".format(data))

#1. Une etape de decomposition
def decomposition(data,OpMoyenne=None,OpCoeff=None):
	"""Renvoie le tableau de moyenne et de coefficients de data
	On considere que data est une puissance de 2
	"""
	moyennes = []
	coeffs = []
	#print(range(0,len(data),2))
	for i in range(0,len(data),2):
		if OpMoyenne :
			moyennes.append(OpMoyenne(data[i],data[i+1]))
		else :
			moyennes.append((data[i]+data[i+1])/2)
		if OpCoeff:
			coeffs.append(OpCoeff(data[i],moyennes[i//2]))
		else :
			coeffs.append(data[i]-moyennes[i//2])
	return moyennes,coeffs
#res = decomposition([1,2,3,4,5,6,7,8])
#print(res)

#1. Une etape de reconstruction
def reconstruction(moyennes,coeffs,OpAdd=None,OpSous=None):
	'''
	Il y a autant de moyennes que de coeffs
	'''
	if len(moyennes)!=len(coeffs):
		raise Exception("Reconstruction {} {}".format(moyennes,coeffs))
	data=[]
	for i,moyenne in enumerate(moyennes):
		if OpAdd:
			data.append(OpAdd(moyenne,coeffs[i]))
		else :
			data.append(moyenne+coeffs[i])
		if OpSous:
			data.append(OpSous(moyenne,coeffs[i]))
		else :
			data.append(moyenne-coeffs[i])
	return data
#a,b = decomposition([1,2,3,4,5,6,7,8])
#res = reconstruction(a,b);
#print(res)


#2.Toutes les etapes de décomposition
def allDecomposition(data,OpMoyenne=None,OpCoeff=None):
	moyennes = data
	coeffs = []
	while len(moyennes)>1 :
		#print(moyennes,coeffs)
		moyennes,coeffs2 = decomposition(moyennes,OpMoyenne=OpMoyenne,OpCoeff=OpCoeff)
		coeffs = coeffs2+coeffs;
	return moyennes[0],coeffs
#res =  allDecomposition(data)
#print(res)
#2.Toutes les étapes de reconstruction
def allReconstruction(moyenne,coeffs,OpAdd=None,OpSous=None):
	localCoeffs = coeffs;
	data = [moyenne]
	while len(localCoeffs)>1:
		data = reconstruction(data,localCoeffs[:len(data)],OpAdd=OpAdd,OpSous=OpSous)
		del localCoeffs[:len(data)//2]
	return data

m,c = allDecomposition(data,verbose=False)
print("-----------")
res = allReconstruction(m,c,verbose=True)


#3.Mettre à 0 les coeff de details d si |d| = epsilon
def cleanCoeff(coeffs,epsilon,defValue=0,OpInf=None):
	''' 
	Retourne un tableau avec remplacement
	des coeffs inferieur à espilon par 0
	'''

	if OpInf:
		return [defValue if OpInf(c,epsilon) else c for c in coeffs]
	else :
		return [defValue if fabs(c)<epsilon else c for c in coeffs]
	
m, c = allDecomposition(data)
newC =  cleanCoeff(c,0.01)


#4.Reconstruire avec les nouveaux coefficients de details => 
#on trouve des approximations des données d'origine

newData = allReconstruction(m,newC)
P.plot(range(0,len(newData)),newData, marker='o', color='r', ls='')
P.show()
# print("NewData: {}".format(newData))

#5 Comparaison du jeu (t) et de l'approximation (s)
#(somme des differences)/n
# RACINE(SOMME((ti-si)^2))
def comparaison1(a,b):
	''' a et b de meme taille
	'''
	res = 0
	for i in range(len(a)):
		res += fabs(a[i]-b[i])
	return res/n

def comparaison2(a,b):
	''' a et b de meme taille
	'''
	res = 0
	for i in range(len(a)):
		res += (a[i]-b[i])**2
	return sqrt(res)
# print("comp1:{}, comp2:{}".format(comparaison1(data,newData),comparaison2(data,newData)))
	
#6 Graphique de l'erreur en fonction d'epsilon
def errorGraphique(data,nEpsilon,errorFunction):
	'''
	errorFunction doit prendre deux tableau 
	et renvoyer un entier
	'''
	epsilonRange = np.linspace(0,max(data),nEpsilon)
	m,c = allDecomposition(data)
	erreur = []
	for e in epsilonRange:
		newC = cleanCoeff(c,e)
		newData = allReconstruction(m,newC)
		erreur.append(errorFunction(data,newData))
	
	P.plot(epsilonRange,erreur)
	P.show()
errorGraphique(data,20,comparaison2);


#7 Histogramme des valeurs absolus des coefficients de details
def coeffHistogramme(coeffs,nGroup):
	P.hist(coeffs, bins=nGroup)
	P.show()

c = [fabs(el) for el in c]
coeffHistogramme(c,50)



## Récupération des valeurs de l'image

moyPixel =lambda data1,data2: tuple(map(lambda a,b:(a+b)//2,data1,data2))
coeffPixel = lambda data,moy: tuple(map(lambda a,b: a-b,data,moy))
addPixel = lambda data,coeff:tuple(map(lambda a,b:a+b,data,coeff))
sousPixel = lambda data,coeff:tuple(map(lambda a,b:a-b,data,coeff))
opInfPixel = lambda data,epsilon: (fabs(data[0])<epsilon or fabs(data[1])<epsilon or fabs(data[2])<epsilon) 
# def imageReconstruction(moyennes,coeffs,saveFileName):

	# data = reconstruction(moyennes,coeffs,addPixel,sousPixel)
	# imNew=Image.new(im.mode ,im.size)  
	# imNew.putdata(data)
	# imNew.save(saveFileName)

 
# imageName = "python_256.jpg"
# saveFileName= "save3.bmp"
# im = Image.open(imageName)

# data = list(im.getdata())
# print("data: {}".format(data))
# m,c = allDecomposition(data,OpMoyenne=moyPixel,OpCoeff=coeffPixel)
# print("C: {}".format(c))
# newC = cleanCoeff(c,0,defValue=(0,0,0),OpInf=opInfPixel)
# print("M: {}".format(m))
# print("newC: {}".format(newC))
# newData = allReconstruction(m,newC,OpAdd=addPixel,OpSous=sousPixel)
# print("newData: {}".format(newData))
# imNew=Image.new(im.mode ,im.size)  
# imNew.putdata(newData)
# imNew.save(saveFileName)

