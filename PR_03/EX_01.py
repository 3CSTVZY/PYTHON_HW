# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число. ['ssss', 'sngujn556', 56] -> Yes ['56', 'sgnbsb'] -> No

list = ['ssss', 'sngujn556', 56]
types = [str(type(i)) for i in list]

if "<class int>" in types or "<class float>" in types:
  print('YES')
else:
  print('NO')