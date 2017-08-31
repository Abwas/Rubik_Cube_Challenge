
def smaller_cubes():
	n = int(input("Please enter a number: "))
	if n > 1:
		print(str(n**3) + " smaller cubes are needed to construct a " + str(n) + "X" + str(n) + "X" + str(n) + " Rubik\'s cube")
	else:
		print("Number must be greater than 1")


smaller_cubes()
