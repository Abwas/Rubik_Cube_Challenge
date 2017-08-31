
def hidden_cubes():
	n = int(input("Please enter a number: "))
	if n > 1:
		print(str((n-1)**3) + " cubes are hidden")
	else:
		print("Number must be greater than 1")


hidden_cubes()
