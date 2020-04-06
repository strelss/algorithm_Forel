from alg_forel import forel
from alg_forel import show_picture as s_pic
import numpy as np














points = np.array([(7, 9), (6, 9), (6, 8), (2, 3), (1, 3), (1, 2)])

radius = 1.5

a = forel.Forel(points, radius)

a = a.cluster()


print(a[0])
print(a[1])

size = [50, 100]

b = s_pic.Picture(a[0], a[1], radius)
b = b.display()