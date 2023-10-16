import numpy as np

def convert_to_dec(s):
    arr = []
    for i in s:
        arr.append(ord(i))
    return arr

plaintext = input("Masukkan plainteks: ")
key = input("Masukkan key: ")

# URUTKAN ARRAY LALU HASILKAN INDEX NYA
decimal_key = convert_to_dec(key)
getIndex = np.argsort(decimal_key)
getIndex = getIndex.tolist()
print(getIndex)

# MEMBUAT MATRIX 2D MENGGUNAKAN DICT
matrix_2d = {}
plainArr = list(plaintext)  # ubah string ke dalam bentuk array

# MEMBUAT KOLOM KEY

# kunci_double berfungsi jika ada huruf kunci yang sama/double
# misal: HELLO, huruf L ada 2. huruf L yg pertama dan kedua harus dibedakan agar bisa membuat kunci baru
# alasan nya adalah setiap kunci didalam dict harus unik
kunci_double = 1
newKey = []

for k in key:
  if matrix_2d.get(k) is None:
    matrix_2d[k] = []
    newKey.append(k)
  else:
    matrix_2d[f'{k}_{kunci_double}'] = []
    newKey.append(f'{k}_{kunci_double}')
    kunci_double+=1

# MEMASUKKAN PLAINTEXT KE DAlAM KOLOM MATRIX 2D
j = 0
while j < len(plainArr):
    k = 0
    while k < len(key) and j < len(plainArr):
        matrix_2d[newKey[k]].append(plainArr[j])
        k += 1
        j += 1

# PRINT MATRIX_2D DENGAN INDEKS YANG TELAH DIURUTKAN (getIndex)
l = 0
chipertext = ""
print("Matrix 2D dengan kunci dan value nya:")
while l < len(key):
  print(newKey[getIndex[l]],":", matrix_2d[newKey[getIndex[l]]])
  for i in matrix_2d[newKey[getIndex[l]]]:
    chipertext += i
  l+=1
print("\nChipertext: ", chipertext)
