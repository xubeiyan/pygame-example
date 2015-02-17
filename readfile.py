file = open("data.txt", "r")
all_data = file.readlines()
print("Lines: ", len(all_data))
for line in all_data:
	print(line.strip())