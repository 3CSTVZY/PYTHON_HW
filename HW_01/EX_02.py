# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

print('Testing...')
print()

x = int(input('Enter x '))
y = int(input('Enter y '))
z = int(input('Enter z '))

a = x * y * z
b = x + y + z

if a > 0:
     a = 0
elif a < 1:
     a = 1
if b > 0:
     b = 1
elif b < 1:
     b = 1

print()

if a == b:
     print("That's true!")
elif a != b:
     print("That's false!")

left = not (x or y or z)
right = not x and not y and not z
result = left == right

if result == True:
     print("That's true!")
else:
    print("That's false!")