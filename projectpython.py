#Main calculator program

# Function to add numbers
def add(num1, num2, num3):
    return num1 + num2 + num3
 
# Function to multiply two numbers
def multiply(num1, num2, num3):
    return num1 * num2 * num3
 
# Function to divide two numbers
def average(num1, num2, num3):
    return (num1 + num2 + num3)/3

#User inputs numbers
number_1 = int(input("Enter a number 1-10: "))
number_2 = int(input("Enter a number 20-30: "))
number_3 = int(input("Enter a number 70-100: "))

print("Please select operation -\n" \
        "1. Sum\n" \
        "2. Average\n" \
        "3. Product\n")
 
 
# User inputs operation choice
select = int(input("Select operation 1, 2, or 3 :"))
 
if select == 1:
    print(add(number_1, number_2, number_3))
 
elif select == 2:
    print((number_1, number_2, number_3))
 
elif select == 3:
    print(multiply(number_1, number_2, number_3))

else:
    print("Invalid input")
