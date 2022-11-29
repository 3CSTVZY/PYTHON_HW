# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

def factorial(n):
    startPoint = 1
    for i in range(1, n+1):
        startPoint *= i
        print(startPoint)
        
n = int(input('Enter the N digit, please: '))
factorial(n)