# Exercise 2

score = input("Enter score: ")

try:
    score = float(score)
except:
    score = -1

def computegrade(score):

    if score >= 0 and score <= 1:
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score < 0.6:
            return "F"
    else:
        print("bad score")
        quit()


result = computegrade(score)
print(result)
