from sklearn import svm
import data_wrangler 
import haar
import numpy as np
import random
"""
U7 (6) 1-5 is bad 
"""

__author__      = "Sammy Sidhu"
__copyright__   = "BSD license"


PARTITION = 4200
REAL_TRAIN = True 

def train():
	global PARTITION
	print "Importing data"
	dataset = data_wrangler.extract_data()
	print "done importing data"
	haar_dataset = []
	for i in range(1,9):
		print "Haar transform of Gesture: " + str(i)
		for j in range(len(dataset[i])):
			if (len(dataset[i][j].shape) == 1):
				continue
			datapoint = [haar.haar_transform(dataset[i][j][k]) for k in range(3)]
			datapoint = np.concatenate(datapoint)
			if (sum(datapoint) != 0):
				haar_dataset.append([datapoint,i])
	random.shuffle(haar_dataset)
	if REAL_TRAIN:
		PARTITION = len(haar_dataset)
	train_data = map(lambda x: x[0], haar_dataset)
	train_labels = map(lambda x: x[1], haar_dataset)

	print "Done Transforms! Now Training"
	gest_classifier = svm.SVC(C=8,kernel='rbf', gamma=0.5)
	gest_classifier.fit(train_data[:PARTITION],train_labels[:PARTITION])
 	print "Done Training! Ready!"
 	if not REAL_TRAIN:
		count_right = 0
		print "Starting Validation"

		for i in range(PARTITION,len(train_labels)):
			if gest_classifier.predict(train_data[i])[0] == train_labels[i]:
				count_right += 1
		print "Accuracy : " + str((count_right+0.0)/(len(train_labels)- PARTITION))

	def predict(x,y,z):
		datapoint = [haar.haar_transform(var) for var in [x,y,z]]
		datapoint = np.concatenate(datapoint)
		return gest_classifier.predict(datapoint)[0]

	return predict


if __name__ == "__main__":
	train()