

from __future__ import division





def processSubdivision(p1,p2):
	res1 = 3/4*p1 + 1/4*p2
	res2 = 1/4*p1 + 3/4*p2
	
	return res1,res2

def subdivisionChaikinOneStep(lPoint):
	res = []
	for i in range(0,len(lPoint)-1):
		a,b = processSubdivision(lPoint[i],lPoint[i+1])
		res.append(a)
		res.append(b)
	return res
