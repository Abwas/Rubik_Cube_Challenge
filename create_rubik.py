
def create_new_rubik():
	n = int(input("Please enter a number: "))
	if n > 1:
		for i in range(n**3):
			print (n-1)**3, ((n-1)-1)**3, (((n-1)-1)-1)**3, ((((n-1)-1)-1)-1)**3
			if i == 1:
				break
			else:
				continue 
	else:
 		print("Number must be greater than 1")


create_new_rubik()
