from random import *


k=2

a = round(random()*10, )
b = round(random()*10, )
c = round(random()*10, )
print(a, b, c)
result = ''
if b == 0: result = f"{a}*x**{k} + {c}*x**{k-2} = 0"
if b == 0 and c == 0: result =  f"{a}*x**{k} = 0"
if c == 0: result = f"{a}*x**{k} + {b}*x**{k-1} = 0 "
else: result =  f"{a}*x**{k} + {b}*x**{k-1} + {c}*x**{k-2} = 0 "

with open("file44.txt", "w") as file44:
    file44.write(result)