def fnc(choice):
	a=int(input("Enter first number"))
	b=int(input("Enter second number"))
	if choice==1:
		ADD(a,b)
		
	elif choice==2:
		Subtract(a,b)
			
	elif choice==3:
		Multiply(a,b)
		
	elif choice==4:
		Divide(a,b)
		



print("MENU")
print("1. ADD")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice=int(input("Make a choice"))
fnc(choice)


