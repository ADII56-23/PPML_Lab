# even length words of a string
x = input("Enter a string: ")
y = []
words = x.split()
for word in words:
    if len(word) % 2 == 0:
        y.append(word)

print("Even length words:", y)    