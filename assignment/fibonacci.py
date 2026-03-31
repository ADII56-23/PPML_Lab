#first 15 fibonnaci series
a = 0 
b = 1
c  = a+b
for i in range(16):
    a, a+b = a, c
       