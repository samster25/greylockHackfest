import numpy as np
import os

"""This file is used to extract and format the uWave dataset in the following order
{
	1 : [[[x..],[y..],[z..]] ... ]
	...
	...


	8 : [[[x..],[y..],[z..]] ... ]


}
The key for the return dict is the gesture number as spec'd in the uWave. the value is a list of matrices that each contain a x,y and z
acceleration vector.
"""

__author__      = "Sammy Sidhu"
__copyright__   = "BSD license"

DATA_DIR = "./uWave/"

def extract_data():
	dataset = dict()
	for i in range(1,9):
		dataset[i] = []
	folders = filter(lambda x: "U" in x, os.listdir(DATA_DIR))
	for folder in folders:
		files = filter(lambda x: "Template" in x, os.listdir(DATA_DIR + folder)) 
		for fil in files:
			gesture = int(fil.split("-")[0][-1])
			dataset[gesture].append(np.loadtxt(DATA_DIR + folder + "/" + fil).T)
	return dataset