#factorial of a number 
def Factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact *i
    print(f"Factorial of {n} is {fact}")
Factorial(5)        
