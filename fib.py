import sys

def fibonacci(number):
    num1, num2 = 0, 1
    if number==1:
        return num1
    if number==2:
        return num2
    else:
        i=0
        while i<number-2:
            temp = num1 + num2
            num1 = num2
            num2 = temp
            i+=1
        return num2

n=len(sys.argv)
if n<2:
    print("No argument provided")
elif n<3:
    number=int(sys.argv[1])
    print(fibonacci(number))
else:
    print("Invalid number of arguments")