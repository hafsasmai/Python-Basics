while(1):
    op1= float(input ("Enter the first operand: "))
    op= str (input("Enter the operation: "))
    op2= float(input ("Enter the second operand: "))
    if op =="+":
        print(op1+op2)
    elif op =="-":
        print(op1-op2)
    elif op =="*":
        print(op1*op2)
    elif op == "**":
        print(op1**op2)
    elif op == "/" and op2 == 0 :
        print(f"Math Error, you cannot divide by 0 !")
    elif op == "/" :
        print(op1/op2)
    else :
        print(f"Syntax Error , please correct the syntax !")   
