def fibonacci(sum):
    fibo = [0, 1]
    i = 2
    while i<= sum:
        nextElement = fibo[i-1] + fibo[i-2]
        fibo.append(nextElement)
        i += 1
    return fibo
def is_int():
    try:
        text = int(input("Enter an fibonacci sequence:"))
        print(fibonacci(text))
    except ValueError:
        print("Please enter an integer!")
is_int()
