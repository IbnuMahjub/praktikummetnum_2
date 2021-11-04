import scipy
from scipy.linalg import lu, lu_factor, lu_solve
import numpy as np

# Definisikan matriks A
A = np.array([[4., 3, -1], [-2, -4., 5], [1, 2, 6]])

# Definisikan vektor b
b = np.array([-4, 40, 14])

# Solusi yang diberikan lu dan b
P, L, U, = lu(A)
lu, piv = lu_factor(A)
x = lu_solve((lu, piv), b)
print('Matriks P :\n ', P)
print('Matriks L :\n ', L)
print('Matriks U :\n ', U)
print('Solutions :\n ', x)
