# Algoritma-Image-Filtering
Algoritma ini menggunakan tiga variabel utama:

H: Matriks atau array kernel (filter).
X: Matriks atau array untuk gambar input (gambar asli).
Y: Matriks atau array untuk hasil dari konvolusi gambar.

```python
import numpy as np

# Definisikan ukuran kernel dan gambar input
kernel_size = 3  # Misalnya 3x3
image_size = 5   # Misalnya 5x5

# 1. Buat variabel H sebagai matriks kernel
H = np.array([[0, -1, 0],
              [-1, 5, -1],
              [0, -1, 0]])

# 2. Buat variabel X sebagai matriks untuk gambar input
X = np.random.randint(0, 256, (image_size, image_size))  # Matriks 5x5 dengan nilai random antara 0-255
print("Input Image (X):\n", X)

# 3. Inisialisasi matriks Y untuk menyimpan hasil konvolusi
Y = np.zeros((image_size - kernel_size + 1, image_size - kernel_size + 1))

# 4. Lakukan konvolusi antara X dan H untuk menghasilkan Y
for i in range(Y.shape[0]):
    for j in range(Y.shape[1]):
        # Ambil bagian dari X yang sesuai dengan ukuran kernel
        region = X[i:i + kernel_size, j:j + kernel_size]
        # Hitung konvolusi: kalikan elemen-elemen region dengan H, lalu jumlahkan
        Y[i, j] = np.sum(region * H)

print("\nOutput Image (Y) setelah konvolusi:\n", Y)
```
Output:
```
Input Image (X):
 [[ 46 247 236 129 118]
 [246 131  19 239 182]
 [ 49 233 201  32 110]
 [182 173 199 235 225]
 [ 22 123 199 164 247]]

Output Image (Y) setelah konvolusi:
 [[ -90. -712.  833.]
 [ 611.  522. -625.]
 [ 128.  187.  555.]]
```
Penjelasan
Matriks H digunakan sebagai kernel, yang akan melakukan operasi filter pada matriks X.
Matriks X berfungsi sebagai gambar input yang nilainya dapat berupa pixel intensitas gambar.
Matriks Y adalah hasil output setelah konvolusi antara kernel H dan gambar X.
