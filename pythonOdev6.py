"""
1.Sayılardan oluşan bir boyutlu array oluşturulur.
Arrayi oluştururken sayıların veri tipini integer olarak belirtilir.
Oluşturulan arrayin boyut,eleman sayısı bilgilerine bakılır.

2.İki ve üç boyutlu arrayler oluşturulur.Bu arraylerin boyut,eleman sayısı,satır,sütun bilgilerine ulaşılır.
Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır.

3.Numpy fonksiyonu kullanarak bir, iki ve üç boyutlu arrayler oluşturulur.
Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır

4.Sıfırlardan oluşan ve birlerden oluşan iki tane iki boyutlu array oluşturulur.
Bu arrayler satır ve sütun bazında birleştirilir.
"""
import numpy as np

dizi_1d = np.array([4,5,6,7,8], dtype = int)
print("Dizi: ",dizi_1d)
print("Dizinin eleman sayısı: ",dizi_1d.size)
print("Dizinin boyutu: ",dizi_1d.ndim)
print("Shape: ",dizi_1d.shape)

dizi_2d = np.array([[7,8,9],[1,2,3]])
print("Dizi: ",dizi_2d)
print("Dizinin eleman sayısı: ",dizi_2d.size)
print("Dizinin boyutu: ",dizi_2d.ndim)
print("Shape: ",dizi_2d.shape)
print("Satır sayısı: ",dizi_2d.shape[0])
print("Sütun sayısı: ",dizi_2d.shape[1])

dizi_3d = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print("Dizi: ",dizi_3d)
print("Dizinin eleman sayısı: ",dizi_3d.size)
print("Dizinin boyutu: ",dizi_3d.ndim)
print("Shape: ",dizi_3d.shape)
print("Derinlik: ",dizi_3d.shape[0])
print("Satır sayısı: ",dizi_3d.shape[1])
print("Sütun sayısı: ",dizi_3d.shape[2])

print("1D dizisinin 2.elemanı :", dizi_1d[1])
print("1D dizisinin 1'den 4'e kadar olan elemanları :", dizi_1d[1:4])

print("2D dizisinin [0, 2] elemanı :", dizi_2d[0, 2])
print("2D dizisinin ilk satırı :", dizi_2d[0, :])
print("2D dizisinin ikinci sütunu :", dizi_2d[:, 1])

print("3D dizisinin [0, 1, 1] elemanı :", dizi_3d[0,1,1])
print("3D dizisinin ilk derinliğindeki tüm elemanlar :\n", dizi_3d[0, :, :])

sıfırlar_dizisi = np.zeros((2,3), dtype = int)
print("Dizi: ",sıfırlar_dizisi)
birler_dizisi = np.ones((2,3), dtype = int)
print("Dizi: ",birler_dizisi)

vertical_stack = np.vstack((sıfırlar_dizisi,birler_dizisi))
print("Vertical Stack :\n", vertical_stack)

horizontal_stack = np.hstack((sıfırlar_dizisi, birler_dizisi))
print("Horizontal Stack :\n", horizontal_stack)