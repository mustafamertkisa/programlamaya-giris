a=0
for i in range(1,501):
    if i % 13 == 0:
        a=a+i
b=0
for i in range(1,501):
    if i % 11 == 0:
        b=b+i
print(b-a)


