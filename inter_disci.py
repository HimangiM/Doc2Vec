import os
import glob
from shutil import copyfile

files = os.listdir("./doc_embedding_64_5/")
txt_files = filter(lambda x: x[-4:] == '.txt', files)
txt_files = glob.glob("./doc_embedding_64_5/*.txt")
txt_files.sort()

print txt_files

d = dict()

with open("tasks2_times.txt", 'r') as infile:
	infile.readline()
	for line in infile.readlines():
		token = line.strip().split("|")
		label_time = token[2].strip().split(" ")
		# print token[0]
		if token[0].strip() not in d.keys():
			d[token[0].strip()] = []
		l = []
		for i in label_time:
			label = i.strip().split("_")
			if label[0] not in l:
				l.append(label[0])

		if str("./doc_embedding_64_5/" + token[0].strip() + ".txt") in txt_files:
			# print token[0]
			print token[0], l
			if len(l) == 1:
				print "disci"
				copyfile("./doc_embedding_64_5/" + token[0].strip() + ".txt", "./disciplinary/" + token[0].strip() + ".txt")
			else:
				print "inter"
				copyfile("./doc_embedding_64_5/" + token[0].strip() + ".txt", "./inter-disciplinary/" + token[0].strip() + ".txt")
