#!/usr/bin/python
import sys
from libPoint import Point3D_C

def main(argv):
	
	nb_ligne = int (argv [0])
	nb_col = int (argv[1])
	fileNameMaillage = "maillage.txt"
	fileNameObj = "grille.obj"

	genMaillage(fileNameMaillage,nb_col,nb_ligne)
	
	fichier = open(fileNameMaillage, "r")
	pointsLoaded = loadMaillage(fichier)
	fichier.close
	
	generateObj(pointsLoaded,fileNameObj)

	
	

#generatemaillage and return point
def genMaillage(filename,nb_col,nb_ligne):
	
	
	fichier = open(filename, "w")

	fichier.write(str(nb_ligne)+ " " + str(nb_col)+"\n") # print du nombre ligne et colone
	

	
	for i in range(0,nb_col) :
		
		for j in range(0,nb_ligne) :
			 
			fichier.write(str(j+0.0)+','+str(i+0.0)+','+str(0+0.0) + ",\n")
			
			#if j == nb_col-1:
				#fichier.write("\n")
	fichier.close


#Return Data loaded
def loadMaillage(fichier):


	data_points = list()
	
	# stockage des points 
	i=0

	for line in fichier:
		
		if i == 0:

			dim = line.split(" ") 
			nb_line = dim[0]
			nb_col = dim[1]
			i =i+1;
		
		elif i != 0 : 
			pt = line.split(",")
			px = pt[0]
			py = pt[1]
			pz = pt[2].split("\\")
			p = Point3D_C(float(px),float(py),float(pz[0]))
			data_points.append(p)

	return data_points

def generateObj(data,filenameObj):

	fichier = open(filenameObj, "w")

	#ecire des V
	for elt in data:
		fichier.write("v " + elt.toVertex() + "\n")
	fichier.close()
	#ToDO : Write Faces


def generateObjFromMatrix(Matrix,filenameObj):
	fichier = open(filenameObj, "w")
	
	for elt in data:
		fichier.write("v " + elt.toVertex() + "\n")
	fichier.close()	

	for x in range(0, nb_col-1):
    	for y in range(0,nb_ligne-1)
    	fichier.write("f "+ getID(x,y) + getID(x+1,y)  + getID(x+1,y+1)   + getID(x,y+1))  

if __name__ == "__main__":
   main(sys.argv[1:])



