import numpy as np
import os

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

