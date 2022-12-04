# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimalDigit = int(input("Enter your decimal digit here: "))
gap = ''
while decimalDigit > 0:
    gap = str(decimalDigit % 2) + gap
    decimalDigit //= 2
print(f'Your binary digit is -> {gap}')