
def rubik_faces():
	n = int(input("Please enter a number: "))
	if n > 1:
		print(str(n**3 - (n-1)**3) + " cubes make up the visible faces of Rubik\'s cube")
	else:
 		print("Number must be greater than 1")


rubik_faces()
