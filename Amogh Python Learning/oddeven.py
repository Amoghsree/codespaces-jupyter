num = float(input("Enter a number: "))

if num < 0:
	print("Negative Number")
elif num % 2 == 0:
	print(str(int(num)) + " is even")
elif num % 2 == 1:
	print(str(int(num)) + " is odd")
else:
	print("Not Defined")