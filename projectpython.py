import math

print("This program is made to calcuate three numbers within a certain range.")

num1 = input("Enter a number between 1-10: ")
num2 = input("Enter a number between 20-30: ")
num3 = input ("Enter a number between 70-100: ")

print("Now choose your option of calcuation and enter the name. 1 for Sum Calcuation, 2 for GCD calcuation, and 3 for average calcuation." )

option = input("Enter the corresponding number option: ")

if option == 1:
    print ( "The sum of the three numbers is: " +  (num1 + num2 + num3) )
elif option == 2:
    print ("The GCD of the three numbers is: " + math.gcd(num1, num2, num3))
elif option == 3:
    print ("The mean of the three numbers is: " + ((num1 + num2 + num3)/3))
