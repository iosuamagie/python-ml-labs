import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Numpy
# Initializare vectori multidimensionali
a = np.array([1, 2, 3])
print(a)
print(type(a))
print(a.dtype)
print(a.shape)
print(a[0])

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
print(b[0][2])
print(b[0, 2])

c = np.asarray([[1, 2], [3, 4]])
print(type(c))
print(c.shape)

# Creare vectori folosind functii
zero_array = np.zeros((3, 2))
print(zero_array)

ones_array = np.ones((2, 2))
print(ones_array)

constant_array = np.full((2, 2), 8)
print(constant_array)

identity_matrix = np.eye(3)
print(identity_matrix)

random_array = np.random.random((1, 2))
print(random_array)

mu, sigma = 0, 0.1
gaussian_random = np.random.normal(mu, sigma, (3, 6))

first_5 = np.arange(5)
print(first_5)

# Indexare si Slicing
first_5 = np.arange(5)
print(first_5)

array_to_slice = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
slice = array_to_slice[:, 0:3]
print(slice)

print(array_to_slice[0][0])
slice[0][0] = 100
print(array_to_slice[0][0])

slice_copy = np.copy(array_to_slice[:, 0:3])
slice_copy[0][0] = 100
print(slice_copy[0][0])
print(array_to_slice[0][0])

# Functii matematice de baza
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# Suma element cu element
print(x + y)
print(np.add(x, y))

# Diferenta element cu element
print(x - y)
print(np.subtract(x, y))

# Produs element cu element
print(x * y)
print(np.multiply(x, y))

# Impartire element cu element
print(x / y)
print(np.divide(x, y))

# Radical element cu element
print(np.sqrt(x))

# Ridicare la putere
my_array = np.arange(5)
powered = np.power(my_array, 3)
print(powered)

# Produsul scalar si inmultirea matricilor
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

# Vector x vector
print(v.dot(w))
print(np.dot(v, w))

# Matrice x vector
print(np.matmul(x, v))

# Matrice x matrice
print(np.matmul(x, y))

# Transpusa unei matrici
my_array = np.array([[1, 2, 3], [4, 5, 6]])
print(my_array.T)

# Inversa unei matrici
my_array = np.array([[1., 2.], [3., 4.]])
print(np.linalg.inv(my_array))

# Suma pe o anumita dimensiune
x = np.array([[1, 2], [3, 4]])
print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))
print(np.sum(x, axis=(0, 1)))

# Media pe o anumita dimensiune
y = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]]])
print(y.shape)
print(y)
print(np.mean(y, axis=0))
print(np.mean(y, axis=1))

# Indexul elementului maxim pe fiecare linie
z = np.array([[10, 12, 5], [17, 11, 19]])
print(np.argmax(z, axis=1))

# Broadcasting (adunarea unui vector la fiecare linie a unei matrici)
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = m + v
print(y)

# Matplotlib

# Plotarea simpla (curba Sinus)
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine')
plt.legend(['Sine'])
plt.show()

# Plotarea mai multor grafice în cadrul aceleiași figuri (Sinus si Cosinus)
x = np.arange(0, 3 * np.pi, 0.1)
y_1 = np.sin(x)
y_2 = np.cos(x)

plt.plot(x, y_1)
plt.plot(x, y_2)
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()

# Plotarea simultana a mai multor grafice în figuri diferite
x = np.arange(0, 3 * np.pi, 0.1)
y_1 = np.sin(x)
y_2 = np.cos(x)

first_plot = plt.figure(1)
plt.plot(x, y_1)
plt.title('Sine')
plt.legend(['Sine'])

second_plot = plt.figure(2)
plt.plot(x, y_2)
plt.title('Cosine')
plt.legend(['Cosine'])

plt.show()

# Subplotare
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('Sine')

plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

plt.show()

