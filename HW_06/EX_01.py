# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

# def sum (digit):
#     sum = 0
#     for i in digit:
#         if i != ',' and i != '.':
#             sum = sum + int(i)
#     return sum
    
# number = input('Enter your digits, please: ')
# print (sum(number))

print(sum(list(map(lambda x: 0 if x == '.' else int(x), input('Enter your digit: ')))))
