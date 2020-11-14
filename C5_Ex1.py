# Exercise

num = None
count = 0
num1 = 0

while True:

    try:
        num = input("Enter a number: ")

        if num == "done":   break

        num2 = int(num)
        num1 += num2
        count += 1

    except ValueError :
        print("Invalid input")


print(num1,count,num1/count)


'''

input_variable = " "
numbers = []

while True:

    input_variable = input("Enter a number: ")

    if input_variable == "done":
        break
    elif input_variable == "delete":
        numbers.pop()

    try:
        in_variable = int(input_variable)
        numbers.append(in_variable)
    except:
        print("invalid input")

total = sum(numbers)
count = len(numbers)
average = total / count

print("The total is",total)
print("The count is",count)
print("The average is",average)

'''







        #elif num != "done":
