# -*- coding: utf-8 -*-

from __future__ import division
from libPoint import Point3D_C
import subdivision as sub
from libGrille import *


if __name__ == "__main__":
	# data = [Point3D_C(i,i,i) for i in range(0,10)]
	# res = sub.subdivisionChaikinOneStep(data)
	# print res
	data = [Point3D_C(i,j,0) for j in range(0,3) for i in range(0,2)]
	simpleG = Grille(2,3,data);
	print simpleG
	# simpleG.subdivisionLine()
	# simpleG.subdivisionColumn()
	# print "Subdivision done"
	simpleG.subdivision()
	print simpleG