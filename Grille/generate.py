#!/usr/bin/python

import sys

def main(argv):
	nb_ligne = int (argv [0])
	nb_col = int (argv[1])
	#plat = argv[2]

	fichier = open("maillage.txt", "w")
	genMaillage(fichier,nb_col,nb_ligne)
	fichier.close
	

def genMaillage(fichier,nb_col,nb_ligne):
	
	fichier.write(str(nb_ligne)+ " " + str(nb_col)+"\n") # print du nombre ligne et colone
	

	
	for i in range(0,nb_col) :
		
		for j in range(0,nb_ligne) :
			 
			fichier.write(str(j+0.0)+','+str(i+0.0)+','+str(0+0.0) + " \n")
			
			#if j == nb_col-1:
				#fichier.write("\n")

if __name__ == "__main__":
   main(sys.argv[1:])