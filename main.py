print("##################")
print("#Grade Calculator#")
print("##################")

grade = int(input("What is the number grade you got? "))
if grade <= 23:
	print("Your letter grade is an F.")
elif grade >=24 and grade <=29:
	print("Your letter grade is an E.")
elif grade >=30 and grade <=35:
	print("Your letter grade is an D.")
elif grade >=36 and grade <=41:
	print("Your letter grade is an C.")
elif grade >= 42 and grade <=47:
	print("Your letter grade is an B.")
elif grade >=48 and grade <=53:
	print("Your letter grade is an A.")
else:
	print("Your letter grade is an A+.")
