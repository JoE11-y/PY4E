L = []
while True:
    try:
        num = input("Enter a number: ")

        if num == "done":
            break

        nums = int(num)
        L.append(nums)

    except ValueError :
        print("Invalid input")

min_value = None
max_value = None
for i in L:
    if max_value is None or i > max_value:
        max_value = i
print("maximum value =", max_value)

for i in L:
    if min_value is None or i < min_value:
        min_value = i
print("minimum value =", min_value)


    #print(L)
    #print("minimum value =",min(L))
    #print("maximum value =", max(L))
