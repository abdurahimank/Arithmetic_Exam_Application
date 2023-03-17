# Stage 1/4: Mini-calculator
x, oper, y = input().split()
x = float(x)
y = float(y)
if oper == "+":
    print(x + y)
elif oper == "-":
    print(x - y)
else:
    print(x * y)