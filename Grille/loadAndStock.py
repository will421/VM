#!/usr/bin/python
from libPoint import Point3D_C
import sys


def main(argv):

	#file = "crocodile512.d.txt"
	if len(argv)>=1:
		file = argv[0]

	data_points = list()
	
	# stockage des points 
	fichier = open (file,'r')


	int i = 0
	for line in fichier:
		
		if i == 0

			dim = line.split(" ") 
			nb_line = dim[0]
			nb_col = dim[1]
			print nb_line
			print nb_col
			i++
		
		pt = line.split(",")
		px = pt[0]
		py = pt [1]
		pz = pt [2]
		p = Point3D_C(float(px),float(py),float(pz))
		data_points.append(p)

	fichier.close

if __name__ == "__main__":
   main(sys.argv[1:])