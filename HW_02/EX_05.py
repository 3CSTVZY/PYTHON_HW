# Реализуйте алгоритм перемешивания списка

import random

print('Input here some digits using commas, please...')

algorithm = list(map(int, input().split(',')))
random.shuffle(algorithm)

print('shuffle ->', algorithm)