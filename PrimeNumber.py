i = int(input("Enter a number: "))

if i > 1:
    for num in range(2,i):
        if i % num == 0:
            print(i, "is not a prime number")
            break
    else:
        print(i,"is a prime number")
else:
    print(i,"is not a prime number")