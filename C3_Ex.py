#Exercise 1
Hrs = input("Enter Hours: ")
Rt = input("Enter Rate: ")
hrs = float(Hrs)
rt = float(Rt)

if hrs > 40:
    exH = (hrs - 40) * 1.5
    totH = exH + 40
    Pay = rt * totH
    print(Pay)
else:
    Pay = rt * int(Hrs)
    print(Pay)


#Exercise 2
try:
    Hrs = input("Enter Hours: ")
    hrs = int(Hrs)
    Rt = input("Enter Rate: ")
    rt = int(Rt)
except:
    hrs = -1

if hrs > 40:
    exH = (hrs - 40) * 1.5
    totH = exH + 40
    Pay = rt * totH
    print(Pay)
elif hrs > 0 and hrs <= 40:
    Pay = rt * hrs
    print(Pay)
else:
    print("Error, please enter a numeric input")
    quit()



#Excercise 3
grd = input("Enter score: ")

try:
    grd = float(grd)
except:
    grd = -1

if grd >= 0 and grd <= 1:
    if grd >= 0.9:
        print("A")
    elif grd >= 0.8:
        print("B")
    elif grd >= 0.7:
        print("C")
    elif grd < 0.6:
        print("F")
else:
    print("bad score")
    quit()
