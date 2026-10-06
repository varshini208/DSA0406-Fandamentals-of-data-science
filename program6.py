numbers = []
for i in range(4):
    n = int(input("Enter number: "))
    numbers.append(n)
for n in numbers:
    if n > 0:
        print(n, "is Positive")
    elif n < 0:
        print(n, "is Negative")
    else:
        print(n, "is Zero")