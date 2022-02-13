import random 
r1 = random.randint(0,100)

while True:
	x = int(input("pls enter your choice"))
	if x < r1:
		print("the number is so small")
	elif x > r1:
		print("the number is so big")
	elif x == r1:
		print("TRUE ANSWER")
		break
