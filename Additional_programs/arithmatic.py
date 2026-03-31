# enter int of 2 numbers and perform all the arithmatic operator
def arithmatic(a,b):
   if ch == '+':
      return a+b
   elif ch == '-':
      return a-b
   elif ch == '*':
      return a*b
   elif ch == '//':
      return a//b
   else:
      return a /b

m = int(input("enter the 1st digit :"))
n = int(input("enter the 2nd digit :"))
ch = input("enter the operator:")
print(arithmatic(m,n))    