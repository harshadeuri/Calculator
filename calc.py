def fnc(choice):
	a=int(input("Enter the first number"))
	b=int(input("Enter the second number"))
	if choice==1:
		ADD(a,b)
		
	elif choice==2:
		Subtract(a,b)
			
	elif choice==3:
		Multiply(a,b)
		
	elif choice==4:
		Divide(a,b)
		



print("Calculator Menu")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice=int(input("Make a choice"))
fnc(choice)


