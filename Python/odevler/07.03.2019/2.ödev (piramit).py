satir=10
for i in range(satir):
    print(' '*(satir-i-1) + '*'*(2*i+2))
for i in range(satir,0,-1):
    print(' '*(satir-i+1) + '*'*(2*i-2))
