import numpy as np

a = np.array([3, 5, 1, 2])

i_max = a.argmax()
i_min = a.argmin()

print(f'o índice do maior elemento é: {i_max}')
print(f'O índice do menor elemento é: {i_min}')

print(f'o valor do maior elemento é: {a[i_max]}')
print(f'O valor do menor elemento é: {a[i_min]}')