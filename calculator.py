def calc(x,y,opt):
	if opt not in "/*-+":
		return("choose avaliable option")
	elif(opt == "*"):
		return(str(x) + opt + str(y) + " =" +str(x*y))
	elif(opt == "-"):
		return(str(x) + opt + str(y) + " =" +str(x-y))
	elif(opt == "+"):
		return(str(x) + opt + str(y) + " =" +str(x+y))
	elif(opt == "/"):
		return(str(x) + opt + str(y) + " =" +str(x/y))

while True:
	x = int(input('Enter first number: '))
	y = int(input('Enter second number: '))
	opt = input("Choose between +, -, *, / ")

	print(calc(x, y, opt))