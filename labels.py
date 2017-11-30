# goes to the author_rep file, and for every name, search for the file in the given time window

import networkx as nx
import os 
import glob
import time

f = open("author_rep_labels_44.txt", 'w')					
input_direc = "./combineSpaceTime_final/final_spacetimecombined44.spacetimerep"	
files = os.listdir("/home/himangi/Internship/Work/DBLP/yearly_conf_labels")

if __name__=='__main__':
	txt_files = filter(lambda x: x[-4:] == '.txt', files)
	txt_files = glob.glob("/home/himangi/Internship/Work/DBLP/yearly_conf_labels/*.txt")
	
	txt_files.sort()


	# print txt_files
	l = []

	with open(input_direc, 'r') as repfile:
		for rline in repfile.readlines():
			tokenr = rline.strip().split("|")
			# print tokenr[0]
			for i in range(36, 45):													
				with open(txt_files[i], 'r') as infile:
					for line in infile.readlines():
						token = line.strip().split("|")
						# print token[0], tokenr[0].strip().split("_")[0]
						# name = tokenr[0].strip().split("_")[0]
						if token[0].strip() == tokenr[0].strip().split("_")[0].strip():
							# print 'yes'
							if token[3].strip() not in l:
								l.append(token[3].strip())
			
 		# 	print l
			if len(l)!=0:
				print l
				# print tokenr[0]

				if len(l) == 1:
					print(str(tokenr[0] + "|" + tokenr[1] +"|0" +"\n"))

					f.write(str(tokenr[0] + "|" + tokenr[1] +"|0" +"\n"))
				else:
					print 'yes'
					print(str(tokenr[0] + "|" + tokenr[1] +"|1" +"\n"))

					f.write(str(tokenr[0] + "|" + tokenr[1] +"|1" +"\n"))
			l = []