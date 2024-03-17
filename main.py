#Jaunel Deans
#October 24, 2023
#We had to modify the starter code. I had to add a line of code asking the user to enter a third number. I also had to add edit the IF/ELIF/ELSE statements to confirm whether the third number is bigger/smaller/the same as the first number and whether it is bigger/smaller/the same as the second number. Also if all three numbers are the same. 

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))
number3 = int(input("Please enter a third number: "))#add a line of code to ask the user for a third number and save it in a variable called number3. It can only be a whole number/interger 

if number1 > number2 and number1 > number3:#Added a line of code to check if number1 is greater than number2 and number3. If it is then the code will run.
  print("Number 1 is bigger than number 2 and number 3")#Added a line of code to print out that number 1 is bigger than number 2 and number 3
  
elif number2 > number1 and number2 > number3: #Added a line of code to check if number2 is greater than number1 and number3. If it is then the code will run. It will run if the if statement if false. 
  print("Number 2 is bigger than number 1 and number 3")#Added a line of code to print out that number 2 is bigger than number 1 and number 3
  
elif number3 > number1 and number3 > number2:#Added a line of code to check if number3 is greater than number1 and number2. If it is then the code will run. It will run if the elif statement if false. 
  print("Number 3 is bigger than number 1 and number 2")#Added a line of code to print out that number 3 is bigger than number 1 and number 2
  
else:#Added a line of code to check if none of the if statements are true. If they are then the code will run. 
  print("Number 1 and number 2 and number 3 are equal")#Added a line of code to print out that number 1 and number 2 and number 3 are equal


