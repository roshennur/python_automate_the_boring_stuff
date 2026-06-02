import sys

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    num = int(input('>'))
    while num != 1:
        num = collatz(num)
        print(num, end=' ')
except ValueError:
    print('Enter valid number!')

















