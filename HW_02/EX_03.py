# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму

n = int(input("Enter the N digit, please: "))
avg = [(1+1/i)**i for i in range(1, n+1)]

print('list -> ', avg)
print('amount -> ', round(sum(avg), 3))