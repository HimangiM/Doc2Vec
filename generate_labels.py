def find_point(name, times):

	# with open("tasks2_times.txt", 'r') as infile:
	# 	for line in infile.readlines():
	# 		token = line.strip().split("|")
	disci = 0
	inter_disci = 0
	point = 0
	for i in reversed(times):
		label = i.strip().split("_")[0]
		if label == "1":
			point = times.index(str(i))
			break
	if (point == 0) and (times[0] != "1"):
		point = len(times)-1
	for i in range(0, point+1):
		label = times[i].strip().split("_")[0]
		if label == "0":
			disci += 1
		else:
			inter_disci += 1

	answer = 0
	if (inter_disci == 0):
		answer = disci
	elif ((point == (len(times)-1)) and (int(times[0].strip().split("_")[0])!=0)):
		print int(times[0].strip().split("_")[1])
		answer = 1
	else:
		answer = (float(disci)/inter_disci)
	
	return disci, inter_disci, answer

			# file.write(str(token[0]) + "|" + str(disci) + "|" +  str(inter_disci) + "|" + str(answer) + "\n")
			# print(str(token[0]) + "|" + str(disci) + "|" +  str(inter_disci) + "|" + str(answer) + "\n")

file = open("task2_locavg_float.txt","w")
with open("tasks2_times.txt", 'r') as infile:
		for line in infile.readlines():
			token = line.strip().split("|")
			times = token[2].strip().split(" ")
			print token[0]
			disci = []
			inter_disci = []
			answer = []
			for i in range(1, len(times)+1):
				dis, inter, ans = find_point(token[0], times[0:i])
				# print dis, inter, ans
				val = str(dis) + "_" + str(times[i-1].strip().split("_")[1])
				disci.append(val)
				val = str(inter) + "_" + str(times[i-1].strip().split("_")[1])
				inter_disci.append(val)
				val = str(ans) + "_" + str(times[i-1].strip().split("_")[1])
				answer.append(val)
			
			# print answer
			file.write(str(token[0]) + "|")
			for i in disci:
				file.write(str(i) + " ")
			file.write("|")
			for i in inter_disci:
				file.write(str(i) + " ")
			file.write("|")
			for i in answer:
				file.write(str(i) + " ")
			file.write("|" + str(max(answer)) + "|" + str(min(answer)) + "\n")

file.close()