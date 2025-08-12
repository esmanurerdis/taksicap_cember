import numpy as np
import matplotlib.pyplot as plt

def min_circle(points):
    # Noktalar arasındaki en küçük x ve y koordinatlarını bul
    min_x, min_y = np.min(points, axis=0)
    max_x, max_y = np.max(points, axis=0)

    # Çemberin merkezi, dikdörtgenin ortası olacak
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    # Yarıçap, dikdörtgenin yarıçapına göre hesaplanacak
    radius = max((max_x - min_x) / 2, (max_y - min_y) / 2)

    return [center_x, center_y], radius

# Kullanıcıdan noktaları al
point_count = int(input("Nokta sayısını girin: "))
points = []
for i in range(point_count):
    x = float(input(f"{i + 1}. noktanın x koordinatını girin: "))
    y = float(input(f"{i + 1}. noktanın y koordinatını girin: "))
    points.append([x, y])

# En küçük çemberi hesapla
center, radius = min_circle(points)

# Dikdörtgenin koordinatlarını belirle
min_x, min_y = np.min(points, axis=0)
max_x, max_y = np.max(points, axis=0)

# Çizim yap
fig, ax = plt.subplots()
ax.scatter(*zip(*points), label='Noktalar', color='blue')

# Dikdörtgeni çizecek ve çemberin içine alacak şekilde ayarla
rectangle = plt.Rectangle((min_x, min_y), max_x - min_x, max_y - min_y, edgecolor='green', facecolor='none', label='Dikdörtgen')
ax.add_patch(rectangle)

# Çemberi dikdörtgeni içine alacak şekilde çiz
circle = plt.Circle(center, radius, edgecolor='red', facecolor='none', label='En Küçük Çember')
ax.add_patch(circle)

# Grafik ayarları
ax.set_aspect('equal', adjustable='box')
ax.legend()
plt.xlabel('X Koordinatı')
plt.ylabel('Y Koordinatı')
plt.title('En Küçük Çember ve Dikdörtgen')

# Çizimi göster
plt.show()
