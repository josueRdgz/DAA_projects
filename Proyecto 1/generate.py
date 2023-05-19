import random


def cases_generator(n=7, m=5, k=2):

    matrix = [[random.randint(1, 4) for j in range(m)] for i in range(n)]

    array_vip = [random.randint(1, 5) for i in range(n)]

    for i in range(k):
        for index, j in enumerate(matrix):
            j.append(array_vip[index])

    return matrix
