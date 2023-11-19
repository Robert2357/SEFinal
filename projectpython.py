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

#User inputs first number
while True:
    try:
        number_1 = int(input("Enter an integer 1-10: "))
    except ValueError:
        print("Please enter a valid integer 1-10")
        continue
    if number_1 >= 1 and number_1 <= 10:
        break
    else:
        print('The integer must be in the range 1-10')

#User inputs 2nd number
while True:
    try:
        number_2 = int(input("Enter an integer 20-30: "))
    except ValueError:
        print("Please enter a valid integer 20-30")
        continue
    if number_2 >= 20 and number_2 <= 30:
        break
    else:
        print('The integer must be in the range 20-30')

#User inputs third number
while True:
    try:
        number_3 = int(input("Enter an integer 70-100: "))
    except ValueError:
        print("Please enter a valid integer 70-100")
        continue
    if number_3 >= 70 and number_3 <= 100:
        break
    else:
        print('The number must be in the range 70-100')

#Choices are shown to user
print("Please select operation -\n" \
        "1. Sum\n" \
        "2. Average\n" \
        "3. Product\n")

#User inputs result choice
while True:
    try:
        select = int(input("Select operation 1, 2, or 3: "))
    except ValueError:
        print("Please enter 1, 2, 0r 3: ")
        continue
    if select == 1 or select == 2 or select == 3:
        break
    else:
        print('You must choose 1, 2, or 3')

#Result is calculated
if select == 1:
    print(add(number_1, number_2, number_3))
 
elif select == 2:
    print(average(number_1, number_2, number_3))
 
elif select == 3:
    print(multiply(number_1, number_2, number_3))

else:
    print("Invalid input")
