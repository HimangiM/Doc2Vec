import gensim
from os import listdir
from os.path import isfile, join


class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
        self.labels_list = labels_list
        self.doc_list = doc_list
    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
              yield gensim.models.doc2vec.LabeledSentence(doc,    
[self.labels_list[idx]])


docLabels = []
docLabels = [f for f in listdir("./vocabulary/") if f.endswith(".txt")]
# print docLabels

data = []
for doc in docLabels:
	# print doc
	data.append(open("./vocabulary/" + doc).read())
	# print "\n"
# print data


it = LabeledLineSentence(data, docLabels)

print "Loading Doc2Vec Model....."

model = gensim.models.Doc2Vec(size = 64, window = 10, min_count = 0, alpha = 0.025)

print "Building Vocabulary..."

model.build_vocab(it)

print "Model loading done"

print "Vocabulary size : ", len(model.docvecs)

# for epoch in range(100):
# 	print 'iteration ' + str(epoch+1)
# 	model.train(it, total_examples = 1000, epochs = model.iter)
# 	model.alpha -= 0.002
# 	model.min_alpha = model.alpha
# 	model.train(it)

for i in zip(it, model.docvecs):
	name = str(i[0][1])
	print name[2:-2]
	f = open(name[2:-2], 'w')
	# print i[1]
	for j in i[1]:
		print str(j) + " "
		f.write(str(str(j) + " "))
	f.close()





