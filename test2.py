'''userNumber=input("Please enter a number: ")
userNumber=int(userNumber)
if userNumber>0:
    print("Positive")
elif userNumber<0:
    print("Negative")
else:
    print("Number is 0")
  '''  
  
userNumber1=input("Please enter a number: ")
userNumber1=float(userNumber1)
 
userOperator=input("Please enter a operator from the options: + , - :   ")
if userOperator=='+':
    print(f"user chose positive operator: {userOperator}")
elif userOperator=='-':
    print(f"user chose negative operator: {userOperator}")
else:
    print(f"ERROR: User chose neither + or - ")
    
userNumber2=input("Please enter a number: ")
userNumber2=float(userNumber2)

if userOperator=='+':
    result=userNumber1+userNumber2
elif userOperator=="-":
    result=userNumber1-userNumber2
print(result)