fruit = "Banana"
index = 0
letter = None

while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

index = -1

while True:
    letter = fruit[index]
    print(letter)
    index -= 1

    if letter == fruit[0]:
        break
