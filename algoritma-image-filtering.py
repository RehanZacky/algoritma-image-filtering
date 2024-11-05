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
