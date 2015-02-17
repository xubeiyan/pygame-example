text_lines = [
	"Chapter 3\n",
	"Sample text data file\n",
	"This is the third line of text\n",
	"The fourth line looks like this\n",
	"Edit the file with any text editor\n" ]

file = open("data.txt", "w")
file.writelines(text_lines)
file.close()