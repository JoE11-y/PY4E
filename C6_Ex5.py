str = "X-DSPAM-CONFIDENCE: 0.8475"

Var = str.find("0")

num = str[Var:]
num = float(num)
print(type(num))
