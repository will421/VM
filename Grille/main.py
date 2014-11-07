# -*- coding: utf-8 -*-

from __future__ import division
from libPoint import Point3D_C
import subdivision as sub


if __name__ == "__main__":
	data = [Point3D_C(i,i,i) for i in range(0,10)]
	res = sub.subdivisionChaikinOneStep(data)
	print res