# def f(x):
#   return x**2

# g = f
# print(f(4))
# print(g(4))




# def calc1(x):
#   return x+10

# def calc2(x):
#   return x*10


# def math(op, x):
#   print(op(x))

# math(calc2, 10)
# math(calc1, 10)




# def sum(x, y):
#   return x+y
# sum = lambda x, y: x+y

# def mylt(x, y):
#   return x*y

# def calc(op, a, b):
#   print(op(a, b))
#   # return op(a, b)

# calc(lambda x, y: x+y, 2, 4)




# list = []

# for i in range(1, 21):
#   if (i%2 == 0):
#     list.append(i)

# print(list)

# list = [i for i in range(1, 21) if i%2 == 0]
# print(list)




# def f(x):
#   return x**3

# list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
# print(list)




# li = [x for x in range(1, 21)]
# li = list(map(lambda x: x+10, li))

# print(li)




# data = list(map(int,input().split()))
# print(data)




# data = [x for x in range(1, 21)]
# res = list(filter(lambda x: not x%2, data))
# print(res)



# users = ['user 1', 'user 2', 'user 3']
# ids = [3, 5, 99]

# data = list(zip(users, ids))
# print(data)


users = ['user 1', 'user 2', 'user 3']
ids = [3, 5, 99]

data = list(enumerate(users, 1))
print(data)