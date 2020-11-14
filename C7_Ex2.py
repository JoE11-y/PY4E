
fname = input("Enter file name:" )

fopen = open(fname)
count = 0
range_of_nums = 0
val = None

for line in fopen:
    if line.startswith("X-DSPAM-Confidence:"):
        val = line.find("0")
        num = line[val:]
        num = float(num)
        range_of_nums += num

        count += 1

average = range_of_nums/count
print("Average spam confidence: %.12f" % average)
