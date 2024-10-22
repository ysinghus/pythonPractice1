'''
count = 0
while count < 5:
    print ("Count:",count)
    count +=1
else:
    print("Count is not less than 5 anymore.")
    
    
numbers=[1,2,3,4,5]
for num in numbers:
    print("Number:",num)
else: 
    print("Loop completed successfully.")
    '''
    
timer=input("Please enter a number between 10-15 for the countdown timer:")
timer=int(timer)
while timer > 0:
    print ("Time remaining to BOOM:",timer)
    timer -=1
else:
    print("BOOM")

#isdigit checks if the timer input is a digit