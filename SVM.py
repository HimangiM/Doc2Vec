import pickle
import random
import os
import glob

import numpy as np
from sklearn import svm
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import normalize

def train_svm(data_x,data_y):
	p = np.array(random.sample(range(len(data_x)), len(data_x)))
	data_x = data_x[p]
	data_y = data_y[p]
	skf = StratifiedKFold(n_splits=10)
	skf.get_n_splits(data_x, data_y)
	l_clf = []
	l_macro = []
	l_micro = []
	clf = svm.SVC()
	for train_idx, test_idx in skf.split(data_x, data_y):
		x_train, x_test = data_x[train_idx], data_x[test_idx]
		y_train, y_test = data_y[train_idx], data_y[test_idx]

		clf.fit(x_train, y_train)
		y_pred = clf.predict(x_test)

		print('classifier score')
		print(clf.score(x_test, y_test))
		l_clf.append(clf.score(x_test, y_test))
		# l_macro.append(f1_score(x_test, y_test, average='macro'))
		# l_micro.append(f1_score(x_test, y_test, average='micro'))
		# print("Micro F1-score" + str(f1_score(data_y, y_pred, average='micro')))
		# print("Macro F1-score" + str(f1_score(data_y, y_pred, average='macro')))
	sum = 0
	# f1_micro = 0
	# f1_macro = 0
	for i in l_clf:
		sum = sum + i
	# for i in l_macro:
	#     f1_macro += i
	# for i in l_micro:
	#     f1_micro += i

	print("accuracy=",str(sum / 10.0))
	# print("Macro F1-score=",str(f1_macro/10.0))
	# print("Micro F1-score=", str(f1_micro / 10.0))
	with open('svm_classifier_dump_1.pkl', 'wb') as fid:
		pickle.dump(clf, fid)

def test_svm(test_x,test_y):
	data_x = test_x
	data_y = test_y

	l = np.array(random.sample(range(len(data_x)), len(data_x)))

	data_x = data_x[l]
	data_y = data_y[l]

	with open('svm_classifier_dump_1.pkl', 'rb') as fid:
		svm_loaded = pickle.load(fid)

	y_pred = svm_loaded.predict(data_x)
	print("test acc:")
	print(svm_loaded.score(data_x, data_y))
	print("Micro F1-score=" + str(f1_score(data_y, y_pred, average='micro')))
	print("Macro F1-score=" + str(f1_score(data_y, y_pred, average='macro')))
	print("F1-score=" + str(f1_score(data_y, y_pred, average='binary')))
	print("confusion matrix = ")
	print(confusion_matrix(data_y, y_pred))


def generate_train_test_data():

	files = os.listdir("./disciplinary/")
	txt_files = filter(lambda x: x[-4:] == '.txt', files)
	txt_files = glob.glob("./disciplinary/*.txt")
	txt_files.sort()

	# print txt_files

	disp_data_x = np.empty((0,64))
	disp_data_y = np.empty((0))


	for i in txt_files:
		with open(i, 'r') as infile:
			for line in infile.readlines():
				rep = np.array([float(k) for k in line.strip().split(" ")])
				disp_data_x = np.append(disp_data_x, np.reshape(rep, (1,64)), axis = 0)
				disp_data_y = np.append(disp_data_y, np.array([0]), axis = 0)
			# print len(rep)

	train_idx = int(disp_data_x.shape[0] * 0.7)  # train=5628, test=2412
	disp_train_x, disp_train_y = disp_data_x[:train_idx], disp_data_y[:train_idx]
	disp_test_x, disp_test_y = disp_data_x[train_idx:], disp_data_y[train_idx:]

	print(disp_train_x.shape)
	print(disp_train_y.shape)
	print(disp_test_x.shape)
	print(disp_test_y.shape)
	# print disp_data_x

	files2 = os.listdir("./inter-disciplinary/")
	txt_files2 = filter(lambda x: x[-4:] == '.txt', files)
	txt_files2 = glob.glob("./inter-disciplinary/*.txt")
	txt_files2.sort()

	interdisp_data_x = np.empty((0,64))
	interdisp_data_y = np.empty((0))

	for i in txt_files2:
		with open(i, 'r') as infile:
			for line in infile.readlines():
				rep = np.array([float(k) for k in line.strip().split(" ")])
				interdisp_data_x = np.append(interdisp_data_x, np.reshape(rep, (1,64)), axis = 0)
				interdisp_data_y = np.append(interdisp_data_y, np.array([1]), axis = 0)
			# print len(rep)

	train_idx = int(interdisp_data_x.shape[0] * 0.7)  # train=5628, test=2412
	interdisp_train_x, interdisp_train_y = interdisp_data_x[:train_idx], interdisp_data_y[:train_idx]
	interdisp_test_x, interdisp_test_y = interdisp_data_x[train_idx:], interdisp_data_y[train_idx:]

	print(interdisp_train_x.shape)
	print(interdisp_train_y.shape)
	print(interdisp_test_x.shape)
	print(interdisp_test_y.shape)

	train_x = np.append(disp_train_x,interdisp_train_x,axis=0) # total train = 10780
	train_y = np.append(disp_train_y,interdisp_train_y,axis=0)

	test_x = np.append(disp_test_x, interdisp_test_x,axis=0) # total test=4620
	test_y = np.append(disp_test_y, interdisp_test_y,axis=0)

	print(train_x.shape)
	print(train_y.shape)
	print(test_x.shape)
	print(test_y.shape)

	np.savetxt("dblp_train_spacetimeemb.txt",train_x)
	np.savetxt("dblp_train_spacetimeemb_labels.txt", train_y)

	np.savetxt("dblp_test_spacetimeemb.txt", test_x)
	np.savetxt("dblp_test_spacetimeemb_labels.txt", test_y)

if __name__=='__main__':

	# generate_train_test_data()
	train_x = np.loadtxt("dblp_train_spacetimeemb.txt")
	train_y = np.loadtxt("dblp_train_spacetimeemb_labels.txt")
	# normalized_train_x = normalize(train_x)
	train_svm(train_x, train_y)

	test_x = np.loadtxt("dblp_test_spacetimeemb.txt")
	test_y = np.loadtxt("dblp_test_spacetimeemb_labels.txt")
	# # normalized_test_x = normalize(test_x)
	test_svm(test_x, test_y)

