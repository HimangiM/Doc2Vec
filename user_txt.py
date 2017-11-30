import os
import glob

files = os.listdir("./random walks/")
txt_files = filter(lambda x: x[-4:] == '.txt', files)
txt_files = glob.glob("./random walks/*.txt")
txt_files.sort()

print txt_files

users = dict()

for i in txt_files:
	time_step = i[15:-4]
# print time_step
	with open(txt_files[0], 'r') as infile:
		for line in infile.readlines():
			token = line.strip().split(",")
			# print token[0],len(token)
			user_name = str(token[0].strip().split("_")[0])
			if user_name not in users.keys():
				users[user_name] = []
			l = []
			for i in range(1, len(token)-1):
				# print token[i] + "_" + str(time_step)
				l.append(str(token[i] + "_" + str(time_step)))
			# print l
			if l not in users[user_name]:
				users[user_name].append(l)

for k, v in users.iteritems():
	f = open(k + ".txt", 'w')
	print k
	for i in v:
		for j in i:
			print j + " ",
			f.write(str(j + " "))

	f.close()










