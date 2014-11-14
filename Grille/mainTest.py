# -*- coding: utf-8 -*-

from __future__ import division
from libPoint import Point3D_C
import subdivision as sub
from libGrille import *


if __name__ == "__main__":
	# data = [Point3D_C(i,i,i) for i in range(0,10)]
	# res = sub.subdivisionChaikinOneStep(data)
	# print res
	data = [Point3D_C(i,i,j) for j in range(0,3) for i in range(0,3)]
	simpleG = Grille(3,3,data);
	print simpleG
	# simpleG.subdivisionLine(True)
	# simpleG.subdivisionColumn()
	simpleG.subdivision(False,True)
	print simpleG