# Exercise 1
try:
    Hrs = input("Enter Hours: ")
    hrs = int(Hrs)
    Rt = input("Enter Rate: ")
    rt = int(Rt)
except:
    hrs = -1
    rt = 0

def computepay(hrs, rt):

    if hrs > 40:
        exH = (hrs - 40) * 1.5
        totH = exH + 40
        Pay = rt * totH
        return Pay
    elif hrs > 0 and hrs <= 40:
        Pay = rt * hrs
        return Pay
    else:
        print("Error, please enter a numeric input")
        quit()


Test = computepay(hrs, rt)
print(Test)
