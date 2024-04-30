import numpy as np
import matplotlib.pyplot as plt

def min_circle(points):
    min_x, min_y = np.min(points, axis=0)
    max_x, max_y = np.max(points, axis=0)

    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

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

# Dikdörtgeni içine alan en küçük çemberi hesapla
rectangle_center, rectangle_radius = min_circle(points)

# Çizim yap
fig, ax = plt.subplots()
ax.scatter(*zip(*points), label='Noktalar', color='blue')

# Dikdörtgeni çemberin içinde tutacak şekilde ayarla
rectangle_radius *= np.sqrt(2)

rectangle = plt.Rectangle((min(points)[0], min(points)[1]), max(points)[0] - min(points)[0], max(points)[1] - min(points)[1], edgecolor='green', facecolor='none', label='Dikdörtgen')
ax.add_patch(rectangle)
circle = plt.Circle(rectangle_center, rectangle_radius, edgecolor='red', facecolor='none', label='En Küçük Çember')
ax.add_patch(circle)

# Grafik ayarları
ax.set_aspect('equal', adjustable='box')
ax.legend()
plt.xlabel('X Koordinatı')
plt.ylabel('Y Koordinatı')
plt.title('En Küçük Çember (Taksimetrik) Dikdörtgen İçinde')

# Çizimi göster
plt.show()