from sklearn.cluster import DBSCAN, KMeans
from sklearn.metrics import silhouette_score
import random
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import os
import glob
from sklearn.metrics.cluster import completeness_score

files = os.listdir("./doc_embedding_64_10/")
txt_files = filter(lambda x: x[-4:] == '.txt', files)
txt_files = glob.glob("./doc_embedding_64_10/*.txt")
txt_files.sort()

rep = dict()

rep_list = []

for i in txt_files:
	with open(i, 'r') as infile:
		for line in infile.readlines():
			token = line.strip().split(" ")
			# print len(token), i[22:]
			if i[23:] not in rep.keys():
				rep[i[23:]] = []

			value = [float(k) for k in token]
			rep[i[23:]] = value
			rep_list.append(value)



# print rep_list

data = []
label = []

numOfNode = 150

for nd in range(numOfNode):
	data.append(rep_list[nd])
	label.append(nd)

# print label

data = np.asarray(data)
label = np.asarray(label) 

# model = KMeans(n_clusters = numOfNode)
model = DBSCAN(eps = 0.9)
model.fit(data)

a = model.labels_
print len(a)
# silh_score = silhouette_score(data, a)
# score = completeness_score(data, a)
# print("silhouette score=",silh_score)

X_tsne = TSNE().fit_transform(data)
fig=plt.figure()
img=fig.add_subplot(111)
plot=img.scatter(X_tsne[:,0],X_tsne[:,1], c=label,cmap=plt.cm.get_cmap("jet",len(label)))
fig.suptitle("Clusters of 100 nodes spaceTimeWalk dbscan(eps="+str(model.eps)+")")
plt.colorbar(plot) 

plt.show()

