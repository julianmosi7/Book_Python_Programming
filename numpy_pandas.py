import numpy as np

L = list(range(10))

x1 = np.array([4, 3, 4, 4, 8, 4])
print('--------One Dimensional Array-------')
print(f'whole x1 array: {x1}')
print(f'FIRST value of array x1: [{x1[0]}]')
print(f'FIFTH value of array x1: [{x1[4]}]')
print(f'LAST value of array x1: [{x1[-1]}]')
print(f'SECOND LAST value of array x1: [{x1[-2]}]')

x2 = np.array([[3, 7, 5, 5], [0, 1, 5, 9], [3, 0, 5, 0]])
print('\n--------Two Dimensional Array-------')
print(f'whole x2 array: {x2}')
print(f'THIRD array FOURTH value value of array x2: [{x2[2,3]}]')
print(f'THIRD array LAST value value of array x2: [{x2[2, -1]}]')
x2[0, 0] = 12
print(x2)

y = np.arange(10)
print('\n--------Arrange Array-------')
print(f'whole aranged array: {y}')
print(f'To 4th value of array aranged: [{y[:5]}]')
print(f'To 4th value backwards of array aranged: [{y[4:]}]')
print(f'From 4th value to 6th value of array aranged: [{y[4:7]}]')
print(f'All even values of array aranged: [{y[::2]}]')
print(f'From 1th value step by to of array aranged: [{y[1::2]}]')
print(f'Reverse array aranged: [{y[::-1]}]')

grid = np.array([[1, 2, 3], [4, 5, 6]])
x = np.array([3, 4, 5])
z = np.array([[9], [9]])
grid2 = np.array([[1, 2, 3], [17, 18, 19]])
print('\n--------Arrange Array-------')
print(f'\n con 1:1 or 2:2: {np.concatenate([grid, grid], axis=1)}')
print(f'\n con 2:1 or 1:2: {np.vstack([x, grid2])}')
print(f'\n con 2:1 or 1:2 rev: {np.hstack([grid2, z])}')
