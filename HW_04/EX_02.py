# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
# * 6 -> [1,2,3]
# * 144 -> [2,3]

def simple_multipliers():
    digit = int(input("Input yout digit here: "))
    multipliers = []
    a = 2

    while digit > 1:
        if digit % a == 0:
            multipliers.append(a)
            digit /= a
        else:
            a += 1

    print(f"The multipliers of your digit is:", *multipliers)

simple_multipliers()