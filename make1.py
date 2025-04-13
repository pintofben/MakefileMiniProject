# Ben Pintof
# Scientific Computing
# Makefile Mini Project

if __name__=='__main__':
	# Creating outFile
	outFile = open("make1.txt", "w")

	# Import Packages
	import numpy as np

	# Creating Variable
	x = 0
	sum = 0
	high = 0
	low = 10

	# Creating the loop
	for i in range(10):
		x = np.random.randint(10)
		sum += x
		if x > high:
			high = x
		if x < low:
			low = x

	avg = sum / 10

	outFile.write("Here are the Prelimary Stats for this run" + "\n")
	outFile.write("The total sum was " + str(sum) + "\n")
	outFile.write("The high number was " + str(high) + "\n")
	outFile.write("The low number was " + str(low) + "\n")
	outFile.write("The average number was " + str(avg) + "\n")
