import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

circle = plt.Circle((0, 0), 1, fill=False, color='black', linestyle='solid')
ax.add_artist(circle)

angulos = [30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]

for angulo in angulos:
    angulo_radianes = np.deg2rad(angulo)
    x = np.cos(angulo_radianes)
    y = np.sin(angulo_radianes)
    ax.plot([0, x], [0, y], 'r--')

plt.title('Circulo radial')
plt.grid(False)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()