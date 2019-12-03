#Function to run nth Fibonacci Series

def fibonacci(number):
    first_num=0
    second_num=1
    if number<0:
        print("Incorrect series")
    elif number==0:
        return first_num
    elif number==1:
        return second_num
    else:
        for num in range(2,number):
            fib=first_num+second_num
            first_num=second_num
            second_num=fib
        return second_num

print(fibonacci(9))
