# swapping of two numbers by using bitwise operator
a = int(input())
b = int(input())
a = a ^ b
b = a ^ b
a = a ^ b
print("after swapping")
print(a)
print(b)