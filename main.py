from alg_forel import forel
import numpy as np

points = np.array([(7, 9), (6, 9), (6, 8), (2, 3), (1, 3), (1, 2)])

radius = 2

a = forel.Cluster(points, radius)

a = a.cluster()

print(a)